"""Funções comuns: datas em Brasília, HTTP, YAML e front matter."""
import re
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlsplit, urlunsplit
from zoneinfo import ZoneInfo

import yaml

FUSO = ZoneInfo("America/Sao_Paulo")
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 InteligenciaPragmatica/1.0"
)

DIAS_SEMANA = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira",
               "sexta-feira", "sábado", "domingo"]
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]


def agora_brasilia() -> datetime:
    return datetime.now(FUSO)


def hoje_brasilia() -> date:
    return agora_brasilia().date()


def data_por_extenso(d: date) -> str:
    """Ex.: 'sábado, 17 de outubro de 2026'."""
    return f"{DIAS_SEMANA[d.weekday()]}, {d.day} de {MESES[d.month - 1]} de {d.year}"


def http_get(url: str, timeout: int = 20, max_bytes: Optional[int] = None,
             metodo: str = "GET", cabecalhos: Optional[dict] = None) -> Tuple[int, bytes, str]:
    """Faz a requisição e devolve (status, corpo, url_final). Não levanta erro de HTTP:
    status 0 significa falha de rede (DNS, timeout, conexão)."""
    h = {"User-Agent": USER_AGENT, "Accept": "*/*", "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8"}
    if cabecalhos:
        h.update(cabecalhos)
    req = urllib.request.Request(url, headers=h, method=metodo)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            corpo = resp.read(max_bytes) if max_bytes else resp.read()
            return resp.status, corpo, resp.geturl()
    except urllib.error.HTTPError as e:
        try:
            corpo = e.read(max_bytes or 65536)
        except Exception:
            corpo = b""
        return e.code, corpo, url
    except Exception:
        return 0, b"", url


def ler_yaml(path: Path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def ler_front_matter(path: Path):
    """Devolve (metadados, corpo) de um .md com front matter YAML entre '---'."""
    texto = Path(path).read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", texto, re.S)
    if not m:
        return {}, texto
    return (yaml.safe_load(m.group(1)) or {}), m.group(2)


def normalizar_url(u: str) -> str:
    """Tira query string, âncora e barra final, para comparar URLs."""
    p = urlsplit(u.strip())
    caminho = p.path.rstrip("/")
    return urlunsplit((p.scheme.lower(), p.netloc.lower().removeprefix("www."), caminho, "", ""))


def edicao_mais_recente(raiz: Path, caderno: str = "geral") -> Optional[str]:
    """Pasta (AAAA-MM-DD, ou AAAA-MM-DD-extra nos cadernos) da edição mais nova do caderno, ou None."""
    from . import cadernos  # importado aqui para não criar ciclo (cadernos usa util)
    base = cadernos.pasta_edicoes(raiz, caderno)
    pastas = sorted(p.name for p in base.glob(cadernos.padrao_pastas(caderno)) if (p / "edicao.md").exists())
    return pastas[-1] if pastas else None
