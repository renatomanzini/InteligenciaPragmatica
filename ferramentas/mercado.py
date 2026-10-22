"""Caderno Mercado: o painel de números e o alarme da edição extra.

Os números entram na edição por código, nunca pela IA. Todas as fontes são públicas e sem chave:
- Ibovespa: B3 (cotacao.b3.com.br);
- índices dos EUA, VIX, juros de 10 anos, Brent, ouro e bitcoin em dólar: CNBC (quote.cnbc.com);
- moedas: AwesomeAPI (economia.awesomeapi.com.br);
- Medo & Ganância: CNN (ações dos EUA) e alternative.me (cripto).
Reservas, para quando a fonte principal falha (na nuvem, a CNBC dá 403 e a AwesomeAPI dá 429):
- índices dos EUA, VIX e juros de 10 anos: FRED, do Fed de St. Louis (fechamento do último pregão);
- dólar, euro e libra: PTAX do Banco Central (fechamento do último dia útil);
- bitcoin: CoinGecko.
Se nem a reserva funcionar, o painel sai sem aquela linha e avisa; nunca inventa número.
"""
import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import List, Optional

from . import cadernos
from .util import FUSO, agora_brasilia, http_get

CADERNO = "mercado"

URL_B3 = "https://cotacao.b3.com.br/mds/api/v1/instrumentQuotation/IBOV"
URL_CNBC = ("https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=%s"
            "&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json&events=1")
URL_MOEDAS = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL,EUR-USD,GBP-USD,BTC-BRL"
URL_CNN = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"
URL_CRIPTO = "https://api.alternative.me/fng/?limit=2"
URL_FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=%s"
URL_PTAX = ("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo("
            "moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='%s'"
            "&@dataInicial='%s'&@dataFinalCotacao='%s'&$format=json"
            "&$filter=tipoBoletim%%20eq%%20'Fechamento'&$select=cotacaoVenda,dataHoraCotacao")
URL_COINGECKO = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true"

# série do FRED → chave do painel
FRED = [("SP500", "sp500"), ("NASDAQCOM", "nasdaq"), ("DJIA", "dow"), ("VIXCLS", "vix"), ("DGS10", "juros10")]
LINKS = {
    "B3": "[B3](https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/ibovespa.htm)",
    "CNBC": "[CNBC](https://www.cnbc.com/markets/)",
    "FRED": "[FRED](https://fred.stlouisfed.org/)",
    "AwesomeAPI": "[AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)",
    "PTAX": "[PTAX do Banco Central](https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes)",
    "CoinGecko": "[CoinGecko](https://www.coingecko.com/pt/moedas/bitcoin)",
    "CNN": "[CNN](https://edition.cnn.com/markets/fear-and-greed)",
    "alternative.me": "[alternative.me](https://alternative.me/crypto/fear-and-greed-index/)",
}

# símbolo da CNBC → (chave, nome no painel, unidade)
CNBC = [
    (".SPX", "sp500", "S&P 500", "pts"),
    (".IXIC", "nasdaq", "Nasdaq", "pts"),
    (".DJI", "dow", "Dow Jones", "pts"),
    (".VIX", "vix", "VIX (o \"medo\" das opções)", ""),
    ("US10Y", "juros10", "Juros de 10 anos dos EUA", "%"),
    ("@LCO.1", "brent", "Petróleo Brent", "US$"),
    ("@GC.1", "ouro", "Ouro", "US$"),
    ("BTC.CM=", "btc_usd", "Bitcoin", "US$"),
]
# par da AwesomeAPI → (chave, nome, moeda de cotação)
MOEDAS = [
    ("USDBRL", "dolar", "Dólar", "R$"),
    ("EURBRL", "euro", "Euro", "R$"),
    ("GBPBRL", "libra", "Libra", "R$"),
    ("EURUSD", "euro_usd", "Euro em dólar", "US$"),
    ("GBPUSD", "libra_usd", "Libra em dólar", "US$"),
    ("BTCBRL", "btc_brl", "Bitcoin em real", "R$"),
]
ROTULO_MEDO = {"extreme fear": "medo extremo", "fear": "medo", "neutral": "neutro",
               "greed": "ganância", "extreme greed": "ganância extrema"}

