---
data: 2026-10-31
tipo: sabado
numero: 13
assunto: "semana de tombos: bolsa, binance e o clique"
previa: "+ como dizer à ia que ela não treina com seu site"
tempo_leitura_min: 8
dia: morno
breakthrough: false
historias:
  - id: claude-code-extensao-cursor
    titulo: "Extensão do Claude Code no marketplace do Cursor sai com backdoor por cerca de 11 horas"
    tema: ia
    urls: ["https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/"]
    em_andamento: true
  - id: ibovespa-pos-eleicao
    titulo: "Ibovespa cai 18,12% na semana, a pior desde março de 2020"
    tema: economia
    urls: ["https://investnews.com.br/investimentos/ibovespa-afunda-18-e-tem-pior-semana-desde-2020-dolar-salta-9/"]
    em_andamento: true
  - id: binance-ataque-2026
    titulo: "Ataque à Binance levou ~20 minutos; empresas de análise apontam a Coreia do Norte"
    tema: economia
    urls: ["https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/"]
    em_andamento: true
  - id: anthropic-receita-ipo
    titulo: "Blackstone espera nota 'junk' alta para a Anthropic depois do IPO, segundo o FT"
    tema: ia
    urls: ["https://techcrunch.com/2026/10/30/anthropic-expected-to-receive-high-junk-rating-from-credit-agencies-following-ipo-report-says/"]
    em_andamento: true
  - id: openai-rodada-ipo
    titulo: "OpenAI levanta menos da metade da meta de US$ 30 bi, segundo o WSJ"
    tema: negocios
    urls: ["https://www.wsj.com/tech/ai/openai-raises-less-than-half-of-30-billion-target-in-latest-round-91aecdc5"]
    em_andamento: true
  - id: reddit-login
    titulo: "Reddit perde mais de 1 milhão de visitas da busca por semana e aponta a IA do Google"
    tema: negocios
    urls: ["https://ppc.land/reddit-ad-revenue-gains-54-to-847m-as-daily-users-stall-at-130-3m/"]
    em_andamento: true
  - id: raizen-transacao-tributaria
    titulo: "Credores aprovam a recuperação da Raízen e ficam com ~80% do capital"
    tema: negocios
    urls: ["https://neofeed.com.br/negocios/credores-viram-socios-na-raizen-e-abrem-caminho-para-fim-de-maior-recuperacao-extrajudicial-do-brasil/"]
    em_andamento: true
  - id: kimi-k3-1-pro
    titulo: "Pesos do Kimi K3.1 Pro ainda não saíram; prazo é 4/11"
    tema: china
    urls: ["https://huggingface.co/moonshotai"]
    em_andamento: true
  - id: robots-txt-treino-ia
    titulo: "Google e Bing apoiam sinal único no robots.txt para recusar treino de IA, a partir de 2027"
    tema: direito_tech
    urls: ["https://developers.google.com/search/blog/2026/10/ai-training-control"]
    em_andamento: true
  - id: gemini-4-carbon
    titulo: "Gemini 4 Carbon tem preço anunciado, mas segue restrito"
    tema: ia
    urls: ["https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/"]
    em_andamento: false
formatos: [semana_em_revista, breakthroughs, historias_em_andamento, numeros, ia_na_pratica, links, pergunta]
---
bom dia. Foi a semana em que a bolsa teve a maior queda desde 2020, uma corretora de cripto perdeu US$ 6,3 bi, a maior parte em cerca de 20 minutos, e Google e Bing anunciaram como o seu site vai poder recusar o treino de IA.

---

#### 🚨 OS BREAKTHROUGHS DA SEMANA

Nenhum esta semana, e tudo bem. O critério é simples: só conta o que muda o que uma pessoa comum consegue fazer, ou quanto custa fazer.

**Não passou no critério:**

