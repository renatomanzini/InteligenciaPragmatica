"""Envio da edição pelo Resend (agendado para o horário de entrega)."""
import json
import os
import urllib.error
import urllib.request
from datetime import date, datetime, time
from pathlib import Path
from typing import Optional

from . import cadernos
from .montagem import assunto_tachado
from .util import FUSO, USER_AGENT, agora_brasilia, ler_front_matter

URL_RESEND = "https://api.resend.com/emails"
REMETENTE = "Inteligência Pragmática <onboarding@resend.dev>"
# O remetente de teste do Resend (resend.dev) não agenda: o envio com scheduled_at falha com
# "Domain is not verified" (aconteceu em 20/10/2026). Sem domínio próprio, o e-mail sai na hora
# e o horário de chegada depende do horário da rotina.
PODE_AGENDAR = not REMETENTE.rstrip(">").endswith("@resend.dev")


def _remetente(config: dict) -> str:
    """Cada caderno pode ter o próprio nome de remetente; o endereço é sempre o mesmo."""
    nome = (config or {}).get("remetente")
    return REMETENTE if not nome else REMETENTE.replace("Inteligência Pragmática", str(nome), 1)
AVISO_HTML = "Versão completa no HTML."


def _horario_agendado(d: date, horario: str) -> Optional[str]:
    """ISO da data no horário de entrega (offset de Brasília), ou None se já passou."""
    try:
        h, m = [int(x) for x in str(horario).split(":")[:2]]
    except ValueError:
        h, m = 6, 30
    alvo = datetime.combine(d, time(h, m), tzinfo=FUSO)
    return alvo.isoformat(timespec="seconds") if alvo > agora_brasilia() else None


def _cabecalhos(chave: str) -> dict:
    h = {"Content-Type": "application/json", "User-Agent": USER_AGENT}
    # Na nuvem, a chave fica num "network secret": o proxy da Anthropic põe o Authorization sozinho.
    if chave:
        h["Authorization"] = "Bearer " + chave
    return h


def _postar(payload: dict, chave: str) -> dict:
    """Faz o POST no Resend. Devolve {'ok': True, 'dados': {...}} ou {'ok': False, 'erro': '...'}."""
    req = urllib.request.Request(
        URL_RESEND,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=_cabecalhos(chave),
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return {"ok": True, "dados": json.loads(resp.read().decode("utf-8") or "{}")}
    except urllib.error.HTTPError as e:
        try:
            detalhe = e.read().decode("utf-8", "replace")[:300]
        except Exception:
            detalhe = ""
        return {"ok": False, "erro": "o Resend respondeu %d. %s" % (e.code, detalhe)}
    except Exception as e:
        return {"ok": False, "erro": "não consegui falar com o Resend (%s)" % type(e).__name__}


def _resultado(status: str, mensagem: str, **extra) -> dict:
    print(mensagem)
    res = {"status": status, "mensagem": mensagem}
    res.update(extra)
    return res


def enviar(data: str, raiz: Path, config: dict, agora: bool = False, forcar: bool = False,
           caderno: str = cadernos.GERAL) -> dict:
    """Envia a edição. Devolve {'status': 'enviado' | 'desligado' | 'erro', 'mensagem': ...}."""
    data = str(data)
    config = config or {}
    if config.get("envio") != "ligado" and not forcar:
        return _resultado("desligado", "Envio desligado no config.yaml (fase de testes). Nada foi enviado.")

    chave = os.environ.get("RESEND_API_KEY", "").strip()
    via_proxy = os.environ.get("RESEND_VIA_PROXY", "") == "1"
    destino = os.environ.get("EMAIL_DESTINO", "").strip()
    faltam = [nome for nome, valor in (("RESEND_API_KEY", chave or via_proxy), ("EMAIL_DESTINO", destino))
              if not valor]
    if faltam:
        return _resultado("erro", "Faltam variáveis de ambiente: %s. Nada foi enviado." % ", ".join(faltam))

    pasta = cadernos.pasta_edicoes(raiz, caderno) / data
    arq_html, arq_curta = pasta / "email.html", pasta / "curta.txt"
    if not (arq_html.exists() and arq_curta.exists()):
        return _resultado("erro", "Faltam email.html e curta.txt em edicoes/%s. Rode antes: python main.py montar %s"
                          % (data, data))
    meta, _ = ler_front_matter(pasta / "edicao.md")

    assunto = assunto_tachado(str(meta.get("assunto") or "Inteligência Pragmática"))
    texto = arq_curta.read_text(encoding="utf-8").rstrip() + "\n\n" + AVISO_HTML + "\n"
    payload = {
        "from": _remetente(config),
        "to": [destino],
        "subject": assunto,
        "html": arq_html.read_text(encoding="utf-8"),
        "text": texto,
    }
    agendado = None if (agora or not PODE_AGENDAR) else _horario_agendado(date.fromisoformat(data[:10]), config.get("horario_entrega", "06:30"))
    if agendado:
        payload["scheduled_at"] = agendado

    resp = _postar(payload, chave)
    if not resp["ok"]:
        return _resultado("erro", "Erro no envio: %s" % resp["erro"])
    id_envio = resp["dados"].get("id", "")
    # O destinatário não é gravado: o repositório é público.
    registro = {"id": id_envio, "assunto": assunto, "agendado_para": agendado,
                "enviado_em": agora_brasilia().isoformat(timespec="seconds")}
    (pasta / "envio.json").write_text(json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8")
    quando = ("agendado para %s" % agendado) if agendado else "enviado agora"
    return _resultado("enviado", "E-mail %s. ID do Resend: %s" % (quando, id_envio), id=id_envio, agendado_para=agendado)
