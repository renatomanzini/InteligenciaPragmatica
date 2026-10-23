# Especificação do código: Inteligência Pragmática

O código é só a parte mecânica: coletar, montar, checar links, guardar histórico e enviar.
Quem pesquisa e escreve é o Claude (a rotina), seguindo `manual/ROTINA.md`.

## Regras gerais
- Python **3.9** no Mac do usuário e 3.11+ na nuvem. Proibido `match` e `X | Y` em tipos; use `Optional[...]`.
- Dependências: só `pyyaml`, `feedparser` e `markdown` (em `requirements.txt`). O resto é biblioteca padrão (`urllib`, `concurrent.futures`, `zoneinfo`, `json`, `re`, `html`).
- Fuso: `America/Sao_Paulo` via `zoneinfo`. "Hoje" é sempre a data em Brasília.
- Toda requisição HTTP:
  - leva `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36 InteligenciaPragmatica/1.0`;
  - tem timeout de 20 s;
  - quando falha, a função NÃO derruba o programa: registra no log e segue.
- Mensagens e comentários em português do Brasil. Comentários curtos.
- O código roda a partir da raiz do projeto: `python main.py ...`. Os caminhos são relativos ao arquivo `main.py` (use `Path(__file__).resolve().parent`).

## Estrutura de pastas
```
main.py                     linha de comando (argparse)
config.yaml                 configuração (envio ligado/desligado, site_url…)
fontes.yaml                 fontes RSS, especiais (APIs) e radar
preferencias.md             gostos do leitor (lido pela rotina, não pelo código)
manual/                     MANUAL_DE_REDACAO.md e ROTINA.md
ferramentas/
  __init__.py
  util.py                   datas, http_get, leitura de yaml, front matter
  coleta.py                 coleta de candidatos
  github.py                 dados oficiais de um repositório (estrelas etc.)
  historico.py              memória das edições
  links.py                  verificação de links de uma edição
  montagem.py               edicao.md → email.html, curta.txt e site
  envio.py                  envio pelo Resend
dados/
  historico.json
  candidatos/AAAA-MM-DD.md, AAAA-MM-DD-fontes.log
edicoes/AAAA-MM-DD/
  edicao.md                 escrita pela rotina (formato abaixo)
  verificacao.md            log de checagem escrito pela rotina (não vai na edição)
  links.json                saída do links.py
  email.html, curta.txt     saídas da montagem
docs/                       site estático (GitHub Pages), gerado pela montagem
```

## Formato da edição: `edicoes/AAAA-MM-DD/edicao.md`
Front matter YAML entre `---` e corpo em Markdown:
```markdown
---
data: 2026-10-17
tipo: dia_util            # dia_util | sabado | domingo
numero: 1                 # número sequencial da edição
assunto: "o ~~disco~~ carro voador da tesla"
previa: "+ por que a anthropic quer seu próprio git"
tempo_leitura_min: 7
dia: morno                # forte | morno
breakthrough: false
historias:                # o que foi coberto (vai para o histórico)
  - id: tesla-roadster-voador          # slug estável; repetir o mesmo id ao acompanhar a história
    titulo: "Tesla mostra Roadster com propulsores"
    tema: negocios                       # ia | economia | negocios | marketing | direito_tech | china | filosofia | outro
    urls: ["https://exemplo.com/a"]
    em_andamento: true                   # vale acompanhar nos próximos dias?
formatos: [materia_principal, ia_na_pratica, stats]   # seções usadas (para variar formatos)
---
bom dia. Reflexão curta…

**Hoje eu aprendi:** fato curioso ([fonte](https://…)).

**Nesta edição:**
- item 1
- item 2

---

#### INTELIGÊNCIA ARTIFICIAL
## Título da matéria
> **TL;DR:** uma frase.

Texto com **números** e [links](https://…).

🔗 [Fonte primária](https://…)

---

#### BRASIL ADENTRO
→ **Empresa**: uma frase ([fonte](https://…))
```

