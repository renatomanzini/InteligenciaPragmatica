"""Caderno Economia: o painel de números oficiais e os dados de apoio da pauta.

Os números entram na edição por código, nunca pela IA. Todas as fontes são oficiais, públicas e sem chave:
- Banco Central, SGS (api.bcb.gov.br): Selic, IPCA, IBC-Br, desemprego (a PNAD do IBGE, pela série do BC),
  dívida bruta, resultado primário e dólar PTAX;
- Banco Central, Focus (olinda.bcb.gov.br): as medianas das apostas do mercado;
- IBGE, SIDRA (apisidra.ibge.gov.br): o PIB trimestral;
- IBGE, serviço de dados (servicodados.ibge.gov.br): os releases publicados e o calendário de divulgações,
  que vão para o arquivo de apoio da pauta (oficiais.md), e não para a edição.
Reservas, para quando o SGS falha: o SIDRA para o IPCA e o desemprego, e a PTAX do Olinda para o dólar.
Se nem a reserva funcionar, o painel sai sem aquela linha e avisa; nunca inventa número.
O painel marca com 🆕 o dado que saiu desde a última edição (o período de referência mudou).
"""
import gzip
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path
from typing import List, Optional, Tuple
from urllib.parse import quote

from . import cadernos, historico
from .mercado import URL_PTAX, _UA_NAVEGADOR, _br  # o mesmo formato de número do Mercado
from .util import FUSO, agora_brasilia, http_get

CADERNO = "economia"

URL_SGS = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.%d/dados?formato=json&dataInicial=%s&dataFinal=%s"
URL_FOCUS = ("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais"
             "?$format=json&$top=2000&$orderby=Data%%20desc&$select=Indicador,Data,DataReferencia,Mediana&$filter=%s")
URL_SIDRA = "https://apisidra.ibge.gov.br/values/t/%s/n1/all/v/%s/p/last%%20%d%s"
URL_IBGE_RELEASES = "https://servicodados.ibge.gov.br/api/v3/noticias/?tipo=release&qtd=60&de=%s&ate=%s"
URL_IBGE_CALENDARIO = "https://servicodados.ibge.gov.br/api/v3/calendario/?qtd=100&de=%s&ate=%s"

# séries do SGS
SELIC, IPCA_MES, IPCA_12M, IBCBR, DESEMPREGO, DIVIDA, PRIMARIO, PTAX = 432, 433, 13522, 24364, 24369, 13762, 5793, 1

# Meta de inflação do CMN: 3% ao ano, com 1,5 ponto de tolerância (meta contínua desde 2025).
META_IPCA, TOLERANCIA_IPCA = 3.0, 1.5

# indicador do Focus → nome no painel
FOCUS = [("IPCA", "IPCA"), ("Selic", "Selic no fim do ano"), ("PIB Total", "PIB"), ("Câmbio", "Dólar no fim do ano")]

LINKS = {
    "SGS": "[Banco Central (SGS)](https://dadosabertos.bcb.gov.br/)",
    "Focus": "[Focus](https://www.bcb.gov.br/publicacoes/focus)",
    "SIDRA": "[IBGE (SIDRA)](https://sidra.ibge.gov.br/)",
    "PTAX": "[PTAX do Banco Central](https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes)",
}
# dados que ganham 🆕 quando saem (dólar e Focus mudam toda semana; marcar seria ruído)
MARCAVEIS = ["selic", "ipca", "pib", "ibcbr", "desemprego", "divida", "primario"]

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro",
         "novembro", "dezembro"]


# ───────────────────────── leitura das fontes ─────────────────────────

def _json(url: str, tentativas: int = 3):
    """GET de JSON com novas tentativas: a API do BC às vezes não responde quando recebe vários pedidos juntos."""
    status, corpo = 0, b""
    for i in range(tentativas):
        status, corpo, _ = http_get(url, timeout=25, cabecalhos={"User-Agent": _UA_NAVEGADOR,
                                                                 "Accept": "application/json"})
        if status == 200:
            if corpo[:2] == b"\x1f\x8b":  # o IBGE às vezes manda gzip sem a gente pedir
                corpo = gzip.decompress(corpo)
            return json.loads(corpo.decode("utf-8"))
        if status not in (0, 429) and status < 500:
            break
        time.sleep(1.5 * (i + 1))
    trecho = re.sub(r"\s+", " ", (corpo or b"")[:160].decode("utf-8", "replace")).strip()
    raise RuntimeError("respondeu %s%s" % (status, (": " + trecho) if trecho else ""))


