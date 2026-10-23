#!/usr/bin/env python3
"""Inteligência Pragmática: linha de comando.

Exemplos:
  python main.py coletar
  python main.py montar 2026-10-17
  python main.py --dry-run
"""
import argparse
import importlib
import re
import sys
import traceback
import webbrowser
from datetime import date
from pathlib import Path
from typing import Optional

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))

from ferramentas import cadernos, historico, util  # noqa: E402


def _carregar_env() -> None:
    """Lê o arquivo .env (só no Mac; fica fora do git) para as variáveis do envio."""
    import os
    for nome in ("chave_resend.txt", ".env"):  # os dois ficam fora do git
        arq = RAIZ / nome
        if not arq.exists():
            continue
        for linha in arq.read_text(encoding="utf-8").splitlines():
            linha = linha.strip()
            if linha and not linha.startswith("#") and "=" in linha:
                chave, valor = linha.split("=", 1)
                if valor.strip():
                    os.environ.setdefault(chave.strip(), valor.strip())


_carregar_env()

try:  # prefere IPv4 (evita esperas em redes com IPv6 quebrado); opcional
    from ferramentas import rede  # noqa: E402,F401
except ImportError:
    pass


# ───────────────────────── ajudantes ─────────────────────────

def _data(texto: str) -> str:
    """Valida AAAA-MM-DD (ou 'hoje') e devolve a data como texto."""
    if texto.lower() == "hoje":
        return str(util.hoje_brasilia())
    try:
        return date.fromisoformat(texto).isoformat()
    except ValueError:
        raise argparse.ArgumentTypeError("data inválida: %r. Use AAAA-MM-DD, por exemplo 2026-10-17." % texto)


def _pasta(texto: str) -> str:
    """Como _data, mas aceita também AAAA-MM-DD-extra (edição extra de um caderno)."""
    if texto.lower().endswith("-extra"):
        return _data(texto[:-6]) + "-extra"
    return _data(texto)


def _importar(nome: str):
    """Importa ferramentas.NOME; devolve None se o arquivo ainda não existe (outros erros sobem)."""
    try:
        return importlib.import_module("ferramentas." + nome)
    except ModuleNotFoundError as e:
        if e.name == "ferramentas." + nome:
            return None
        raise


def _caderno(args) -> str:
    caderno = getattr(args, "caderno", None) or cadernos.GERAL
    if not cadernos.existe(RAIZ, caderno):
        raise ValueError("caderno desconhecido: %s. Os que existem: %s"
                         % (caderno, ", ".join([cadernos.GERAL] + cadernos.nomes(RAIZ))))
    return caderno


def _config(caderno: str = cadernos.GERAL) -> dict:
    return cadernos.config(RAIZ, caderno)


def _resolver_data(data: Optional[str], caderno: str = cadernos.GERAL) -> str:
    """Pasta pedida, ou a da edição mais recente do caderno. Confere se o edicao.md existe."""
    base = cadernos.pasta_edicoes(RAIZ, caderno)
    rel = base.relative_to(RAIZ).as_posix()
    if data:
        if not (base / data / "edicao.md").exists():
            raise FileNotFoundError("Não achei %s/%s/edicao.md. A edição desse dia já foi escrita?" % (rel, data))
        return data
    recente = util.edicao_mais_recente(RAIZ, caderno)
    if not recente:
        raise FileNotFoundError("Ainda não há nenhuma edição em %s/. A edição é escrita pela rotina." % rel)
    return recente


# ───────────────────────── comandos ─────────────────────────

def cmd_coletar(args) -> int:
    coleta = _importar("coleta")
    if coleta is None:
        print("A coleta ainda não está instalada (falta ferramentas/coleta.py).")
        return 1
    data = date.fromisoformat(args.data or str(util.hoje_brasilia()))
    coleta.coletar(data, RAIZ, _caderno(args))
    return 0


def cmd_historico(args) -> int:
    print(historico.resumo(args.dias, RAIZ, _caderno(args)))
    return 0


def _formatar_repo(info: dict) -> str:
    def milhar(n):
        return "{:,}".format(n).replace(",", ".") if isinstance(n, int) else "?"
    dia = lambda iso: (iso or "?")[:10]  # noqa: E731
    linha = "%s · %s estrelas · %s forks · criado em %s · último push em %s" % (
        info.get("full_name", "?"), milhar(info.get("estrelas")), milhar(info.get("forks")),
        dia(info.get("created_at")), dia(info.get("pushed_at")))
    if info.get("arquivado"):
        linha += " · ARQUIVADO"
    if info.get("descricao"):
        linha += "\n    " + str(info["descricao"])
    if info.get("html_url"):
        linha += "\n    " + str(info["html_url"])
    return linha


