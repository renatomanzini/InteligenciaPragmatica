"""Publicação na main que aguenta várias rotinas rodando ao mesmo tempo.

O problema: a geral e os cadernos escrevem em paralelo e todas mexem em dois lugares comuns,
o histórico (dados/historico.json) e o site (docs/index.html, docs/<caderno>.html). Com
`git pull --rebase`, dois commits que mexem nesses arquivos dão conflito.

A solução:
1. A rotina grava primeiro só o que é dela: a pasta da edição, os candidatos e os dados do caderno.
   Ninguém mais mexe nesses arquivos, então o rebase nunca conflita.
2. Depois de trazer o que as outras publicaram, ela refaz o histórico e o site por código
   (`registrar` e `montar`), já com as edições das outras, e grava isso num segundo commit.
3. Se o push for recusado porque alguém publicou no meio, ela descarta o segundo commit e repete.
4. Se desistir, guarda a edição no ramo pendente/<caderno>-<data> e avisa (o clone da nuvem some no fim).

O guardar é a versão curta, para os dias sem edição dos cadernos com dias fixos: publica só a curadoria.

Atenção: o publicar descarta mudanças sem commit em docs/ e em dados/historico.json, que ele mesmo refaz.
Correção feita à mão nesses arquivos precisa de commit antes.
"""
import subprocess
import time
from pathlib import Path
from typing import List, Optional

from . import cadernos, historico, montagem

COMPARTILHADOS = ["dados/historico.json", "docs"]


class ErroPublicacao(RuntimeError):
    pass


def _git(raiz: Path, *args: str, checar: bool = True) -> subprocess.CompletedProcess:
    p = subprocess.run(["git"] + list(args), cwd=str(raiz), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       universal_newlines=True)
    if checar and p.returncode != 0:
        raise ErroPublicacao("git %s falhou: %s" % (" ".join(args), p.stdout.strip()[-400:]))
    return p


def arquivos_proprios(raiz: Path, data: str, caderno: str = cadernos.GERAL) -> List[str]:
    """Os caminhos que só esta edição usa (relativos à raiz e que existem)."""
    raiz = Path(raiz)
    prefixo = cadernos.prefixo(caderno)
    dia = data[:10]
    candidatos = [cadernos.pasta_edicoes(raiz, caderno) / data]
    candidatos += sorted((raiz / "dados" / "candidatos").glob("%s%s*" % (prefixo, dia)))
    if caderno != cadernos.GERAL:
        candidatos += sorted((raiz / "dados" / caderno).glob("%s*" % data))
        candidatos.append(cadernos.arquivo_curadoria(raiz, caderno))  # o que sobrou da curadoria vai junto
    candidatos.append(raiz / "docs" / ("%s%s.html" % (prefixo, data)))  # a página da edição no site
    # Na geral, o glob "AAAA-MM-DD*" não pega candidatos de caderno, que começam com o nome do caderno.
    return [c.relative_to(raiz).as_posix() for c in candidatos if c.exists()]


def _resgatar(raiz: Path, remoto: str, caderno: str, data: str, motivo: str,
              oque: str = "a edição") -> ErroPublicacao:
    """Quando desiste, guarda a edição num ramo próprio: o clone da rotina na nuvem é descartado no fim."""
    ramo = "pendente/%s-%s" % (caderno, data)
    p = _git(raiz, "push", "-q", remoto, "+HEAD:refs/heads/%s" % ramo, checar=False)
    if p.returncode == 0:
        return ErroPublicacao("%s. %s NÃO entrou na main: ficou guardada no ramo %s." % (motivo, oque.capitalize(), ramo))
    return ErroPublicacao("%s. Também não consegui guardar %s no ramo %s: ela só existe neste clone."
                          % (motivo, oque, ramo))


def _rastreado(raiz: Path, caminho: str) -> bool:
    return bool(_git(raiz, "ls-files", "--", caminho, checar=False).stdout.strip())


def _ha_mudanca_preparada(raiz: Path) -> bool:
    return _git(raiz, "diff", "--cached", "--quiet", checar=False).returncode != 0


