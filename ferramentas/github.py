"""Dados oficiais de um repositório do GitHub (para a checagem confirmar estrelas etc.)."""
import json
import os
import re
import time
from typing import Optional

from .util import http_get

# Na nuvem, GITHUB_TOKEN e GH_TOKEN valem "proxy-injected": o proxy do GitHub da Anthropic troca esse
# marcador pela credencial do app do Claude, que só alcança o repositório da newsletter (o resto dá 403).
# A chave de leitura do leitor fica em GITHUB_TOKEN_LEITURA, para não mexer na credencial que publica.
MARCADOR_PROXY = "proxy-injected"


def cabecalhos_api() -> dict:
    """Cabeçalhos da API do GitHub, com a chave de leitura se houver (o marcador do proxy não conta)."""
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    for var in ("GITHUB_TOKEN_LEITURA", "GITHUB_TOKEN"):
        token = os.environ.get(var, "").strip()
        if token and token != MARCADOR_PROXY:
            h["Authorization"] = "Bearer " + token
            break
    return h


def motivo(status: int, corpo: bytes) -> str:
    """'HTTP 403 (mensagem do GitHub ou do proxy)', para o log dizer quem bloqueou e por quê."""
    texto = (corpo or b"")[:2000].decode("utf-8", "replace")
    try:
        msg = str(json.loads(texto).get("message") or "")
    except (ValueError, AttributeError):
        msg = "" if "<" in texto[:200] else texto  # página HTML não ajuda
    msg = re.sub(r"\s+", " ", msg).strip()[:160]
    return "HTTP %d (%s)" % (status, msg) if msg else "HTTP %d" % status


def _limpar(repo: str) -> Optional[str]:
    """Aceita 'dono/repo' ou uma URL do GitHub e devolve 'dono/repo' (ou None se não der)."""
    repo = repo.strip()
    repo = re.sub(r"^https?://(www\.)?github\.com/", "", repo)
    m = re.match(r"([\w.-]+)/([\w.-]+)", repo.strip("/"))
    if not m:
        return None
    return "%s/%s" % (m.group(1), re.sub(r"\.git$", "", m.group(2)))


def info(repo: str) -> dict:
    """Consulta https://api.github.com/repos/DONO/REPO.

    Devolve full_name, estrelas, forks, created_at, pushed_at, descricao, html_url e arquivado.
    Se falhar, não levanta erro: devolve {"repo": ..., "erro": "motivo"}.
    """
    nome = _limpar(repo)
    if not nome:
        return {"repo": repo, "erro": "nome inválido (use DONO/REPO)"}
    cabecalhos = cabecalhos_api()
    url = "https://api.github.com/repos/" + nome
    status, corpo = 0, b""
    for tentativa in range(2):
        status, corpo, _ = http_get(url, cabecalhos=cabecalhos)
        if status == 0 or status >= 500:
            time.sleep(2)
            continue
        break
    if status == 404:
        return {"repo": nome, "erro": "repositório não encontrado (HTTP 404)"}
    if status in (403, 429):
        return {"repo": nome, "erro": "%s: limite da API ou bloqueio do proxy? Tente depois ou defina "
                                      "GITHUB_TOKEN_LEITURA" % motivo(status, corpo)}
    if status != 200:
        return {"repo": nome, "erro": "sem resposta (timeout, DNS ou conexão)" if status == 0 else motivo(status, corpo)}
    try:
        d = json.loads(corpo.decode("utf-8"))
    except ValueError:
        return {"repo": nome, "erro": "resposta não é JSON válido"}
    return {
        "full_name": d.get("full_name"),
        "estrelas": d.get("stargazers_count"),
        "forks": d.get("forks_count"),
        "created_at": d.get("created_at"),
        "pushed_at": d.get("pushed_at"),
        "descricao": d.get("description"),
        "html_url": d.get("html_url"),
        "arquivado": d.get("archived"),
    }


def linha(d: dict) -> str:
    """Uma linha legível por repositório (usada pelo comando `github` do main.py)."""
    if d.get("erro"):
        return "%s: ERRO — %s" % (d.get("repo"), d["erro"])
    est = d.get("estrelas")
    estrelas = "{:,}".format(est).replace(",", ".") if isinstance(est, int) else "?"
    return "%s · %s estrelas · %s forks · criado em %s · último push %s%s · %s · %s" % (
        d["full_name"], estrelas, d.get("forks"), (d.get("created_at") or "?")[:10],
        (d.get("pushed_at") or "?")[:10], " · ARQUIVADO" if d.get("arquivado") else "",
        d.get("descricao") or "(sem descrição)", d["html_url"])