def cmd_github(args) -> int:
    github = _importar("github")
    if github is None:
        print("A consulta ao GitHub ainda não está instalada (falta ferramentas/github.py).")
        return 1
    falhou = False
    for repo in args.repos:
        # aceita também o endereço completo: https://github.com/dono/repo
        limpo = re.sub(r"^https?://(www\.)?github\.com/", "", repo.strip()).strip("/")
        limpo = re.sub(r"\.git$", "", limpo)
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", limpo):
            print("%s: formato inválido. Use DONO/REPO, por exemplo anthropics/claude-code." % repo)
            falhou = True
            continue
        try:
            info = github.info(limpo)
        except Exception as e:
            print("%s: não consegui consultar (%s)." % (limpo, e))
            falhou = True
            continue
        if not isinstance(info, dict) or info.get("erro") or not info.get("full_name"):
            motivo = info.get("erro") if isinstance(info, dict) else None
            print("%s: não consegui consultar%s." % (limpo, " (%s)" % motivo if motivo else ""))
            falhou = True
            continue
        print(_formatar_repo(info))
    return 1 if falhou else 0


def cmd_links(args) -> int:
    from ferramentas import links
    caderno = _caderno(args)
    data = _resolver_data(args.data, caderno)
    res = links.verificar(data, RAIZ, caderno=caderno)
    return 1 if res["resumo"]["quebrado"] else 0


def cmd_montar(args) -> int:
    from ferramentas import montagem
    caderno = _caderno(args)
    data = _resolver_data(args.data, caderno)
    res = montagem.montar(data, RAIZ, _config(caderno), caderno)
    print("Edição de %s montada%s:" % (data, "" if caderno == cadernos.GERAL else " (caderno %s)" % caderno))
    print("  e-mail:      %s" % res["email"])
    print("  versão curta: %s (%d caracteres)" % (res["curta"], res["caracteres_curta"]))
    print("  site:        %s e %s" % (res["pagina"], res["indice"]))
    print("  tempo de leitura: %d min" % res["minutos"])
    for aviso in res["avisos"]:
        print("  Atenção: %s" % aviso)
    return 0


def cmd_registrar(args) -> int:
    caderno = _caderno(args)
    data = _resolver_data(args.data, caderno)
    entrada = historico.registrar(data, RAIZ, caderno)
    historias = entrada.get("historias") or []
    print("Edição de %s registrada no histórico (nº %s, %d histórias)." % (data, entrada.get("numero"), len(historias)))
    faltando = [c for c in ("assunto", "numero", "historias", "formatos") if not entrada.get(c)]
    if faltando:
        print("Atenção: faltam no front matter: %s." % ", ".join(faltando))
    return 0


def cmd_enviar(args) -> int:
    from ferramentas import envio
    caderno = _caderno(args)
    data = _resolver_data(args.data, caderno)
    res = envio.enviar(data, RAIZ, _config(caderno), agora=args.agora, forcar=args.forcar, caderno=caderno)
    # "desligado", "aguardando" e "ja_enviada" não são erro.
    return 1 if res["status"] == "erro" else 0


def cmd_publicar(args) -> int:
    """Publica a edição na main de um jeito que aguenta várias rotinas publicando ao mesmo tempo."""
    from ferramentas import publicar
    caderno = _caderno(args)
    data = _resolver_data(args.data, caderno)
    try:
        res = publicar.publicar(data, RAIZ, args.mensagem, caderno)
    except publicar.ErroPublicacao as e:
        print("Erro na publicação: %s" % e)
        return 1
    print("Publicada na main (commit %s, %d tentativa%s)." % (res["commit"], res["tentativas"],
                                                             "" if res["tentativas"] == 1 else "s"))
    return 0


