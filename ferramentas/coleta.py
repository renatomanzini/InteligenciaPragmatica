"""Coleta de candidatos: RSS, fontes especiais (APIs), radar de newsletters.

Uso: coletar(data, raiz) -> dict. Grava em dados/candidatos/AAAA-MM-DD.md e -fontes.log.
Nenhuma falha de fonte derruba a coleta: o erro vai para o log e a coleta segue.
"""
import hashlib
import html
import json
import re
import threading
import time
import unicodedata
import zlib
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import parse_qsl, quote, urlencode, urljoin, urlsplit, urlunsplit

try:  # o feedparser precisa do sgmllib; na nuvem o pip não compila o sgmllib3k, então usamos a cópia local
    import sgmllib  # noqa: F401
except ImportError:
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent / "_vendor"))
import feedparser  # noqa: E402

from . import cadernos, github, historico
from .util import FUSO, agora_brasilia, hoje_brasilia, http_get, ler_yaml, normalizar_url

WORKERS = 8
TIMEOUT = 20
PRAZO = 25  # tempo total máximo da 1ª tentativa (s)
PRAZO_RETENTATIVA = 12
RESUMO_JSON = 300
RESUMO_MD = 160
FILTRO_RESUMO = 400  # quanto do resumo o filtro de fonte olha
RADAR_MAX_PAGINAS = 8
RADAR_MAX_BYTES = 1_500_000  # o suficiente para ler os intertítulos da edição

# Temas na ordem em que aparecem no .md.
TEMAS = [
    ("ia", "Inteligência Artificial"),
    ("china", "China"),
    ("economia", "Economia"),
    ("negocios", "Negócios"),
    ("marketing", "Marketing"),
    ("direito_tech", "Direito & Tech"),
    ("filosofia", "Filosofia"),
    ("comunidade", "Comunidade"),
]
ORDEM_TIPO = {"primaria": 0, "analise": 1, "imprensa": 2, "comunidade": 3}

# Parâmetros de rastreamento que não fazem parte da identidade da página.
_RASTREIO = re.compile(r"^(utm_|fbclid|gclid|mc_|ref$|ref_|source$|cmp$|mod$)", re.I)


# ───────────────────────── utilidades ─────────────────────────

def _descompactar(corpo: bytes) -> bytes:
    """Alguns sites mandam gzip mesmo sem pedirmos (e o urllib não descompacta)."""
    if corpo[:2] == b"\x1f\x8b":
        try:
            return zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(corpo)
        except Exception:
            return corpo
    return corpo


def _http_com_prazo(url: str, timeout: int, prazo: float, max_bytes: Optional[int],
                    cabecalhos: Optional[dict]) -> Tuple[int, bytes, str]:
    """http_get com prazo total. O timeout do urllib vale por operação: um site com vários IPs
    fora do ar, ou que pinga os bytes aos poucos, pode levar minutos. Passado o prazo,
    seguimos adiante (a linha de execução esquecida morre sozinha, é daemon)."""
    resposta = []

    def alvo():
        resposta.append(http_get(url, timeout=timeout, max_bytes=max_bytes, cabecalhos=cabecalhos))

    th = threading.Thread(target=alvo, daemon=True)
    th.start()
    th.join(prazo)
    return resposta[0] if resposta else (0, b"", url)


def _baixar(url: str, max_bytes: Optional[int] = None, tentativas: int = 3,
            espera: float = 1.0, cabecalhos: Optional[dict] = None) -> Tuple[int, bytes, str]:
    """http_get com novas tentativas para falha de rede, 429 e 5xx, e com gunzip.
    A 1ª tentativa tem o timeout cheio (20 s); as seguintes esperam menos, para que uma
    fonte fora do ar não segure a coleta."""
    status, corpo, final = 0, b"", url
    for i in range(tentativas):
        status, corpo, final = _http_com_prazo(
            url, TIMEOUT if i == 0 else TIMEOUT // 2, PRAZO if i == 0 else PRAZO_RETENTATIVA,
            max_bytes, cabecalhos)
        if status in (0, 429) or status >= 500:
            if i + 1 < tentativas:
                time.sleep(espera * (i + 1))
                continue
        break
    return status, _descompactar(corpo), final


def _descricao_erro(status: int, corpo: bytes = b"") -> str:
    if status == 0:
        return "sem resposta (timeout, DNS ou conexão)"
    if status in (403, 503) and b"Just a moment" in corpo[:4000]:
        return "HTTP %d (bloqueio anti-robô do site)" % status
    return "HTTP %d" % status


def _texto(s: Optional[str]) -> str:
    """Tira HTML, comentários e espaços repetidos."""
    if not s:
        return ""
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()


