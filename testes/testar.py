"""Teste de ponta a ponta do código (sem enviar e-mail e sem tocar nas pastas reais).

Rode da raiz do projeto:
    .venv/bin/python testes/testar.py

Tudo acontece numa pasta temporária: a edição de exemplo é copiada para lá, montada,
registrada no histórico e conferida. Os links do exemplo apontam para sites reais, então
a verificação de links usa a internet (sem internet, ela vira "inconclusiva" e o teste segue).
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ_PROJETO))

from ferramentas import envio, historico, links, montagem, util  # noqa: E402

DATA = "2026-01-15"
falhas = []


def conferir(condicao, descricao):
    print(("  ok     " if condicao else "  FALHOU ") + descricao)
    if not condicao:
        falhas.append(descricao)


def secao(titulo):
    print("\n== %s" % titulo)


def preparar_raiz(tmp: Path, copiar_codigo: bool = False) -> Path:
    raiz = tmp / "projeto"
    pasta = raiz / "edicoes" / DATA
    pasta.mkdir(parents=True)
    shutil.copy(RAIZ_PROJETO / "testes" / "edicao_exemplo.md", pasta / "edicao.md")
    if copiar_codigo:  # para rodar o main.py de verdade (ele usa a pasta onde está)
        shutil.copy(RAIZ_PROJETO / "main.py", raiz / "main.py")
        cfg = (RAIZ_PROJETO / "config.yaml").read_text(encoding="utf-8")
        # a cópia de teste nunca envia de verdade, mesmo com o envio ligado no projeto
        (raiz / "config.yaml").write_text(re.sub(r"(?m)^envio:.*$", "envio: desligado", cfg), encoding="utf-8")
        shutil.copytree(RAIZ_PROJETO / "ferramentas", raiz / "ferramentas",
                        ignore=shutil.ignore_patterns("__pycache__", "coleta.py", "github.py"))
    return raiz


def testar_links(raiz):
    secao("links.verificar")
    res = links.verificar(DATA, raiz, imprimir=False)
    arq = raiz / "edicoes" / DATA / "links.json"
    conferir(arq.exists(), "gravou links.json")
    conferir(json.loads(arq.read_text(encoding="utf-8"))["total"] == res["total"], "links.json bate com o resultado")
    urls = [i["url"] for i in res["links"]]
    conferir(res["total"] == 6, "achou os 6 links diferentes do corpo e do front matter (%d)" % res["total"])
    conferir("https://www.python.org" in urls and "https://github.com" in urls, "inclui links do front matter e do texto")
    conferir(not any(u.endswith((")", ".", ",")) for u in urls), "nenhuma URL ficou com pontuação colada")
    conferir(res["resumo"]["quebrado"] == 0, "nenhum link do exemplo está quebrado: %s" % res["resumo"])
    # extração de URLs em casos chatos
    texto = "veja [x](https://a.com/foo_(bar)) e https://b.com/p?q=1. Também <https://c.com/z>, fim."
    conferir(links.extrair_urls(texto) == ["https://a.com/foo_(bar)", "https://b.com/p?q=1", "https://c.com/z"],
             "extrair_urls lida com parênteses, ponto final e <autolink>")

    # classificação com um link morto de verdade (só se a internet estiver funcionando)
    if res["resumo"]["ok"] == 0:
        print("  (sem internet: pulei o teste de link quebrado)")
        return
    pasta = raiz / "edicoes" / "2026-01-16"
    pasta.mkdir()
    (pasta / "edicao.md").write_text(
        "---\ndata: 2026-01-16\n---\n[a](https://github.com/pagina-que-nao-existe-ip-teste-404-xyz) "
        "[b](https://dominio-que-nao-existe.invalid/x) [c](https://github.com)\n", encoding="utf-8")
    r2 = links.verificar("2026-01-16", raiz, imprimir=False)
    por_url = {i["url"]: i["resultado"] for i in r2["links"]}
    conferir(por_url["https://github.com/pagina-que-nao-existe-ip-teste-404-xyz"] == "quebrado", "404 é 'quebrado'")
    conferir(por_url["https://dominio-que-nao-existe.invalid/x"] == "quebrado", "domínio que não existe é 'quebrado'")
    conferir(por_url["https://github.com"] == "ok", "github.com é 'ok'")
    shutil.rmtree(pasta)


def png_tamanho(dados: bytes):
    if dados[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return int.from_bytes(dados[16:20], "big"), int.from_bytes(dados[20:24], "big")


def testar_montagem(raiz):
    secao("montagem.montar")
    config = util.ler_yaml(RAIZ_PROJETO / "config.yaml")
    config["site_url"] = ""
    res = montagem.montar(DATA, raiz, config)
    pasta = raiz / "edicoes" / DATA
    docs = raiz / "docs"
    conferir(res["avisos"] == [], "sem avisos de front matter/TL;DR (%s)" % res["avisos"])
    for caminho in (pasta / "email.html", pasta / "curta.txt", docs / (DATA + ".html"), docs / "index.html",
                    docs / "manifest.webmanifest", docs / "sw.js", docs / "icon.svg",
                    docs / "icon-192.png", docs / "icon-512.png"):
        conferir(caminho.exists() and caminho.stat().st_size > 0, "gerou %s" % caminho.relative_to(raiz))
    conferir(png_tamanho((docs / "icon-192.png").read_bytes()) == (192, 192), "icon-192.png é um PNG 192x192")
    conferir(png_tamanho((docs / "icon-512.png").read_bytes()) == (512, 512), "icon-512.png é um PNG 512x512")
    json.loads((docs / "manifest.webmanifest").read_text(encoding="utf-8"))
    conferir(True, "manifest.webmanifest é um JSON válido")

    email = (pasta / "email.html").read_text(encoding="utf-8")
    secao("email.html: convenções convertidas")
    conferir("~~" not in email, "nenhum ~~ sobrou")
    conferir(email.count("<del ") == 2 and "</del>" in email, "os 2 tachados do corpo viraram <del> (o assunto não aparece no corpo)")
    conferir(not re.search(r"<(h[1-4]|p|ul|li|blockquote|hr)>", email), "todas as tags principais têm style inline")
    conferir("####" not in email and "<h4" in email and "text-transform:uppercase" in email, "#### virou rótulo em caixa alta")
    conferir(email.count("border-left:4px solid #0F5C6E") == 4, "4 TL;DR viraram caixa com borda (%d)" % email.count("border-left:4px solid #0F5C6E"))
    conferir(re.search(r"TL;DR:</strong> \w", email) is not None, "TL;DR com espaço depois do rótulo")
    conferir(email.count('class="seta"') == 5, "5 linhas → viraram itens com seta (%d)" % email.count('class="seta"'))
    conferir('class="setas"' in email, "linhas → consecutivas formam bloco")
    conferir(email.count('class="fonte"') == 5 and "13.5px" in email, "5 linhas 🔗 viraram linha de fonte menor (%d)" % email.count('class="fonte"'))
    conferir('class="opiniao"' in email and 'class="selo"' in email and "font-style:italic" in email,
             "**Opinião:** virou parágrafo com selo")
    conferir("Opinião:</strong>" not in email, "o '**Opinião:**' cru sumiu")
    conferir("<hr" in email and "border-top:1px solid" in email, "--- virou linha fina")
    conferir("<h3" in email and "<h2" in email, "## e ### viram títulos")
    conferir("Georgia" in email and "#FAF8F5" in email and "#0F5C6E" in email and "#1F1F1F" in email, "paleta e fontes do visual")
    conferir('max-width:640px' in email and 'width="640"' in email, "tabela centralizada de 640 px")
    conferir("prefers-color-scheme: dark" in email, "tem modo escuro")
    conferir("Inteligência Pragmática" in email and "quinta-feira, 15 de janeiro de 2026" in email
             and "Edição nº 1" in email and "7 min de leitura" in email, "cabeçalho: nome, data por extenso, nº e minutos")
    conferir("display:none" in email and "EXEMPLO FICTÍCIO · + quanto custa" in email, "pré-header escondido com a prévia")
    conferir("Feita por IA para um leitor só. Fontes linkadas em cada afirmação." in email, "rodapé com a frase fixa")
    conferir("Arquivo de edições" not in email, "sem site_url, sem link de arquivo no rodapé")
    conferir(not re.search(r"<img|src=\"http|url\(http", email), "sem imagens externas")

    curta = (pasta / "curta.txt").read_text(encoding="utf-8")
    secao("curta.txt")
    conferir(len(curta.strip()) <= 900, "cabe em 900 caracteres (%d)" % len(curta.strip()))
    conferir(3 <= curta.count("• ") <= 5, "tem de 3 a 5 bullets (%d)" % curta.count("• "))
    conferir("TL;DR" not in curta and "**" not in curta and "~~" not in curta, "sem marcas de Markdown")
    conferir("̶" in curta.splitlines()[0], "assunto com tachado combinante na primeira linha")
    conferir("quinta-feira, 15 de janeiro de 2026" in curta, "tem a data por extenso")
    conferir("Edição completa" not in curta, "sem site_url, sem link de edição completa")

    pagina = (docs / (DATA + ".html")).read_text(encoding="utf-8")
    indice = (docs / "index.html").read_text(encoding="utf-8")
    secao("site (docs/)")
    for nome, texto in (("página da edição", pagina), ("índice", indice)):
        conferir('rel="manifest"' in texto and "apple-touch-icon" in texto and 'name="theme-color"' in texto,
                 "%s: manifest, apple-touch-icon e theme-color" % nome)
        internos = [u for u in re.findall(r'(?:href|src)="([^"]+)"', texto) if not re.match(r"(https?:|#|mailto:)", u)]
        conferir(internos and not any(u.startswith("/") for u in internos), "%s: links internos são relativos %s" % (nome, sorted(set(internos))))
    conferir("← todas as edições" in pagina and 'href="index.html"' in pagina, "página tem o link '← todas as edições'")
    conferir("prefers-color-scheme: dark" in pagina and "max-width" in pagina and "viewport" in pagina,
             "página é responsiva e tem modo escuro")
    conferir("<del>" in pagina and '<h1 class="assunto">o <del>estagiário</del>' in pagina, "assunto com <del> na página")
    conferir(f'href="{DATA}.html"' in indice and "<del>estagiário</del>" in indice and "nº 1" in indice,
             "índice lista a edição com data, nº e assunto com <del>")
    conferir("EXEMPLO FICTÍCIO" in indice, "índice mostra a prévia")
    conferir("serviceWorker" in pagina and "serviceWorker" in indice, "páginas registram o service worker")
    conferir("caches.open" in (docs / "sw.js").read_text(encoding="utf-8"), "sw.js guarda páginas em cache")

    # segunda edição: o índice deve ordenar da mais nova para a mais antiga
    pasta2 = raiz / "edicoes" / "2026-01-16"
    pasta2.mkdir()
    texto2 = (pasta / "edicao.md").read_text(encoding="utf-8").replace("2026-01-15", "2026-01-16").replace("numero: 1", "numero: 2")
    (pasta2 / "edicao.md").write_text(texto2, encoding="utf-8")
    montagem.montar("2026-01-16", raiz, config)
    indice2 = (docs / "index.html").read_text(encoding="utf-8")
    conferir(indice2.index("2026-01-16.html") < indice2.index("2026-01-15.html"), "índice ordena da mais nova para a mais antiga")
    shutil.rmtree(pasta2)
    (docs / "2026-01-16.html").unlink()
    montagem.montar(DATA, raiz, config)

    # com site_url preenchido
    config["site_url"] = "https://exemplo.github.io/ip/"
    montagem.montar(DATA, raiz, config)
    email = (pasta / "email.html").read_text(encoding="utf-8")
    curta = (pasta / "curta.txt").read_text(encoding="utf-8")
    secao("com site_url preenchido")
    conferir('href="https://exemplo.github.io/ip/"' in email and "Arquivo de edições" in email, "rodapé do e-mail linka o arquivo")
    conferir(curta.strip().endswith("Edição completa: https://exemplo.github.io/ip/%s.html" % DATA), "curta.txt termina com o link da edição")
    conferir(len(curta.strip()) <= 900, "curta.txt continua cabendo em 900 (%d)" % len(curta.strip()))
    pagina = (docs / (DATA + ".html")).read_text(encoding="utf-8")
    conferir("exemplo.github.io" not in pagina, "links internos do site não usam o site_url (continuam relativos)")


def testar_historico(raiz):
    secao("historico.registrar e resumo")
    entrada = historico.registrar(DATA, raiz)
    arq = raiz / "dados" / "historico.json"
    conferir(arq.exists(), "gravou dados/historico.json")
    dados = json.loads(arq.read_text(encoding="utf-8"))
    conferir(len(dados) == 1 and dados[0]["data"] == DATA and dados[0]["numero"] == 1, "entrada com data e número certos")
    conferir(len(entrada["historias"]) == 3, "3 histórias registradas")
    historico.registrar(DATA, raiz)
    conferir(len(json.loads(arq.read_text(encoding="utf-8"))) == 1, "registrar de novo substitui, não duplica")
    texto = historico.resumo(36500, raiz)
    conferir("exemplo-agente-de-contratos" in texto and "(em andamento)" in texto, "resumo lista as histórias e o 'em andamento'")
    conferir("Histórias em andamento" in texto and DATA in texto, "resumo tem a seção de histórias em andamento")
    conferir(historico.proximo_numero(raiz) == 2, "próximo número é 2")
    conferir("https://www.python.org" in {u.rstrip("/") for u in historico.urls_cobertas(raiz)} or len(historico.urls_cobertas(raiz)) >= 3,
             "urls_cobertas devolve as URLs das histórias")


def testar_envio(raiz):
    secao("envio.enviar (sem chamar o Resend de verdade)")
    chamadas = []
    original_postar = envio._postar

    def postar_falso(payload, chave):
        chamadas.append((payload, chave))
        return {"ok": True, "dados": {"id": "id-de-teste"}}

    envio._postar = postar_falso
    guardadas = {k: os.environ.pop(k, None) for k in ("RESEND_API_KEY", "EMAIL_DESTINO")}
    try:
        cfg_desligado = {"envio": "desligado", "horario_entrega": "06:30"}
        r = envio.enviar(DATA, raiz, cfg_desligado)
        conferir(r["status"] == "desligado" and "Envio desligado no config.yaml (fase de testes)" in r["mensagem"] and not chamadas,
                 "desligado: recusa e não chama a API")
        r = envio.enviar(DATA, raiz, {"envio": "ligado"})
        conferir(r["status"] == "erro" and "RESEND_API_KEY" in r["mensagem"] and "EMAIL_DESTINO" in r["mensagem"] and not chamadas,
                 "ligado sem variáveis: avisa quais faltam")
        os.environ["RESEND_API_KEY"] = "chave-de-teste"
        r = envio.enviar(DATA, raiz, {"envio": "ligado"})
        conferir(r["status"] == "erro" and "EMAIL_DESTINO" in r["mensagem"] and "RESEND_API_KEY" not in r["mensagem"] and not chamadas,
                 "falta só EMAIL_DESTINO: avisa só ele")
        # com tudo preenchido, o envio falso confere o conteúdo que iria para o Resend
        os.environ["EMAIL_DESTINO"] = "leitor@exemplo.test"
        r = envio.enviar(DATA, raiz, cfg_desligado, forcar=True, agora=True)
        conferir(r["status"] == "enviado" and len(chamadas) == 1, "--forcar envia mesmo desligado (com API falsa)")
        payload = chamadas[0][0]
        conferir(payload["to"] == ["leitor@exemplo.test"] and payload["from"].startswith("Inteligência Pragmática <"), "remetente e destino")
        conferir("~~" not in payload["subject"] and "̶" in payload["subject"], "assunto com tachado combinante")
        conferir("scheduled_at" not in payload, "--agora não agenda")
        conferir(payload["html"].startswith("<!DOCTYPE html>") and payload["text"].rstrip().endswith("Versão completa no HTML."),
                 "html é o email.html e text é curta.txt + aviso")
        env = json.loads((raiz / "edicoes" / DATA / "envio.json").read_text(encoding="utf-8"))
        conferir(env["id"] == "id-de-teste" and "leitor@exemplo.test" not in json.dumps(env), "envio.json guarda o id e NÃO guarda o e-mail")
        # agendamento: data futura entra com offset -03:00; passada não
        futura = envio._horario_agendado(util.hoje_brasilia().replace(year=util.hoje_brasilia().year + 1), "06:30")
        conferir(futura is not None and futura.endswith("T06:30:00-03:00"), "horário futuro agenda com -03:00 (%s)" % futura)
        conferir(envio._horario_agendado(util.hoje_brasilia().replace(year=2020), "06:30") is None, "horário passado não agenda")
        (raiz / "edicoes" / DATA / "envio.json").unlink()
    finally:
        envio._postar = original_postar
        for k, v in guardadas.items():
            os.environ.pop(k, None)
            if v is not None:
                os.environ[k] = v


def testar_cli(tmp):
    secao("main.py (linha de comando, numa cópia temporária)")
    raiz = preparar_raiz(tmp / "cli", copiar_codigo=True)
    env = {k: v for k, v in os.environ.items() if k not in ("RESEND_API_KEY", "EMAIL_DESTINO")}
    env["BROWSER"] = "true"  # se alguma coisa tentar abrir o navegador, não abre nada

    def rodar(*args):
        p = subprocess.run([sys.executable, str(raiz / "main.py")] + list(args), cwd=str(raiz), env=env,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, timeout=300)
        return p.returncode, p.stdout

    codigo, saida = rodar("--help")
    conferir(codigo == 0 and "montar" in saida and "--dry-run" in saida, "--help lista os comandos")
    codigo, saida = rodar("montar", DATA)
    conferir(codigo == 0 and (raiz / "edicoes" / DATA / "email.html").exists(), "montar DATA gera o email.html")
    codigo, saida = rodar("montar")
    conferir(codigo == 0 and DATA in saida, "montar sem data usa a edição mais recente")
    codigo, saida = rodar("registrar", DATA)
    conferir(codigo == 0 and "registrada" in saida, "registrar grava no histórico")
    codigo, saida = rodar("historico", "--dias", "36500")
    conferir(codigo == 0 and "exemplo-agente-de-contratos" in saida, "historico imprime o resumo")
    codigo, saida = rodar("enviar", DATA)
    conferir(codigo == 0 and "Envio desligado no config.yaml (fase de testes)" in saida, "enviar com envio desligado recusa (saída 0)")
    codigo, saida = rodar("enviar", DATA, "--forcar")
    conferir(codigo == 1 and "RESEND_API_KEY" in saida and "EMAIL_DESTINO" in saida, "enviar --forcar sem variáveis dá erro (saída 1)")
    codigo, saida = rodar("montar", "2030-01-01")
    conferir(codigo == 1 and "Não achei" in saida, "data sem edição dá erro claro (saída 1)")
    codigo, saida = rodar("montar", "ontem")
    conferir(codigo == 1 and "Use AAAA-MM-DD" in saida, "data inválida explica o formato")
    codigo, saida = rodar("coletar")
    conferir(codigo == 1 and "coleta" in saida.lower(), "coletar sem o módulo avisa em vez de quebrar")
    codigo, saida = rodar("--dry-run", DATA)
    conferir(codigo == 0 and "nenhum e-mail foi enviado" in saida, "--dry-run monta e não envia")
    conferir(not (raiz / "edicoes" / DATA / "envio.json").exists(), "--dry-run não criou envio.json")
    # links: uma edição só com link quebrado deve sair com 1
    pasta = raiz / "edicoes" / "2026-01-17"
    pasta.mkdir()
    (pasta / "edicao.md").write_text("---\ndata: 2026-01-17\n---\n[x](https://dominio-que-nao-existe.invalid/)\n", encoding="utf-8")
    codigo, saida = rodar("links", "2026-01-17")
    if "sem internet" in saida:
        print("  (sem internet: pulei o teste de saída do comando links)")
    else:
        conferir(codigo == 1 and "quebrado" in saida, "links com link quebrado sai com 1")


def testar_conversao():
    secao("conversão Markdown → HTML em casos chatos (sem linhas em branco)")
    md = (
        "**Nesta edição:**\n- um\n- dois\ntexto colado\n"
        "#### ROTULO\n## Título com ~~óbvio~~ real\n> **TL;DR:** colado no título.\n"
        "Texto depois da citação com [link](https://a.com/x_(y)).\n"
        "→ **A**: um\n→ **B**: dois\n🔗 [Fonte](https://x.com)\n🔗 [Fonte2](https://y.com)\n"
        "Parágrafo\n---\n### Subtítulo\n**Opinião:** eu acho.\n"
    )
    h = montagem._semantico(montagem._renderizar(md))
    conferir("<ul>" in h and "<p>texto colado</p>" in h, "lista sem linha em branco antes funciona e termina")
    conferir('<h4 class="rotulo">ROTULO</h4>' in h and "<h2>Título com <del>óbvio</del> real</h2>" in h, "título e tachado")
    conferir('<blockquote class="tldr">' in h and "<p>Texto depois da citação" in h, "TL;DR colado ao título e texto colado à citação")
    conferir(h.count('<p class="seta">') == 2 and h.count('<div class="setas">') == 1, "duas linhas → coladas viram um bloco com 2 itens")
    conferir(h.count('<p class="fonte">') == 2, "duas linhas 🔗 coladas viram 2 linhas de fonte")
    conferir("<hr>" in h and "<h2>Parágrafo" not in h, "--- depois de texto colado vira linha, não título")
    conferir('<p class="opiniao"><span class="selo">Opinião</span> eu acho.' in h, "**Opinião:** vira selo")
    conferir('a.com/x_(y)"' in h, "link com parêntese no endereço")
    tit = montagem.assunto_tachado("o ~~óbvio~~ real")
    conferir(tit == "o ó\u0336b\u0336v\u0336i\u0336o\u0336 real" and montagem.assunto_sem_marcas("o ~~óbvio~~ real") == "o óbvio real",
             "assunto: tachado combinante e sem marcas")


PAINEL_FALSO = {
    "gerado_em": "2026-01-15T06:50:00-03:00",
    "falhas": {"CNN": "respondeu 503"},
    "itens": {
        "ibov": {"nome": "Ibovespa", "valor": 206495.23, "var": -0.86, "unidade": "pts", "data": "", "fonte": "B3"},
        "sp500": {"nome": "S&P 500", "valor": 7757.17, "var": 0.58, "unidade": "pts", "data": "2026-01-14", "fonte": "CNBC"},
        "juros10": {"nome": "Juros de 10 anos dos EUA", "valor": 5.046, "var": -1.94, "var_pp": -0.10,
                    "unidade": "%", "data": "2026-01-15", "fonte": "CNBC"},
        "dolar": {"nome": "Dólar", "valor": 5.047, "var": 0.0, "unidade": "R$", "data": "2026-01-15", "fonte": "AwesomeAPI"},
        "btc_usd": {"nome": "Bitcoin", "valor": 81689.65, "var": -11.2, "unidade": "US$", "data": "2026-01-15", "fonte": "CNBC"},
        "medo_cripto": {"nome": "Cripto (alternative.me)", "valor": 68, "rotulo": "ganância", "ontem": 63, "fonte": "alternative.me"},
    },
}

EDICAO_MERCADO = """---
data: 2026-01-15
tipo: dia_util
numero: 1
assunto: "o touro tropeçou"
previa: "+ o dólar parado"
tempo_leitura_min: 3
dia: morno
breakthrough: false
historias:
  - id: teste-mercado
    titulo: "Teste do caderno"
    tema: bolsa_br
    urls: ["https://www.python.org"]
    em_andamento: false