def cmd_enviar_pendentes(args) -> int:
    """Rotina de envio: manda, na ordem (geral e depois os cadernos), as edições de hoje ainda não enviadas."""
    from ferramentas import envio
    hoje = str(util.hoje_brasilia())
    erros = 0
    for caderno in [cadernos.GERAL] + cadernos.nomes(RAIZ):
        pasta = cadernos.pasta_edicoes(RAIZ, caderno) / hoje
        if not (pasta / "edicao.md").exists():
            print("%s: sem edição hoje." % caderno)
            continue
        if (pasta / "envio.json").exists():
            print("%s: já enviada." % caderno)
            continue
        if not (pasta / "email.html").exists():
            print("%s: a edição existe, mas não foi montada (falta email.html). Não enviei." % caderno)
            erros += 1
            continue
        print("%s: " % caderno, end="")
        res = envio.enviar(hoje, RAIZ, _config(caderno), agora=True, caderno=caderno)
        erros += res["status"] == "erro"
    return 1 if erros else 0


def cmd_mercado_painel(args) -> int:
    from ferramentas import mercado
    pasta = args.pasta or str(util.hoje_brasilia())
    res = mercado.gravar_painel(pasta, RAIZ)
    print(res["texto"])
    print("Painel gravado em %s." % res["arquivo"])
    if res["painel"]["falhas"]:
        print("Atenção: estas fontes falharam: %s"
              % "; ".join("%s (%s)" % kv for kv in sorted(res["painel"]["falhas"].items())))
    if res["painel"].get("reservas_usadas"):
        print("Reservas usadas no lugar delas: %s" % ", ".join(res["painel"]["reservas_usadas"]))
    return 0


def cmd_mercado_alarme(args) -> int:
    """Confere os gatilhos numéricos da edição extra. Sai com 0 sempre; o veredito vai no texto."""
    from ferramentas import mercado
    painel = mercado.coletar_painel()
    motivos = mercado.alarme(painel)
    faltam = mercado.nao_conferidos(painel)
    if motivos:
        print("ALARME: há gatilho numérico para edição extra.")
        for m in motivos:
            print("- " + m)
    elif faltam:
        print("SEM ALARME NUMÉRICO nos itens conferidos (os outros estão abaixo).")
    else:
        print("SEM ALARME NUMÉRICO: nenhum gatilho de preço disparou hoje.")
    if faltam:
        print("NÃO CONFERIDO (sem número de hoje): %s. Confira pelas manchetes antes de decidir." % ", ".join(faltam))
    if painel["falhas"]:
        print("Fontes fora do ar: %s" % "; ".join("%s (%s)" % kv for kv in sorted(painel["falhas"].items())))
    if painel.get("reservas_usadas"):
        print("Reservas usadas: %s" % ", ".join(painel["reservas_usadas"]))
    return 0


def cmd_economia_painel(args) -> int:
    from ferramentas import economia
    if args.sem_gravar:  # teste de fontes: não mexe na edição de hoje, que pode já estar publicada
        from datetime import timedelta
        painel = economia.coletar_painel()
        print(economia.painel_md(painel))
        hoje = util.hoje_brasilia()
        texto_apoio, falhas_apoio = economia.apoio(painel, hoje - timedelta(days=7), hoje)
        print("\n".join(l for l in texto_apoio.splitlines() if l.startswith("## ")))
        print("Fontes do painel que falharam: %s" % ("; ".join("%s (%s)" % kv for kv in sorted(painel["falhas"].items()))
                                                    or "nenhuma"))
        print("Apoio da pauta (IBGE): %s" % ("; ".join(falhas_apoio) or "ok"))
        print("Nada foi gravado (--sem-gravar).")
        return 0
    pasta = args.pasta or str(util.hoje_brasilia())
    caderno = args.caderno
    if caderno != economia.CADERNO and not cadernos.existe(RAIZ, caderno):
        raise ValueError("caderno desconhecido: %s" % caderno)
    res = economia.gravar_painel(pasta, RAIZ, caderno=caderno)
    print(res["texto"])
    print("Painel gravado em %s. Apoio da pauta (releases e agenda do IBGE) em %s." % (res["arquivo"], res["apoio"]))
    novos = res["painel"]["novos"]
    print("Dados novos desde a última edição: %s." % (", ".join(novos) if novos else "nenhum"))
    if res["painel"]["falhas"]:
        print("Atenção: estas fontes falharam: %s"
              % "; ".join("%s (%s)" % kv for kv in sorted(res["painel"]["falhas"].items())))
    if res["falhas_apoio"]:
        print("Atenção: o apoio da pauta saiu incompleto: %s" % "; ".join(res["falhas_apoio"]))
    return 0