def _dmy(d: date) -> str:
    return d.strftime("%d/%m/%Y")


def _sgs(codigo: int, inicio: date, fim: date) -> List[Tuple[date, float]]:
    """Os pontos de uma série do SGS entre duas datas, do mais antigo para o mais novo."""
    pontos = []
    for p in _json(URL_SGS % (codigo, _dmy(inicio), _dmy(fim))):
        dia, mes, ano = p["data"].split("/")
        pontos.append((date(int(ano), int(mes), int(dia)), float(p["valor"])))
    if not pontos:
        raise RuntimeError("série %d sem dados" % codigo)
    return sorted(pontos)


def _mes(d: date) -> str:
    return "%04d-%02d" % (d.year, d.month)


def _selic(hoje: date) -> dict:
    """Meta da Selic de hoje, desde quando vale e a anterior. A série do BC já traz os dias até a próxima
    decisão do Copom, com a taxa de hoje repetida: o último dia dela é a data da próxima decisão."""
    pontos = _sgs(SELIC, hoje - timedelta(days=500), hoje + timedelta(days=120))
    passado = [p for p in pontos if p[0] <= hoje]
    if not passado:
        raise RuntimeError("Selic sem dado até hoje")
    valor = passado[-1][1]
    desde, antes = None, None  # sem mudança nos 500 dias pedidos: não sabemos desde quando
    for (d0, v0), (d1, v1) in zip(passado, passado[1:]):
        if v1 != v0:
            desde, antes = d1, v0
    proxima = pontos[-1][0] if pontos[-1][0] > hoje else None
    return {"valor": valor, "desde": desde.isoformat() if desde else None, "antes": antes,
            "proximo_copom": proxima.isoformat() if proxima else None,
            "ref": desde.isoformat() if desde else "sem-mudanca", "fonte": "SGS"}


def _ipca(hoje: date) -> dict:
    mes = _sgs(IPCA_MES, hoje - timedelta(days=120), hoje)
    doze = _sgs(IPCA_12M, hoje - timedelta(days=120), hoje)
    if mes[-1][0] != doze[-1][0] or len(doze) < 2:
        raise RuntimeError("IPCA do mês e de 12 meses desencontrados")
    return {"mes": mes[-1][1], "doze": doze[-1][1], "doze_antes": doze[-2][1], "ref": _mes(mes[-1][0]),
            "fonte": "SGS"}


def _ibcbr(hoje: date) -> dict:
    pontos = _sgs(IBCBR, hoje - timedelta(days=150), hoje)
    if len(pontos) < 2:
        raise RuntimeError("IBC-Br sem dois meses")
    (_, antes), (d, valor) = pontos[-2:]
    return {"var": (valor / antes - 1) * 100, "ref": _mes(d), "fonte": "SGS"}


def _desemprego_de(pontos: List[Tuple[str, float]], fonte: str) -> dict:
    """pontos: [(AAAA-MM do fim do trimestre móvel, taxa)], do mais antigo ao mais novo, desde o início da série."""
    if len(pontos) < 13:
        raise RuntimeError("desemprego com menos de 13 meses")
    ref, valor = pontos[-1]
    return {"valor": valor, "antes": pontos[-2][1], "ano_antes": pontos[-13][1],
            "menor_da_serie": valor <= min(v for _, v in pontos[:-1]), "ref": ref, "fonte": fonte}


def _desemprego(hoje: date) -> dict:
    # a PNAD Contínua começa em 2012: pedir a série inteira permite dizer "o menor da série"
    pontos = _sgs(DESEMPREGO, date(2012, 1, 1), hoje)
    return _desemprego_de([(_mes(d), v) for d, v in pontos], "SGS")


def _mensal_pct_pib(codigo: int, hoje: date) -> dict:
    pontos = _sgs(codigo, hoje - timedelta(days=150), hoje)
    if len(pontos) < 2:
        raise RuntimeError("série %d sem dois meses" % codigo)
    return {"valor": pontos[-1][1], "antes": pontos[-2][1], "ref": _mes(pontos[-1][0]), "fonte": "SGS"}