# Gatilhos numéricos da edição extra (variação do dia, em %).
GATILHOS = {
    "ibov": 3.0, "sp500": 3.0, "nasdaq": 4.0, "dow": 3.0,
    "dolar": 2.5, "btc_usd": 10.0, "brent": 8.0,
}
VIX_ALARME = 35.0
MEDO_EXTREMO, GANANCIA_EXTREMA = 10, 90

_UA_NAVEGADOR = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/126 Safari/537.36")


# ───────────────────────── leitura das fontes ─────────────────────────

def _json(url: str, cabecalhos: Optional[dict] = None):
    cab = {"User-Agent": _UA_NAVEGADOR, "Accept": "application/json"}
    cab.update(cabecalhos or {})
    status, corpo, _ = http_get(url, timeout=20, cabecalhos=cab)
    if status != 200:
        trecho = re.sub(r"\s+", " ", (corpo or b"")[:160].decode("utf-8", "replace")).strip()
        raise RuntimeError("respondeu %s%s" % (status, (": " + trecho) if trecho else ""))
    return json.loads(corpo.decode("utf-8"))


def _numero(txt) -> Optional[float]:
    """'7,757.17' → 7757.17; '+0.58%' → 0.58; 'UNCH' → 0.0; vazio → None."""
    if txt is None:
        return None
    s = str(txt).strip()
    if s.upper() == "UNCH":
        return 0.0
    s = s.replace(",", "").replace("%", "").replace("+", "")
    try:
        return float(s)
    except ValueError:
        return None


def _data_cnbc(txt: str) -> str:
    """'2026-10-21' ou '2026-10-22T08:12:17.000-0400' → 'AAAA-MM-DD' (no horário de Brasília)."""
    if not txt:
        return ""
    if len(txt) == 10:
        return txt
    try:
        return datetime.strptime(txt[:19] + txt[23:], "%Y-%m-%dT%H:%M:%S%z").astimezone(FUSO).date().isoformat()
    except ValueError:
        return txt[:10]


def _b3() -> dict:
    d = _json(URL_B3)
    q = d["Trad"][0]["scty"]["SctyQtn"]
    # A B3 não diz de que pregão é o número. Antes das 10h (abertura), é o fechamento do último pregão.
    agora = agora_brasilia()
    quando = agora.date().isoformat() if agora.hour >= 10 else ""
    return {"ibov": {"nome": "Ibovespa", "valor": float(q["curPrc"]), "var": float(q["prcFlcn"]),
                     "unidade": "pts", "data": quando, "fonte": "B3"}}


def _cnbc() -> dict:
    simbolos = "%7C".join(s.replace("@", "%40").replace("=", "%3D") for s, _, _, _ in CNBC)
    d = _json(URL_CNBC % simbolos)
    por_simbolo = {q.get("symbol"): q for q in d["FormattedQuoteResult"]["FormattedQuote"]}
    saida = {}
    for simbolo, chave, nome, unidade in CNBC:
        q = por_simbolo.get(simbolo)
        valor = _numero(q.get("last")) if q else None
        if valor is None:
            continue
        item = {"nome": nome, "valor": valor, "var": _numero(q.get("change_pct")), "unidade": unidade,
                "data": _data_cnbc(q.get("last_time") or ""), "fonte": "CNBC"}
        if len(q.get("last_time") or "") > 10:  # cotação ao vivo (com horário), não fechamento
            item["hora"] = agora_brasilia().strftime("%H:%M")
        if chave == "juros10":  # para juros, a variação que importa é em pontos percentuais
            item["var_pp"] = _numero(q.get("change"))
        saida[chave] = item
    return saida


def _moedas() -> dict:
    d = _json(URL_MOEDAS)
    saida = {}
    for par, chave, nome, unidade in MOEDAS:
        q = d.get(par)
        if not q:
            continue
        saida[chave] = {"nome": nome, "valor": float(q["bid"]), "var": float(q["pctChange"]),
                        "unidade": unidade, "data": (q.get("create_date") or "")[:10],
                        "hora": (q.get("create_date") or "")[11:16], "fonte": "AwesomeAPI"}
    return saida


def _medo_cnn() -> dict:
    d = _json(URL_CNN, {"Referer": "https://edition.cnn.com/", "Origin": "https://edition.cnn.com"})
    f = d["fear_and_greed"]
    return {"medo_acoes": {"nome": "Ações dos EUA (CNN)", "valor": round(float(f["score"])),
                           "rotulo": ROTULO_MEDO.get(str(f.get("rating", "")).lower(), f.get("rating")),
                           "ontem": round(float(f["previous_close"])) if f.get("previous_close") is not None else None,
                           "semana": round(float(f["previous_1_week"])) if f.get("previous_1_week") is not None else None,
                           "fonte": "CNN"}}