def cmd_configurar_email(args) -> int:
    """Pede a chave do Resend sem mostrar na tela e grava no .env (fora do git)."""
    import getpass
    import os
    print("Configuração do e-mail (Resend). Nada do que você digitar aparece na tela nem vai para o GitHub.")
    chave = ""
    for tentativa in range(3):
        chave = getpass.getpass("Cole a chave do Resend (começa com re_) e aperte Enter: ").strip()
        if chave.startswith("re_"):
            break
        if not chave:
            print("Não recebi nada: o colar não funcionou. Clique dentro desta janela e use Cmd+V.")
        else:
            # Mostra só o começo e o tamanho, para ajudar sem expor a chave.
            print("O que chegou começa com '%s' e tem %d caracteres. A chave do Resend começa com 're_'."
                  % (chave[:3], len(chave)))
            print("No Resend, a chave aparece uma vez só, logo depois de 'Create API Key'.")
            print("Se ela sumiu, crie outra e copie com o botão de copiar.")
    else:
        print("Nada foi gravado. Rode o comando de novo quando tiver a chave.")
        return 1
    destino = input("E-mail que recebe a newsletter: ").strip() or os.environ.get("EMAIL_DESTINO", "")
    arq = RAIZ / ".env"
    arq.write_text("RESEND_API_KEY=%s\nEMAIL_DESTINO=%s\n" % (chave, destino), encoding="utf-8")
    os.chmod(arq, 0o600)
    print("Pronto: chave guardada em .env (só você lê esse arquivo). Pode voltar para o Claude.")
    return 0


def cmd_dry_run(data_arg: Optional[str]) -> int:
    """Ensaio: coleta, checa links, monta e abre o e-mail no navegador. Nunca envia."""
    coletou = False
    try:
        coleta = _importar("coleta")
        if coleta is None:
            print("Aviso: a coleta ainda não está instalada; sigo sem ela.")
        else:
            coleta.coletar(util.hoje_brasilia(), RAIZ)
            coletou = True
    except Exception as e:
        print("Aviso: a coleta falhou (%s); sigo sem ela." % e)

    try:
        data = _resolver_data(data_arg)
    except FileNotFoundError as e:
        if data_arg:
            print("Erro: %s" % e)
            return 1
        if coletou:
            print("Coleta pronta. A edição é escrita pela rotina (manual/ROTINA.md).")
        else:
            print("Ainda não há edição para montar. A edição é escrita pela rotina (manual/ROTINA.md).")
        return 0

    from ferramentas import links
    print("\nChecando os links da edição de %s..." % data)
    res_links = links.verificar(data, RAIZ)
    if res_links["resumo"]["quebrado"]:
        print("Aviso: há link quebrado (veja acima). Sigo com a montagem.")
    print("\nMontando...")
    cmd_montar(argparse.Namespace(data=data, caderno=cadernos.GERAL))
    email = RAIZ / "edicoes" / data / "email.html"
    webbrowser.open(email.as_uri())
    print("\nAbri %s no navegador. Ensaio terminado: nenhum e-mail foi enviado." % email.relative_to(RAIZ))
    return 0


# ───────────────────────── linha de comando ─────────────────────────

class _Parser(argparse.ArgumentParser):
    """Igual ao padrão, mas erro de uso sai com código 1 (e não 2), como o resto do programa."""

    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(1, "Erro: %s\n" % message)