### Convenções que a montagem precisa tratar
| No Markdown | Vira |
|---|---|
| `#### TEXTO` | rótulo (kicker): versalete pequeno, cor de destaque, espaçamento entre letras |
| `## Título` | título de matéria |
| `### Subtítulo` | subtítulo |
| `> **TL;DR:** …` (blockquote) | caixa de destaque com fundo suave e borda à esquerda |
| `---` | separador de seção (linha fina) |
| `~~texto~~` | `<del>` (o Markdown padrão não faz isso: converter antes com regex) |
| linha que começa com `→ ` | item de lista "seta". Linhas consecutivas viram um bloco; cada uma é um parágrafo curto com a seta |
| linha que começa com `🔗 ` | linha de fonte: fonte menor, cor secundária |
| `**Opinião:**` no início de um parágrafo | parágrafo com selo "opinião" (itálico, cor secundária) |
| links | sublinhados, cor de destaque |

## Comandos do `main.py`
```
python main.py coletar [--data AAAA-MM-DD]
python main.py historico [--dias 14]
python main.py github DONO/REPO [DONO/REPO ...]
python main.py links [AAAA-MM-DD]
python main.py montar [AAAA-MM-DD]
python main.py registrar [AAAA-MM-DD]
python main.py enviar [AAAA-MM-DD] [--agora] [--forcar]
python main.py --dry-run [AAAA-MM-DD]
```
- Quando a data é omitida: `coletar` usa hoje (Brasília) e os outros usam a edição mais recente em `edicoes/`.
- `--dry-run` faz: `coletar` (hoje) → se existir edição na data (ou a mais recente), roda `links` e `montar` → abre `email.html` no navegador (`webbrowser.open`). **Nunca envia.** Sem edição, avisa: "Coleta pronta. A edição é escrita pela rotina (manual/ROTINA.md)."
- Os códigos de saída são 0 em sucesso e 1 em erro. `links` sai com 1 se houver link quebrado.

## `coleta.py`: `coletar(data: date, raiz: Path) -> dict`
1. Lê `fontes.yaml`. A janela de horas sai de `janela_horas`, conforme o dia da semana da data (segunda, sábado, domingo ou padrão).
2. Lê em paralelo (`ThreadPoolExecutor`, 8 workers) as fontes ativas com `rss`, usando `feedparser`. Busque o conteúdo com o `http_get` próprio (por causa do User-Agent e do timeout) e passe os bytes ao feedparser. Fica com os itens dentro da janela, ou sem data (marque `sem_data: true`), até `limite_por_fonte`.
3. Especiais:
   - **Hacker News:** `https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=50` → título, url (ou o link do HN quando não houver url), pontos, comentários e link da discussão `https://news.ycombinator.com/item?id=…`. Ordene por pontos e pegue `limite`.
   - **GitHub em alta:** `https://api.github.com/search/repositories?q=created:>AAAA-MM-DD&sort=stars&order=desc&per_page=N`, com a data igual a hoje menos `dias` → full_name, descrição, estrelas, linguagem, html_url e created_at.
   - **Hugging Face:**
     - modelos em alta: `https://huggingface.co/api/models?sort=trendingScore&direction=-1&limit=N`;
     - papers do dia: `https://huggingface.co/api/daily_papers?limit=N`.
     - Se algum endpoint falhar, registre e siga.
   - **Reddit:** `https://www.reddit.com/r/SUB/top/.rss?t=day`, pelo feedparser, com o mesmo User-Agent.
4. Radar:
   - itens com `rss`: lidos normalmente, marcados `radar: true`;
   - itens com `sitemap`: baixe o XML e pegue as `<url>` com `<loc>` contendo `/p/` e `<lastmod>` dentro da janela (no máximo 8 por newsletter). Para cada uma, baixe a página e extraia só `og:title` e `og:description` (ou `<title>`). Não guarde o texto da matéria.
