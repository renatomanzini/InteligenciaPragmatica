# Apuração — 2026-11-02

## (a) Matéria principal: a IA produz mais do que dá para revisar
(ficha do apurador a, colada abaixo)

ALERTAS
- "Mathematics has changed. Let's act like it" no blog do Tao é **guest post de Frank Calegari**, não do Tao. Não atribuir ao Tao. CONFIRMADO.
- Haas não dá contagem de bugs; só commits. Não inventar "N bugs". A frase dele de que o master "declined slightly" contradiz os números (1037 → 1443): não usar o dado do master.

### Postgres 19 (Robert Haas)
- Fonte: https://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html — Robert Haas, Sr. Staff Software Engineer da Databricks, committer do PostgreSQL; sexta, 30/10/2026. CONFIRMADO.
- Na última década, as versões major saem entre meados de setembro e meados de outubro; este ano deve sair "most likely" em novembro, e não é impossível atrasar mais. Feature freeze todo ano em 8 de abril. CONFIRMADO. Atraso ~1 mês: PARCIAL (inferido).
- 3 funcionalidades grandes revertidas entre 27/08 e 15/09 (UPDATE/DELETE FOR PORTION OF; SQL/PGQ; MERGE/SPLIT PARTITION). CONFIRMADO.
- Commits de 08/04 a 25/09 no branch de correções do ano anterior: REL_17_STABLE (2025) 248 → REL_18_STABLE (2026) 433, "mais de 74%". CONFIRMADO. Branch da versão nova: REL_18_STABLE (2025) 724 → REL_19_STABLE (2026) 1169, "mais de 60%". CONFIRMADO.
- Mecanismo (opinião do autor): muita gente reporta bugs achados com LLMs; LLMs rascunham correções que "aren't always correct" e precisam de revisão humana; o tempo de revisão foi para segurança e bugs nos branches antigos, atrasando a decisão do que reverter. CONFIRMADO como afirmação do autor.
- Contexto: histórico git de mais de 30 anos; "forty years of bugs". CONFIRMADO.
- Citação: "LLMs are going to require every PostgreSQL developer [...] to raise their game". CONFIRMADO.
- Tom: atraso "não é preocupante"; o longo prazo é "mais preocupante"; diz não saber como o projeto vai alcançar o acúmulo. Também vê código mais seguro por ser mais escrutinado. CONFIRMADO.

### Calegari no blog do Tao
- https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/ — 01/11/2026, guest post de Frank Calegari. CONFIRMADO.
- Propostas: avaliar todo trabalho como se fosse assistido por IA; contratação com mais entrevista presencial e menos peso no dossiê de papers; exigir mais dos periódicos; formação mais ampla; responsabilidade coletiva sobre resultados de IA; provas em Lean (linguagem que verifica prova por computador). CONFIRMADO.
- "mais de 700" artigos liberados pela OpenAI em 6 de outubro. CONFIRMADO (no texto).
- Citação: "Choosing worthwhile problems may end up mattering more than producing proofs." CONFIRMADO.
- Escala histórica: classificação dos grupos simples finitos anunciada em 1972, declarada completa em 1983, caso quasithin fechado ~duas décadas depois. CONFIRMADO.

### OpenAI / Altman
- https://www.theverge.com/ai-artificial-intelligence/1023054/altman-cheeky-pint-ai-math-interview — Robert Hart, The Verge, 30/10/2026; podcast Cheeky Pint (29/10). CONFIRMADO.
- Altman: "I do have empathy for the method"; "Humanity deserves fundamental knowledge"; diz ter mais resultados guardados; gasto na ordem de centenas de milhões de dólares; ~US$ 10 milhões só na solução de Navier-Stokes. CONFIRMADO.
- Verge: OpenAI liberou "centenas" de resultados neste mês, textos curtos e difíceis de seguir; críticas de atribuição, contexto e verificação insuficientes. CONFIRMADO.
- 722 preprints, só 162 com resultado formalizado em Lean; 3 retirados, 14 revisados; citações de Martin, Harris, Sutherland, Alpöge: PARCIAL (só agregador, Nature não aberta). Não usar sem ressalva; preferir cortar.

