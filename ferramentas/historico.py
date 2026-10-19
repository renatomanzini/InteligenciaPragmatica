"""Memória da newsletter: o que já saiu, histórias em andamento e formatos usados."""
import json
from datetime import timedelta
from pathlib import Path

from .util import hoje_brasilia, ler_front_matter, normalizar_url

CAMPOS = ["data", "tipo", "numero", "assunto", "previa", "dia", "breakthrough", "historias", "formatos"]


def _arquivo(raiz: Path) -> Path:
    return raiz / "dados" / "historico.json"


def carregar(raiz: Path) -> list:
    arq = _arquivo(raiz)
    if not arq.exists():
        return []
    return json.loads(arq.read_text(encoding="utf-8"))


def registrar(data: str, raiz: Path) -> dict:
    meta, _ = ler_front_matter(raiz / "edicoes" / data / "edicao.md")
    entrada = {c: meta.get(c) for c in CAMPOS}
    entrada["data"] = str(meta.get("data") or data)
    edicoes = [e for e in carregar(raiz) if e["data"] != entrada["data"]]
    edicoes.append(entrada)
    edicoes.sort(key=lambda e: e["data"])
    arq = _arquivo(raiz)
    arq.parent.mkdir(parents=True, exist_ok=True)
    arq.write_text(json.dumps(edicoes, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    return entrada


def proximo_numero(raiz: Path) -> int:
    numeros = [e.get("numero") or 0 for e in carregar(raiz)]
    return (max(numeros) if numeros else 0) + 1


def urls_cobertas(raiz: Path) -> set:
    urls = set()
    for e in carregar(raiz):
        for h in e.get("historias") or []:
            for u in h.get("urls") or []:
                urls.add(normalizar_url(u))
    return urls


def resumo(dias: int = 14, raiz: Path = Path(".")) -> str:
    edicoes = carregar(raiz)
    if not edicoes:
        return "Nenhuma edição registrada ainda. Esta será a edição nº 1."
    limite = str(hoje_brasilia() - timedelta(days=dias))
    recentes = [e for e in edicoes if e["data"] >= limite] or edicoes[-3:]
    linhas = [f"# Histórico: últimas {len(recentes)} edições (próxima: nº {proximo_numero(raiz)})", ""]
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
    if ultima:
        linhas.append("## Histórias em andamento (data da última menção)")
        for hid, (d, titulo) in sorted(ultima.items(), key=lambda x: x[1][0], reverse=True):
            linhas.append(f"- {hid}: {titulo} (última vez em {d})")
        linhas.append("")
    if any("filosofia" in (e.get("formatos") or []) for e in recentes):
        datas = [e["data"] for e in recentes if "filosofia" in (e.get("formatos") or [])]
        linhas.append(f"Filosofia usada em: {', '.join(datas)}. Máximo uma vez por semana.")
    return "\n".join(linhas)