formatos: [painel, radar]
---
bom dia. Dia de teste.

<!-- painel -->

#### RADAR
→ **Teste**: uma linha com fonte ([Python](https://www.python.org)).

Não é recomendação de investimento.
"""


def testar_cadernos(tmp: Path):
    secao("cadernos e caderno Mercado")
    from ferramentas import cadernos, mercado
    raiz = preparar_raiz(tmp / "cadernos")
    (raiz / "cadernos.yaml").write_text(
        'mercado:\n  nome: "Inteligência Pragmática · Mercado"\n  remetente: "IP · Mercado"\n'
        '  envio: desligado\n  fontes: fontes_mercado.yaml\n', encoding="utf-8")
    conferir(cadernos.nomes(raiz) == ["mercado"], "cadernos.yaml lista o mercado")
    conferir(cadernos.pasta_edicoes(raiz, "mercado") == raiz / "edicoes" / "mercado", "pasta das edições do caderno")
    conferir(cadernos.config(raiz, "mercado")["envio"] == "desligado", "config do caderno vem do cadernos.yaml")

    # painel: formato brasileiro, setas, falhas e escala
    texto = mercado.painel_md(PAINEL_FALSO)
    conferir("206.495 pts ▼ 0,86%" in texto, "Ibovespa com milhar e seta de queda")
    conferir("último fechamento" in texto, "sem data da B3, diz 'último fechamento'")
    conferir("fechamento de 14/01" in texto, "fechamento dos EUA com a data")
    conferir("5,05% ▼ 0,10 p.p." in texto, "juros com variação em pontos percentuais")
    conferir("R$ 5,05 · estável" in texto, "variação zero vira 'estável'")
    conferir("Fora do ar hoje: CNN" in texto, "fonte que falhou aparece no rodapé")
    conferir("68, ganância (ontem 63)" in texto, "Medo & Ganância com o dia anterior")
    # alarme: só conta número de hoje
    motivos = mercado.alarme(PAINEL_FALSO, hoje=date(2026, 1, 15))
    conferir(len(motivos) == 1 and "Bitcoin" in motivos[0], "alarme dispara com bitcoin -11,2%% hoje (%s)" % motivos)
    conferir(mercado.alarme(PAINEL_FALSO, hoje=date(2026, 1, 16)) == [], "variação de outro dia não dispara alarme")

    # reservas: se a principal falha, a reserva cobre só as chaves que faltaram
    fontes_orig, reservas_orig = mercado.FONTES, mercado.RESERVAS
    try:
        def cai():
            raise RuntimeError("respondeu 403")
        mercado.FONTES = [("B3", lambda: {"ibov": PAINEL_FALSO["itens"]["ibov"]}), ("CNBC", cai)]
        mercado.RESERVAS = [("FRED", lambda: {"sp500": dict(PAINEL_FALSO["itens"]["sp500"], fonte="FRED")},
                             ["sp500"], "CNBC")]
        p = mercado.coletar_painel()
        conferir("sp500" in p["itens"] and p["itens"]["sp500"]["fonte"] == "FRED" and p["reservas_usadas"] == ["FRED"],
                 "a reserva entra quando a principal falha")
        conferir("FRED" in mercado.painel_md(p) and "Fora do ar hoje: CNBC" in mercado.painel_md(p),
                 "o rodapé cita a reserva e a principal fora do ar")
    finally:
        mercado.FONTES, mercado.RESERVAS = fontes_orig, reservas_orig

    # montagem do caderno: painel no lugar do marcador, setas coloridas, páginas próprias e navegação
    pasta = raiz / "edicoes" / "mercado" / "2026-01-15"
    pasta.mkdir(parents=True)
    (pasta / "edicao.md").write_text(EDICAO_MERCADO, encoding="utf-8")
    (pasta / "painel.md").write_text(texto, encoding="utf-8")
    cfg = cadernos.config(raiz, "mercado")
    cfg["site_url"] = "https://exemplo.github.io/ip"
    res = montagem.montar("2026-01-15", raiz, cfg, "mercado")
    email = (pasta / "email.html").read_text(encoding="utf-8")
    conferir("<!-- painel -->" not in email and "206.495 pts" in email, "o painel entrou no lugar do marcador")
    conferir('class="desce"' in email and "color:#D93025" in email, "seta de queda vermelha no e-mail")
    docs = raiz / "docs"
    conferir((docs / "mercado-2026-01-15.html").exists() and (docs / "mercado.html").exists(),
             "página e arquivo do caderno em docs/")
    conferir('href="mercado.html"' in (docs / "index.html").read_text(encoding="utf-8"),
             "o arquivo da geral tem link para o caderno")
    conferir("Mercado" not in json.loads((docs / "manifest.webmanifest").read_text(encoding="utf-8"))["name"],
             "o nome do app instalado continua o da geral depois de montar um caderno")
    pagina = (docs / "mercado-2026-01-15.html").read_text(encoding="utf-8")
    conferir('href="mercado.html"' in pagina, "a página volta para o arquivo do caderno")
    conferir("ip/mercado-2026-01-15.html" in (pasta / "curta.txt").read_text(encoding="utf-8"),
             "a versão curta aponta para a página do caderno")
    conferir(res["pagina"] == "docs/mercado-2026-01-15.html", "montar devolve a página do caderno")
    # edição extra no mesmo dia
    extra = raiz / "edicoes" / "mercado" / "2026-01-15-extra"
    extra.mkdir()
    (extra / "edicao.md").write_text(EDICAO_MERCADO.replace("numero: 1", "numero: 2"), encoding="utf-8")
    (extra / "painel.md").write_text(texto, encoding="utf-8")
    montagem.montar("2026-01-15-extra", raiz, cfg, "mercado")
    conferir("edição extra" in (docs / "mercado.html").read_text(encoding="utf-8"), "a extra aparece marcada no arquivo")
    conferir(util.edicao_mais_recente(raiz, "mercado") == "2026-01-15-extra", "a mais recente do caderno é a extra")

    # histórico: numeração separada, o mesmo arquivo
    historico.registrar(DATA, raiz)
    historico.registrar("2026-01-15", raiz, "mercado")
    historico.registrar("2026-01-15-extra", raiz, "mercado")
    historico.registrar("2026-01-15", raiz, "mercado")  # regravar não duplica
    todas = historico.carregar(raiz)
    conferir(len(todas) == 3, "geral + 2 do mercado no mesmo histórico (%d)" % len(todas))
    conferir(historico.proximo_numero(raiz, "mercado") == 3 and historico.proximo_numero(raiz) == 2,
             "cada caderno tem a própria numeração")
    conferir(all(e.get("caderno") == "mercado" for e in historico.carregar(raiz, "mercado")), "entradas marcadas com o caderno")


FEED_FALSO = """<?xml version="1.0"?><rss version="2.0"><channel><title>Jornal</title>%s</channel></rss>"""
ITEM_FALSO = "<item><title>%s</title><link>https://jornal.exemplo/%s</link><pubDate>%s</pubDate><description>%s</description></item>"


def testar_coleta_filtros():
    secao("coleta: filtro por cidade e páginas extras do feed (caderno Niterói)")
    from datetime import datetime, timedelta, timezone
    from email.utils import format_datetime
    from ferramentas import coleta
    conferir(coleta._passa_filtro(["Niterói"], "Obra em NITEROI começa hoje"), "filtro ignora acento e maiúscula")
    conferir(coleta._passa_filtro("Búzios", "https://site/policia-prende-em-buzios-x"), "filtro olha o endereço também")
    conferir(not coleta._passa_filtro(["Niterói"], "Tiroteio em Queimados"), "filtro barra outra cidade")
    conferir(coleta._passa_filtro(None, "qualquer coisa"), "sem filtro, tudo passa")
    conferir(coleta._pagina_feed("https://s/feed/", 2) == "https://s/feed/?paged=2"
             and coleta._pagina_feed("https://s/?s=X&feed=rss2", 3) == "https://s/?s=X&feed=rss2&paged=3",
             "endereço da página N do feed")

    agora = datetime.now(timezone.utc)

    def item(n, horas, titulo, resumo=""):
        return ITEM_FALSO % (titulo, "n%d" % n, format_datetime(agora - timedelta(hours=horas)), resumo)
    # página 1: itens de 1 a 10 h atrás; página 2: de 20 a 30 h; página 3: de 100 h (fora da janela de 48 h)
    paginas = {
        1: [item(i, i, "Niterói abre vagas %d" % i) for i in range(1, 11)],
        2: [item(10 + i, 20 + i, "Notícia de Niterói %d" % i) for i in range(1, 11)],
        3: [item(30, 100, "Niterói antiga")],
    }
    pedidos = []
    original = coleta._baixar
    try:
        def baixar_falso(url, *a, **k):
            pedidos.append(url)
            n = int(url.rsplit("paged=", 1)[1]) if "paged=" in url else 1
            return 200, (FEED_FALSO % "".join(paginas.get(n, []))).encode(), url
        coleta._baixar = baixar_falso
        fim = agora + timedelta(minutes=1)
        itens, stat = coleta._ler_feed("Jornal", "https://jornal.exemplo/feed/", "niteroi", "imprensa",
                                       fim - timedelta(hours=48), fim, 50, paginas=5)
        conferir(len(itens) == 20, "lê as páginas 1 e 2, que estão na janela (%d itens)" % len(itens))
        conferir(len(pedidos) == 3, "para na página 3, que já sai da janela (%d pedidos)" % len(pedidos))
        pedidos.clear()
        itens, _ = coleta._ler_feed("Jornal", "https://jornal.exemplo/feed/", "niteroi", "imprensa",
                                    fim - timedelta(hours=48), fim, 50)
        conferir(len(itens) == 10 and len(pedidos) == 1, "sem 'paginas', lê só a primeira")
        paginas[1] = [item(1, 1, "Tiroteio em Queimados", "Texto longo " * 60 + "e também em Niterói"),
                      item(2, 2, "Obras na orla", "A prefeitura de Niterói começou as obras")]
        itens, _ = coleta._ler_feed("Jornal", "https://jornal.exemplo/feed/", "niteroi", "imprensa",
                                    fim - timedelta(hours=48), fim, 50, filtro=["Niterói"])
        conferir([c["titulo"] for c in itens] == ["Obras na orla"],
                 "filtro usa o título e o começo do resumo; cidade citada de passagem no fim não conta")
    finally:
        coleta._baixar = original
    md = coleta._montar_md(date(2026, 10, 22), agora, agora, 48,
                           [coleta._candidato("A", "https://a/1", "F", "buzios", "imprensa", None),
                            coleta._candidato("B", "https://a/2", "F", "niteroi", "imprensa", None)],
                           {}, [], {"niteroi": "Niterói", "buzios": "Búzios"})
    conferir(md.index("## Niterói (1)") < md.index("## Búzios (1)"), "seções com o nome e a ordem do arquivo de fontes")
    janela = {"padrao": 48, "segunda": 72, "terca": 30}
    conferir([coleta._horas_janela(janela, date(2026, 10, d)) for d in (26, 27, 28, 29, 30, 31)] == [72, 30, 48, 48, 48, 48],
             "janela_horas aceita o nome de qualquer dia da semana, e os outros caem no padrao")
    conferir(coleta._horas_janela(168, date(2026, 10, 26)) == 168 and coleta._horas_janela({}, date(2026, 10, 26)) == 30,
             "janela_horas da fonte pode ser um número; sem nada, 30 horas")
    setas = montagem._setas("→ **Água:** falta na terça ([Cedae](https://c))\n→ **Trânsito**: rua fechada")
    conferir(setas == [("Água", "falta na terça"), ("Trânsito", "rua fechada")],
             "linha → com os dois-pontos dentro ou fora do negrito (%s)" % setas)


TENDENCIAS_FALSAS = """<html><body>
<article class="Box-row"><h2 class="h3 lh-condensed"><a href="/dono/agente"><span>dono /</span> agente</a></h2>
<p class="col-9 color-fg-muted my-1">Um agente que faz tudo.</p>
<span itemprop="programmingLanguage">Python</span>
<a href="/dono/agente/stargazers" class="Link"><svg><path d="M8 .25a.75"></path></svg>
  12,345</a>
<span class="d-inline-block float-sm-right"><svg><path d="M1 2"></path></svg> 6,789 stars this week</span></article>
<article class="Box-row"><h2 class="h3"><a href="/outro/sem-descricao">outro / sem-descricao</a></h2></article>
</body></html>"""


def testar_coleta_ia():
    secao("coleta: filtro com palavra curta e GitHub em alta pela página de tendências (caderno IA)")
    from ferramentas import cadernos, coleta
    conferir(coleta._passa_filtro(["IA"], "A IA do Google chegou"), "filtro 'IA' casa a palavra inteira")
    conferir(coleta._passa_filtro(["IA"], "https://tecnoblog.net/noticias/ia-do-google/"), "filtro 'IA' olha o endereço")
    conferir(not coleta._passa_filtro(["IA"], "Bom dia: a mídia e a polícia"), "filtro 'IA' não casa com 'dia' nem 'mídia'")
    conferir(coleta._passa_filtro(["inteligência artificial"], "Inteligencia Artificial no STF"),
             "palavra longa continua casando dentro do texto")

    original = coleta._baixar
    try:
        def baixar_falso(url, *a, **k):
            if "api.github.com" in url:
                return 403, b'{"message": "API rate limit exceeded"}', url
            return 200, TENDENCIAS_FALSAS.encode(), url
        coleta._baixar = baixar_falso
        itens, stat = coleta._github_em_alta({"limite": 15}, date(2026, 10, 22))
        coleta._baixar = lambda url, *a, **k: (200, (b'{"items": []}' if "api.github.com" in url
                                                     else TENDENCIAS_FALSAS.encode()), url)
        vazia, _ = coleta._github_em_alta({"limite": 15}, date(2026, 10, 22))
        conferir(len(vazia) == 2, "busca da API vazia também cai na página de tendências")
        coleta._baixar = lambda url, *a, **k: (403 if "api.github.com" in url else 429, b"", url)
        _, stat_falha = coleta._github_em_alta({"limite": 15}, date(2026, 10, 22))
        conferir(not stat_falha["ok"] and "HTTP 429" in stat_falha["erro"],
                 "quando as duas falham, o log diz o motivo da página também (%s)" % stat_falha["erro"])
        proxy = b'{"message": "GitHub access to x/y is not enabled for this session"}'
        coleta._baixar = lambda url, *a, **k: (403, proxy if "api.github.com" in url else b"<html>", url)
        _, stat_proxy = coleta._github_em_alta({"limite": 15}, date(2026, 10, 22))
        conferir("HTTP 403 (GitHub access to x/y is not enabled" in stat_proxy["erro"]
                 and "tendências: HTTP 403" in stat_proxy["erro"],
                 "o log traz a mensagem do 403 da API, que diz quem barrou (%s)" % stat_proxy["erro"])
    finally:
        coleta._baixar = original
    from ferramentas import github
    guardado = {v: os.environ.pop(v, None) for v in ("GITHUB_TOKEN_LEITURA", "GITHUB_TOKEN")}
    try:
        os.environ["GITHUB_TOKEN"] = "proxy-injected"
        conferir("Authorization" not in github.cabecalhos_api(), "o marcador 'proxy-injected' da nuvem não vira chave")
        os.environ["GITHUB_TOKEN_LEITURA"] = "github_pat_teste"
        conferir(github.cabecalhos_api().get("Authorization") == "Bearer github_pat_teste",
                 "a chave de leitura (GITHUB_TOKEN_LEITURA) vai no Authorization")
    finally:
        for v, valor in guardado.items():
            os.environ.pop(v, None)
            if valor is not None:
                os.environ[v] = valor
    conferir(stat["ok"] and "tendências" in (stat["erro"] or ""), "API com 403 cai na página de tendências (%s)" % stat)
    conferir([c["titulo"] for c in itens] == ["dono/agente", "outro/sem-descricao"], "lê os repositórios da página")
    primeiro = itens[0] if itens else {"extra": {}, "resumo": ""}
    conferir(primeiro["extra"] == {"estrelas": 12345, "linguagem": "Python", "estrelas_semana": 6789}
             and primeiro["resumo"] == "Um agente que faz tudo.", "estrelas, estrelas da semana, linguagem e descrição")
    conferir("+6789 ★ na semana" in coleta._linha_md(primeiro), "as estrelas da semana aparecem nos candidatos")

    # o caderno IA do projeto: fontes com os campos certos e temas que existem
    if "ia" in cadernos.nomes(RAIZ_PROJETO):
        cfg = util.ler_yaml(cadernos.arquivo_fontes(RAIZ_PROJETO, "ia"))
        temas = set(cfg.get("temas") or {})
        ruins = [f.get("nome") for f in cfg.get("fontes") or []
                 if not f.get("nome") or f.get("tema") not in temas or not (f.get("rss") or f.get("pagina"))]
        conferir(not ruins, "fontes_ia.yaml: toda fonte tem nome, tema da lista e rss ou página (%s)" % ruins)
        conferir([r["nome"] for r in cfg.get("radar") or []] and all(r.get("sitemap") or r.get("rss")
                 for r in cfg["radar"]), "fontes_ia.yaml: o radar tem endereço")
        for chave in ("manual", "roteiro"):
            conferir((RAIZ_PROJETO / cadernos.config(RAIZ_PROJETO, "ia")[chave]).exists(), "caderno IA: %s existe" % chave)


PAINEL_ECONOMIA_FALSO = {
    "gerado_em": "2026-10-22T05:16:00-03:00",
    "itens": {
        "selic": {"valor": 13.75, "desde": "2026-09-17", "antes": 14.0, "proximo_copom": "2026-11-04",
                  "ref": "2026-09-17", "fonte": "SGS"},
        "ipca": {"mes": 0.82, "doze": 4.58, "doze_antes": 4.22, "ref": "2026-09", "fonte": "SGS"},
        "pib": {"tri": 0.5, "ano": 2.0, "ref": "202602", "fonte": "SIDRA"},
        "desemprego": {"valor": 5.3, "antes": 5.3, "ano_antes": 5.6, "menor_da_serie": True, "ref": "2026-08",
                       "fonte": "SGS"},
        "divida": {"valor": 82.87, "antes": 82.55, "ref": "2026-08", "fonte": "SGS"},
        "primario": {"valor": 0.62, "antes": -0.1, "ref": "2026-08", "fonte": "SGS"},
        "dolar": {"valor": 5.0383, "data": "2026-10-22", "var_ano": -8.42, "ref": "2026-10-22", "fonte": "PTAX"},
        "focus": {"data": "2026-10-16", "antes_data": "2026-09-18", "anos": ["2026", "2027"], "ref": "2026-10-16",
                  "fonte": "Focus", "valores": {"IPCA": {"2026": {"agora": 5.219, "antes": 4.92},
                                                         "2027": {"agora": 4.3206}},
                                                "Câmbio": {"2026": {"agora": 5.13, "antes": 5.2}}}},
    },
    "falhas": {"IBC-Br (BC)": "respondeu 0"}, "fora_do_ar": ["IBC-Br (BC)"], "novos": [], "anterior": None,
}


def testar_caderno_economia(tmp: Path):
    secao("caderno Economia: painel oficial, dias fixos, curadoria e histórico")
    import copy
    from datetime import timedelta
    from ferramentas import cadernos, economia
    texto = economia.painel_md(PAINEL_ECONOMIA_FALSO)
    conferir("13,75% ao ano · desde 17/09, quando caiu de 14,00% · próxima decisão do Copom: 04/11" in texto,
             "Selic com a data da mudança, a taxa anterior e a próxima decisão")
    conferir("0,82% em setembro · 4,58% em 12 meses (até agosto: 4,22%) · a meta é 3%, com teto de 4,5%" in texto,
             "IPCA do mês, de 12 meses e a meta")
    conferir("▲ 0,5% no 2º tri de 2026 sobre o trimestre anterior" in texto, "PIB com o trimestre por extenso")
    conferir("o menor da série, que começa em 2012" in texto, "desemprego diz quando é o menor da série")
    conferir("82,9% do PIB em agosto (julho: 82,6%)" in texto, "arredonda como as notas oficiais (82,55 → 82,6)")
    conferir("déficit de 0,62% do PIB até agosto (até julho: superávit de 0,10%)" in texto,
             "primário: positivo é déficit, negativo é superávit")
    conferir("R$ 5,0383 em 22/10 · ▼ 8,4% no ano" in texto, "dólar PTAX com a variação no ano")
    conferir("→ **IPCA**: 5,22% em 2026 (4,92%) · 4,32% em 2027" in texto and "R$ 5,13 em 2026 (R$ 5,20)" in texto,
             "Focus com a mediana de 4 semanas antes entre parênteses")
    conferir("Fora do ar hoje: IBC-Br (BC)" in texto and "IBC-Br (a prévia" not in texto,
             "fonte que falhou some do painel e aparece no rodapé")
    conferir("🆕" not in texto, "sem painel anterior, nada é marcado como novo")

    # 🆕: o período de referência mudou desde o painel da última edição
    novo = copy.deepcopy(PAINEL_ECONOMIA_FALSO)
    antigo = copy.deepcopy(PAINEL_ECONOMIA_FALSO)
    antigo["itens"]["ipca"]["ref"] = "2026-08"
    antigo["itens"]["dolar"]["ref"] = "2026-10-20"
    conferir(economia._novos(novo, antigo) == ["ipca"], "só o IPCA é novo (o dólar muda todo dia e não conta)")
    novo["novos"], novo["anterior"] = ["ipca"], "2026-10-20"
    t = economia.painel_md(novo)
    conferir("teto de 4,5% · 🆕" in t and "saiu desde a última edição (20/10)" in t, "o dado novo ganha 🆕 e o rodapé explica")

    # Selic: acha a última mudança e a próxima decisão (os dias até ela já vêm na série)
    original = economia._sgs
    try:
        dias = [date(2026, 9, 1) + timedelta(days=i) for i in range(70)]
        economia._sgs = lambda *a: [(d, 14.0 if d < date(2026, 9, 17) else 13.75) for d in dias]
        s = economia._selic(date(2026, 10, 22))
        conferir(s["desde"] == "2026-09-17" and s["antes"] == 14.0 and s["proximo_copom"] == "2026-11-09",
                 "Selic: desde, antes e próxima decisão (%s)" % s)
    finally:
        economia._sgs = original
    # segunda tentativa: a fonte que falhou na rajada tenta de novo, sozinha, antes das reservas
    fontes_orig, reservas_orig = economia._fontes, economia._reservas
    tentativas = []
    try:
        def ibcbr_instavel():
            tentativas.append(1)
            if len(tentativas) == 1:
                raise RuntimeError("respondeu 0")
            return {"ibcbr": {"var": 0.34, "ref": "2026-08", "fonte": "SGS"}}
        economia._fontes = lambda h: [("IBC-Br (BC)", ibcbr_instavel, ["ibcbr"])]
        economia._reservas = lambda h: []
        p = economia.coletar_painel(date(2026, 10, 22))
        conferir("ibcbr" in p["itens"] and not p["falhas"] and not p["fora_do_ar"] and len(tentativas) == 2,
                 "a fonte que não respondeu na rajada entra na segunda tentativa")
    finally:
        economia._fontes, economia._reservas = fontes_orig, reservas_orig
    # resposta em gzip sem pedir (o IBGE fez isso em 22/10)
    import gzip as _gzip
    http_orig = economia.http_get
    try:
        economia.http_get = lambda *a, **k: (200, _gzip.compress(b'{"items": [1, 2]}'), "")
        conferir(economia._json("https://servicodados.ibge.gov.br/x") == {"items": [1, 2]}, "lê JSON que vem em gzip")
    finally:
        economia.http_get = http_orig
    serie = [("2012-%02d" % m, 7.0) for m in range(3, 13)] + [("2026-%02d" % m, 5.4 - m / 100) for m in range(1, 9)]
    conferir(economia._desemprego_de(serie, "SGS")["menor_da_serie"], "desemprego: menor da série")
    conferir(not economia._desemprego_de(serie + [("2026-09", 6.0)], "SGS")["menor_da_serie"], "subiu: não é o menor")

    # histórico: última edição do caderno e quantos dias olhar nos outros cadernos
    raiz = preparar_raiz(tmp / "economia")
    hoje = util.hoje_brasilia()
    (raiz / "cadernos.yaml").write_text('economia:\n  nome: "IP · Economia"\n  envio: desligado\n'
                                        '  dias_envio: [segunda, Quarta, sexta-feira]\n'
                                        'mercado:\n  nome: "IP · Mercado"\n', encoding="utf-8")
    conferir(cadernos.dias_envio(raiz, "economia") == ["segunda", "quarta", "sexta"], "dias fixos aceitam acento e '-feira'")
    conferir(cadernos.dia_de_envio(raiz, "economia", date(2026, 10, 23))
             and not cadernos.dia_de_envio(raiz, "economia", date(2026, 10, 22)), "sexta é dia fixo; quinta não")
    conferir(cadernos.dia_de_envio(raiz, "mercado", date(2026, 10, 22)) and cadernos.dias_envio(raiz, cadernos.GERAL) == [],
             "caderno sem dias fixos sai todo dia")
    sit = "\n".join(historico.situacao(raiz, "economia", date(2026, 10, 22)))
    conferir("quinta, 22/10 · não é dia fixo (os dias fixos de envio são segunda, quarta e sexta)" in sit
             and "curadoria guardada: 0 itens em dados/economia/curadoria.md" in sit, "a situação do dia sai no histórico")
    conferir("DIA FIXO DE ENVIO" in "\n".join(historico.situacao(raiz, "economia", date(2026, 10, 23))), "sexta: dia fixo")
    conferir(historico.situacao(raiz, "mercado") == [], "caderno sem dias fixos não ganha a linha")
    conferir(historico.ultima_data(raiz, "economia") is None and historico._dias_outros(raiz, "economia") == 3,
             "sem edição: nenhuma data e 3 dias nos outros cadernos")
    dia_antigo = (hoje - timedelta(days=6)).isoformat()
    for pasta in (dia_antigo, dia_antigo + "-extra"):
        (raiz / "edicoes" / "economia" / pasta).mkdir(parents=True)
        (raiz / "edicoes" / "economia" / pasta / "edicao.md").write_text(
            EDICAO_MERCADO.replace("data: 2026-01-15", "data: " + dia_antigo), encoding="utf-8")
        historico.registrar(pasta, raiz, "economia")
    conferir(historico.ultima_data(raiz, "economia") == dia_antigo, "a extra conta pelo dia")
    conferir(historico.ultima_data(raiz, "economia", antes_de=dia_antigo) is None, "antes_de olha só os dias anteriores")
    conferir(historico._dias_outros(raiz, "economia") == 7, "seis dias depois, olha 7 dias nos outros cadernos")

    # gravação: painel.md, oficiais.md e o JSON, com o 🆕 contra o painel da última edição
    (raiz / "dados" / "economia").mkdir(parents=True)
    (raiz / "dados" / "economia" / ("%s.json" % dia_antigo)).write_text(json.dumps(antigo), encoding="utf-8")
    original = economia.apoio
    try:
        economia.apoio = lambda painel, desde, h: ("# apoio desde %s\n" % desde.isoformat(), [])
        res = economia.gravar_painel(hoje.isoformat(), raiz, copy.deepcopy(PAINEL_ECONOMIA_FALSO), hoje)
    finally:
        economia.apoio = original
    pasta = raiz / "edicoes" / "economia" / hoje.isoformat()
    conferir(res["painel"]["novos"] == ["ipca"] and "🆕" in (pasta / "painel.md").read_text(encoding="utf-8"),
             "o IPCA novo desde a última edição ganha 🆕 no painel gravado")
    conferir((pasta / "oficiais.md").read_text(encoding="utf-8") == "# apoio desde %s\n" % dia_antigo,
             "o apoio da pauta começa na última edição")
    conferir((raiz / "dados" / "economia" / ("%s.json" % hoje.isoformat())).exists(), "o JSON do painel fica em dados/economia")
    curadoria = cadernos.arquivo_curadoria(raiz, "economia")
    curadoria.write_text("# Curadoria\n\n## 2026-10-22\n- [juros] Item um (https://a)\n- [mundo] Item dois (https://b)\n",
                         encoding="utf-8")
    proprios = publicar_arquivos(raiz, hoje.isoformat(), "economia")
    conferir(("dados/economia/%s.json" % hoje.isoformat()) in proprios and "dados/economia/curadoria.md" in proprios,
             "o publicar leva o JSON do painel e a curadoria junto com a edição")
    conferir(cadernos.itens_curadoria(raiz, "economia") == 2, "conta os itens da curadoria")

    # caderno que não guarda curadoria (Niterói, com o radar no lugar): a linha da situação não fala dela
    (raiz / "cadernos.yaml").write_text((raiz / "cadernos.yaml").read_text(encoding="utf-8")
                                        + 'niteroi:\n  dias_envio: [segunda, quarta, sexta]\n  curadoria: nao\n',
                                        encoding="utf-8")
    sit = "\n".join(historico.situacao(raiz, "niteroi", date(2026, 10, 26)))
    conferir("DIA FIXO DE ENVIO" in sit and "Última edição: nenhuma" in sit and "curadoria" not in sit,
             "curadoria: nao tira a curadoria da situação do dia")
    conferir(cadernos.usa_curadoria(raiz, "economia") and not cadernos.usa_curadoria(raiz, "niteroi"),
             "usa_curadoria: sim por padrão, não com `curadoria: nao`")

    # bloco ECONOMIA do Mercado: painel_economia.md sem o dólar, 🆕 contra o painel anterior, JSON que o publicar leva
    texto_mercado = economia.painel_md(PAINEL_ECONOMIA_FALSO, economia.TITULO_PAINEL_MERCADO, sem=("dolar",))
    conferir(texto_mercado.startswith("**📊 Painel oficial do Brasil") and "PTAX" not in texto_mercado
             and "5,0383" not in texto_mercado and "Câmbio**" not in texto_mercado.replace("**Dólar no fim do ano**", ""),
             "no Mercado, o painel oficial tem outro título e deixa o dólar para o painel de cotações")
    conferir("13,75% ao ano" in texto_mercado and "Dólar no fim do ano" in texto_mercado,
             "o resto do painel (Selic, Focus...) continua")
    p1, p2 = (hoje + timedelta(days=1)).isoformat(), (hoje + timedelta(days=3)).isoformat()
    novo_bloco = copy.deepcopy(PAINEL_ECONOMIA_FALSO)
    novo_bloco["itens"]["selic"]["ref"] = "2026-10-28"
    original = economia.apoio
    try:
        economia.apoio = lambda painel, desde, h: ("# apoio desde %s\n" % desde.isoformat(), [])
        res1 = economia.gravar_painel(p1, raiz, copy.deepcopy(novo_bloco), hoje, caderno="mercado")
        res2 = economia.gravar_painel(p2, raiz, copy.deepcopy(novo_bloco), hoje, caderno="mercado")
    finally:
        economia.apoio = original
    pasta1 = raiz / "edicoes" / "mercado" / p1
    conferir(res1["painel"]["anterior"] == hoje.isoformat() and res1["painel"]["novos"] == ["selic"]
             and "🆕" in (pasta1 / "painel_economia.md").read_text(encoding="utf-8"),
             "1º bloco no Mercado: compara com o painel do caderno Economia e marca o que saiu")
    conferir(res2["painel"]["anterior"] == p1 and res2["painel"]["novos"] == [],
             "2º bloco: compara com o bloco anterior do Mercado (dados/mercado/DATA-economia.json)")
    conferir((pasta1 / "oficiais.md").exists() and not (pasta1 / "painel.md").exists()
             and res1["arquivo"] == "edicoes/mercado/%s/painel_economia.md" % p1,
             "grava painel_economia.md e oficiais.md, sem tocar no painel.md de cotações do Mercado")
    conferir(("dados/mercado/%s-economia.json" % p1) in publicar_arquivos(raiz, p1, "mercado"),
             "o publicar leva o JSON do bloco ECONOMIA junto com a edição do Mercado")
    conferir(not (raiz / "dados" / "economia" / ("%s.json" % p1)).exists(), "o bloco do Mercado não grava no caderno Economia")

    # a montagem troca os dois marcadores, cada um pelo seu arquivo, e avisa quando falta um
    bloco = EDICAO_MERCADO.replace("<!-- painel -->", "<!-- painel -->\n\n#### ECONOMIA\n\n<!-- painel-economia -->")
    (pasta1 / "edicao.md").write_text(bloco.replace("data: 2026-01-15", "data: " + p1), encoding="utf-8")
    (pasta1 / "painel.md").write_text("**PAINEL DE COTACOES**", encoding="utf-8")
    cfg = cadernos.config(raiz, "mercado")
    res = montagem.montar(p1, raiz, cfg, "mercado")
    email = (pasta1 / "email.html").read_text(encoding="utf-8")
    conferir("PAINEL DE COTACOES" in email and "Painel oficial do Brasil" in email and "<!-- painel" not in email
             and not [a for a in res["avisos"] if "painel" in a], "os dois painéis entram no lugar dos marcadores")
    (pasta1 / "painel_economia.md").unlink()
    res = montagem.montar(p1, raiz, cfg, "mercado")
    conferir(any("painel_economia.md" in a for a in res["avisos"]), "sem o painel_economia.md, a montagem avisa")


def publicar_arquivos(raiz, data, caderno):
    from ferramentas import publicar
    return publicar.arquivos_proprios(raiz, data, caderno)


def testar_horario_de_entrega(raiz):
    secao("envio junto no horário de entrega")
    from datetime import datetime as _dt
    original, postar = envio.agora_brasilia, envio._postar
    envio._postar = lambda payload, chave: {"ok": False, "erro": "teste: nada sai daqui"}  # nunca envia de verdade
    try:
        envio.agora_brasilia = lambda: _dt(2026, 1, 15, 5, 10, tzinfo=util.FUSO)
        cfg = {"envio": "ligado", "horario_entrega": "06:00"}
        r = envio.enviar(DATA, raiz, cfg)
        conferir(r["status"] == "aguardando" and "06:00" in r["mensagem"], "antes das 06:00, a edição de hoje espera")
        r = envio.enviar(DATA, raiz, cfg, agora=True)
        conferir(r["status"] != "aguardando", "--agora (rotina de envio) não espera")
        r = envio.enviar("2026-01-14", raiz, cfg)
        conferir(r["status"] != "aguardando", "edição de outro dia não espera")
        envio.agora_brasilia = lambda: _dt(2026, 1, 15, 6, 20, tzinfo=util.FUSO)
        r = envio.enviar(DATA, raiz, cfg)
        conferir(r["status"] != "aguardando", "depois das 06:00 (rotina atrasada), envia na hora")
        r = envio.enviar(DATA + "-extra", raiz, cfg)
        conferir(r["status"] != "aguardando", "edição extra da tarde não espera")
        envio.agora_brasilia = lambda: _dt(2026, 1, 15, 5, 56, tzinfo=util.FUSO)
        r = envio.enviar(DATA, raiz, cfg)
        conferir(r["status"] != "aguardando", "de 05:55 em diante não espera (a rotina de envio pode já ter lido a main)")
    finally:
        envio.agora_brasilia, envio._postar = original, postar


def testar_publicar_em_paralelo(tmp: Path):
    secao("publicar: três rotinas publicando ao mesmo tempo")
    from concurrent.futures import ThreadPoolExecutor
    from ferramentas import publicar

    def git(cwd, *args):
        return subprocess.run(["git", "-c", "init.defaultBranch=main"] + list(args), cwd=str(cwd),
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    origem, base = tmp / "pub" / "origem.git", tmp / "pub" / "base"
    origem.mkdir(parents=True)
    git(origem, "init", "-q", "--bare")
    base.mkdir()
    git(base, "init", "-q")
    shutil.copy(RAIZ_PROJETO / "cadernos.yaml", base / "cadernos.yaml")
    (base / "config.yaml").write_text('nome: "Inteligência Pragmática"\nenvio: desligado\n'
                                      'site_url: "https://exemplo.github.io/ip"\n', encoding="utf-8")
    (base / "dados").mkdir()
    (base / "dados" / "historico.json").write_text("[]\n", encoding="utf-8")
    (base / "docs").mkdir()
    (base / "docs" / "index.html").write_text("vazio\n", encoding="utf-8")
    for cmd in (["config", "user.email", "t@t"], ["config", "user.name", "Teste"], ["add", "-A"],
                ["commit", "-q", "-m", "base"], ["remote", "add", "origin", str(origem)], ["push", "-q", "origin", "HEAD:main"]):
        git(base, *cmd)

    edicoes = {
        "geral": ("edicoes/2026-01-15", (RAIZ_PROJETO / "testes" / "edicao_exemplo.md").read_text(encoding="utf-8")),
        "mercado": ("edicoes/mercado/2026-01-15", EDICAO_MERCADO),
        "niteroi": ("edicoes/niteroi/2026-01-15", EDICAO_MERCADO.replace("o touro tropeçou", "a barca atrasou")),
    }
    clones = {}
    for caderno, (pasta, texto) in edicoes.items():
        c = tmp / "pub" / caderno
        git(tmp / "pub", "clone", "-q", str(origem), str(c))
        git(c, "config", "user.email", "t@t")
        git(c, "config", "user.name", "Teste")
        (c / pasta).mkdir(parents=True)
        (c / pasta / "edicao.md").write_text(texto, encoding="utf-8")
        if caderno != "geral":
            (c / pasta / "painel.md").write_text("**Painel de teste**\n", encoding="utf-8")
        # como a rotina faz: monta e registra antes de publicar (isso suja docs/ e o histórico)
        cfg = cadernos_cfg(c, caderno)
        montagem.montar("2026-01-15", c, cfg, caderno)
        historico.registrar("2026-01-15", c, caderno)
        clones[caderno] = c

    def roda(caderno):
        try:
            return publicar.publicar("2026-01-15", clones[caderno], "%s nº 1 — teste" % caderno, caderno, espera=0.3)
        except Exception as e:
            return {"erro": str(e)}

    # A geral publica primeiro (e leva os índices dos cadernos, que nenhum clone tinha); depois os dois
    # cadernos publicam juntos. Sem o "git clean" no publicar, o pull deles travava em docs/<caderno>.html.
    res = {"geral": roda("geral")}
    with ThreadPoolExecutor(2) as pool:
        res.update(zip(["mercado", "niteroi"], pool.map(roda, ["mercado", "niteroi"])))
    conferir(all("erro" not in r for r in res.values()), "as três publicaram sem erro (%s)" % res)

    final = tmp / "pub" / "final"
    git(tmp / "pub", "clone", "-q", str(origem), str(final))
    hist_txt = (final / "dados" / "historico.json").read_text(encoding="utf-8")
    hist = json.loads(hist_txt)
    conferir("<<<<<<<" not in hist_txt and len(hist) == 3, "histórico sem conflito e com as 3 edições (%d)" % len(hist))
    conferir(sorted(e.get("caderno") or "geral" for e in hist) == ["geral", "mercado", "niteroi"],
             "uma edição de cada caderno no histórico")
    docs = final / "docs"
    paginas = ["2026-01-15.html", "mercado-2026-01-15.html", "niteroi-2026-01-15.html", "mercado.html", "niteroi.html"]
    conferir(all((docs / p).exists() for p in paginas), "as páginas e os arquivos dos 3 cadernos estão no site")
    indice = (docs / "index.html").read_text(encoding="utf-8")
    conferir('href="mercado.html"' in indice and 'href="niteroi.html"' in indice and "2026-01-15.html" in indice,
             "o índice da geral foi refeito com a edição e os links dos cadernos")
    conferir((docs / "mercado.html").read_text(encoding="utf-8").count("mercado-2026-01-15.html") == 1,
             "o arquivo do Mercado lista a edição dele")
    log = git(final, "log", "--format=%s").stdout
    conferir(all(("%s nº 1 — teste" % c) in log for c in clones), "os commits das três rotinas estão na main")


def testar_guardar_curadoria(tmp: Path):
    secao("guardar: a curadoria do dia sem edição vai para a main, mesmo com outra rotina publicando")
    from ferramentas import cadernos, publicar

    def git(cwd, *args):
        return subprocess.run(["git", "-c", "init.defaultBranch=main"] + list(args), cwd=str(cwd),
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    origem, base = tmp / "guardar" / "origem.git", tmp / "guardar" / "base"
    origem.mkdir(parents=True)
    git(origem, "init", "-q", "--bare")
    base.mkdir()
    git(base, "init", "-q")
    (base / "cadernos.yaml").write_text("economia:\n  dias_envio: [segunda, quarta, sexta]\n", encoding="utf-8")
    (base / "docs").mkdir()
    (base / "docs" / "index.html").write_text("vazio\n", encoding="utf-8")
    for cmd in (["config", "user.email", "t@t"], ["config", "user.name", "Teste"], ["add", "-A"],
                ["commit", "-q", "-m", "base"], ["remote", "add", "origin", str(origem)], ["push", "-q", "origin", "HEAD:main"]):
        git(base, *cmd)
    clones = {}
    for nome in ("economia", "geral"):
        c = tmp / "guardar" / nome
        git(tmp / "guardar", "clone", "-q", str(origem), str(c))
        git(c, "config", "user.email", "t@t")
        git(c, "config", "user.name", "Teste")
        clones[nome] = c
    # a geral publica no meio: a main andou, e o push da curadoria precisa de rebase
    (clones["geral"] / "docs" / "index.html").write_text("geral nº 9\n", encoding="utf-8")
    git(clones["geral"], "commit", "-q", "-am", "geral nº 9")
    git(clones["geral"], "push", "-q", "origin", "HEAD:main")
    eco = clones["economia"]
    arq = cadernos.arquivo_curadoria(eco, "economia")
    arq.parent.mkdir(parents=True)
    arq.write_text("# Curadoria\n\n## 2026-10-22\n- [juros] Selic (https://a)\n", encoding="utf-8")
    (eco / "dados" / "candidatos.md").write_text("não vai junto\n", encoding="utf-8")
    res = publicar.guardar("2026-10-22", eco, "Economia: curadoria de 2026-10-22", "economia", espera=0.1)
    final = tmp / "guardar" / "final"
    git(tmp / "guardar", "clone", "-q", str(origem), str(final))
    conferir(res["commit"] and (final / "dados" / "economia" / "curadoria.md").exists()
             and (final / "docs" / "index.html").read_text(encoding="utf-8") == "geral nº 9\n",
             "a curadoria chegou à main sem desfazer a geral publicada no meio")
    conferir(not (final / "dados" / "candidatos.md").exists(), "o guardar publica só a curadoria")
    conferir(publicar.guardar("2026-10-22", eco, "de novo", "economia", espera=0.1)["commit"] is None,
             "sem mudança na curadoria, não faz commit")


def cadernos_cfg(raiz, caderno):
    from ferramentas import cadernos as _c
    return _c.config(raiz, caderno)


def fotografia():
    """Lista de arquivos de edicoes/ e docs/ e o estado do historico.json do projeto real."""
    arquivos = sorted(str(p.relative_to(RAIZ_PROJETO)) for pasta in ("edicoes", "docs")
                      for p in (RAIZ_PROJETO / pasta).rglob("*"))
    hist = RAIZ_PROJETO / "dados" / "historico.json"
    return arquivos, (hist.stat().st_mtime if hist.exists() else None)


def main():
    antes = fotografia()
    with tempfile.TemporaryDirectory(prefix="ip-teste-") as t:
        tmp = Path(t)
        raiz = preparar_raiz(tmp / "api")
        testar_links(raiz)
        testar_montagem(raiz)
        testar_conversao()
        testar_historico(raiz)
        testar_envio(raiz)
        testar_cli(tmp)
        testar_cadernos(tmp)
        testar_horario_de_entrega(raiz)
        testar_publicar_em_paralelo(tmp)
        testar_coleta_filtros()
        testar_coleta_ia()
        testar_caderno_economia(tmp)
        testar_guardar_curadoria(tmp)
    secao("projeto real")
    conferir(fotografia() == antes, "o teste não criou nem mexeu em nada de edicoes/, docs/ e dados/historico.json")
    print("\n" + ("TUDO CERTO" if not falhas else "%d FALHA(S):\n  - " % len(falhas) + "\n  - ".join(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
