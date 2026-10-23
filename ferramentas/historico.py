"""Memória da newsletter: o que já saiu, histórias em andamento e formatos usados."""
import json
from datetime import date, timedelta
from pathlib import Path
from typing import List, Optional

from . import cadernos
from .util import hoje_brasilia, ler_front_matter

CAMPOS = ["data", "tipo", "numero", "assunto", "previa", "dia", "breakthrough", "historias", "formatos"]


def _caderno(e: dict) -> str:
    """Edições antigas não têm o campo: são da geral."""
    return e.get("caderno") or cadernos.GERAL


def _arquivo(raiz: Path) -> Path:
    return raiz / "dados" / "historico.json"


def carregar(raiz: Path, caderno: str = None) -> list:
    """Todas as edições registradas, ou só as de um caderno."""
    arq = _arquivo(raiz)
    if not arq.exists():
        return []
    edicoes = json.loads(arq.read_text(encoding="utf-8"))
    return edicoes if caderno is None else [e for e in edicoes if _caderno(e) == caderno]


def registrar(data: str, raiz: Path, caderno: str = cadernos.GERAL) -> dict:
    """Grava (ou regrava) a edição da pasta DATA do caderno. DATA pode ser AAAA-MM-DD-extra."""
    meta, _ = ler_front_matter(cadernos.pasta_edicoes(raiz, caderno) / data / "edicao.md")
    entrada = {c: meta.get(c) for c in CAMPOS}
    entrada["data"] = str(meta.get("data") or data) if caderno == cadernos.GERAL else str(data)
    if caderno != cadernos.GERAL:
        entrada["caderno"] = caderno
    edicoes = [e for e in carregar(raiz)
               if not (e["data"] == entrada["data"] and _caderno(e) == caderno)]
    edicoes.append(entrada)
    edicoes.sort(key=lambda e: e["data"])
    arq = _arquivo(raiz)
    arq.parent.mkdir(parents=True, exist_ok=True)
    arq.write_text(json.dumps(edicoes, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    return entrada


def proximo_numero(raiz: Path, caderno: str = cadernos.GERAL) -> int:
    numeros = [e.get("numero") or 0 for e in carregar(raiz, caderno)]
    return (max(numeros) if numeros else 0) + 1


def ultima_data(raiz: Path, caderno: str = cadernos.GERAL, antes_de: Optional[str] = None) -> Optional[str]:
    """Dia (AAAA-MM-DD) da última edição registrada do caderno, ou None. A edição extra conta pelo dia.
    Com antes_de, só olha as edições de dias anteriores a ele."""
    dias = [str(e["data"])[:10] for e in carregar(raiz, caderno)]
    if antes_de:
        dias = [d for d in dias if d < str(antes_de)[:10]]
    return max(dias) if dias else None


NOMES_DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]


def situacao(raiz: Path, caderno: str, hoje: Optional[date] = None) -> List[str]:
    """Para os cadernos com dias fixos: se hoje é dia fixo e a data da última edição."""
    dias = cadernos.dias_envio(raiz, caderno)
    if not dias:
        return []
    hoje = hoje or hoje_brasilia()
    fixos = [NOMES_DIAS[cadernos.DIAS.index(d)] for d in dias]
    fixos_txt = fixos[0] if len(fixos) == 1 else ", ".join(fixos[:-1]) + " e " + fixos[-1]
    eh = cadernos.dia_de_envio(raiz, caderno, hoje)
    return [
        "## Hoje: %s, %s · %s (os dias fixos de envio são %s)"
        % (NOMES_DIAS[hoje.weekday()], hoje.strftime("%d/%m"), "DIA FIXO DE ENVIO" if eh else "não é dia fixo", fixos_txt),
        "Última edição: %s" % (ultima_data(raiz, caderno) or "nenhuma"),
        "",
    ]


def resumo(dias: int = 14, raiz: Path = Path("."), caderno: str = cadernos.GERAL) -> str:
    edicoes = carregar(raiz, caderno)
    outros = _outros_cadernos(raiz, caderno, _dias_outros(raiz, caderno))
    hoje = situacao(raiz, caderno)
    if not edicoes:
        return "\n".join(hoje + ["Nenhuma edição registrada ainda neste caderno. Esta será a edição nº 1.", ""] + outros)
    limite = str(hoje_brasilia() - timedelta(days=dias))
    recentes = [e for e in edicoes if e["data"] >= limite] or edicoes[-3:]
    nome = "" if caderno == cadernos.GERAL else f" do caderno {caderno}"
    linhas = hoje + [f"# Histórico{nome}: últimas {len(recentes)} edições (próxima: nº {proximo_numero(raiz, caderno)})", ""]
    for e in reversed(recentes):
        marca = " 🚨" if e.get("breakthrough") else ""
        linhas.append(f"## {e['data']} · {e.get('tipo')} · nº {e.get('numero')} · dia {e.get('dia')}{marca}")
        linhas.append(f"Assunto: {e.get('assunto')}")
        linhas.append(f"Formatos: {', '.join(e.get('formatos') or [])}")
        for h in e.get("historias") or []:
            andamento = " (em andamento)" if h.get("em_andamento") else ""
            linhas.append(f"- [{h.get('tema')}] {h.get('id')}: {h.get('titulo')}{andamento}")
        linhas.append("")
    # histórias em andamento: última menção de cada id
    ultima = {}
    for e in edicoes:
        for h in e.get("historias") or []:
            if h.get("em_andamento"):
                ultima[h["id"]] = (e["data"], h.get("titulo"))
            elif h.get("id") in ultima:
                ultima.pop(h["id"])
    # Sem menção há 45 dias, a história esfriou: a lista entra no contexto de toda rotina e só cresceria.
    corte = str(hoje_brasilia() - timedelta(days=45))
    ultima = {hid: v for hid, v in ultima.items() if v[0] >= corte}
    if ultima:
        linhas.append("## Histórias em andamento (data da última menção)")
        for hid, (d, titulo) in sorted(ultima.items(), key=lambda x: x[1][0], reverse=True):
            linhas.append(f"- {hid}: {titulo} (última vez em {d})")
        linhas.append("")
    if any("filosofia" in (e.get("formatos") or []) for e in recentes):
        datas = [e["data"] for e in recentes if "filosofia" in (e.get("formatos") or [])]
        linhas.append(f"Filosofia usada em: {', '.join(datas)}. Máximo uma vez por semana.")
    return "\n".join(linhas + outros)


def _dias_outros(raiz: Path, caderno: str) -> int:
    """Quantos dias olhar nos outros cadernos: desde a última edição deste, com no mínimo 3 e no máximo 14.
    Um caderno que não sai todo dia precisa ver tudo o que a geral publicou desde a edição anterior dele."""
    ultima = ultima_data(raiz, caderno)
    if not ultima:
        return 3
    return max(3, min((hoje_brasilia() - date.fromisoformat(ultima)).days + 1, 14))


def _outros_cadernos(raiz: Path, caderno: str, dias: int = 3) -> list:
    """O que os outros cadernos publicaram nos últimos dias, para não repetir sem trazer nada novo."""
    limite = str(hoje_brasilia() - timedelta(days=dias))
    outras = [e for e in carregar(raiz) if _caderno(e) != caderno and e["data"] >= limite]
    if not outras:
        return []
    linhas = [f"## Nos outros cadernos (últimos {dias} dias)"]
    for e in reversed(outras):
        titulos = "; ".join(h.get("titulo") or h.get("id") or "" for h in (e.get("historias") or []))
        linhas.append(f"- {_caderno(e)} · {e['data']} · {e.get('assunto')}: {titulos}")
    return linhas + [""]