def criar_parser() -> argparse.ArgumentParser:
    p = _Parser(
        prog="python main.py",
        description="Inteligência Pragmática: coleta, checa, monta e envia a newsletter diária.",
        epilog="Sem data, 'coletar' usa hoje e os outros comandos usam a edição mais recente.")
    p.add_argument("--dry-run", nargs="?", const=True, default=None, metavar="AAAA-MM-DD", type=_data,
                   help="ensaio: coleta, checa links, monta e abre o e-mail no navegador. Nunca envia.")
    sub = p.add_subparsers(dest="comando", metavar="comando")

    ajuda_caderno = "caderno da newsletter (padrão: geral; os outros estão em cadernos.yaml)"
    c = sub.add_parser("coletar", help="busca as fontes e grava os candidatos do dia")
    c.add_argument("--data", type=_data, metavar="AAAA-MM-DD", help="padrão: hoje (Brasília)")
    c.add_argument("--caderno", default=cadernos.GERAL, help=ajuda_caderno)
    c.set_defaults(func=cmd_coletar)

    c = sub.add_parser("historico", help="mostra as últimas edições e as histórias em andamento")
    c.add_argument("--dias", type=int, default=14, help="quantos dias olhar para trás (padrão: 14)")
    c.add_argument("--caderno", default=cadernos.GERAL, help=ajuda_caderno)
    c.set_defaults(func=cmd_historico)

    c = sub.add_parser("github", help="confere estrelas e datas de repositórios")
    c.add_argument("repos", nargs="+", metavar="DONO/REPO")
    c.set_defaults(func=cmd_github)

    for nome, func, ajuda in (
            ("links", cmd_links, "testa os links da edição (sai com erro se algum estiver quebrado)"),
            ("montar", cmd_montar, "gera email.html, curta.txt e o site em docs/"),
            ("registrar", cmd_registrar, "guarda a edição no histórico")):
        c = sub.add_parser(nome, help=ajuda)
        c.add_argument("data", nargs="?", type=_pasta, metavar="AAAA-MM-DD")
        c.add_argument("--caderno", default=cadernos.GERAL, help=ajuda_caderno)
        c.set_defaults(func=func)

    c = sub.add_parser("enviar", help="envia a edição por e-mail (só com envio: ligado no config.yaml)")
    c.add_argument("data", nargs="?", type=_pasta, metavar="AAAA-MM-DD")
    c.add_argument("--caderno", default=cadernos.GERAL, help=ajuda_caderno)
    c.add_argument("--agora", action="store_true", help="envia já, sem agendar para o horário de entrega")
    c.add_argument("--forcar", action="store_true", help="envia mesmo com envio: desligado ou com a edição já enviada")
    c.set_defaults(func=cmd_enviar)

    c = sub.add_parser("publicar", help="grava e publica a edição na main (seguro com várias rotinas ao mesmo tempo)")
    c.add_argument("data", nargs="?", type=_pasta, metavar="AAAA-MM-DD")
    c.add_argument("--caderno", default=cadernos.GERAL, help=ajuda_caderno)
    c.add_argument("-m", "--mensagem", required=True, help='mensagem do commit, por ex. "Edição nº 9 — 2026-10-23: ..."')
    c.set_defaults(func=cmd_publicar)

    c = sub.add_parser("enviar-pendentes", help="rotina de envio: manda juntas as edições de hoje ainda não enviadas")
    c.set_defaults(func=cmd_enviar_pendentes)

    c = sub.add_parser("mercado-painel", help="caderno Mercado: coleta as cotações e grava o painel da edição")
    c.add_argument("pasta", nargs="?", type=_pasta, metavar="AAAA-MM-DD[-extra]", help="padrão: hoje")
    c.set_defaults(func=cmd_mercado_painel)

    c = sub.add_parser("mercado-alarme", help="caderno Mercado: confere os gatilhos de preço da edição extra")
    c.set_defaults(func=cmd_mercado_alarme)

    c = sub.add_parser("economia-painel", help="números oficiais do BC e do IBGE: grava o painel do bloco "
                                              "ECONOMIA do Mercado")
    c.add_argument("pasta", nargs="?", type=_pasta, metavar="AAAA-MM-DD", help="padrão: hoje")
    c.add_argument("--caderno", default="mercado", metavar="CADERNO",
                   help="onde gravar: mercado (padrão), para o bloco ECONOMIA de segunda, quarta e sexta (grava "
                        "painel_economia.md e oficiais.md na pasta da edição do Mercado), ou economia, o caderno "
                        "encerrado em 22/10/2026 (o jeito antigo)")
    c.add_argument("--sem-gravar", action="store_true", help="teste de fontes: só mostra, não grava nada")
    c.set_defaults(func=cmd_economia_painel)

    c = sub.add_parser("configurar-email", help="guarda a chave do Resend no .env (pede sem mostrar na tela)")
    c.set_defaults(func=cmd_configurar_email)
    return p


def main(argv=None) -> int:
    parser = criar_parser()
    args = parser.parse_args(argv)
    try:
        if args.dry_run is not None:
            if args.comando:
                parser.error("use --dry-run sozinho, sem outro comando")
            return cmd_dry_run(None if args.dry_run is True else args.dry_run)
        if not args.comando:
            parser.print_help()
            return 0
        return args.func(args)
    except (FileNotFoundError, ValueError) as e:
        print("Erro: %s" % e)
        return 1
    except KeyboardInterrupt:
        print("\nInterrompido.")
        return 1
    except Exception as e:
        print("Erro inesperado: %s: %s" % (type(e).__name__, e))
        traceback.print_exc(file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
