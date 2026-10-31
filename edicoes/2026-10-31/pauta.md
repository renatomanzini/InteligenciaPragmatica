# Pauta — 2026-10-31 (sábado, nº 13)

Início: 04:38 (Brasília). Tipo: `sabado` (semana em revista). MARKETING: não (sábado).
Coleta: 563 candidatos de 63 fontes (2 falharam). Coleta funcionou.

## Veredito do dia
**Morno.** Nenhum breakthrough provável: o Gemini 4 Carbon (28/10) saiu só para um grupo restrito de defensores de cibersegurança (já noticiado em 29/10); GPT-6.1 Terra e Genie 4 a conferir na apuração (preço/disponibilidade). Na dúvida, não marca.

## O que entra
- **Breakthroughs da semana:** provável "nenhum esta semana, e tudo bem", com o "não passou" mais relevante (GPT-6.1 Terra ou Genie 4), a depender da apuração.
- **Histórias em andamento:** Binance (20 min, Coreia do Norte); Anthropic IPO (nota "junk" prevista, FT); OpenAI rodada (menos da metade dos US$ 30 bi, WSJ); Google Modo IA x tráfego (Reddit, CTR 0,9%); bolsa brasileira (pior semana desde 2020) – só números, sem política eleitoral; Raízen (credores viram sócios); Kimi pesos (prazo 4/11); Meta termos (20/11). Nova: extensão do Claude Code no marketplace do Cursor com backdoor (o leitor usa Claude Code).
- **Números da semana:** desemprego 5,2% (IBGE), DoorDash "algumas centenas" de pedidos por agentes, Microsoft ~11% da receita vinda da OpenAI, Kalshi US$ 40 bi, Fujifilm 5x fitas.
- **IA na prática da semana:** o novo sinal compartilhado no robots.txt para recusar treino de IA (OpenAI, Google, Microsoft, Anthropic). Útil direto para quem faz site de cliente; tem ângulo jurídico (opt-out da diretiva europeia) e vira serviço.
- **Links:** nesformer (NES dentro de pesos de modelo), "AI isn't replacing SREs, it's deskilling them", OpenAI "The future of the firm" ou Wikimedia x direito autoral.

## O que ficou de fora e por quê
- Raízen transação tributária e Anúncios no Modo IA em novos mercados: JÁ COBERTO (só entram se houver fato novo).
- Eleição, Flávio Bolsonaro, PEC da Segurança: política sem efeito direto em negócios (manual, seção 12). A queda da bolsa entra só com números.
- Halloween, loterias, filmes, Patrick Stewart: fora da pauta.
- Mistral Large 4, LFM3: já saíram (28 e 30/10).

## Veredito de breakthrough (após apuração)
**Nenhum.** Gemini 4 Carbon e Genie 4: só para grupos restritos. GPT-6.1 Terra: modelo intermediário, US$ 1/US$ 5 por milhão de tokens (PARCIAL), não é queda de 10x. A tese do Simon Willison sobre jogos feitos por IA é de um blogueiro só, com exemplos dele. `breakthrough: false`.

## Plano de redação
Estrutura de sábado (manual, seção 4). Alvo total: **1.300 a 1.700 palavras** (6 a 8 min). Fio da edição: **semana de tombos** (bolsa, Binance, tráfego do Reddit) e, no meio do barulho, um pedido de licença: o site agora pode dizer "não treine com isto", mas só a partir de 2027. Humor seco só nas partes de tecnologia; **nenhum humor** na bolsa (perda de dinheiro de gente) nem no roubo.

### 1. bom dia (1 frase, ~35 palavras)
"bom dia." em minúsculas e uma frase: semana em que a bolsa teve a pior semana desde 2020, uma corretora perdeu US$ 6,3 bi em ~20 minutos e as big techs combinaram como pedir licença antes de treinar IA com o seu site. Sem número em negrito aqui é ok.

### 2. #### 🚨 OS BREAKTHROUGHS DA SEMANA (~200 palavras)
- "Nenhum esta semana, e tudo bem." + o critério em uma frase.
- **Não passou no critério:** 
  - Gemini 4 Carbon (28/10): só para um grupo de defensores de cibersegurança; preço anunciado de **US$ 2** (entrada) e **US$ 10** (saída) por milhão de tokens no período introdutório, depois **US$ 4/US$ 20**; sem data para o público. Link: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ (CONFIRMADO).
  - Genie 4 (27/10): modelo de mundo (explique: gera um ambiente interativo que você controla pelo teclado, como um videogame inventado na hora); prévia só para testadores; link https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/ (CONFIRMADO).
  - GPT-6.1 Terra: intermediário, **US$ 1/US$ 5**, segundo o Simon Willison (PARCIAL → escreva "segundo Simon Willison"); cerca de metade do Sol. Link: https://simonwillison.net/2026/Oct/26/gpt-61-terra/