def _medo_cripto() -> dict:
    d = _json(URL_CRIPTO)
    hoje, ontem = d["data"][0], (d["data"][1] if len(d["data"]) > 1 else None)
    return {"medo_cripto": {"nome": "Cripto (alternative.me)", "valor": int(hoje["value"]),
                            "rotulo": ROTULO_MEDO.get(hoje.get("value_classification", "").lower(),
                                                      hoje.get("value_classification")),
                            "ontem": int(ontem["value"]) if ontem else None, "fonte": "alternative.me"}}


def _fred_serie(serie: str):
    """Os dois últimos valores de uma série diária do FRED: [(data, valor), (data, valor)]."""
    # O FRED trava pedidos com cara de navegador; identificação simples passa. Duas tentativas.
    status, corpo = 0, b""
    for ua in ("InteligenciaPragmatica/1.0", "curl/8.7.1"):
        status, corpo, _ = http_get(URL_FRED % serie, timeout=20, cabecalhos={"User-Agent": ua})
        if status == 200:
            break
    if status != 200:
        raise RuntimeError("respondeu %s" % status)
    pontos = []
    for linha in corpo.decode("utf-8", "replace").splitlines()[1:]:
        partes = linha.split(",")
        if len(partes) == 2 and partes[1].strip() not in ("", "."):
            pontos.append((partes[0].strip(), float(partes[1])))
    if len(pontos) < 2:
        raise RuntimeError("série %s sem dados" % serie)
    return pontos[-2:]


def _fred() -> dict:
    """Reserva da CNBC para os EUA: fechamento do último pregão no FRED."""
    nomes = {chave: (nome, unidade) for _, chave, nome, unidade in CNBC}
    saida = {}
    for serie, chave in FRED:
        (_, anterior), (data, valor) = _fred_serie(serie)
        nome, unidade = nomes[chave]
        item = {"nome": nome, "valor": valor, "var": (valor / anterior - 1) * 100 if anterior else None,
                "unidade": unidade, "data": data, "fonte": "FRED"}
        if chave == "juros10":
            item["var_pp"] = valor - anterior
        saida[chave] = item
    return saida


def _ptax() -> dict:
    """Reserva da AwesomeAPI: PTAX de fechamento do Banco Central (último dia útil e o anterior)."""
    hoje = agora_brasilia().date()
    ini = (hoje - timedelta(days=10)).strftime("%m-%d-%Y")
    fim = hoje.strftime("%m-%d-%Y")
    cot = {}
    for moeda in ("USD", "EUR", "GBP"):
        valores = _json(URL_PTAX % (moeda, ini, fim)).get("value") or []
        if len(valores) < 2:
            raise RuntimeError("PTAX de %s sem dados" % moeda)
        cot[moeda] = [(v["dataHoraCotacao"][:10], float(v["cotacaoVenda"])) for v in valores[-2:]]
    saida = {}
    for moeda, chave, nome in (("USD", "dolar", "Dólar"), ("EUR", "euro", "Euro"), ("GBP", "libra", "Libra")):
        (_, antes), (data, agora) = cot[moeda]
        saida[chave] = {"nome": nome, "valor": agora, "var": (agora / antes - 1) * 100, "unidade": "R$",
                        "data": data, "fonte": "PTAX"}
    for moeda, chave, nome in (("EUR", "euro_usd", "Euro em dólar"), ("GBP", "libra_usd", "Libra em dólar")):
        antes = cot[moeda][0][1] / cot["USD"][0][1]
        agora = cot[moeda][1][1] / cot["USD"][1][1]
        saida[chave] = {"nome": nome, "valor": agora, "var": (agora / antes - 1) * 100, "unidade": "US$",
                        "data": cot["USD"][1][0], "fonte": "PTAX"}
    return saida


def _coingecko() -> dict:
    d = _json(URL_COINGECKO)["bitcoin"]
    return {"btc_usd": {"nome": "Bitcoin", "valor": float(d["usd"]), "var": float(d["usd_24h_change"]),
                        "unidade": "US$", "data": agora_brasilia().date().isoformat(),
                        "hora": agora_brasilia().strftime("%H:%M"), "fonte": "CoinGecko"}}