def _dolar_de(pontos: List[Tuple[date, float]], fonte: str) -> dict:
    """pontos: cotações de fechamento desde o fim do ano anterior."""
    data, valor = pontos[-1]
    ano_antes = [v for d, v in pontos if d.year < data.year]
    return {"valor": valor, "data": data.isoformat(), "fonte": fonte, "ref": data.isoformat(),
            "var_ano": (valor / ano_antes[-1] - 1) * 100 if ano_antes else None}


def _dolar(hoje: date) -> dict:
    return _dolar_de(_sgs(PTAX, date(hoje.year - 1, 12, 15), hoje), "SGS")


def _dolar_ptax(hoje: date) -> dict:
    """Reserva do SGS: a PTAX de fechamento pelo Olinda, o mesmo serviço que o Mercado usa."""
    url = URL_PTAX % ("USD", date(hoje.year - 1, 12, 15).strftime("%m-%d-%Y"), hoje.strftime("%m-%d-%Y"))
    valores = _json(url).get("value") or []
    if not valores:
        raise RuntimeError("PTAX sem dados")
    return _dolar_de(sorted((date.fromisoformat(v["dataHoraCotacao"][:10]), float(v["cotacaoVenda"]))
                            for v in valores), "PTAX")


def _sidra(tabela: str, variaveis: str, ultimos: int, extra: str = "") -> List[dict]:
    """Linhas de uma tabela do SIDRA (sem o cabeçalho): cada uma com D2C (variável), D3C (período) e V (valor)."""
    linhas = _json(URL_SIDRA % (tabela, variaveis, ultimos, extra))
    saida = []
    for linha in linhas[1:]:
        try:
            saida.append({"var": linha["D2C"], "periodo": linha["D3C"], "valor": float(linha["V"])})
        except (KeyError, ValueError):  # "..." ou "-" quando o dado não existe
            continue
    if not saida:
        raise RuntimeError("tabela %s sem dados" % tabela)
    return saida


def _pib() -> dict:
    linhas = _sidra("5932", "6561,6564", 1, "/c11255/90707")
    por_var = {l["var"]: l for l in linhas}
    if "6564" not in por_var or "6561" not in por_var:
        raise RuntimeError("PIB sem as duas taxas")
    return {"tri": por_var["6564"]["valor"], "ano": por_var["6561"]["valor"], "ref": por_var["6564"]["periodo"],
            "fonte": "SIDRA"}


def _ipca_sidra() -> dict:
    linhas = _sidra("7060", "63,2265", 2, "/c315/7169")
    mes = sorted((l["periodo"], l["valor"]) for l in linhas if l["var"] == "63")
    doze = sorted((l["periodo"], l["valor"]) for l in linhas if l["var"] == "2265")
    if not mes or len(doze) < 2:
        raise RuntimeError("IPCA incompleto")
    p = mes[-1][0]
    return {"mes": mes[-1][1], "doze": doze[-1][1], "doze_antes": doze[-2][1], "ref": "%s-%s" % (p[:4], p[4:]),
            "fonte": "SIDRA"}


def _desemprego_sidra() -> dict:
    linhas = sorted((l["periodo"], l["valor"]) for l in _sidra("6381", "4099", 200) if l["var"] == "4099")
    return _desemprego_de([("%s-%s" % (p[:4], p[4:]), v) for p, v in linhas], "SIDRA")


def _focus(hoje: date) -> dict:
    """Medianas do Focus para este ano e o próximo, na data mais recente e na de 4 semanas antes."""
    anos = [str(hoje.year), str(hoje.year + 1)]
    filtro = "(%s) and baseCalculo eq 0 and (%s) and Data ge '%s'" % (
        " or ".join("Indicador eq '%s'" % i for i, _ in FOCUS),
        " or ".join("DataReferencia eq '%s'" % a for a in anos),
        (hoje - timedelta(days=50)).isoformat())
    linhas = _json(URL_FOCUS % quote(filtro, safe="'()")).get("value") or []
    if not linhas:
        raise RuntimeError("Focus sem dados")
    datas = sorted({l["Data"] for l in linhas})
    recente = datas[-1]
    limite = (date.fromisoformat(recente) - timedelta(days=28)).isoformat()
    antes = max([d for d in datas if d <= limite] or [datas[0]])
    valores = {}
    for l in linhas:
        if l["Data"] in (recente, antes) and l.get("Mediana") is not None:
            valores.setdefault(l["Indicador"], {}).setdefault(l["DataReferencia"], {})[
                "agora" if l["Data"] == recente else "antes"] = float(l["Mediana"])
    return {"data": recente, "antes_data": antes, "anos": anos, "valores": valores, "ref": recente, "fonte": "Focus"}