- **O mais perto:** a tese de Simon Willison (28/10) de que, em outubro, a IA passou a fazer jogos que são divertidos de jogar, e o difícil virou o design. Citação curta permitida: "Building games that play well is shockingly easy now." Freio: é a opinião de um blogueiro, com exemplos dele mesmo. Link: https://simonwillison.net/2026/Oct/28/vibe-game-development/
- **Opinião:** (1–2 linhas) um modelo de fronteira que você não pode usar não muda o seu dia; a gente volta quando abrir.
- Fechar com: *Transparência: esta newsletter é escrita com modelos da Anthropic.* (há itens da Anthropic na edição)

### 3. #### O QUE MUDOU NAS HISTÓRIAS EM ANDAMENTO (~550 palavras, linhas `→` com data)
Ordem e conteúdo (uma linha `→` cada, de 1 a 3 frases, sempre com data e link):
1. **Novo, e é com você (extensão do Claude Code)**: em 29/10, por cerca de **11 horas**, a versão 2.1.313 da extensão "Claude Code for VS Code" distribuída no marketplace do Cursor veio com código malicioso que instalava uma chave SSH do atacante (acesso remoto à máquina) e mandava dados como usuário, e-mail do Git e os **nomes** (não os valores) de variáveis com KEY/TOKEN/SECRET. O Cursor fala em no máximo **5.000** usuários (teto, não contagem). A Anthropic diz que não fez nem publicou essa versão; a 2.1.314 é limpa, mas atualizar **não** remove o que já foi instalado. Quem baixou a 2.1.313 procura a chave "svc-telemetry" no authorized_keys. Links: https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/ ; https://www.bankinfosecurity.com/cursor-confirms-anthropic-claude-code-extension-compromised-a-33263 . Tom: sério, prático. Não afirme nada sobre o marketplace oficial do VS Code (não apurado).
2. **Bolsa**: Ibovespa caiu **18,12%** na semana, a pior desde março de 2020, e fechou a sexta (30/10) a **167.922** pontos; na segunda (26/10), **−14%** com circuit breaker (explique: pausa automática do pregão). É a 4ª maior queda semanal do século; a maior foi a de 10/10/2008 (**−20,01%**). Dólar a **R$ 5,44**, **+9%** na semana. Fundos perderam **R$ 157,5 bi** de patrimônio do dia seguinte à eleição até 28/10 (Economática). Itaú corta o PIB de 2027 de 1,2% para **0,5%** e sobe o IPCA para **6,1%**, acima do teto de 4,5%. Links: InvestNews, InfoMoney, Folha (fundos), Folha (Itaú) — URLs exatas no apuracao.md, bloco C item 5. Sem política eleitoral (só "depois da eleição" como marco de data). Sem recomendação de investimento. Pode usar a cadeia `»` aqui (a única da edição): dólar alto » combustível e importados mais caros » inflação de 2027 acima do teto » Selic parada em 13,75% (projeção do Itaú).
3. **Binance**: o que mudou desde 30/10: a maior parte saiu em ~**20 minutos**, depois de ao menos 36 horas de preparação (TRM Labs, via Wired); TRM e Chainalysis apontam o grupo norte-coreano TraderTraitor, e a Elliptic acha "provável" a Coreia do Norte, mas nem a Binance nem governos atribuíram; **US$ 2,8 bi** (44%) congelados, quase tudo stablecoin, e **US$ 3,3 bi** em Bitcoin, Ether e XRP sem como congelar; a Binance agora diz que o notebook não explica tudo ("pontos adicionais de violação"). Links: Wired, Estadão.
4. **Anthropic**: depois do S-1 (26/10), o FT diz que a Blackstone espera nota "alto junk" (o topo do grau especulativo) para a dívida da empresa depois do IPO, segundo a TechCrunch; explique o "junk" (nota que diz "risco maior, juro maior"). Anthropic e Blackstone não comentaram. Link: TechCrunch (bloco C item 2). Não cite "BB" nem "US$ 63 bi" (PARCIAL).
5. **OpenAI**: o WSJ diz que a rodada levantou menos da metade da meta de **US$ 30 bi**, a **US$ 1,25 tri** de valuation, abaixo dos US$ 1,4 tri buscados antes. Desde 23/10 (quando a gente falou de US$ 30 bi a US$ 1,25 tri). Link: WSJ. Não cite valor exato.
6. **Google, Reddit e o clique**: o Reddit diz que, em outubro, perdeu em média **mais de 1 milhão** de visitas por semana vindas da busca e que os usuários diários (130,3 mi) podem cair "dois dígitos baixos" no 4º tri; na teleconferência, Steve Huffman apontou as AI Overviews e o AI Mode como hipótese principal. Vai testar login obrigatório fora dos EUA nos próximos meses. E um estudo de caso de um site só (Cyrus Shepard) estima ~**0,9%** de cliques nas respostas de IA. Links: ppc.land (2), SEJ, seroundtable (CTR). Freio: um site só.
7. **Raízen**: em 30/10, credores aprovaram a recuperação extrajudicial: passivo de **R$ 65 bi**, credores ficam com ~**80%** do capital, Shell com 13% a 15% e aporte de R$ 3,5 bi; a empresa se divide em duas (Energia e Combustíveis) a partir da 2ª quinzena de dezembro. O que mudou desde 30/10 (acordo tributário). Link: NeoFeed.
8. **Kimi e Meta (prazos à vista)**: em uma linha: os pesos do Kimi K3.1 Pro ainda não estavam no Hugging Face da Moonshot em 31/10 (prazo: 4/11); os termos comerciais da Meta seguem para 20/11, sem mudança. Links: https://huggingface.co/moonshotai ; ppc.land Meta.