5. Para cada candidato, monte:
   ```
   {id (sha1 curto da url), titulo, url, fonte, tema, tipo_fonte, publicado_em (ISO, Brasília),
    resumo (até 300 caracteres, sem HTML), radar (bool), extra (dict: pontos, comentarios,
    discussao, estrelas, linguagem…), ja_coberto (bool)}
   ```
   `ja_coberto` é true quando a url (sem query string e sem barra final) aparece em alguma história de `dados/historico.json`.
6. Remove duplicatas por url normalizada.
7. Grava:
   - `dados/candidatos/AAAA-MM-DD.md`: compacto, para o Claude ler. A ordem é:
     1. cabeçalho com data, janela e totais;
     2. seções por tema (IA, China, Economia, Negócios, Marketing, Direito & Tech, Filosofia, Comunidade);
     3. a seção "Radar (newsletters que o leitor já recebe)";
     4. a seção "Fontes sem RSS para visitar na apuração", com nome e página.
     Uma linha por item: `- [Fonte] Título — resumo curto (url) · extra · JÁ COBERTO`. Use o resumo cortado em ~160 caracteres no .md.
   - `dados/candidatos/AAAA-MM-DD-fontes.log`: as fontes que falharam e o motivo.
8. Imprime um resumo, por exemplo: "312 candidatos de 58 fontes (4 falharam). Arquivo: dados/candidatos/…md".

## `github.py`: `info(repo: str) -> dict`
Chama `https://api.github.com/repos/DONO/REPO` → full_name, estrelas, forks, created_at, pushed_at, descricao, html_url e arquivado. O comando `github` imprime uma linha por repositório. Isso existe para a checagem confirmar números de estrelas.

## `historico.py`
- `carregar(raiz) -> list`: lê `dados/historico.json`, ou devolve lista vazia.
- `registrar(data, raiz)`: lê o front matter de `edicoes/DATA/edicao.md`. Insere ou substitui a entrada daquela data com data, tipo, numero, assunto, previa, dia, breakthrough, historias e formatos. Ordena por data e grava com `ensure_ascii=False, indent=2`.
- `resumo(dias=14, raiz) -> str`: um texto legível com as últimas N edições, contendo a data, o tipo, o assunto e uma linha por história (id, título, tema e "(em andamento)"). Inclui também uma seção "Histórias em andamento", com a data da última menção (só as citadas nos últimos 45 dias), e os formatos usados por dia, para variar. É isso que o comando `historico` imprime.
- `proximo_numero(raiz) -> int`.
- `urls_cobertas(raiz) -> set`.

## `links.py`: `verificar(data, raiz) -> dict`
- Extrai todas as URLs http(s) do `edicao.md`: links Markdown e URLs soltas, inclusive no front matter (`historias[].urls`).
- Testa em paralelo (8 workers). Tenta HEAD primeiro; se HEAD der erro ou 405, usa GET (lendo só os primeiros 64 KB). Segue redirecionamentos.
- Classifica:
  - `ok` (2xx/3xx final);
  - `quebrado` (404, 410 ou erro de DNS);
  - `inconclusivo` (401, 403, 429, 5xx ou timeout, comum em sites com paywall ou anti-robô).
- Grava `edicoes/DATA/links.json` e imprime uma tabela simples. Sai com código 1 se houver `quebrado`.

## `montagem.py`: `montar(data, raiz, config) -> dict`
Lê `edicao.md` (front matter + corpo) e gera três coisas.