def _fontes(hoje: date) -> list:
    """(nome no rodapé, função, chaves que ela cobre)."""
    return [
        ("Selic (BC)", lambda: {"selic": _selic(hoje)}, ["selic"]),
        ("IPCA (BC)", lambda: {"ipca": _ipca(hoje)}, ["ipca"]),
        ("IBC-Br (BC)", lambda: {"ibcbr": _ibcbr(hoje)}, ["ibcbr"]),
        ("Desemprego (BC)", lambda: {"desemprego": _desemprego(hoje)}, ["desemprego"]),
        ("Dívida (BC)", lambda: {"divida": _mensal_pct_pib(DIVIDA, hoje)}, ["divida"]),
        ("Primário (BC)", lambda: {"primario": _mensal_pct_pib(PRIMARIO, hoje)}, ["primario"]),
        ("Dólar (BC)", lambda: {"dolar": _dolar(hoje)}, ["dolar"]),
        ("PIB (IBGE)", lambda: {"pib": _pib()}, ["pib"]),
        ("Focus (BC)", lambda: {"focus": _focus(hoje)}, ["focus"]),
    ]


def _reservas(hoje: date) -> list:
    return [
        ("IPCA (IBGE)", lambda: {"ipca": _ipca_sidra()}, ["ipca"]),
        ("Desemprego (IBGE)", lambda: {"desemprego": _desemprego_sidra()}, ["desemprego"]),
        ("PTAX (BC)", lambda: {"dolar": _dolar_ptax(hoje)}, ["dolar"]),
    ]


def _rodar(fontes, trabalhadores: int = 4) -> tuple:
    dados, falhas = {}, {}
    with ThreadPoolExecutor(trabalhadores) as pool:  # poucos de cada vez: o SGS do BC derruba pedidos em rajada
        futuros = [(nome, pool.submit(fn)) for nome, fn, _ in fontes]
        for nome, fut in futuros:
            try:
                dados.update(fut.result())
            except Exception as e:  # uma fonte nunca derruba o painel
                falhas[nome] = str(e)[:160] or type(e).__name__
    return dados, falhas


def coletar_painel(hoje: Optional[date] = None) -> dict:
    """Lê as fontes em paralelo e, onde a principal falhou, a reserva. O que faltar só some do painel."""
    hoje = hoje or agora_brasilia().date()
    fontes = _fontes(hoje)
    dados, falhas = _rodar(fontes)
    # Na nuvem, o SGS às vezes não responde quando recebe vários pedidos juntos (22/10, o IBC-Br):
    # as que falharam tentam mais uma vez, uma de cada vez, antes das reservas.
    de_novo = [f for f in fontes if f[0] in falhas]
    if de_novo:
        extras, falhas_de_novo = _rodar(de_novo, 1)
        dados.update(extras)
        for nome, _, _ in de_novo:
            falhas.pop(nome, None)
        falhas.update(falhas_de_novo)
    precisa = [r for r in _reservas(hoje) if any(c not in dados for c in r[2])]
    if precisa:
        extras, falhas_res = _rodar(precisa)
        for chave, item in extras.items():
            dados.setdefault(chave, item)
        falhas.update(falhas_res)
    fora = sorted(nome for nome, _, chaves in _fontes(hoje) + _reservas(hoje)
                  if nome in falhas and any(c not in dados for c in chaves))
    return {"gerado_em": agora_brasilia().isoformat(timespec="seconds"), "itens": dados, "falhas": falhas,
            "fora_do_ar": fora, "novos": [], "anterior": None}


# ───────────────────────── painel em markdown ─────────────────────────

def _pct(v: float, casas: int = 2) -> str:
    """Percentual arredondado como nas notas oficiais (82,55 → 82,6, e não 82,5 do arredondamento binário)."""
    arredondado = float(Decimal(str(v)).quantize(Decimal(1).scaleb(-casas), rounding=ROUND_HALF_UP))
    return "%s%%" % _br(arredondado, casas)