### 4. #### 📊 OS NÚMEROS DA SEMANA (~220 palavras; 5 linhas `→` com escala)
- **5,2%**: desemprego no trimestre até setembro (IBGE, divulgado 30/10), o menor para esse trimestre desde 2012; 5,6% um ano antes; FGV e Inter já veem perda de fôlego (Estadão). Escrever "menor para o período", nunca "menor da série".
- **"Algumas centenas"**: pedidos feitos por agentes de IA de terceiros na DoorDash, segundo o CEO Tony Xu, contra **993 milhões** de pedidos só no 3º tri (TechCrunch + release na SEC). Ressalva: "no total", sem período.
- **~11%**: fatia da receita trimestral da Microsoft (US$ 10 bi de US$ 92,3 bi, trimestre até 30/09) que vem de acordos com a OpenAI (Startups.com.br). Não citar "10-Q".
- **US$ 40 bi**: valuation da Kalshi (mercado de apostas em eventos), +82% desde maio (US$ 22 bi) e quase o dobro da Polymarket (US$ 21 bi) (Folha/NYT).
- **5 vezes**: a capacidade de fitas magnéticas LTO que a Fujifilm quer ter até o ano fiscal de 2028, com ~¥10 bi (~US$ 63 mi), por causa da IA (Ars Technica). Analogia curta possível: guardar dado em fita, como nos anos 90.