- **Gemini 4 Carbon** (28/10): só para um grupo de defensores de cibersegurança, sem data para o público. O preço anunciado é de **US$ 2** por milhão de tokens de entrada e **US$ 10** de saída no período introdutório, depois **US$ 4** e **US$ 20** ([Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)).
- **Genie 4** (27/10): um modelo de mundo, que gera um ambiente interativo que você controla pelo teclado, como um videogame inventado na hora. A prévia é só para testadores ([DeepMind](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)).
- **GPT-6.1 Terra**: modelo intermediário, a **US$ 1** de entrada e **US$ 5** de saída por milhão de tokens, segundo Simon Willison, cerca de metade do preço do Sol. Pelo critério, metade do preço não é uma queda de 10 vezes ([Willison](https://simonwillison.net/2026/Oct/26/gpt-61-terra/)).

**O mais perto:** a tese de Simon Willison (28/10) de que, em outubro, a IA passou a fazer jogos que são divertidos de jogar, e o difícil virou o design. Nas palavras dele: "Building games that play well is shockingly easy now." O freio: é a opinião de um blogueiro, com exemplos dele mesmo ([Willison](https://simonwillison.net/2026/Oct/28/vibe-game-development/)).

**Opinião:** um modelo de fronteira que você não pode usar não muda o seu dia. A gente volta quando abrir.

*Transparência: esta newsletter é escrita com modelos da Anthropic.*

---

#### O QUE MUDOU NAS HISTÓRIAS EM ANDAMENTO

→ **Novo, e é com você (extensão do Claude Code)**: em 29/10, por cerca de **11 horas**, a versão 2.1.313 da extensão "Claude Code for VS Code", distribuída no marketplace do Cursor, veio com código malicioso. Ele instalava uma chave SSH do atacante (acesso remoto à máquina) e enviava usuário, e-mail do Git e os **nomes** (não os valores) de variáveis com KEY, TOKEN ou SECRET. O Cursor fala em no máximo **5.000** usuários, um teto, não uma contagem. A Anthropic diz que não fez nem publicou essa versão. A 2.1.314 é limpa, mas atualizar **não** remove o que já foi instalado: quem baixou a 2.1.313 deve procurar a chave "svc-telemetry" no arquivo authorized_keys e, se achar, isolar a máquina e trocar os segredos ([BleepingComputer](https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/); [BankInfoSecurity](https://www.bankinfosecurity.com/cursor-confirms-anthropic-claude-code-extension-compromised-a-33263)).

→ **Bolsa**: o Ibovespa caiu **18,12%** na semana, a pior desde março de 2020, e fechou a sexta (30/10) a **167.922** pontos. Na segunda (26/10), a queda foi de **14%**, com circuit breaker, a pausa automática do pregão. É a 4ª maior queda semanal do século, empatada com uma de 2001; a maior foi a de 10/10/2008 (**−20,01%**) ([InvestNews](https://investnews.com.br/investimentos/ibovespa-afunda-18-e-tem-pior-semana-desde-2020-dolar-salta-9/); [InfoMoney](https://www.infomoney.com.br/mercados/maiores-quedas-semanais-ibovespa-2008-covid-11-setembro-eleicao/)). O dólar fechou a **R$ 5,44**, alta de **9%** na semana. Os fundos perderam **R$ 157,5 bi** de patrimônio do dia seguinte à eleição até 28/10, segundo a Economática ([Folha](https://c-level.folha.uol.com.br/financas/2026/10/fundos-de-investimento-perdem-r-1575-bilhoes-apos-reeleicao-de-lula.shtml)). O Itaú cortou a projeção do PIB de 2027 de 1,2% para **0,5%** e subiu a do IPCA de 4,6% para **6,1%**, acima do teto da meta (4,5%) ([Folha](https://www1.folha.uol.com.br/mercado/2026/10/itau-corta-projecao-do-pib-de-2027-para-05-e-ve-inflacao-acima-da-meta.shtml)). Na conta do banco: dólar mais caro e mais imposto sobre combustível » inflação de 2027 acima do teto » Selic parada em 13,75% em todo 2027.

→ **Binance**: o que mudou desde a primeira notícia (29/10) é o desenho do ataque. A maior parte saiu em cerca de **20 minutos**, depois de ao menos 36 horas de preparação, segundo a TRM Labs ([Wired](https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/)). TRM e Chainalysis dizem que o grupo norte-coreano TraderTraitor pode estar por trás, e a Elliptic considera provável que seja a Coreia do Norte, mas nem a Binance nem governos atribuíram o ataque. Foram congelados **US$ 2,8 bi** (44%), quase tudo em stablecoins, e **US$ 3,3 bi**, a maior parte em Bitcoin, Ether e XRP, não têm como ser congelados. A Binance, que diz que cobrirá todas as perdas, agora admite ter achado outros pontos de invasão, além do notebook comprometido ([Wired](https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/); [Estadão](https://www.estadao.com.br/economia/hackers-ligados-a-coreia-do-norte-sao-apontados-como-responsaveis-por-ataque-bilionario-a-binance-npr/)).

→ **Anthropic**: depois do S-1 de 26/10, o documento de abertura de capital na SEC ([Anthropic](https://www.anthropic.com/news/s1-sec)), o FT diz que a Blackstone espera nota "alto junk" para a dívida da empresa depois do IPO. "Junk" é a nota que diz "risco maior, juro maior". Anthropic e Blackstone não comentaram ([TechCrunch](https://techcrunch.com/2026/10/30/anthropic-expected-to-receive-high-junk-rating-from-credit-agencies-following-ipo-report-says/)).

→ **OpenAI**: o WSJ diz que a rodada levantou menos da metade da meta de **US$ 30 bi**, a **US$ 1,25 tri** de valuation, abaixo dos US$ 1,4 tri buscados antes. É o que mudou desde 23/10, quando a gente falou de US$ 30 bi a US$ 1,25 tri ([WSJ](https://www.wsj.com/tech/ai/openai-raises-less-than-half-of-30-billion-target-in-latest-round-91aecdc5)).

→ **Google, Reddit e o clique**: o Reddit diz que, em outubro, perdeu em média mais de **1 milhão** de visitas por semana vindas da busca, e que os usuários diários (130,3 mi) podem cair na casa de 10% ou pouco mais no 4º trimestre, se o ritmo continuar ([PPC Land](https://ppc.land/reddit-ad-revenue-gains-54-to-847m-as-daily-users-stall-at-130-3m/)). Na teleconferência, o CEO Steve Huffman apontou as AI Overviews e o AI Mode como hipótese principal ([Search Engine Journal](https://www.searchenginejournal.com/reddit-to-test-login-only-mode-as-google-search-traffic-drops/595270/)). O Reddit vai testar login obrigatório fora dos EUA nos próximos meses ([PPC Land](https://ppc.land/reddit-plans-to-make-logins-the-norm-after-20-years-of-open-browsing/)). Um estudo de caso de Cyrus Shepard estima cerca de **0,9%** de cliques nas respostas de IA, mas é de um site só ([Search Engine Roundtable](https://www.seroundtable.com/google-ai-overviews-mode-ctr-42421.html)).

→ **Raízen**: em 30/10, credores aprovaram a recuperação extrajudicial. O passivo é de **R$ 65 bi**, os credores ficam com cerca de **80%** do capital, a Shell com 13% a 15% e faz um aporte de R$ 3,5 bi. A empresa se divide em Energia e Combustíveis: a cisão sai na 2ª quinzena de dezembro, e as duas operam a partir de meados de janeiro de 2027 ([NeoFeed](https://neofeed.com.br/negocios/credores-viram-socios-na-raizen-e-abrem-caminho-para-fim-de-maior-recuperacao-extrajudicial-do-brasil/)).

→ **Kimi e Meta**: os pesos do Kimi K3.1 Pro ainda não estavam no Hugging Face da Moonshot em 31/10, e o prazo prometido pela Moonshot é 4/11 ([Hugging Face](https://huggingface.co/moonshotai); [Moonshot](https://www.kimi.ai/blog/kimi-k3-1-pro)). Os novos termos comerciais da Meta seguem marcados para 20/11, data anunciada em 23/10 ([PPC Land](https://ppc.land/meta-delays-website-crawling-terms-to-nov-20-after-publisher-complaints/)).

---

#### 📊 OS NÚMEROS DA SEMANA

→ **5,2%**: o desemprego no trimestre até setembro (IBGE, divulgado em 30/10), o menor para esse trimestre desde 2012, contra 5,6% um ano antes. FGV e Inter já veem perda de fôlego ([Estadão](https://www.estadao.com.br/economia/ibge-pnad-desemprego-setembro-2026/)).

→ **"Algumas centenas"**: os pedidos feitos por agentes de IA de terceiros na DoorDash, segundo o CEO Tony Xu, no total e sem período definido, contra **993 milhões** de pedidos só no 3º trimestre ([TechCrunch](https://techcrunch.com/2026/10/30/doordash-said-its-only-received-several-hundred-orders-from-ai-agents/); [SEC](https://www.sec.gov/Archives/edgar/data/0001792789/000179278926000062/proddashex991-pressrelease.htm)).

→ **~11%**: a fatia da receita trimestral da Microsoft que vem de acordos com a OpenAI, US$ 10 bi de US$ 92,3 bi no trimestre até 30/09. Não se sabe quanto é repasse e quanto é Azure ([Startups](https://startups.com.br/negocios/big-techs/microsoft-tem-quase-11-da-receita-trimestral-vinda-da-openai/)).

→ **US$ 40 bi**: o valuation da Kalshi, mercado de apostas em eventos, alta de 82% desde maio (US$ 22 bi) e quase o dobro da Polymarket (US$ 21 bi) ([Folha](https://c-level.folha.uol.com.br/negocios/2026/10/kalshi-e-avaliada-em-us-40-bilhoes-e-se-aproxima-de-possivel-ipo.shtml)).

→ **5 vezes**: a capacidade de produção de fitas magnéticas LTO que a Fujifilm quer ter, em relação ao ano fiscal de 2025, com um investimento de cerca de ¥10 bi (~US$ 63 mi) entre 2026 e 2028, porque a IA generativa aumentou a demanda por arquivar dados ([Ars Technica](https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/)).

---

#### 🧠 IA NA PRÁTICA DA SEMANA
## Seu site agora pode dizer "não treine com isto" (a partir de 2027)
> **TL;DR:** Google e Bing apoiam um sinal único no robots.txt para recusar treino de IA, mas ele ainda não vale: o Google mira 2027 e o Bing começa em 01/02/2027.

O robots.txt é a placa na porta do site que diz aos robôs onde podem entrar. Vale por educação, não por fechadura. A novidade é uma placa só, comum a várias empresas, que diz "não use para treinar IA".

Em 30/10, o Google (John Mueller) anunciou que vai suportar um controle novo, baseado no grupo AIPREF do IETF, a entidade que padroniza a internet. A meta é 2027, e é rascunho, não padrão final. Segundo o PPC Land, a linha é `user-agent: __usage_ai-training` com um Disallow embaixo; o post do Google não a escreve. Se o site recusar treino por ela e não mencionar o Google-Extended, o Google pretende tratar como se o Google-Extended estivesse bloqueado.

O Bing separou treino de "grounding", que é usar a sua página para montar uma resposta com citação. Dá para recusar treino e continuar citado no Copilot, e o ranking normal do Bing não muda. Passa a valer em **01/02/2027**. OpenAI e Anthropic também aderem, segundo o [Search Engine Roundtable](https://www.seroundtable.com/google-ai-training-control-42430.html).
🔗 [Google](https://developers.google.com/search/blog/2026/10/ai-training-control)
🔗 [Search Engine Roundtable](https://www.seroundtable.com/microsoft-bing-ai-controls-42429.html)
🔗 [PPC Land](https://ppc.land/google-and-bing-back-one-robots-txt-rule-to-opt-out-of-ai-training/)

⚠️ **Freio de realidade:** ainda não vale (Google em 2027, Bing em fevereiro de 2027) e o rascunho pode mudar. O robots.txt é um pedido, não uma tranca. Nate Hake, dono de site de conteúdo que participou do grupo, diz que o trabalho está incompleto, segundo o PPC Land. E o post do Google não diz o que muda nas AI Overviews da busca.

⚖️ Na União Europeia, a Diretiva 2019/790, art. 4(3), só libera a mineração de texto e dados se o titular não reservou o direito; em conteúdo público online, a reserva se faz por meios legíveis por máquina ([EUR-Lex](https://eur-lex.europa.eu/eli/dir/2019/790/oj)). **Opinião:** um sinal padronizado facilita provar essa reserva.

**Agora aplica no mundo real:**
- **Advogado ou escritório:** blog com artigos próprios, decidindo se quer treino, sem sair das citações.
- **Dono de e-commerce:** nas descrições de produto, talvez queira ser citado, não treinado.
- **Jornalista, criador ou professor:** material autoral que dá trabalho para fazer.

**Como isso vira serviço:** uma "política de IA do site". Audite o robots.txt dos clientes, explique a diferença entre treino e citação, escreva a decisão do cliente e deixe a configuração pronta (Google-Extended e controles do Bing hoje, o token novo quando valer). Para escritórios, clínicas e blogs de nicho. Por que agora: o Bing prevê controles temporários em 15/12 (para sites com NoArchive ou NoCache) e a migração das regras antigas até 01/03/2027. **Opinião:** é serviço pequeno, de entrada, que puxa a manutenção do site.

**Para testar hoje (15 minutos):** abra seusite.com/robots.txt, veja se cita Google-Extended ou GPTBot e anote o que está permitido.

---

**Para ler no fim de semana:**
- [Para ler] [AI Isn't Replacing SREs. It's Deskilling Them.](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) (SigNoz, 28/02/2026): a autora pergunta o que acontece com o engenheiro quando a IA resolve quase todos os incidentes: ele pode piorar justamente nos poucos que importam.
- [Para ler] [Wikimedia e o fair use](https://www.theverge.com/policy/1022880/wikipedia-openai-new-york-times-copyright): a The Verge (Lauren Feiner, 30/10) conta que a Wikimedia diz, em amicus brief, que treinar IA deve ser fair use, mas regurgitar artigos não. Liga com o IA na prática; pode ter paywall.
- [Curiosidade] [nesformer](https://simonwillison.net/2026/Oct/30/nesformer/): Drew Breunig pôs a CPU do NES dentro dos pesos do Qwen3.5-4B, e o Super Mario roda "very slowly". O [repositório](https://github.com/dbreunig/nesformer) foi criado em 30/10 e tinha 194 estrelas em 31/10.

---

**Pergunta da semana:** se o seu trabalho publicado na internet pudesse escolher entre treinar uma IA e ser citado por ela, qual das duas você escolheria?
