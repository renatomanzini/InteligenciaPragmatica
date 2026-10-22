"""Cadernos: newsletters especializadas que vivem ao lado da geral.

A geral continua como sempre (edicoes/DATA, docs/DATA.html, fontes.yaml, config.yaml).
Cada caderno (por exemplo, "mercado") tem:
- as edições em edicoes/<caderno>/DATA/ (ou DATA-extra/ para edição extra);
- as fontes no arquivo indicado em cadernos.yaml;
- as páginas do site em docs/<caderno>-DATA.html e o arquivo em docs/<caderno>.html;
- o próprio número de edição no histórico (que é um só, para nenhum caderno repetir o outro).
"""
from pathlib import Path
from typing import List

from .util import ler_yaml

GERAL = "geral"


def _todos(raiz: Path) -> dict:
    arq = Path(raiz) / "cadernos.yaml"
    return (ler_yaml(arq) or {}) if arq.exists() else {}


def nomes(raiz: Path) -> List[str]:
    """Os cadernos especializados (sem a geral), na ordem do cadernos.yaml."""
    return list(_todos(raiz).keys())


def existe(raiz: Path, caderno: str) -> bool:
    return caderno == GERAL or caderno in _todos(raiz)


def config(raiz: Path, caderno: str = GERAL) -> dict:
    """Config da geral (config.yaml) com o bloco do caderno por cima."""
    raiz = Path(raiz)
    arq = raiz / "config.yaml"
    base = (ler_yaml(arq) or {}) if arq.exists() else {}
    if caderno == GERAL:
        return base
    proprio = _todos(raiz).get(caderno)
    if proprio is None:
        raise ValueError("Caderno desconhecido: %s (veja cadernos.yaml)" % caderno)
    cfg = dict(base)
    cfg.update(proprio)
    cfg["caderno"] = caderno
    return cfg


def pasta_edicoes(raiz: Path, caderno: str = GERAL) -> Path:
    raiz = Path(raiz)
    return raiz / "edicoes" if caderno == GERAL else raiz / "edicoes" / caderno


def arquivo_fontes(raiz: Path, caderno: str = GERAL) -> Path:
    raiz = Path(raiz)
    if caderno == GERAL:
        return raiz / "fontes.yaml"
    return raiz / (config(raiz, caderno).get("fontes") or ("fontes_%s.yaml" % caderno))


def prefixo(caderno: str = GERAL) -> str:
    """Prefixo dos arquivos do caderno (páginas do site e candidatos): '' na geral."""
    return "" if caderno == GERAL else caderno + "-"


def indice_site(caderno: str = GERAL) -> str:
    """Página do arquivo de edições do caderno, dentro de docs/."""
    return "index.html" if caderno == GERAL else caderno + ".html"


def padrao_pastas(caderno: str = GERAL) -> str:
    """Glob das pastas de edição. Os cadernos aceitam DATA-extra (edição extra no mesmo dia)."""
    return "????-??-??" if caderno == GERAL else "????-??-??*"