### Kingsbury
- Willison cita Kingsbury: https://simonwillison.net/2026/Nov/1/kyle-kingsbury/ (01/11/2026). CONFIRMADO.
- Original: Kyle Kingsbury (Jepsen), análise "ParticleDB 1.1.4", 31/10/2026: https://jepsen.io/analyses/particledb-1.1.4 — CONFIRMADO.
- Citação: LLMs "erode trust in documentation, in software, and in the organizations which produce them". CONFIRMADO (via Willison).
- 96 problemas encontrados no ParticleDB; site prometia "Full ACID" e "formally proven" com TLA+, mas não havia especificação TLA+; documentação se contradizia. CONFIRMADO. Que a documentação foi gerada por LLM: NÃO CONFIRMADO — não afirmar.

### Dois lados
- Pessimistas: Haas (revisão humana não escala), Kingsbury (confiança corroída), matemáticos na Verge (verificação insuficiente).
- Otimistas: Altman (humanidade merece o conhecimento), Calegari (adaptar a cultura; Lean), Haas (código mais escrutinado = mais seguro).

## (d) STATS, Hoje eu aprendi, links, Anthropic

### STATS: DoorDash e agentes de IA de fora
- Tony Xu, cofundador e CEO da DoorDash, na teleconferência do 3º tri (quinta, 29/10/2026): agentes de IA de terceiros geraram "several hundred orders" no total, desde que estão no ar; chamou de "fairly low use case". CONFIRMADO. Transcrição: https://www.fool.com/earnings/call-transcripts/2026/10/29/doordash-dash-q3-2026-earnings-call-transcript/ · Ars Technica (30/10): https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/
- Usar "algumas centenas"/"várias centenas"; o número é acumulado, sem período definido. CONFIRMADO.
- Escala: 993 milhões de pedidos no 3º tri de 2026 (+28% ano a ano, com ajuda da Deliveroo); receita de US$ 4,6 bi (+34%). CONFIRMADO (via transcrição).
- O conector (MCP) tem menos de um mês, restrito a parceiros de beta, usado sobretudo em pedidos corporativos de almoço: https://about.doordash.com/en-us/news/doordash-ordering-connector — CONFIRMADO. Xu vê potencial em compras de "long consideration" (pensadas). CONFIRMADO.
- Contraponto: Microsoft Clarity (29/10/2026), https://clarity.microsoft.com/blog/agentic-analytics-what-agents-do-on-websites/ — o evento "checkout" aparece em 25,21% das sessões de agentes contra 14,65% das humanas; dados de 13/08 a 09/09/2026, 230.511 projetos. CONFIRMADO. O próprio post diz que a sessão pode incluir humano assumindo e que não prova compra concluída. CONFIRMADO. Inconsistência na base (5,2 mi de sessões vs ~1,2 mi implícitas): não usar o "5,2 milhões". "Checkout" é evento de página, não compra.

### Hoje eu aprendi
- Pardela-de-Manx (Puffinus puffinus), ave marinha do tamanho de um pombo: usa o Sol como bússola e recalibra o relógio interno no amanhecer e no anoitecer; voando muito para leste ou oeste, o relógio se desalinha (4 minutos por grau de longitude) e o rumo erra até ~15 graus; num voo de 1.000 km, erro médio de ~7 graus. Estudo na Science liderado por Patrick Lewin (Oxford), 20 anos de GPS, 1.045 aves. CONFIRMADO no Ars: https://arstechnica.com/science/2026/10/seabirds-racing-home-over-the-ocean-can-get-jet-lagged/ (paper: https://doi.org/10.1126/science.adz2542, PARCIAL).