### 5. #### 🧠 IA NA PRÁTICA DA SEMANA (~400 palavras)
- `## ` Título-tese: "Seu site agora pode dizer 'não treine com isto' (a partir de 2027)" ou parecido. `> **TL;DR:**` obrigatório (o montador cobra TL;DR de todo `##`).
- **Conceito + analogia:** o robots.txt é a placa na porta do site que diz aos robôs onde podem entrar; vale por educação, não por fechadura. A novidade é uma placa só, comum a várias empresas, para "não use para treinar IA".
- **O caso:** em 30/10 o Google (John Mueller) anunciou que vai suportar um controle novo, baseado no grupo AIPREF do IETF (explicar: entidade que padroniza a internet), e mira **2027**; é rascunho, não padrão final. A linha é `user-agent: __usage_ai-training` com um Disallow (segundo Search Engine Roundtable e PPC Land; o post do Google não escreve a linha). Se o site recusar treino por ela e não falar do Google-Extended, o Google trata como Google-Extended bloqueado. O Bing (30/10) separou treino de "grounding" (usar sua página para montar uma resposta com citação): dá para recusar treino e continuar citado no Copilot, e o ranking normal não muda; passa a valer em **01/02/2027**. OpenAI e Anthropic também aderem, segundo Search Engine Roundtable e PPC Land (PARCIAL → atribuir). Links: https://developers.google.com/search/blog/2026/10/ai-training-control ; https://www.seroundtable.com/microsoft-bing-ai-controls-42429.html ; https://ppc.land/google-and-bing-back-one-robots-txt-rule-to-opt-out-of-ai-training/ (cada um com 🔗 em linha própria ou inline).
- **⚠️ Freio de realidade:** ainda não vale (Google em 2027, Bing em fev/2027); é rascunho e pode mudar; robots.txt é pedido, não fechadura (análise, sem atribuir); não se sabe o efeito sobre AI Overviews na busca do Google (não afirmar); Nate Hake, editor que participou do grupo, diz que o trabalho está incompleto (segundo o PPC Land). Meta não aparece entre os adotantes nas fontes lidas — **não** escrever isso como fato; omitir.
- ⚖️ 1–2 linhas: na UE, a Diretiva 2019/790, art. 4(3), só libera a mineração de texto e dados se o titular não reservou o direito "por meios legíveis por máquina" em conteúdo online; um sinal padronizado dá forma a essa reserva. Link oficial: https://eur-lex.europa.eu/eli/dir/2019/790/oj . Não citar lei brasileira.
- **Agora aplica no mundo real** (3 linhas): advogado/escritório (blog com artigos próprios: decidir se quer treino, sem sair das citações); dono de e-commerce/loja (descrições de produto: talvez queira ser citado, não treinado); jornalista ou criador de conteúdo/ professor com material autoral.
- **Como isso vira serviço:** "política de IA do site": auditar o robots.txt dos clientes, explicar a diferença entre treino e citação, escrever a decisão do cliente e deixar a configuração pronta (Google-Extended e controles do Bing hoje, o token novo quando valer). Para quem: escritórios, clínicas, blogs de nicho. Por que agora: prazos do Bing (15/12 controles temporários; 01/03/2027 migração). **Opinião:** é serviço pequeno, de entrada, que puxa a manutenção do site.
- **Para testar hoje (15 min):** abra seusite.com/robots.txt e veja se cita Google-Extended ou GPTBot; anote o que está permitido.

### 6. **Para ler no fim de semana:** (3 links, ~110 palavras)
- [Para ler] "AI Isn't Replacing SREs. It's Deskilling Them." (SigNoz, 28/02/2026), https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling : quando a IA resolve 95% dos incidentes, o humano piora nos 5% que importam (Willison já está no bloco 2).
- [Para ler] The Verge (Lauren Feiner, 30/10): a Wikimedia diz em amicus brief que treinar IA deve ser fair use, mas regurgitar artigos não — liga com o IA na prática. Avisar "pode ter paywall".
- [Curiosidade] nesformer: Drew Breunig pôs a CPU do NES dentro dos pesos do Qwen3.5-4B; roda Super Mario "muito devagar"; repo criado em 30/10 com 194 estrelas. Links: simonwillison.net/2026/Oct/30/nesformer/ e github.com/dbreunig/nesformer. Não citar "1 GB".

### 7. **Pergunta da semana:** (1 linha)
Algo como: "se o seu trabalho publicado na internet pudesse escolher entre treinar uma IA e ser citado por ela, qual das duas você escolheria?"

### Assunto, prévia e front matter
- **assunto:** "semana de tombos: bolsa, binance e o clique" (7 palavras, minúsculas).
- **prévia:** "+ como dizer à ia que ela não treina com seu site"
- **front matter:**
```yaml
data: 2026-10-31
tipo: sabado
numero: 13
assunto: "semana de tombos: bolsa, binance e o clique"
previa: "+ como dizer à ia que ela não treina com seu site"
tempo_leitura_min: (palavras ÷ 220)
dia: morno
breakthrough: false   # Gemini 4 Carbon e Genie 4 restritos; GPT-6.1 Terra não barateia 10x
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
    titulo: "Google, Bing, OpenAI e Anthropic apoiam sinal único no robots.txt para recusar treino de IA, a partir de 2027"
    tema: direito_tech
    urls: ["https://developers.google.com/search/blog/2026/10/ai-training-control"]
    em_andamento: true
  - id: gemini-4-carbon
    titulo: "Gemini 4 Carbon tem preço anunciado, mas segue restrito"
    tema: ia
    urls: ["https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/"]
    em_andamento: false
formatos: [semana_em_revista, breakthroughs, historias_em_andamento, numeros, ia_na_pratica, links, pergunta]
```