def _var(v: Optional[float], casas: int = 2) -> str:
    """Variação com seta: ▲ 0,34% / ▼ 1,20% / estável."""
    if v is None:
        return ""
    if round(v, casas) == 0:
        return "estável"
    return "%s %s" % ("▲" if v > 0 else "▼", _pct(abs(v), casas))


def _dia(iso: str) -> str:
    """'2026-09-17' → '17/09' (com o ano, se não for o ano corrente)."""
    d = date.fromisoformat(iso[:10])
    if d.year != agora_brasilia().year:
        return "%02d/%02d/%d" % (d.day, d.month, d.year)
    return "%02d/%02d" % (d.day, d.month)


def _nome_mes(ref: str) -> str:
    """'2026-09' → 'setembro'."""
    return MESES[int(ref[5:7]) - 1]


def _mes_anterior(ref: str) -> str:
    return MESES[(int(ref[5:7]) - 2) % 12]


def _trimestre(ref: str) -> str:
    """'202602' → '2º tri de 2026'."""
    return "%dº tri de %s" % (int(ref[4:]), ref[:4])


def _linhas(it: dict) -> dict:
    """Uma linha por chave do painel (só as que têm dado)."""
    saida = {}
    if "selic" in it:
        s = it["selic"]
        txt = "→ **Selic (o juro básico)**: %s ao ano" % _pct(s["valor"])
        txt += (" · desde %s" % _dia(s["desde"])) if s.get("desde") else " · sem mudança há mais de um ano"
        if s.get("antes") is not None:
            txt += ", quando %s de %s" % ("caiu" if s["valor"] < s["antes"] else "subiu", _pct(s["antes"]))
        if s.get("proximo_copom"):
            txt += " · próxima decisão do Copom: %s" % _dia(s["proximo_copom"])
        saida["selic"] = txt
    if "ipca" in it:
        i = it["ipca"]
        saida["ipca"] = ("→ **IPCA (a inflação oficial)**: %s em %s · %s em 12 meses (até %s: %s) · a meta é %s, "
                         "com teto de %s" % (_pct(i["mes"]), _nome_mes(i["ref"]), _pct(i["doze"]),
                                             _mes_anterior(i["ref"]), _pct(i["doze_antes"]),
                                             _pct(META_IPCA, 0), _pct(META_IPCA + TOLERANCIA_IPCA, 1)))
    if "pib" in it:
        p = it["pib"]
        saida["pib"] = "→ **PIB**: %s no %s sobre o trimestre anterior · %s sobre um ano antes" % (
            _var(p["tri"], 1), _trimestre(p["ref"]), _var(p["ano"], 1))
    if "ibcbr" in it:
        b = it["ibcbr"]
        saida["ibcbr"] = "→ **IBC-Br (a prévia mensal do PIB, feita pelo BC)**: %s em %s sobre %s" % (
            _var(b["var"]), _nome_mes(b["ref"]), _mes_anterior(b["ref"]))
    if "desemprego" in it:
        d = it["desemprego"]
        txt = "→ **Desemprego**: %s no trimestre até %s (até %s: %s; um ano antes: %s)" % (
            _pct(d["valor"], 1), _nome_mes(d["ref"]), _mes_anterior(d["ref"]), _pct(d["antes"], 1),
            _pct(d["ano_antes"], 1))
        if d.get("menor_da_serie"):
            txt += " · o menor da série, que começa em 2012"
        saida["desemprego"] = txt
    if "divida" in it:
        v = it["divida"]
        saida["divida"] = "→ **Dívida bruta do governo**: %s do PIB em %s (%s: %s)" % (
            _pct(v["valor"], 1), _nome_mes(v["ref"]), _mes_anterior(v["ref"]), _pct(v["antes"], 1))
    if "primario" in it:
        v = it["primario"]

        def saldo(x):  # a série do BC mede a necessidade de financiamento: positivo é déficit
            return ("déficit de %s" if x > 0 else "superávit de %s") % _pct(abs(x))
        saida["primario"] = ("→ **Resultado primário em 12 meses** (receitas menos despesas, sem os juros): %s do "
                             "PIB até %s (até %s: %s)" % (saldo(v["valor"]), _nome_mes(v["ref"]),
                                                          _mes_anterior(v["ref"]), saldo(v["antes"])))
    if "dolar" in it:
        v = it["dolar"]
        txt = "→ **Dólar (PTAX, a cotação oficial do BC)**: R$ %s em %s" % (_br(v["valor"], 4), _dia(v["data"]))
        if v.get("var_ano") is not None:
            txt += " · %s no ano" % _var(v["var_ano"], 1)
        saida["dolar"] = txt
    if "focus" in it:
        f = it["focus"]
        for indicador, nome in FOCUS:
            por_ano = f["valores"].get(indicador) or {}
            partes = []
            for ano in f["anos"]:
                v = por_ano.get(ano) or {}
                if "agora" not in v:
                    continue
                fmt = (lambda x: "R$ %s" % _br(x, 2)) if indicador == "Câmbio" else (lambda x: _pct(x))
                partes.append("%s em %s%s" % (fmt(v["agora"]), ano, (" (%s)" % fmt(v["antes"])) if "antes" in v else ""))
            if partes:
                saida["focus_" + indicador] = "→ **%s**: %s" % (nome, " · ".join(partes))
    return saida