**1. `edicoes/DATA/email.html`:** HTML de e-mail.
- Tabela centralizada com 640 px de largura máxima e **estilos inline** (o Gmail ignora boa parte de `<style>`). Pode haver um `<style>` extra só para o modo escuro e para o celular.
- Pré-header escondido com a `previa`.
- Cabeçalho com o nome "Inteligência Pragmática", a data por extenso em português ("sábado, 17 de outubro de 2026"), "Edição nº N" e "X min de leitura".
- Corpo convertido pelas convenções acima.
- Rodapé discreto:
  - "Arquivo de edições" com link para `config.site_url`, se preenchido;
  - a linha "Feita por IA para um leitor só. Fontes linkadas em cada afirmação.".
- **Visual:**
  - sóbrio e editorial: fundo off-white `#FAF8F5`, texto `#1F1F1F`;
  - cor de destaque azul-petróleo `#0F5C6E` nos rótulos e links;
  - títulos em fonte serifada do sistema (`Georgia, 'Times New Roman', serif`) e corpo em sans do sistema (`-apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif`), com 16–17 px e line-height 1.6;
  - sem imagens externas.

**2. `edicoes/DATA/curta.txt`:** a versão curta para mensageiro, com até ~900 caracteres. Contém:
- o assunto em uma linha;
- a data;
- 3 a 5 bullets "• Título: TL;DR" (pegue os `##` e o TL;DR seguinte, quando houver);
- "Edição completa: <site_url>/AAAA-MM-DD.html", se `site_url` existir.

**3. Site em `docs/` (GitHub Pages, PWA instalável):**
- `docs/AAAA-MM-DD.html`: a mesma edição em versão web. Pode usar `<style>` normal, é responsiva, tem modo claro e escuro (`prefers-color-scheme`) e um link "← todas as edições".
- `docs/index.html`: a lista de todas as edições (lendo `edicoes/*/edicao.md`), da mais nova para a mais antiga, com data, número, assunto (sem `~~`, mostrando o tachado como `<del>`) e prévia.
- `docs/manifest.webmanifest`, `docs/sw.js` (cache das páginas visitadas, para ler offline), `docs/icon.svg` e `docs/icon-192.png` / `docs/icon-512.png` são arquivos fixos do repositório, que a montagem não regrava: fundo `#0F5C6E` e um "IP" desenhado em blocos de pixel, em cor clara.
- As páginas incluem `<link rel="manifest">`, `apple-touch-icon` e `theme-color`.
- Todos os links internos são **relativos** (o site vai morar em `usuario.github.io/repo/`).

## `envio.py`: `enviar(data, raiz, config, agora=False, forcar=False)`
- Se `config.envio != "ligado"` e não houver `forcar`, recusa com a mensagem "Envio desligado no config.yaml (fase de testes)".
- Se `edicoes/DATA/envio.json` já existir e não houver `forcar`, não envia de novo (status `ja_enviada`, com o ID antigo).
- Precisa das variáveis de ambiente `RESEND_API_KEY` e `EMAIL_DESTINO`. Se faltar alguma, avisa qual.
- Faz `POST https://api.resend.com/emails` com JSON:
  - `from`: "Inteligência Pragmática <onboarding@resend.dev>"
  - `to`: [EMAIL_DESTINO]
  - `subject`: o assunto. Remova `~~x~~` mantendo o texto, porque o assunto do e-mail não aceita tachado; para o tachado use os caracteres combinantes U+0336 em cada letra, como as Drops fazem.
  - `html` e `text`: `curta.txt` mais o aviso "versão completa no HTML".
  - `scheduled_at`: o ISO da data às `horario_entrega` com offset -03:00, só se esse horário ainda estiver no futuro e `--agora` não for usado.
- Imprime o id devolvido e grava `edicoes/DATA/envio.json`.

## `util.py`
Helpers usados por todos:
- `hoje_brasilia()`, `agora_brasilia()`, `data_por_extenso(d)`;
- `http_get(url, timeout=20, max_bytes=None) -> (status, bytes, url_final)`;
- `ler_yaml(path)`;
- `ler_front_matter(path) -> (dict, corpo)`;
- `normalizar_url(u)`;
- `edicao_mais_recente(raiz)`.
