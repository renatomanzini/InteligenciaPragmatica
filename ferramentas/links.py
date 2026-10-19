"""Verificação dos links de uma edição (edicoes/DATA/edicao.md → links.json)."""
import json
import re
import socket
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urlsplit

from .util import agora_brasilia, http_get

# Começa em http(s):// e vai até um espaço ou um caractere que nunca faz parte do link.
RE_URL = re.compile(r"https?://[A-Za-z0-9][^\s<>\"'`\[\]|{}\\^]*")
PONTUACAO_FINAL = ".,;:!?…*"

OK, QUEBRADO, INCONCLUSIVO = "ok", "quebrado", "inconclusivo"


def _limpar(url: str) -> str:
    """Tira pontuação colada no fim do link e parêntese de fechamento que sobra."""
    while url:
        if url[-1] in PONTUACAO_FINAL:
            url = url[:-1]
        elif url[-1] == ")" and url.count("(") < url.count(")"):
            url = url[:-1]
        else:
            break
    return url


def extrair_urls(texto: str) -> List[str]:
    """Todas as URLs http(s) do texto, sem repetir, na ordem em que aparecem."""
    vistas, urls = set(), []
    for m in RE_URL.finditer(texto):
        u = _limpar(m.group(0))
        if u and u not in vistas:
            vistas.add(u)
            urls.append(u)
    return urls


@lru_cache(maxsize=1)
def _sem_internet() -> bool:
    """True se nem sites conhecidos resolvem: aí o erro de DNS é da conexão, não do link."""
    for host in ("www.google.com", "github.com"):
        try:
            socket.getaddrinfo(host, 443)
            return False
        except OSError:
            continue
    return True


def _dns_falhou(url: str) -> bool:
    host = urlsplit(url).hostname
    if not host:
        return True
    try:
        socket.getaddrinfo(host, None)
        return False
    except socket.gaierror:
        return True
    except OSError:
        return False


def _classificar(status: int, url: str) -> Tuple[str, str]:
    """Devolve (resultado, detalhe)."""
    if 200 <= status < 400:
        return OK, ""
    if status in (404, 410):
        return QUEBRADO, "página não existe (%d)" % status
    if status == 0:
        if _dns_falhou(url):
            if _sem_internet():
                return INCONCLUSIVO, "sem internet para testar"
            return QUEBRADO, "o endereço do site não existe (DNS)"
        return INCONCLUSIVO, "sem resposta (tempo esgotado ou conexão recusada)"
    if status in (401, 403, 429):
        return INCONCLUSIVO, "o site bloqueia robôs ou exige login (%d)" % status
    if status >= 500:
        return INCONCLUSIVO, "erro no servidor do site (%d)" % status
    return INCONCLUSIVO, "resposta inesperada (%d)" % status


def _caiu_na_home(url: str, final: str) -> bool:
    """Link para uma página interna que, depois dos redirecionamentos, terminou na raiz do site."""
    if not final:
        return False
    original, destino = urlsplit(url), urlsplit(final)
    return original.path.strip("/") != "" and destino.path.strip("/") == "" and not destino.query


def _checar(url: str) -> dict:
    """HEAD primeiro; se não deu certo, confirma com GET (só os primeiros 64 KB)."""
    metodo = "HEAD"
    status, _, final = http_get(url, metodo="HEAD")
    if not 200 <= status < 400:
        metodo = "GET"
        status, _, final = http_get(url, max_bytes=64 * 1024)
    resultado, detalhe = _classificar(status, url)
    if resultado == OK and _caiu_na_home(url, final):
        # Ex.: http://classics.mit.edu/... → https://classics.mit.edu/ (abre, mas não é a página citada)
        resultado, detalhe = INCONCLUSIVO, "redirecionou para a página inicial do site"
    item = {"url": url, "status": status, "resultado": resultado, "metodo": metodo}
    if final and final != url:
        item["url_final"] = final
    if detalhe:
        item["detalhe"] = detalhe
    return item


def _tabela(res: dict) -> str:
    r = res["resumo"]
    linhas = ["Links da edição %s: %d verificados · %d ok · %d quebrados · %d inconclusivos"
              % (res["data"], res["total"], r[OK], r[QUEBRADO], r[INCONCLUSIVO]), ""]
    ordem = {QUEBRADO: 0, INCONCLUSIVO: 1, OK: 2}
    for it in sorted(res["links"], key=lambda i: ordem[i["resultado"]]):
        nota = "  (%s)" % it["detalhe"] if it.get("detalhe") else ""
        linhas.append("%-13s %-5s %s%s" % (it["resultado"], it["status"] or "-", it["url"], nota))
    if r[QUEBRADO]:
        linhas += ["", "Há link quebrado: troque pela fonte certa ou corte o item."]
    return "\n".join(linhas)


def verificar(data: str, raiz: Path, imprimir: bool = True) -> dict:
    """Testa os links de edicoes/DATA/edicao.md, grava links.json e imprime a tabela."""
    data = str(data)
    arq = raiz / "edicoes" / data / "edicao.md"
    if not arq.exists():
        raise FileNotFoundError("Não achei %s" % arq.relative_to(raiz))
    urls = extrair_urls(arq.read_text(encoding="utf-8"))
    with ThreadPoolExecutor(max_workers=8) as ex:
        itens = list(ex.map(_checar, urls))
    resumo = {OK: 0, QUEBRADO: 0, INCONCLUSIVO: 0}
    for it in itens:
        resumo[it["resultado"]] += 1
    res = {
        "data": data,
        "verificado_em": agora_brasilia().isoformat(timespec="seconds"),
        "total": len(itens),
        "resumo": resumo,
        "links": itens,
    }
    (arq.parent / "links.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    if imprimir:
        print(_tabela(res))
    return res