def painel_md(painel: dict) -> str:
    """O bloco do painel que entra no lugar de <!-- painel --> na edição."""
    it = painel["itens"]
    linhas = _linhas(it)
    novos = set(painel.get("novos") or [])
    blocos = []

    def bloco(titulo, chaves):
        corpo = [linhas[c] + (" · 🆕" if c in novos else "") for c in chaves if c in linhas]
        if corpo:
            blocos.append("\n\n".join([titulo] + corpo))

    bloco("**🏦 Juros e inflação**", ["selic", "ipca"])
    bloco("**📈 Atividade e emprego**", ["pib", "ibcbr", "desemprego"])
    bloco("**🏛️ Contas públicas**", ["divida", "primario"])
    bloco("**💱 Câmbio**", ["dolar"])
    if "focus" in it:
        f = it["focus"]
        bloco("**🔮 O que o mercado espera** · mediana do Focus de %s; entre parênteses, a de %s"
              % (_dia(f["data"]), _dia(f["antes_data"])), ["focus_" + i for i, _ in FOCUS])

    hora = painel["gerado_em"][11:16]
    usadas = [LINKS[f] for f in LINKS if f in {i.get("fonte") for i in it.values()}]
    rodape = "🔗 Números oficiais coletados às %s, sem passar pela IA: %s." % (hora, " · ".join(usadas))
    if novos:
        rodape += " 🆕 = saiu desde a última edição"
        rodape += " (%s)." % _dia(painel["anterior"]) if painel.get("anterior") else "."
    if painel.get("fora_do_ar"):
        rodape += " Fora do ar hoje: %s." % ", ".join(painel["fora_do_ar"])
    return "#### 📊 PAINEL\n\n" + "\n\n".join(blocos) + "\n\n" + rodape + "\n"


# ───────────────────────── apoio da pauta (IBGE) ─────────────────────────

def _ibge_releases(desde: date, ate: date) -> List[dict]:
    d = _json(URL_IBGE_RELEASES % (desde.strftime("%m-%d-%Y"), ate.strftime("%m-%d-%Y")))
    saida = []
    for it in d.get("items") or []:
        saida.append({"quando": it.get("data_publicacao", "")[:16], "titulo": it.get("titulo", ""),
                      "resumo": (it.get("introducao") or "")[:300],
                      "link": (it.get("link") or "").replace("http://", "https://", 1)})
    return saida


def _ibge_agenda(de: date, ate: date) -> List[dict]:
    """Divulgações de indicadores do IBGE no período. O calendário vem em UTC; aqui sai em Brasília."""
    d = _json(URL_IBGE_CALENDARIO % (de.strftime("%m-%d-%Y"), ate.strftime("%m-%d-%Y")))
    saida = []
    for it in d.get("items") or []:
        if it.get("tipo") != "Divulgação de Indicadores":
            continue
        try:
            quando = datetime.strptime(it["data_divulgacao"], "%d/%m/%Y %H:%M:%S").replace(tzinfo=timezone.utc)
        except (KeyError, ValueError):
            continue
        saida.append({"quando": quando.astimezone(FUSO).strftime("%d/%m %H:%M"), "titulo": it.get("titulo", ""),
                      "ordem": quando.isoformat()})
    return sorted(saida, key=lambda x: x["ordem"])