### Links
- HackerTube, Andrej Karpathy, 31/10/2026: 6.454 vídeos do YouTube recomendados em ~40 mil comentários do Hacker News (2007 a 2026); ele diz ter pedido ao Claude para construir, em ~2 horas. CONFIRMADO. https://karpathy.bearblog.dev/hacker-tube/
- Lenny's Podcast, 01/11/2026, 1h27: Hector Serrano, Head of Content da Wispr Flow (voz para texto com IA); ~50 criadores produzem 500 a 600 anúncios UGC pagos por mês; empresa avaliada em US$ 2 bi. CONFIRMADO pela descrição (episódio não ouvido). https://www.lennysnewsletter.com/p/how-a-19-year-old-intern-built-the
- Nolan Lawson, 28/10/2026, "The AI cost of JavaScript frameworks": agentes de código fazem o mesmo app em 12 frameworks; mediana de custo por execução de US$ 2,67 (Hono+htmx) a US$ 4,97 (Angular), quase o dobro; custo estimado a preço de API, app pequeno. CONFIRMADO. https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/

### Anthropic
- Nenhuma manchete em /news ou /engineering de 31/10 a 02/11. Mais recente: 28/10. Nada entra.

## (b) IA na prática: lexifina/global-law (leis como histórico git)
Método: `main.py github` falhou (HTTP 403 no proxy). Estrelas e datas exatas NÃO CONFIRMADAS: não citar estrelas.