FONTES = [("B3", _b3), ("CNBC", _cnbc), ("AwesomeAPI", _moedas), ("CNN", _medo_cnn),
          ("alternative.me", _medo_cripto)]
# reserva → (chaves que ela cobre, principal que ela substitui)
RESERVAS = [
    ("FRED", _fred, ["sp500", "nasdaq", "dow", "vix", "juros10"], "CNBC"),
    ("PTAX", _ptax, ["dolar", "euro", "libra", "euro_usd", "libra_usd"], "AwesomeAPI"),
    ("CoinGecko", _coingecko, ["btc_usd"], "CNBC"),
]


def _rodar(fontes) -> tuple:
    dados, falhas = {}, {}
    with ThreadPoolExecutor(max(1, len(fontes))) as pool:
        futuros = [(nome, pool.submit(fn)) for nome, fn in fontes]
        for nome, fut in futuros:
            try:
                dados.update(fut.result())
            except Exception as e:  # uma fonte nunca derruba o painel
                falhas[nome] = str(e)[:160] or type(e).__name__
    return dados, falhas


def coletar_painel() -> dict:
    """Lê as fontes em paralelo e, onde a principal falhou, a reserva. O que faltar só some do painel."""
    dados, falhas = _rodar(FONTES)
    precisa = [(nome, fn) for nome, fn, chaves, _ in RESERVAS if any(c not in dados for c in chaves)]
    if precisa:
        extras, falhas_res = _rodar(precisa)
        for nome, fn, chaves, _ in RESERVAS:
            for c in chaves:
                if c not in dados and c in extras:
                    dados[c] = extras[c]
        falhas.update(falhas_res)
    reservas = sorted({i["fonte"] for i in dados.values()} & {nome for nome, _, _, _ in RESERVAS})
    return {"gerado_em": agora_brasilia().isoformat(timespec="seconds"), "itens": dados, "falhas": falhas,
            "reservas_usadas": reservas}


# ───────────────────────── painel em markdown ─────────────────────────

def _br(n: float, casas: int = 2) -> str:
    """Número no formato brasileiro: 7757.17 → '7.757,17'."""
    s = "{:,.{c}f}".format(n, c=casas)
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def _seta(var: Optional[float], casas: int = 2, sufixo: str = "%") -> str:
    if var is None:
        return ""
    if round(var, casas) == 0:
        return "· estável"
    return "%s %s%s" % ("▲" if var > 0 else "▼", _br(abs(var), casas), sufixo)


def _valor(item: dict) -> str:
    v, u = item["valor"], item["unidade"]
    if u == "pts":
        return "%s pts" % _br(v, 0)
    if u == "%":
        return "%s%%" % _br(v, 2)
    if u in ("R$", "US$"):
        casas = 0 if v >= 10000 else (4 if v < 2 else 2)
        return "%s %s" % (u, _br(v, casas))
    return _br(v, 2)


def _linha(item: dict) -> str:
    if "var_pp" in item and item["var_pp"] is not None:
        variacao = _seta(item["var_pp"], 2, " p.p.")
    else:
        variacao = _seta(item.get("var"))
    return "→ **%s**: %s %s" % (item["nome"], _valor(item), variacao)


def _dia(iso: str) -> str:
    try:
        d = date.fromisoformat(iso[:10])
        return "%02d/%02d" % (d.day, d.month)
    except ValueError:
        return ""