def _cortar(s: str, n: int) -> str:
    if len(s) <= n:
        return s
    corte = s[:n - 1]
    if " " in corte[n // 2:]:
        corte = corte[:corte.rfind(" ")]
    return corte.rstrip(" ,;:.-—") + "…"


def _chave(url: str) -> str:
    """Chave de deduplicação: tira rastreamento, âncora, www e barra final, mas mantém
    parâmetros que identificam a página (ex.: news.ycombinator.com/item?id=123)."""
    p = urlsplit(url.strip())
    query = urlencode(sorted((k, v) for k, v in parse_qsl(p.query) if not _RASTREIO.match(k)))
    return urlunsplit((p.scheme.lower(), p.netloc.lower().removeprefix("www."), p.path.rstrip("/"), query, ""))


def _sem_rastreio(url: str) -> str:
    """Tira utm_* e afins da URL guardada (mantém os demais parâmetros e tira a âncora)."""
    p = urlsplit(url.strip())
    query = urlencode([(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not _RASTREIO.match(k)])
    return urlunsplit((p.scheme, p.netloc, p.path, query, ""))


def _sem_urls(s: str) -> str:
    """Resumo de HN/Reddit: tira links soltos e deixa só o texto."""
    s = re.sub(r"https?://\S+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) >= 15 else ""


def _identidade_na_query(url: str) -> bool:
    host = urlsplit(url).netloc.lower().removeprefix("www.")
    return host in ("news.ycombinator.com", "youtube.com", "m.youtube.com")


def _id_curto(url: str) -> str:
    return hashlib.sha1(_chave(url).encode("utf-8")).hexdigest()[:10]


def _sem_acento(s: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFKD", s) if not unicodedata.combining(ch)).lower()


def _passa_filtro(filtro, texto: str) -> bool:
    """Filtro de fonte: lista de palavras (ou uma só); basta uma aparecer, sem ligar para acento,
    maiúscula ou hífen (vale também para o endereço: '.../niteroi-ganha-...' casa com 'Niterói').
    Palavra de até 3 letras (como 'IA') só casa inteira: senão 'dia' e 'mídia' passariam."""
    if not filtro:
        return True
    palavras = [filtro] if isinstance(filtro, str) else filtro
    alvo = _sem_acento(texto).replace("-", " ")

    def casa(p):
        p = _sem_acento(str(p)).replace("-", " ")
        if len(p) <= 3:
            return re.search(r"(?<![a-z0-9])%s(?![a-z0-9])" % re.escape(p), alvo) is not None
        return p in alvo
    return any(casa(p) for p in palavras)


def _iso(dt: Optional[datetime]) -> Optional[str]:
    return dt.astimezone(FUSO).isoformat(timespec="seconds") if dt else None


def _parse_iso(s: Optional[str]) -> Optional[datetime]:
    """ISO 8601 ('Z' ou offset). Sem hora (só a data) vira meia-noite de Brasília."""
    if not s:
        return None
    s = s.strip()
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
            return datetime.fromisoformat(s).replace(tzinfo=FUSO)
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def _data_entrada(e) -> Optional[datetime]:
    for campo in ("published_parsed", "updated_parsed", "created_parsed"):
        t = e.get(campo)
        if t:
            try:
                return datetime(*t[:6], tzinfo=timezone.utc)
            except Exception:
                pass
    return None


DIAS_JANELA = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]  # as chaves do janela_horas


def _horas_janela(horas_cfg, data: date, padrao: int = 30) -> int:
    """Quantas horas olhar para trás. `horas_cfg` é um número ou um dicionário com `padrao` e, se quiser,
    o nome de um dia da semana (segunda, terca, quarta, quinta, sexta, sabado, domingo) que vale só nele."""
    if not isinstance(horas_cfg, dict):
        return int(horas_cfg or padrao)
    return int(horas_cfg.get(DIAS_JANELA[data.weekday()]) or horas_cfg.get("padrao") or padrao)


def _janela(cfg: dict, data: date) -> Tuple[datetime, datetime, int]:
    horas = _horas_janela(cfg.get("janela_horas") or {}, data)
    if data >= hoje_brasilia():
        fim = agora_brasilia()
    else:
        fim = datetime(data.year, data.month, data.day, 23, 59, 59, tzinfo=FUSO)
    return fim - timedelta(hours=horas), fim, horas


def _candidato(titulo: str, url: str, fonte: str, tema: str, tipo: str, publicado: Optional[datetime],
               resumo: str = "", radar: bool = False, extra: Optional[dict] = None) -> dict:
    url = _sem_rastreio(url)
    c = {
        "id": _id_curto(url),
        "titulo": _cortar(_texto(titulo), 250),
        "url": url,
        "fonte": fonte,
        "tema": tema,
        "tipo_fonte": tipo,
        "publicado_em": _iso(publicado),
        "resumo": _cortar(_texto(resumo), RESUMO_JSON),
        "radar": radar,
        "extra": extra or {},
        "ja_coberto": False,
    }
    if publicado is None:
        c["sem_data"] = True
    return c


def _stat(ok: bool, itens: int, erro: Optional[str], t0: float, tipo: str, **mais) -> dict:
    s = {"ok": ok, "itens": itens, "erro": erro, "tipo": tipo, "segundos": round(time.time() - t0, 1)}
    s.update(mais)
    return s


# ───────────────────────── RSS ─────────────────────────

def _pagina_feed(url: str, n: int) -> str:
    """Endereço da página N de um feed do WordPress (?paged=N)."""
    return url if n == 1 else "%s%spaged=%d" % (url, "&" if "?" in url else "?", n)


def _mais_paginas(url: str, primeira, paginas: int, inicio: datetime) -> list:
    """Itens das páginas 2..N do feed, enquanto a página anterior ainda tiver item dentro da janela.
    Serve para sites que publicam muito e só mostram os 10 últimos no feed (prefeituras)."""
    entradas, ultima = list(primeira.entries), primeira
    for n in range(2, paginas + 1):
        datas = [d for d in (_data_entrada(e) for e in ultima.entries) if d]
        if not datas or min(datas) < inicio:
            break
        status, corpo, _ = _baixar(_pagina_feed(url, n), tentativas=2)
        ultima = feedparser.parse(corpo) if status == 200 else None
        if not ultima or not ultima.entries:
            break
        entradas += ultima.entries
    return entradas


def _ler_feed(nome: str, url: str, tema: str, tipo: str, inicio: datetime, fim: datetime,
              limite: int, radar: bool = False, filtro=None, paginas: int = 1) -> Tuple[List[dict], dict]:
    t0 = time.time()
    status, corpo, final = 0, b"", url
    d = None
    for tentativa in range(2):
        status, corpo, final = _baixar(url)
        if status != 200:
            break
        d = feedparser.parse(corpo)
        if d.entries:
            break
        # 200 sem itens: pode ser resposta cortada no meio. Tenta uma vez mais.
        if tentativa == 0:
            time.sleep(2)
    if status != 200:
        return [], _stat(False, 0, _descricao_erro(status, corpo), t0, "rss")
    if not d or not d.entries:
        motivo = "XML inválido" if (d and d.bozo) else "feed sem itens"
        return [], _stat(False, 0, motivo, t0, "rss")

    entradas = _mais_paginas(url, d, paginas, inicio) if paginas > 1 else d.entries
    itens = []
    for e in entradas:
        link = (e.get("link") or "").strip()
        titulo = _texto(e.get("title"))
        if not link or not titulo:
            continue
        link = urljoin(final, link)
        pub = _data_entrada(e)
        if pub is not None and not (inicio <= pub <= fim + timedelta(hours=6)):
            continue
        resumo = _texto(e.get("summary"))
        if not resumo and not radar and e.get("content"):
            resumo = _texto(e["content"][0].get("value"))
        # só o começo do resumo: em feed com o texto inteiro, a cidade citada de passagem não conta
        if not _passa_filtro(filtro, " ".join((titulo, resumo[:FILTRO_RESUMO], link))):
            continue
        extra = {}
        if radar:
            html = (e["content"][0].get("value") if e.get("content") else e.get("summary")) or ""
            extra["manchetes"] = _manchetes(html)
        itens.append(_candidato(titulo, link, nome, tema, tipo, pub, resumo, radar=radar, extra=extra))
    # mais novos primeiro; sem data no fim
    itens.sort(key=lambda c: c["publicado_em"] or "", reverse=True)
    com_data = [c for c in itens if c["publicado_em"]]
    sem_data = [c for c in itens if not c["publicado_em"]]
    itens = (com_data + sem_data)[:limite]
    return itens, _stat(True, len(itens), None, t0, "rss", total_no_feed=len(entradas))


# ───────────────────────── Especiais ─────────────────────────

def _json(url: str, cabecalhos: Optional[dict] = None, descrever=None):
    status, corpo, _ = _baixar(url, cabecalhos=cabecalhos)
    if status != 200:
        raise RuntimeError(descrever(status, corpo) if descrever and status else _descricao_erro(status, corpo))
    try:
        return json.loads(corpo.decode("utf-8"))
    except ValueError:
        raise RuntimeError("resposta não é JSON válido")


def _hacker_news(cfg: dict) -> Tuple[List[dict], dict]:
    t0 = time.time()
    try:
        dados = _json("https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=50")
        hits = sorted(dados.get("hits") or [], key=lambda h: h.get("points") or 0, reverse=True)
        itens = []
        for h in hits[:int(cfg.get("limite", 30))]:
            hn = "https://news.ycombinator.com/item?id=%s" % h.get("objectID")
            url = h.get("url") or hn
            c = _candidato(h.get("title") or "", url, "Hacker News", "comunidade", "comunidade",
                           _parse_iso(h.get("created_at")), _sem_urls(_texto(h.get("story_text"))),
                           extra={"pontos": h.get("points") or 0, "comentarios": h.get("num_comments") or 0,
                                  "discussao": hn})
            if c["titulo"]:
                itens.append(c)
        return itens, _stat(True, len(itens), None, t0, "api")
    except Exception as ex:
        return [], _stat(False, 0, str(ex), t0, "api")


def _github_em_alta(cfg: dict, data: date) -> Tuple[List[dict], dict]:
    t0 = time.time()
    try:
        desde = (data - timedelta(days=int(cfg.get("dias", 7)))).isoformat()
        q = quote("created:>" + desde, safe="")
        url = ("https://api.github.com/search/repositories?q=%s&sort=stars&order=desc&per_page=%d"
               % (q, int(cfg.get("limite", 15))))
        # o motivo do erro diz se quem barrou foi o limite do GitHub ou o proxy da nuvem
        dados = _json(url, cabecalhos=github.cabecalhos_api(), descrever=github.motivo)
        itens = []
        for r in dados.get("items") or []:
            itens.append(_candidato(
                r.get("full_name") or "", r.get("html_url") or "", "GitHub em alta", "comunidade", "comunidade",
                _parse_iso(r.get("created_at")), r.get("description") or "",
                extra={"estrelas": r.get("stargazers_count"), "linguagem": r.get("language")}))
        itens = [c for c in itens if c["titulo"] and c["url"]]
        if not itens:  # a busca às vezes estoura o tempo do GitHub e volta vazia
            raise RuntimeError("a busca voltou vazia")
        return itens, _stat(True, len(itens), None, t0, "api")
    except Exception as ex:
        # Na nuvem, sem GITHUB_TOKEN_LEITURA, a busca dá 403 (o proxy só libera o repositório da newsletter).
        # A página de tendências não usa a API: os repositórios com mais estrelas na semana.
        itens, motivo = _github_tendencias(cfg)
        if itens:
            return itens, _stat(True, len(itens), "API: %s; usei a página de tendências" % ex, t0, "api")
        return [], _stat(False, 0, "API: %s; página de tendências: %s" % (ex, motivo), t0, "api")


def _numero(s: str) -> Optional[int]:
    s = re.sub(r"[^\d]", "", s or "")
    return int(s) if s else None


def _github_tendencias(cfg: dict) -> Tuple[List[dict], Optional[str]]:
    """github.com/trending da semana: (itens, motivo da falha). Sem data de criação: os itens ficam 'sem data'."""
    status, corpo, _ = _baixar("https://github.com/trending?since=weekly", tentativas=2)
    if status != 200:
        anti_robo = b"Just a moment" in corpo[:4000]
        return [], github.motivo(status, corpo) if status in (403, 429) and not anti_robo else _descricao_erro(
            status, corpo)
    texto = corpo.decode("utf-8", "replace")
    itens = []
    for bloco in re.findall(r'<article class="Box-row">(.*?)</article>', texto, re.S):
        nome = re.search(r'<h2[^>]*>.*?href="/([\w.-]+/[\w.-]+)"', bloco, re.S)
        if not nome:
            continue
        desc = re.search(r"<p(?:\s[^>]*)?>(.*?)</p>", bloco, re.S)
        lingua = re.search(r'itemprop="programmingLanguage">([^<]+)<', bloco)
        total = re.search(r'/stargazers"[^>]*>.*?</svg>\s*([\d,.]+)', bloco, re.S)
        semana = re.search(r"([\d,.]+) stars this week", bloco)
        extra = {"estrelas": _numero(total.group(1)) if total else None,
                 "linguagem": lingua.group(1).strip() if lingua else None,
                 "estrelas_semana": _numero(semana.group(1)) if semana else None}
        itens.append(_candidato(nome.group(1), "https://github.com/" + nome.group(1), "GitHub em alta",
                                "comunidade", "comunidade", None, _texto(desc.group(1)) if desc else "",
                                extra={k: v for k, v in extra.items() if v is not None}))
    return itens[:int(cfg.get("limite", 15))], (None if itens else "nenhum repositório na página")


def _hugging_face(cfg: dict) -> Tuple[List[dict], dict]:
    t0 = time.time()
    n = int(cfg.get("limite", 12))
    itens, erros = [], []
    try:
        modelos = _json("https://huggingface.co/api/models?sort=trendingScore&direction=-1&limit=%d" % n)
        for m in modelos[:n]:
            mid = m.get("id") or m.get("modelId")
            if not mid:
                continue
            partes = [x for x in (m.get("pipeline_tag"), m.get("library_name")) if x]
            itens.append(_candidato(
                mid, "https://huggingface.co/" + mid, "Hugging Face (modelos em alta)", "comunidade", "comunidade",
                _parse_iso(m.get("createdAt")), "modelo em alta" + (": " + ", ".join(partes) if partes else ""),
                extra={"curtidas": m.get("likes"), "downloads": m.get("downloads"),
                       "tendencia": m.get("trendingScore")}))
    except Exception as ex:
        erros.append("modelos: %s" % ex)
    try:
        papers = _json("https://huggingface.co/api/daily_papers?limit=%d" % n)
        for p in papers[:n]:
            pa = p.get("paper") or {}
            if not pa.get("id"):
                continue
            extra = {"votos": pa.get("upvotes"), "comentarios": p.get("numComments")}
            if pa.get("githubRepo"):
                extra["github"] = pa["githubRepo"]
            itens.append(_candidato(
                p.get("title") or pa.get("title") or "", "https://huggingface.co/papers/" + pa["id"],
                "Hugging Face (papers do dia)", "comunidade", "comunidade",
                _parse_iso(p.get("publishedAt") or pa.get("publishedAt")),
                pa.get("ai_summary") or p.get("summary") or pa.get("summary") or "", extra=extra))
    except Exception as ex:
        erros.append("papers: %s" % ex)
    return itens, _stat(not erros or bool(itens), len(itens), "; ".join(erros) or None, t0, "api")


def _reddit(cfg: dict) -> Tuple[List[dict], dict]:
    """Os subreddits são lidos um por vez, com pausa: o Reddit devolve 429 se for rápido demais."""
    t0 = time.time()
    itens, erros = [], []
    for i, sub in enumerate(cfg.get("subreddits") or []):
        if i:
            time.sleep(3)
        url = "https://www.reddit.com/r/%s/top/.rss?t=day" % sub
        status, corpo, _ = _baixar(url, tentativas=3, espera=4.0)
        if status != 200:
            erros.append("r/%s: %s" % (sub, _descricao_erro(status, corpo)))
            continue
        d = feedparser.parse(corpo)
        for e in list(d.entries)[:int(cfg.get("limite", 10))]:
            conteudo = (e.get("content") or [{}])[0].get("value", "") or e.get("summary", "")
            md = re.search(r'<div class="md">(.*?)</div><!-- SC_ON -->', conteudo, re.S)
            extra = {}
            ext = re.search(r'<a href="([^"]+)">\[link\]</a>', conteudo)
            if ext and "reddit.com" not in ext.group(1):
                extra["link_externo"] = html.unescape(ext.group(1))
            if e.get("link") and e.get("title"):
                itens.append(_candidato(e["title"], e["link"], "Reddit r/%s" % sub, "comunidade", "comunidade",
                                        _data_entrada(e), _sem_urls(_texto(md.group(1))) if md else "", extra=extra))
    return itens, _stat(not erros or bool(itens), len(itens), "; ".join(erros) or None, t0, "rss")


# ───────────────────────── Radar por sitemap ─────────────────────────

def _lista_sitemap(nome: str, url: str, inicio: datetime, fim: datetime) -> Tuple[List[dict], dict]:
    """Devolve as páginas /p/ recentes do sitemap (ainda sem título): [{url, lastmod}]."""
    t0 = time.time()
    status, corpo, _ = _baixar(url)
    if status != 200:
        return [], _stat(False, 0, _descricao_erro(status, corpo), t0, "sitemap")
    texto = corpo.decode("utf-8", "replace")
    achadas = []
    for bloco in re.findall(r"<url>(.*?)</url>", texto, re.S):
        loc = re.search(r"<loc>\s*(.*?)\s*</loc>", bloco, re.S)
        lm = re.search(r"<lastmod>\s*(.*?)\s*</lastmod>", bloco, re.S)
        if not loc or "/p/" not in loc.group(1):
            continue
        quando = _parse_iso(lm.group(1)) if lm else None
        if quando is None:
            continue
        # lastmod costuma vir só com a data: compara pelo dia
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", lm.group(1).strip()):
            if not (inicio.date() <= quando.date() <= fim.date()):
                continue
        elif not (inicio <= quando <= fim + timedelta(hours=6)):
            continue
        achadas.append({"url": html.unescape(loc.group(1)), "quando": quando, "lastmod": lm.group(1).strip()})
    achadas.sort(key=lambda a: a["quando"], reverse=True)
    achadas = achadas[:RADAR_MAX_PAGINAS]
    return achadas, _stat(True, len(achadas), None, t0, "sitemap")


def _meta(texto: str, propriedade: str) -> str:
    """Valor do <meta property|name=propriedade content=...>, em qualquer ordem de atributos."""
    for tag in re.findall(r"<meta\b[^>]*>", texto, re.I):
        if re.search(r'(?:property|name)\s*=\s*["\']%s["\']' % re.escape(propriedade), tag, re.I):
            m = re.search(r'content\s*=\s*"([^"]*)"', tag, re.I) or re.search(r"content\s*=\s*'([^']*)'", tag, re.I)
            if m:
                return _texto(m.group(1))
    return ""


RADAR_IGNORAR = re.compile(
    r"^(bom dia|boa noite|quick takes|apresentado por|collab|dropped by|recado|quem somos|opini[aã]o do leitor|"
    r"indique|para ler|para ouvir|curiosidade|descubra|stat|dicas?|extras|need to know|foto do dia|aspas|"
    r"around the web|drop like|trending|mundo afora|brasil adentro|hoje eu aprendi|ia por a[ií]|"
    r"contra dados|stats|meme|quiz|poll|sponsored|together with)\b"
    r"|^(o que (voc[eê] )?achou|veja as edi|acompanhe o|qual imagem|recomenda[cç][aã]o dos analistas|"
    r"choose the prompt|\+\d|\{\{)", re.I)


def _manchetes(html: str, limite: int = 15) -> List[str]:
    """Só os intertítulos (h1–h3) de uma edição do radar: servem para não repetir assunto.
    O texto da matéria nunca é guardado."""
    vistos, saida = set(), []
    for bruto in re.findall(r"<h[1-3][^>]*>(.*?)</h[1-3]>", html, re.S | re.I):
        t = _cortar(_texto(bruto), 120)
        if len(t) < 12 or RADAR_IGNORAR.match(t) or t.lower() in vistos:
            continue
        vistos.add(t.lower())
        saida.append(t)
        if len(saida) >= limite:
            break
    return saida


def _pagina_radar(nome: str, item: dict) -> Optional[dict]:
    """Baixa a página e guarda só og:title e og:description (nunca o texto da matéria)."""
    status, corpo, _ = _baixar(item["url"], max_bytes=RADAR_MAX_BYTES)
    if status != 200:
        return None
    try:
        texto = corpo.decode("utf-8")
    except UnicodeDecodeError:
        texto = corpo.decode("latin-1")
    cabeca = texto.split("</head>")[0]
    titulo = _meta(cabeca, "og:title")
    if not titulo:
        m = re.search(r"<title[^>]*>(.*?)</title>", cabeca, re.S | re.I)
        titulo = _texto(m.group(1)) if m else ""
    if not titulo:
        return None
    descricao = _meta(cabeca, "og:description") or _meta(cabeca, "description")
    return _candidato(titulo, item["url"], nome, "radar", "radar", item["quando"], descricao, radar=True,
                      extra={"lastmod": item["lastmod"], "manchetes": _manchetes(texto)})


# ───────────────────────── Orquestração ─────────────────────────

def _coberto(url: str, chaves: set, normais: set) -> bool:
    if _chave(url) in chaves:
        return True
    return (not _identidade_na_query(url)) and normalizar_url(url) in normais


def _deduplicar(candidatos: List[dict]) -> List[dict]:
    """Remove repetidos pela url. O primeiro fica; os dados extras dos outros são somados a ele."""
    vistos = {}  # type: Dict[str, dict]
    saida = []
    for c in candidatos:
        k = _chave(c["url"])
        if k in vistos:
            ficou = vistos[k]
            ficou["extra"].setdefault("tambem_em", [])
            if c["fonte"] != ficou["fonte"] and c["fonte"] not in ficou["extra"]["tambem_em"]:
                ficou["extra"]["tambem_em"].append(c["fonte"])
            for chave, valor in c["extra"].items():
                if chave != "tambem_em":
                    ficou["extra"].setdefault(chave, valor)
            if not ficou["extra"]["tambem_em"]:
                del ficou["extra"]["tambem_em"]
            continue
        vistos[k] = c
        saida.append(c)
    return saida


def _extra_texto(extra: dict) -> str:
    rotulos = [("pontos", "{} pts"), ("comentarios", "{} comentários"), ("curtidas", "{} curtidas"),
               ("votos", "{} votos"), ("estrelas", "★ {}"), ("estrelas_semana", "+{} ★ na semana"),
               ("linguagem", "{}"), ("downloads", "{} downloads")]
    partes = []
    usados = set()
    for chave, formato in rotulos:
        if extra.get(chave) not in (None, ""):
            partes.append(formato.format(extra[chave]))
            usados.add(chave)
    if extra.get("tambem_em"):
        partes.append("também em: " + ", ".join(extra["tambem_em"]))
    if extra.get("discussao"):
        partes.append("discussão: " + extra["discussao"])
    if extra.get("link_externo"):
        partes.append("link: " + extra["link_externo"])
    if extra.get("github"):
        partes.append("código: " + extra["github"])
    return " · ".join(partes)


def _linha_md(c: dict) -> str:
    quando = "sem data"
    if c.get("publicado_em"):
        quando = datetime.fromisoformat(c["publicado_em"]).strftime("%d/%m %H:%M")
        if c["publicado_em"].endswith("T00:00:00-03:00") and c["tipo_fonte"] == "radar":
            quando = quando[:5]
    texto = "- [%s] %s" % (c["fonte"], c["titulo"])
    resumo = _cortar(c["resumo"], RESUMO_MD)
    if resumo and resumo != c["titulo"]:
        texto += " — " + resumo
    texto += " (%s) · %s" % (c["url"], quando)
    extra = _extra_texto(c["extra"])
    if extra:
        texto += " · " + extra
    if c["ja_coberto"]:
        texto += " · JÁ COBERTO"
    if c["extra"].get("manchetes"):
        texto += "\n  manchetes: " + " | ".join(c["extra"]["manchetes"])
    return texto


def _montar_md(data: date, inicio: datetime, fim: datetime, horas: int, candidatos: List[dict],
               stats: dict, paginas: List[dict], rotulos: Optional[dict] = None) -> str:
    """rotulos: {tema: rótulo} do arquivo de fontes (opcional); os temas dele vêm primeiro, nessa ordem."""
    falharam = sum(1 for s in stats.values() if not s["ok"])
    linhas = [
        "# Candidatos de %s" % data.isoformat(),
        "",
        "Janela: %s a %s (%d h). %d candidatos de %d fontes (%d falharam)."
        % (inicio.strftime("%d/%m %H:%M"), fim.strftime("%d/%m %H:%M"), horas, len(candidatos), len(stats), falharam),
        "Itens marcados JÁ COBERTO já saíram em edição anterior. Radar = newsletters que o leitor já recebe "
        "(servem para achar pauta; nunca citar).",
        "",
    ]
    normais = [c for c in candidatos if not c["radar"]]
    ordem = [(t, r) for t, r in (rotulos or {}).items()] + [t for t in TEMAS[:-1] if t[0] not in (rotulos or {})]
    conhecidos = {t for t, _ in ordem} | {TEMAS[-1][0]}
    outros = sorted({c["tema"] for c in normais} - conhecidos)
    for tema, rotulo in ordem + [(o, o.capitalize()) for o in outros] + TEMAS[-1:]:
        itens = [c for c in normais if c["tema"] == tema]
        if not itens:
            continue
        if tema != "comunidade":
            itens.sort(key=lambda c: c["publicado_em"] or "", reverse=True)
            itens.sort(key=lambda c: (ORDEM_TIPO.get(c["tipo_fonte"], 9), c["fonte"]))
        linhas.append("## %s (%d)" % (rotulo, len(itens)))
        linhas.extend(_linha_md(c) for c in itens)
        linhas.append("")
    radar = sorted((c for c in candidatos if c["radar"]), key=lambda c: c["publicado_em"] or "", reverse=True)
    radar.sort(key=lambda c: c["fonte"])
    if radar:
        linhas.append("## Radar (newsletters que o leitor já recebe) (%d)" % len(radar))
        linhas.extend(_linha_md(c) for c in radar)
        linhas.append("")
    if paginas:
        linhas.append("## Fontes sem RSS para visitar na apuração (%d)" % len(paginas))
        for p in paginas:
            linhas.append("- %s: %s" % (p["nome"], p["pagina"]))
        linhas.append("")
    return "\n".join(linhas)


def _montar_log(data: date, stats: dict) -> str:
    linhas = ["Fontes que falharam em %s" % data.isoformat(), ""]
    falhas = [(n, s) for n, s in stats.items() if not s["ok"]]
    if falhas:
        linhas.extend("- %s: %s" % (n, s["erro"]) for n, s in falhas)
    else:
        linhas.append("(nenhuma)")
    parciais = [(n, s) for n, s in stats.items() if s["ok"] and s.get("erro")]
    if parciais:
        linhas += ["", "Falhas parciais:"] + ["- %s: %s" % (n, s["erro"]) for n, s in parciais]
    vazias = [n for n, s in stats.items() if s["ok"] and s["itens"] == 0]
    if vazias:
        linhas += ["", "Responderam, mas sem itens na janela:"] + ["- " + n for n in vazias]
    return "\n".join(linhas) + "\n"


def coletar(data: date, raiz: Path, caderno: str = cadernos.GERAL) -> dict:
    t0 = time.time()
    raiz = Path(raiz)
    cfg = ler_yaml(cadernos.arquivo_fontes(raiz, caderno))
    inicio, fim, horas = _janela(cfg, data)
    limite = int(cfg.get("limite_por_fonte") or 15)
    especiais = cfg.get("especiais") or {}
    fontes = [f for f in (cfg.get("fontes") or []) if f.get("ativo", True)]
    radar_cfg = [r for r in (cfg.get("radar") or []) if r.get("ativo", True)]
    paginas = [{"nome": f["nome"], "pagina": f["pagina"], "tema": f.get("tema")}
               for f in fontes if f.get("pagina") and not f.get("rss")]

    # Etapa 1: tudo o que depende só de uma requisição, em paralelo.
    tarefas = []  # (nome, tipo, função)
    for f in fontes:
        if f.get("rss"):
            # janela_horas na fonte vale só para ela (ex.: bloco semanal de outra cidade); pode ser um número
            # ou um dicionário por dia da semana, como o janela_horas do arquivo
            inicio_f = fim - timedelta(hours=_horas_janela(f["janela_horas"], data)) if f.get("janela_horas") else inicio
            tarefas.append((f["nome"], "rss", lambda f=f, inicio_f=inicio_f: _ler_feed(
                f["nome"], f["rss"], f.get("tema", "outro"), f.get("tipo", "imprensa"), inicio_f, fim,
                int(f.get("limite") or limite), filtro=f.get("filtro"), paginas=int(f.get("paginas") or 1))))
    for r in radar_cfg:
        if r.get("rss"):
            tarefas.append((r["nome"], "radar_rss", lambda r=r: _ler_feed(
                r["nome"], r["rss"], "radar", "radar", inicio, fim, limite, radar=True)))
        elif r.get("sitemap"):
            tarefas.append((r["nome"], "radar_sitemap", lambda r=r: _lista_sitemap(
                r["nome"], r["sitemap"], inicio, fim)))
    if (especiais.get("hacker_news") or {}).get("ativo"):
        tarefas.append(("Hacker News", "especial", lambda: _hacker_news(especiais["hacker_news"])))
    if (especiais.get("github_em_alta") or {}).get("ativo"):
        tarefas.append(("GitHub em alta", "especial", lambda: _github_em_alta(especiais["github_em_alta"], data)))
    if (especiais.get("hugging_face") or {}).get("ativo"):
        tarefas.append(("Hugging Face", "especial", lambda: _hugging_face(especiais["hugging_face"])))
    if (especiais.get("reddit") or {}).get("ativo"):
        tarefas.append(("Reddit", "especial", lambda: _reddit(especiais["reddit"])))

    por_nome = {}  # nome -> (tipo, itens, stat)
    with ThreadPoolExecutor(WORKERS) as pool:
        futuros = [(nome, tipo, pool.submit(fn)) for nome, tipo, fn in tarefas]
        for nome, tipo, fut in futuros:
            try:
                itens, stat = fut.result()
            except Exception as ex:  # defesa: uma fonte nunca derruba a coleta
                itens, stat = [], _stat(False, 0, "erro inesperado: %s" % ex, time.time(), tipo)
            por_nome[nome] = (tipo, itens, stat)

        # Etapa 2: radar por sitemap precisa baixar cada página (só og:title e og:description).
        paginas_radar = []
        for nome, (tipo, itens, stat) in por_nome.items():
            if tipo == "radar_sitemap" and stat["ok"]:
                paginas_radar += [(nome, it) for it in itens]
        resultados = [(nome, pool.submit(_pagina_radar, nome, it)) for nome, it in paginas_radar]
        radar_sitemap = {}  # type: Dict[str, List[dict]]
        for nome, fut in resultados:
            try:
                c = fut.result()
            except Exception:
                c = None
            if c:
                radar_sitemap.setdefault(nome, []).append(c)

    # Junta tudo na ordem do fontes.yaml: RSS, radar, especiais.
    candidatos, stats = [], {}  # type: List[dict], dict
    for nome, (tipo, itens, stat) in por_nome.items():
        if tipo == "radar_sitemap":
            itens = radar_sitemap.get(nome, [])
            falhas = sum(1 for n, _ in paginas_radar if n == nome) - len(itens)
            stat = dict(stat, itens=len(itens))
            if stat["ok"] and falhas > 0:
                stat["erro"] = "%d página(s) do radar não carregaram" % falhas
        stats[nome] = stat
        candidatos.extend(itens)

    candidatos = _deduplicar(candidatos)

    cobertas_norm = historico.urls_cobertas(raiz)
    cobertas_chave = set()
    for ed in historico.carregar(raiz):
        for h in ed.get("historias") or []:
            cobertas_chave.update(_chave(u) for u in h.get("urls") or [])
    for c in candidatos:
        c["ja_coberto"] = _coberto(c["url"], cobertas_chave, cobertas_norm)

    resultado = {
        "data": data.isoformat(),
        "gerado_em": agora_brasilia().isoformat(timespec="seconds"),
        "janela": {"horas": horas, "inicio": inicio.isoformat(timespec="seconds"),
                   "fim": fim.isoformat(timespec="seconds")},
        "total": len(candidatos),
        "fontes_total": len(stats),
        "fontes_falharam": sum(1 for s in stats.values() if not s["ok"]),
        "segundos": round(time.time() - t0, 1),
        "stats": stats,
        "paginas_sem_rss": paginas,
        "candidatos": candidatos,
    }

    pasta = raiz / "dados" / "candidatos"
    pasta.mkdir(parents=True, exist_ok=True)
    nome_base = cadernos.prefixo(caderno) + data.isoformat()
    base = pasta / nome_base
    base.with_suffix(".md").write_text(_montar_md(data, inicio, fim, horas, candidatos, stats, paginas,
                                                  cfg.get("temas")), encoding="utf-8")
    (pasta / (nome_base + "-fontes.log")).write_text(_montar_log(data, stats), encoding="utf-8")

    print("%d candidatos de %d fontes (%d falharam), em %.0f s. Arquivo: %s"
          % (len(candidatos), len(stats), resultado["fontes_falharam"], resultado["segundos"],
             (pasta / (nome_base + ".md")).relative_to(raiz)))
    return resultado
