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
        testar_coleta_filtros()
    secao("projeto real")
    conferir(fotografia() == antes, "o teste não criou nem mexeu em nada de edicoes/, docs/ e dados/historico.json")
    print("\n" + ("TUDO CERTO" if not falhas else "%d FALHA(S):\n  - " % len(falhas) + "\n  - ".join(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
