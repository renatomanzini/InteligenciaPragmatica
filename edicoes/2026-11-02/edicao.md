---
data: 2026-11-02
tipo: dia_util
numero: 15
assunto: "a ia escreve, alguém tem que conferir"
previa: "+ as leis do brasil com histórico de versões"
tempo_leitura_min: 7
dia: morno
breakthrough: false
historias:
  - id: ia-gargalo-revisao
    titulo: "Postgres 19 atrasa e matemáticos pedem nova cultura: a IA produz mais do que dá para revisar"
    tema: ia
    urls: ["https://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html", "https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/"]
    em_andamento: true
  - id: global-law-git
    titulo: "Projeto aberto põe as leis do Brasil e de outros países em histórico git, com servidor MCP"
    tema: direito_tech
    urls: ["https://github.com/lexifina/global-law"]
    em_andamento: false
  - id: agentes-compras-realidade
    titulo: "DoorDash diz que agentes de IA de fora renderam só algumas centenas de pedidos"
    tema: negocios
    urls: ["https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/"]
    em_andamento: true
  - id: selic-copom-2026
    titulo: "Copom decide a Selic na quarta (04/11); Itaú espera manutenção em 13,75%"
    tema: economia
    urls: ["https://neofeed.com.br/economia/itau-ve-fim-do-ciclo-de-cortes-da-selic-diante-de-cenario-mais-adverso/"]
    em_andamento: true
  - id: binance-ataque-2026
    titulo: "Binance reabre saques e tem saída líquida de ~US$ 3,64 bi no domingo"
    tema: economia
    urls: ["https://www.estadao.com.br/economia/binance-registra-retiradas-liquidas-de-us-364-bilhoes-apos-retomada-de-saques/"]
    em_andamento: true
  - id: raizen-transacao-tributaria
    titulo: "Credores aprovam dividir a Raízen em duas empresas listadas"
    tema: negocios
    urls: ["https://investnews.com.br/negocios/raizen-assembleia-credores-outubro26/"]
    em_andamento: true
formatos: [explicador, materia_principal, ia_na_pratica, economia, rodadas, stats, links, pergunta]
---
bom dia. Escrever ficou barato: código, parecer e prova matemática saem em segundos. Conferir continua custando o mesmo tempo de sempre. Hoje a edição anda em volta dessa diferença.