def apoio(painel: dict, desde: date, hoje: date) -> Tuple[str, List[str]]:
    """O arquivo oficiais.md (fora da edição): releases do IBGE desde a última edição, agenda dos próximos
    8 dias e o que mudou no painel. Devolve (texto, falhas)."""
    falhas = []
    linhas = ["# Dados oficiais para a pauta (%s)" % hoje.isoformat(), "",
              "Serve para achar pauta e conferir número. Na edição, o link é o do release oficial.", ""]
    novos = painel.get("novos") or []
    nomes = {"selic": "Selic", "ipca": "IPCA", "pib": "PIB", "ibcbr": "IBC-Br", "desemprego": "desemprego",
             "divida": "dívida bruta", "primario": "resultado primário"}
    linhas.append("## Dados do painel que saíram desde a última edição")
    linhas.append(", ".join(nomes[n] for n in novos) + "." if novos else "Nenhum.")
    linhas.append("")
    try:
        rel = _ibge_releases(desde, hoje)
        linhas.append("## Releases do IBGE desde %s (%d)" % (_dia(desde.isoformat()), len(rel)))
        linhas += ["- %s · %s — %s (%s)" % (r["quando"], r["titulo"], r["resumo"], r["link"]) for r in rel] or ["Nenhum."]
    except Exception as e:
        falhas.append("releases do IBGE (%s)" % str(e)[:100])
        linhas.append("## Releases do IBGE: fora do ar hoje")
    linhas.append("")
    try:
        agenda = _ibge_agenda(hoje, hoje + timedelta(days=8))
        linhas.append("## Próximas divulgações do IBGE (8 dias, horário de Brasília)")
        linhas += ["- %s · %s" % (a["quando"], a["titulo"]) for a in agenda] or ["Nenhuma."]
    except Exception as e:
        falhas.append("calendário do IBGE (%s)" % str(e)[:100])
        linhas.append("## Calendário do IBGE: fora do ar hoje")
    selic = painel["itens"].get("selic") or {}
    if selic.get("proximo_copom"):
        linhas.append("- Copom: próxima decisão da Selic em %s, à noite (pela série da Selic do BC)."
                      % _dia(selic["proximo_copom"]))
    return "\n".join(linhas) + "\n", falhas


# ───────────────────────── gravação ─────────────────────────

def _novos(painel: dict, anterior: Optional[dict]) -> List[str]:
    """Chaves cujo período de referência mudou desde o painel anterior (sem painel anterior: nenhuma)."""
    if not anterior:
        return []
    antigos = anterior.get("itens") or {}
    return [c for c in MARCAVEIS if c in painel["itens"] and c in antigos
            and painel["itens"][c].get("ref") != antigos[c].get("ref")]


def gravar_painel(pasta_edicao: str, raiz: Path, painel: Optional[dict] = None, hoje: Optional[date] = None) -> dict:
    """Coleta (se preciso) e grava painel.md e oficiais.md na pasta da edição e o JSON em dados/economia/."""
    raiz = Path(raiz)
    hoje = hoje or agora_brasilia().date()
    painel = painel or coletar_painel(hoje)
    ultima = historico.ultima_data(raiz, CADERNO, antes_de=pasta_edicao)
    anterior = None
    if ultima and (raiz / "dados" / CADERNO / ("%s.json" % ultima)).exists():
        anterior = json.loads((raiz / "dados" / CADERNO / ("%s.json" % ultima)).read_text(encoding="utf-8"))
    painel["novos"] = _novos(painel, anterior)
    painel["anterior"] = ultima
    destino = cadernos.pasta_edicoes(raiz, CADERNO) / pasta_edicao
    destino.mkdir(parents=True, exist_ok=True)
    texto = painel_md(painel)
    (destino / "painel.md").write_text(texto, encoding="utf-8")
    desde = date.fromisoformat(ultima) if ultima else hoje - timedelta(days=7)
    texto_apoio, falhas_apoio = apoio(painel, desde, hoje)
    (destino / "oficiais.md").write_text(texto_apoio, encoding="utf-8")
    dados = raiz / "dados" / CADERNO
    dados.mkdir(parents=True, exist_ok=True)
    (dados / ("%s.json" % pasta_edicao)).write_text(json.dumps(painel, ensure_ascii=False, indent=2),
                                                    encoding="utf-8")
    rel = lambda p: p.relative_to(raiz).as_posix()  # noqa: E731
    return {"painel": painel, "texto": texto, "arquivo": rel(destino / "painel.md"),
            "apoio": rel(destino / "oficiais.md"), "falhas_apoio": falhas_apoio}