- Repositório: https://github.com/lexifina/global-law — "Git for Global Law": cada jurisdição é um repositório próprio ligado como submódulo; cada commit é uma lei entrando em vigor. README: https://raw.githubusercontent.com/lexifina/global-law/HEAD/README.md — CONFIRMADO.
- Licença CC0 para a árvore, ferramentas e docs; o texto da lei fica sob os termos de cada repositório de país. https://raw.githubusercontent.com/lexifina/global-law/HEAD/LICENSE.md — CONFIRMADO.
- Quem mantém: organização "lexifina", sem identificação de pessoa ou empresa. Não é oficial. CONFIRMADO (ausência).
- Escala: o manifest tem 211 jurisdições, mas só 107 com algum corpus; a cobertura varia de código inteiro a "a few acts, or a sample" (EUA = 9 títulos do US Code). https://raw.githubusercontent.com/lexifina/global-law/HEAD/manifest.json — CONFIRMADO.
- Brasil: https://github.com/lexifina/brazil-law — fonte declarada: Planalto; "one file per article, one commit per amendment on the day it took effect"; registro até 28/10/2026. CONFIRMADO. Inclui Constituição de 1988 (122 versões, EC 1 a 141), Código Civil (64 versões), Código Penal (111), CPC, CLT (220), CDC (16), LGPD (11), Marco Civil (4), Estatuto da Advocacia (17). README: https://raw.githubusercontent.com/lexifina/brazil-law/HEAD/README.md — CONFIRMADO. Mais de 100 atos: PARCIAL.
- Limites do Brasil: várias leis param em datas passadas (Lei 8.666/1993 até 30/12/2023; Lei 9.099/1995 até 23/11/2021; LAI até 03/06/2025); anexos e tabelas ficam de fora; alguns períodos faltam. CONFIRMADO. O manifest avisa que as citações do Brasil não são reconhecidas pela ferramenta de checar citação. CONFIRMADO.
- Contexto: o próprio SOURCES.md lista o LexML (https://www.lexml.gov.br, sem versões por data) e o Planalto (https://www.planalto.gov.br/ccivil_03/leis/, texto compilado com redação revogada riscada, sem seletor de data) e o projeto legislacao-br (https://github.com/Evaldoes/legislacao-br). https://raw.githubusercontent.com/lexifina/global-law/HEAD/brazil/SOURCES.md — CONFIRMADO.
- Uso com agente: servidor MCP local (MCP = padrão para plugar ferramentas num assistente de IA) em tools/mcp_server.py; precisa de Python 3.10+ e git; roda na máquina, só lê o repositório, "makes no network calls"; `claude mcp add global-law -- python tools/mcp_server.py`; 18 ferramentas só de leitura (ler dispositivo numa data, comparar datas, ver qual lei escreveu cada linha, checar citações de uma peça). Funciona com Claude Code, Claude Desktop e Cursor. CONFIRMADO (README).
- Exemplo do README: "Check every citation in this brief against the law in force today." CONFIRMADO.
- O repositório é reconstruído do zero e "force-pushed" quando um corpus muda (hashes mudam). CONFIRMADO.
- Limites do README: arquivo ausente numa data pode ser lei não vigente OU corpus que não chega lá; lei retroativa não reescreve o texto das datas anteriores. CONFIRMADO.
- Requisito de RAM/disco: NÃO CONFIRMADO; clonar com todos os submódulos pode ser pesado; sugestão: clonar só o brazil-law (NÃO TESTADO — escrever como sugestão).
- "#1 no Hacker News": NÃO CONFIRMADO — não usar.

### Alternativa (não usada como principal): floorplan
- https://github.com/haydenschmitty/floorplan — plugin para Claude Code e Codex que desenha mapa interativo do código com nomes em inglês simples; licença MIT; "Health check" com ressalva "A check, not an audit." CONFIRMADO (README). Estrelas não confirmadas.

## (c) Economia e rodadas

### Por aqui
- Copom decide na quarta (04/11), depois do fechamento; Selic em 13,75%. O Itaú espera manutenção e "escolha unânime de interromper o ciclo" (NeoFeed, 30/10). Projeção do Itaú: com Selic em 13,75% até o fim de 2028, a inflação converge a 3%; com a trajetória do Focus (11,75% em 2027), fica em 3,4%. https://neofeed.com.br/economia/itau-ve-fim-do-ciclo-de-cortes-da-selic-diante-de-cenario-mais-adverso/ — CONFIRMADO. A grade do InfoMoney traz 13,5% para o Copom, e o Focus de 13/10 apontava corte para 13,50%: mercado dividido. PARCIAL.
- Agenda da semana (InfoMoney, 01/11): Caged de setembro na quarta (esperado 150 mil); produção industrial na quinta (esperado -0,1% no mês); payroll dos EUA na sexta. https://www.infomoney.com.br/mercados/calendario-economico-da-semana-copom-trabalho-e-eleicoes-nos-eua-sao-destaques/ — CONFIRMADO.
- Petrobras sobe o querosene de aviação em 7,2% (+R$ 0,45 por litro) a partir de domingo (01/11), por cotações internacionais, Oriente Médio e refino na Rússia; em outubro, a alta tinha sido de 11,8%. https://www.estadao.com.br/economia/petrobras-aumenta-preco-do-querosene-de-aviacao-em-72-a-partir-deste-domingo/ — CONFIRMADO (Estadão citando nota da Petrobras).
- Binance: saídas líquidas de ~US$ 3,64 bi no domingo (01/11), entre manhã e começo da tarde, após retomar saques (US$ 4,649 bi em retiradas contra US$ 1,01 bi em depósitos), equivalente a 2,1% dos ativos; números da própria Binance. https://www.estadao.com.br/economia/binance-registra-retiradas-liquidas-de-us-364-bilhoes-apos-retomada-de-saques/ — CONFIRMADO.

### Lá fora
- Opep+ (sete membros) mantém metas de produção para dezembro (domingo, 01/11); decisão sobre 2027 em 29/11; Brent fechou perto de US$ 118 na sexta (30/10), o maior desde abril. https://www1.folha.uol.com.br/mercado/2026/11/opep-mantem-metas-de-producao-de-petroleo-para-dezembro-antes-de-decisao-sobre-2027.shtml — CONFIRMADO.
- Banco da Inglaterra decide na quinta (05/11); taxa em 3,75%, mantida em 17/09 por 6 a 3 (três votos por 4%). https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate — CONFIRMADO. Expectativa de alta: PARCIAL (WSJ não abriu) — escrever "parte do mercado espera alta", ou omitir.
- PMI industrial RatingDog da China: 52,0 em outubro, contra 52,1 em setembro; o PMI oficial caiu de 50,1 para 49,3 (abaixo de 50 = contração). https://valor.globo.com/mundo/noticia/2026/11/01/pmi-industrial-da-ratingdog-da-china-recua-para-520-em-outubro.ghtml — CONFIRMADO.
- Eleições de meio de mandato nos EUA na terça (03/11), agenda de mercado. CONFIRMADO (InfoMoney acima).

### Brasil adentro
- Chilli Beans pediu recuperação extrajudicial na sexta (30/10), com R$ 340 mi em dívidas; plano com aporte de R$ 50 mi em capital novo (Itaú, Akron e Vega); 900 franquias em 14 países. https://neofeed.com.br/negocios/com-dividas-de-r-340-milhoes-chilli-beans-entra-com-pedido-de-recuperacao-extrajudicial/ — CONFIRMADO.
- Raízen: assembleias de sexta (30/10) aprovaram dividir a empresa em duas listadas (distribuição com a marca Shell; açúcar, etanol e bioenergia); aumento de capital de até R$ 39,8 bi, conselho vota em 06/11; separação ainda depende de condições do plano. https://investnews.com.br/negocios/raizen-assembleia-credores-outubro26/ — CONFIRMADO.
- 99: maioria das operações de delivery com mais de um ano já é rentável, segundo Simeng Wang, diretor-geral no Brasil; sem números; R$ 3 bi anunciados em investimento; ~150 cidades. https://www.estadao.com.br/economia/coluna-da-broad/maioria-das-operacoes-de-delivery-da-99-com-mais-de-um-ano-e-rentavel-diz-executivo/ — CONFIRMADO como declaração.
- Itaú compra a NeoSpace por R$ 2,925 bi, sujeito a Cade e BC; em janeiro de 2025 pagou US$ 15 mi por 15%. https://www.bloomberglinea.com.br/startups/rodadas-da-semana-kalshi-capta-us-1-bilhao-e-chega-a-us-40-bi-de-valuation/ — CONFIRMADO (o que a NeoSpace faz: não caracterizado — não descrever).
- AST SpaceMobile (rival da Starlink): autorização da Anatel de 09/10 (não é nova) — FORA.

### Mundo afora
- FTC, sete estados e dois governos locais da Califórnia processam a Toast (sistema para restaurantes) na quinta (29/10) por taxa escondida de US$ 0,99 em pedidos online e cancelamento difícil; a Toast "discorda fortemente". Comunicado da FTC: https://ftc.gov/news-events/news/press-releases/2026/10/ftc-states-take-action-against-toast-inc-over-hidden-unauthorized-fees-deceptive-subscription — CONFIRMADO. ("oito estados" = PARCIAL: não usar.)
- Apple corta a comissão da App Store em Taiwan de 30% para 26%, em compromisso com o órgão de concorrência, que suspendeu a investigação sem declarar infração; a Apple diz que 26% iguala Japão e Brasil. https://ppc.land/apple-cuts-taiwan-app-store-commission-to-26-after-antitrust-probe/ — CONFIRMADO.
- Shopify, em prévia para desenvolvedores (por convite, EUA), deixa lojas pagarem comissão à empresa do agente de compras de IA: base de 0,3% do pedido; detalhes "not final". https://www.searchenginejournal.com/shopify-now-lets-stores-pay-the-company-behind-your-ai-shopping-agent/594544/ — PARCIAL (escrever como prévia).
- ChatGPT Ads liga por padrão, desde sexta (30/10), os ajustes automáticos de criativo: pode reescrever título, traduzir, redimensionar imagem e trocar a URL de destino sem aprovação prévia; dá para desligar. https://www.searchenginejournal.com/chatgpt-ads-turns-on-automatic-ad-changes-by-default/595117/ — CONFIRMADO (SEJ citando a ajuda da OpenAI).