def publicar(data: str, raiz: Path, mensagem: str, caderno: str = cadernos.GERAL, remoto: str = "origin",
             ramo: str = "main", tentativas: int = 6, espera: float = 4.0, config: Optional[dict] = None) -> dict:
    """Publica a edição da pasta DATA do caderno na main. Devolve {'commits': [...], 'tentativas': n}."""
    raiz = Path(raiz)
    data = str(data)
    if not (cadernos.pasta_edicoes(raiz, caderno) / data / "edicao.md").exists():
        raise ErroPublicacao("não achei a edição %s do caderno %s" % (data, caderno))
    config = config if config is not None else cadernos.config(raiz, caderno)

    # 1) só os arquivos desta edição
    proprios = arquivos_proprios(raiz, data, caderno)
    _git(raiz, "add", "--", *proprios)
    if _ha_mudanca_preparada(raiz):
        _git(raiz, "commit", "-q", "-m", mensagem)

    for tentativa in range(1, tentativas + 1):
        # 2) traz o que as outras rotinas publicaram; os arquivos próprios não conflitam com ninguém.
        #    Os compartilhados são refeitos logo abaixo, então a versão local deles pode ser descartada.
        _git(raiz, "checkout", "-q", "HEAD", "--", *[c for c in COMPARTILHADOS if _rastreado(raiz, c)],
             checar=False)
        # O checkout não apaga arquivo novo, e o montar cria em todo clone o índice de um caderno novo
        # (docs/<caderno>.html). Se ficasse, o pull de quem publica depois travaria nele.
        _git(raiz, "clean", "-fdq", "--", *COMPARTILHADOS, checar=False)
        p = _git(raiz, "pull", "-q", "--rebase", "--autostash", remoto, ramo, checar=False)
        if p.returncode != 0:
            _git(raiz, "rebase", "--abort", checar=False)
            raise _resgatar(raiz, remoto, caderno, data,
                            "o pull --rebase falhou mesmo só com arquivos próprios: %s" % p.stdout.strip()[-400:])

        # 3) refaz histórico e site com todas as edições que agora estão na pasta
        historico.registrar(data, raiz, caderno)
        montagem.montar(data, raiz, config, caderno)
        _git(raiz, "add", "--", *[c for c in COMPARTILHADOS if (raiz / c).exists()],
             *arquivos_proprios(raiz, data, caderno))
        fez_commit = _ha_mudanca_preparada(raiz)
        if fez_commit:
            _git(raiz, "commit", "-q", "-m", "Histórico e site: %s" % mensagem.splitlines()[0])

        # 4) publica; se alguém publicou no meio, descarta o commit do histórico e tenta de novo
        p = _git(raiz, "push", "-q", remoto, "HEAD:%s" % ramo, checar=False)
        if p.returncode == 0:
            topo = _git(raiz, "log", "-1", "--format=%h").stdout.strip()
            return {"tentativas": tentativa, "commit": topo}
        if fez_commit:
            # --keep (e não --hard): desfaz só o commit do histórico e do site e preserva qualquer outra
            # alteração local sem commit; se tivesse de mexer numa delas, aborta em vez de apagar.
            _git(raiz, "reset", "-q", "--keep", "HEAD~1")
        time.sleep(espera * tentativa)
    raise _resgatar(raiz, remoto, caderno, data, "o push foi recusado %d vezes seguidas (último erro: %s)"
                    % (tentativas, p.stdout.strip()[-300:]))


def guardar(data: str, raiz: Path, mensagem: str, caderno: str, remoto: str = "origin", ramo: str = "main",
            tentativas: int = 6, espera: float = 4.0) -> dict:
    """Publica só a curadoria do caderno (dados/<caderno>/curadoria.md), no dia em que não há edição.
    Ninguém mais mexe nesse arquivo, então o rebase nunca conflita. Devolve {'commit': ..., 'tentativas': n};
    commit None quando a curadoria não mudou."""
    raiz = Path(raiz)
    arq = cadernos.arquivo_curadoria(raiz, caderno)
    if caderno == cadernos.GERAL or not arq.exists():
        raise ErroPublicacao("não achei a curadoria do caderno %s (%s)" % (caderno, arq.relative_to(raiz).as_posix()))
    _git(raiz, "add", "--", arq.relative_to(raiz).as_posix())
    if not _ha_mudanca_preparada(raiz):
        return {"commit": None, "tentativas": 0}
    _git(raiz, "commit", "-q", "-m", mensagem)
    p = None
    for tentativa in range(1, tentativas + 1):
        p = _git(raiz, "pull", "-q", "--rebase", "--autostash", remoto, ramo, checar=False)
        if p.returncode != 0:
            _git(raiz, "rebase", "--abort", checar=False)
            raise _resgatar(raiz, remoto, caderno, "curadoria-" + str(data),
                            "o pull --rebase falhou: %s" % p.stdout.strip()[-400:], "a curadoria")
        p = _git(raiz, "push", "-q", remoto, "HEAD:%s" % ramo, checar=False)
        if p.returncode == 0:
            return {"tentativas": tentativa, "commit": _git(raiz, "log", "-1", "--format=%h").stdout.strip()}
        time.sleep(espera * tentativa)
    raise _resgatar(raiz, remoto, caderno, "curadoria-" + str(data), "o push foi recusado %d vezes seguidas "
                    "(último erro: %s)" % (tentativas, p.stdout.strip()[-300:]), "a curadoria")