**Hoje eu aprendi:** a pardela-de-Manx, ave marinha do tamanho de um pombo, tem jet lag: ela usa o Sol como bússola, e, voando muito para leste ou oeste, o relógio interno desalinha e o rumo erra até ~**15 graus**. É o que mostra um estudo na Science, com 20 anos de GPS ([Ars Technica](https://arstechnica.com/science/2026/10/seabirds-racing-home-over-the-ocean-can-get-jet-lagged/)).

**Nesta edição:**
- O Postgres 19 atrasou porque a IA achou bugs demais, e ninguém dá conta de revisar
- As leis do Brasil com histórico de versões, prontas para um agente consultar
- Copom na quarta: o Itaú já dá o ciclo de cortes como encerrado
- Chilli Beans, Raízen, 99 e a compra da NeoSpace pelo Itaú
- STATS: quantos pedidos os agentes de IA trouxeram para a DoorDash (spoiler: poucos)

---

#### IA
## Quem confere o que a IA escreveu?
> **TL;DR:** o Postgres 19 atrasou porque a IA ajudou a achar bugs demais, e a matemática recebeu mais de **700** artigos de uma vez: o gargalo agora é revisar.

Em 30/10, Robert Haas, engenheiro da Databricks e *committer* do PostgreSQL (quem pode gravar mudanças no código oficial do banco de dados aberto que muita empresa usa), escreveu que a versão 19 deve sair "most likely" em novembro. Na última década, saíram entre meados de setembro e meados de outubro ([blog de Haas](https://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html)).

Ele culpa a IA. Muita gente reporta bugs achados com LLMs (os modelos de linguagem). A IA também rascunha correções que nem sempre estão certas, e alguém precisa revisar. Entre 08/04 e 25/09, os *commits* (cada alteração registrada no código) no ramo de correções da versão anterior foram de **248** para **433** na comparação com o ano passado, **mais de 74%**. No ramo da versão nova, de **724** para **1.169**, **mais de 60%**. Haas diz não saber como o projeto vai alcançar o acúmulo.

A matemática vive a versão dela. No blog do matemático Terence Tao, o convidado Frank Calegari (01/11) lembra que a OpenAI liberou **mais de 700** artigos em 6 de outubro e propõe tratar todo trabalho como se tivesse ajuda de IA, com mais entrevista presencial nas contratações e mais espaço para provas em Lean, linguagem que o computador usa para verificar uma prova ([texto de Calegari](https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/)). Para ele, "Choosing worthwhile problems may end up mattering more than producing proofs".

Revisar sempre foi lento, lembra Calegari: o programa de classificação dos grupos simples finitos foi anunciado em 1972, a classificação foi declarada completa em 1983, e um caso só fechou umas duas décadas depois.

Sam Altman, num podcast, disse ter mais resultados guardados e um gasto na casa das centenas de milhões de dólares, **~US$ 10 milhões** só no problema de Navier-Stokes. O Verge registra críticas de verificação insuficiente ([The Verge](https://www.theverge.com/ai-artificial-intelligence/1023054/altman-cheeky-pint-ai-math-interview)). Já Kyle Kingsbury, do Jepsen, achou **96 problemas** no banco de dados ParticleDB, que se dizia "formally proven" sem ter a especificação que o provaria; para ele, LLMs corroem a confiança em documentação e software ([Jepsen](https://jepsen.io/analyses/particledb-1.1.4), [Willison](https://simonwillison.net/2026/Nov/1/kyle-kingsbury/)).

**Os otimistas:** Altman (a humanidade merece o conhecimento), Calegari (adaptar a cultura e verificar por máquina) e o próprio Haas (que vê "desafio e oportunidade").

**Os pessimistas:** Haas (a revisão humana não escala), Kingsbury (a confiança corroída) e matemáticos ouvidos pelo Verge.

**Por que isso importa pra você:** o advogado já conhece essa cena: a peça escrita por IA que cita jurisprudência inventada. Quem entrega app feito com IA também precisa de alguém que leia o que foi gerado, e a IA agora é o estagiário que entrega 700 artigos na sexta às 18h.

**Opinião:** o valor migra de produzir para conferir e assinar, e a aposta é que "revisão" vira serviço vendável, com preço próprio, separado de "produção".

🔗 [Fonte primária](https://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html)

---

#### 🧠 IA NA PRÁTICA
## As leis do Brasil com histórico de versões, prontas para um agente
> **TL;DR:** um projeto aberto guarda a Constituição, a CLT e outras leis com uma versão para cada alteração, na data em que entrou em vigor, e liga isso a agentes de IA.

É o "controlar alterações" do Word, mas para a lei inteira. O *git* é um sistema de histórico de versões; aqui, cada emenda vira uma versão datada, e dá para perguntar "o que dizia o artigo X em tal data". O MCP é a tomada que pluga uma ferramenta no assistente de IA, e o projeto traz um servidor MCP local.

**O caso.** O repositório `global-law`, da organização lexifina, reúne leis de vários países; o do Brasil, o `brazil-law`, declara o Planalto como fonte, com um arquivo por artigo e um commit por alteração. Tem a Constituição com **122** versões, o Código Civil com **64**, a CLT com **220** e a LGPD com **11**, com registro até 28/10/2026 no conjunto (cada lei tem a própria data final; a CLT vai até 06/04/2026). O servidor roda na máquina, só lê o repositório, não faz chamadas de rede e tem **18** ferramentas, como ler um dispositivo numa data. Com o repositório clonado, liga no Claude Code com `claude mcp add global-law -- python tools/mcp_server.py`.

🔗 [global-law](https://github.com/lexifina/global-law) e [brazil-law](https://github.com/lexifina/brazil-law)

⚠️ **Freio de realidade:** não é oficial: a fonte oficial continua sendo o Planalto. Há leis paradas no passado (a 9.099, dos juizados, vai só até 23/11/2021), alguns anexos e tabelas ficam de fora, e a checagem de citações não reconhece citações do Brasil. Requisito de máquina: não informado. É o tipo de coisa que se confere antes de confiar: [Planalto](https://www.planalto.gov.br/ccivil_03/leis/) e [LexML](https://www.lexml.gov.br).

**Agora aplica no mundo real:**
- **Advogado ou escritório:** achar a redação vigente na data do fato, o direito intertemporal.
- **Estudante de Direito:** ver como a CLT mudou, artigo por artigo.
- **Contador ou RH:** consultar a CLT por data.

**Como isso vira serviço:** montar, para um escritório pequeno, um "assistente de vigência": agente, base versionada e checagem humana no Planalto. O cliente pagaria porque errar a redação vigente custa caro. O limite: não substitui a conferência na fonte oficial.

**Para testar hoje (15 min):** abra o [brazil-law](https://github.com/lexifina/brazil-law) no navegador e veja o histórico de um artigo da LGPD ou do CDC. Sem instalar nada. Para o MCP, é preciso Python 3.10+ e git; clonar tudo com submódulos pode pesar num notebook de 8 GB (não testado).

---

#### ECONOMIA
**🇧🇷 Por aqui**

→ **Copom**: decide na quarta (04/11), com Selic em **13,75%**; o Itaú espera que o Copom interrompa os cortes ([NeoFeed](https://neofeed.com.br/economia/itau-ve-fim-do-ciclo-de-cortes-da-selic-diante-de-cenario-mais-adverso/)), e a previsão geral é de parada, embora a tabela de eventos do InfoMoney traga **13,50%** ([InfoMoney](https://www.infomoney.com.br/mercados/calendario-economico-da-semana-copom-trabalho-e-eleicoes-nos-eua-sao-destaques/)).

→ **Petrobras**: querosene de aviação **+7,2%** (+R$ 0,45 por litro) desde domingo (01/11), depois de **+11,8%** em outubro; é o combustível dos aviões ([Estadão](https://www.estadao.com.br/economia/petrobras-aumenta-preco-do-querosene-de-aviacao-em-72-a-partir-deste-domingo/)).

→ **Binance**: depois de suspender os saques pelo ataque hacker, reabriu e teve saída líquida de ~**US$ 3,64 bi** entre a manhã e o começo da tarde de domingo (01/11), **2,1%** dos ativos, segundo a própria Binance ([Estadão](https://www.estadao.com.br/economia/binance-registra-retiradas-liquidas-de-us-364-bilhoes-apos-retomada-de-saques/)).

**🌎 Lá fora**

→ **Opep+**: manteve as metas de produção para dezembro (01/11); o Brent fechou perto de **US$ 118** na sexta (30/10), o maior nível desde abril ([Folha](https://www1.folha.uol.com.br/mercado/2026/11/opep-mantem-metas-de-producao-de-petroleo-para-dezembro-antes-de-decisao-sobre-2027.shtml)).

→ **Banco da Inglaterra**: decide na quinta (05/11), com a taxa em **3,75%** ([BoE](https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate)).

→ **China**: o PMI industrial RatingDog ficou em **52,0** em outubro, contra 52,1 em setembro, enquanto o oficial caiu de 50,1 para **49,3** (abaixo de 50 é contração) ([Valor](https://valor.globo.com/mundo/noticia/2026/11/01/pmi-industrial-da-ratingdog-da-china-recua-para-520-em-outubro.ghtml)); na agenda, as eleições de meio de mandato nos EUA, terça (03/11) ([InfoMoney](https://www.infomoney.com.br/mercados/calendario-economico-da-semana-copom-trabalho-e-eleicoes-nos-eua-sao-destaques/)).

---

#### 🇧🇷 BRASIL ADENTRO
→ **Chilli Beans**: pediu recuperação extrajudicial na sexta (30/10), com **R$ 340 mi** em dívidas ([NeoFeed](https://neofeed.com.br/negocios/com-dividas-de-r-340-milhoes-chilli-beans-entra-com-pedido-de-recuperacao-extrajudicial/)).

→ **Raízen**: as assembleias de acionistas de 30/10 aprovaram dividir a empresa em duas listadas (distribuição com a marca Shell; açúcar, etanol e bioenergia); o conselho vota o aumento de capital de até **R$ 39,8 bi** em 06/11 ([InvestNews](https://investnews.com.br/negocios/raizen-assembleia-credores-outubro26/)).

→ **99**: segundo o diretor-geral no Brasil, Simeng Wang, a maioria das operações de delivery com mais de um ano já é rentável, sem números ([Estadão](https://www.estadao.com.br/economia/coluna-da-broad/maioria-das-operacoes-de-delivery-da-99-com-mais-de-um-ano-e-rentavel-diz-executivo/)).

→ **Itaú**: compra a NeoSpace por **R$ 2,925 bi**, sujeito a Cade e Banco Central; em janeiro de 2025 pagou US$ 15 mi por **15%** ([Bloomberg Línea](https://www.bloomberglinea.com.br/startups/rodadas-da-semana-kalshi-capta-us-1-bilhao-e-chega-a-us-40-bi-de-valuation/)).

#### 🌎 MUNDO AFORA
→ **Toast**: a FTC, oito estados e dois governos locais da Califórnia processam o sistema para restaurantes por taxa escondida de **US$ 0,99** em pedidos online acima de US$ 10 (de 2021 a 2023) e por cancelamento difícil; a Toast "discorda fortemente" ([PPC Land](https://ppc.land/affle-agrees-to-buy-perion-for-420m-as-ftc-sues-toast-over-fees/)).

→ **Apple**: corta a comissão da App Store em Taiwan de **30%** para **26%**; segundo a autoridade de concorrência de Taiwan, iguala Japão e Brasil ([PPC Land](https://ppc.land/apple-cuts-taiwan-app-store-commission-to-26-after-antitrust-probe/)).

→ **Shopify**: em prévia por convite para desenvolvedores nos EUA, deixa a loja pagar comissão à empresa do agente de compras de IA, base de **0,3%** do pedido, detalhes ainda "not final" ([Search Engine Journal](https://www.searchenginejournal.com/shopify-now-lets-stores-pay-the-company-behind-your-ai-shopping-agent/594544/)).

→ **ChatGPT Ads**: desde sexta (30/10), os ajustes automáticos de anúncio vêm ligados por padrão e podem reescrever título, traduzir e trocar a URL de destino sem aprovação; dá para desligar ([Search Engine Journal](https://www.searchenginejournal.com/chatgpt-ads-turns-on-automatic-ad-changes-by-default/595117/)).

---

#### 📊 STATS
## "Algumas centenas"
> **TL;DR:** os agentes de IA de fora trouxeram só "several hundred orders" à DoorDash desde que entraram no ar, contra **993 milhões** de pedidos só no 3º tri.

Tony Xu, CEO, disse isso na teleconferência de 29/10 ([transcrição](https://www.fool.com/earnings/call-transcripts/2026/10/29/doordash-dash-q3-2026-earnings-call-transcript/), [Ars Technica](https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/)).

O contraponto vem da Microsoft: o evento "checkout" aparece em **25,21%** das sessões de agentes contra **14,65%** das humanas ([Clarity](https://clarity.microsoft.com/blog/agentic-analytics-what-agents-do-on-websites/)). Mas é evento de página: o próprio Clarity diz que não prova que o agente concluiu a compra.

**Opinião:** conector em beta (menos de um mês) » pedido simples vai direto ao app » agente fica para a compra pensada » quem vende "venda por agente" hoje vende promessa.

---

**Para ler, ouvir ou assistir:**
- [Para ler] [The AI cost of JavaScript frameworks](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/), de Nolan Lawson (28/10): o mesmo app em 12 frameworks; o custo por execução vai de US$ 2,67 a US$ 4,97.
- [Para ouvir] [Lenny's Podcast com Hector Serrano](https://www.lennysnewsletter.com/p/how-a-19-year-old-intern-built-the), da Wispr Flow (1h27): cerca de 50 criadores fazem 500 a 600 anúncios UGC (conteúdo feito por criador, não pela marca) por mês.
- [Curiosidade] [HackerTube](https://karpathy.bearblog.dev/hacker-tube/), de Andrej Karpathy: 6.454 vídeos recomendados no Hacker News, feito com o Claude em ~2 horas, segundo ele.

---

**Pergunta do dia:** no seu trabalho, quanto do que você entrega você realmente conferiu?