def painel_md(painel: dict) -> str:
    """O bloco do painel que entra no lugar de <!-- painel --> na edição."""
    it = painel["itens"]
    hora = painel["gerado_em"][11:16]
    blocos = []

    def quando(chaves):
        """Rótulo de tempo do bloco, pelo primeiro item: ao vivo (hora), fechamento (data) ou último fechamento."""
        primeiro = next((it[c] for c in chaves if c in it), None)
        if not primeiro:
            return ""
        if primeiro.get("hora"):
            return "às %s" % primeiro["hora"]
        if primeiro.get("data"):
            prefixo = "PTAX de " if primeiro.get("fonte") == "PTAX" else "fechamento de "
            return prefixo + _dia(primeiro["data"])
        return "último fechamento"

    def bloco(titulo, chaves):
        linhas = [_linha(it[c]) for c in chaves if c in it]
        if linhas:
            rotulo = quando(chaves)
            cab = "**%s**%s" % (titulo, (" · " + rotulo) if rotulo else "")
            blocos.append("\n\n".join([cab] + linhas))

    bloco("🇧🇷 Bolsa brasileira", ["ibov"])
    bloco("🇺🇸 Bolsas americanas", ["sp500", "nasdaq", "dow", "vix", "juros10"])
    bloco("💱 Moedas", ["dolar", "euro", "libra", "euro_usd", "libra_usd"])
    # O bitcoin em real (AwesomeAPI) mede a variação numa janela diferente da CNBC; mostrar os dois confunde.
    bloco("🛢️ Petróleo, ouro e bitcoin", ["brent", "ouro", "btc_usd"])

    medos = []
    for chave in ("medo_acoes", "medo_cripto"):
        if chave in it:
            m = it[chave]
            extra = []
            if m.get("ontem") is not None:
                extra.append("ontem %s" % m["ontem"])
            if m.get("semana") is not None:
                extra.append("uma semana atrás %s" % m["semana"])
            medos.append("→ **%s**: %s, %s%s" % (m["nome"], m["valor"], m["rotulo"],
                                                  (" (%s)" % "; ".join(extra)) if extra else ""))
    if medos:
        blocos.append("\n\n".join(["**😨 Medo & Ganância** · de 0 (medo extremo) a 100 (ganância extrema)"] + medos))

    usadas = [LINKS[f] for f in LINKS if f in {i.get("fonte") for i in it.values()}]
    rodape = "🔗 Números coletados às %s, sem passar pela IA: %s." % (hora, " · ".join(usadas))
    fora = sorted(f for f in painel.get("falhas") or {} if f not in {i.get("fonte") for i in it.values()})
    if fora:
        rodape += " Fora do ar hoje: %s." % ", ".join(fora)
    return "#### 📊 PAINEL\n\n" + "\n\n".join(blocos) + "\n\n" + rodape + "\n"


# ───────────────────────── alarme da edição extra ─────────────────────────

def alarme(painel: dict, hoje: Optional[date] = None) -> List[str]:
    """Motivos numéricos para uma edição extra. Só conta variação de pregão de hoje."""
    hoje = hoje or agora_brasilia().date()
    it = painel["itens"]
    motivos = []
    for chave, limite in GATILHOS.items():
        item = it.get(chave)
        if not item or item.get("var") is None:
            continue
        if item.get("data") and item["data"] != hoje.isoformat():
            continue  # número de outro dia (feriado, mercado fechado)
        if abs(item["var"]) >= limite:
            motivos.append("%s %s no dia (gatilho: %s%%)" % (item["nome"], _seta(item["var"]), _br(limite, 1)))
    vix = it.get("vix")
    if vix and vix["valor"] >= VIX_ALARME:
        motivos.append("VIX em %s (gatilho: %s)" % (_br(vix["valor"]), _br(VIX_ALARME, 0)))
    medo = it.get("medo_acoes")
    if medo and (medo["valor"] <= MEDO_EXTREMO or medo["valor"] >= GANANCIA_EXTREMA):
        motivos.append("Medo & Ganância das ações em %s (%s)" % (medo["valor"], medo["rotulo"]))
    return motivos


# ───────────────────────── gravação ─────────────────────────

def gravar_painel(pasta_edicao: str, raiz: Path, painel: Optional[dict] = None) -> dict:
    """Coleta (se preciso) e grava painel.md na pasta da edição e o JSON em dados/mercado/."""
    raiz = Path(raiz)
    painel = painel or coletar_painel()
    destino = cadernos.pasta_edicoes(raiz, CADERNO) / pasta_edicao
    destino.mkdir(parents=True, exist_ok=True)
    texto = painel_md(painel)
    (destino / "painel.md").write_text(texto, encoding="utf-8")
    dados = raiz / "dados" / CADERNO
    dados.mkdir(parents=True, exist_ok=True)
    (dados / ("%s.json" % pasta_edicao)).write_text(json.dumps(painel, ensure_ascii=False, indent=2),
                                                    encoding="utf-8")
    return {"painel": painel, "texto": texto, "arquivo": (destino / "painel.md").relative_to(raiz).as_posix()}


def pasta_valida(nome: str) -> bool:
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}(-extra)?", nome or ""))
