# Apuração — 2026-10-31

## Bloco A — breakthroughs da semana e incidente da extensão

A) GPT-6.1 Terra (OpenAI)
- Modelo "midrange", entre Luna (mais barato) e Sol (mais caro); OpenAI diz que combina raciocínio visual, uso de computador e escrita mais clara → https://simonwillison.net/2026/Oct/26/gpt-61-terra/ → CONFIRMADO (via Willison)
- API: US$ 1 entrada / US$ 5 saída por milhão de tokens; cerca de metade do preço do GPT-6.1 Sol e ~10x o do GPT-6 Luna → mesma URL → PARCIAL
- Disponível na API e no ChatGPT pago; grátis não confirmado → mesma URL → CONFIRMADO (API/pago)
- Página oficial OpenAI deu 403 → NÃO CONFIRMADO na fonte primária
- Breakthrough: NÃO passa.

B) Genie 4 (Google DeepMind), 27/10/2026
- Modelo de mundo para simulação interativa em tempo real; controle por teclado e texto; gera som ambiente, música e diálogos → https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/ → CONFIRMADO
- Acesso: prévia de pesquisa só para testadores confiáveis; "em breve" para assinantes do Google AI Ultra (Project Genie) e parceiros na Gemini API/AI Studio; lista de espera → mesma URL → CONFIRMADO
- Limitação: detalhes visuais e permanência de objetos derivam em sessões longas → CONFIRMADO
- Breakthrough: NÃO passa (não está disponível ao público).

C) Gemini 4 Carbon (28/10)
- Fonte primária: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
- Só para um subconjunto de defensores de cibersegurança; ampliação a parceiros pelo "Fairwind Program"; desenvolvedores, empresas e consumidores "assim que possível", sem data → CONFIRMADO
- Preço: US$ 2 entrada / US$ 10 saída por milhão de tokens no período introdutório, depois US$ 4 / US$ 20; fim do período não informado → CONFIRMADO
- 1º no Artificial Analysis Intelligence Index v5.0 (nota 59), segundo o Google → CONFIRMADO (dado do Google)
- Breakthrough: NÃO passa.

D) Extensão "Claude Code for VS Code" adulterada no marketplace do Cursor
- Versão maliciosa 2.1.313, distribuída em 29/10/2026 pelo marketplace do Cursor, de 02:27 a 13:35 (horário do Pacífico), cerca de 11 horas → https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/ e https://www.bankinfosecurity.com/cursor-confirms-anthropic-claude-code-extension-compromised-a-33263 → CONFIRMADO ("quase 12 horas" no título da Ars não foi verificado; usar "cerca de 11 horas")
- Afetados: no máximo 5.000 usuários, segundo o Cursor (teto, não contagem) → BankInfoSecurity → PARCIAL
- O que fazia: carregador JS de 66 linhas rodava ao carregar a extensão; adicionava chave SSH do atacante (nome "svc-telemetry"), tentava abrir túnel SSH reverso e criava persistência; enviava hostname, usuário, SO, e-mail do Git e nomes (não valores) de até 40 variáveis de ambiente com KEY/TOKEN/SECRET → BleepingComputer + BankInfoSecurity → CONFIRMADO
- Cursor: a versão não foi feita pela Anthropic; tirou o marketplace do ar, auditou, rotacionou chaves; aviso em 30/10 às 07:46 UTC; não explicou como o ataque ocorreu → BankInfoSecurity → CONFIRMADO
- Anthropic: "we were not involved with building, publishing or hosting this" (via BankInfoSecurity); lançou 2.1.314 limpa na noite de 29/10 → PARCIAL (imprensa)
- O que fazer: quem baixou a 2.1.313 deve procurar a chave "svc-telemetry" em authorized_keys; se houver, isolar, trocar segredos e reconstruir; atualizar para 2.1.314 NÃO remove o que já foi instalado (Kevin Beaumont) → CONFIRMADO (imprensa)

E) Anthropic News (24–31/10): 26/10 S-1 na SEC (https://www.anthropic.com/news/s1-sec); 27/10 progresso em desenvolvimento de fármacos; 27/10 parceria ampliada com a GSA; 28/10 AI for Science se expande. Nada sobre o incidente D.

F) Simon Willison, "The October inflection point for vibe game development" (28/10) → https://simonwillison.net/2026/Oct/28/vibe-game-development/ → CONFIRMADO
- Tese: em outubro de 2026 os modelos passaram a criar jogos divertidos de jogar, não só com cara de jogo; o difícil agora é o design. Citação: "Building games that play well is shockingly easy now."
- Exemplos: Tree Appreciator (um único prompt), Emberwick (RPG de ~15 min), Battle Drones, Pumpkin Farmer.
- Tese de um blogueiro, com exemplos dele mesmo; não é breakthrough pelo critério.

## Bloco B — IA na prática: o sinal de treino de IA no robots.txt

1. Sintaxe e padrão
- Linha `user-agent: __usage_ai-training` no robots.txt; um Disallow sob ela = recusar treino → https://www.seroundtable.com/google-ai-training-control-42430.html (Barry Schwartz, 30/10/2026) e https://ppc.land/google-and-bing-back-one-robots-txt-rule-to-opt-out-of-ai-training/ (31/10/2026) → CONFIRMADO em 2 fontes secundárias; o post do Google chama de "policy token" sem escrever a linha → PARCIAL quanto à fonte oficial
- Padroniza: grupo de trabalho AIPREF do IETF; Google: "based on work from the AIPREF working group" → https://developers.google.com/search/blog/2026/10/ai-training-control (John Mueller, 30/10/2026) → CONFIRMADO
- É rascunho ("draft proposal", "future standard"), não RFC final → Google → CONFIRMADO; nome do draft (draft-kelley-aipref-training-preference-signal) só no ppc.land → PARCIAL

2. Adotantes, datas, escopo
- Google: planeja suportar em 2027 ("We aim to support this new control along with other AI providers in 2027") → ainda não vale → post do Google → CONFIRMADO
- Google: se o site nega treino pelo token e não menciona Google-Extended, o Google trata como Google-Extended bloqueado; controles por empresa seguem valendo; Google-Extended existe desde 2023 → CONFIRMADO
- Google: sites que permitem Google-Extended podem aparecer em respostas e receber cliques via grounding nos apps do Gemini → CONFIRMADO. Efeito na Busca/AI Overviews: NÃO CONFIRMADO (não afirmar)
- Microsoft Bing (anúncio de 30/10/2026, Krishna Madhavan, Principal Product Manager): três controles — AI Training, AI Grounding e Limited Grounding; dá para bloquear treino e continuar citado no Copilot; ranking tradicional do Bing não é afetado; bloquear grounding pode reduzir visibilidade em respostas de IA → https://www.seroundtable.com/microsoft-bing-ai-controls-42429.html → CONFIRMADO
- Cronograma Bing: 15/12/2026 controles temporários no Bing Webmaster Tools; 01/02/2027 o Bing passa a honrar as novas preferências; 01/03/2027 prazo para migrar das diretivas antigas → mesma URL → CONFIRMADO
- OpenAI e Anthropic também aderem, segundo o Search Engine Roundtable e o PPC Land → PARCIAL (post da OpenAI, https://openai.com/index/helping-websites-express-ai-training-preferences, deu 403)
- Quem ficou de fora (Meta, xAI, chinesas): NÃO CONFIRMADO, não afirmar

3. Dois lados
- Apoio: Google diz que a proposta reflete feedback de "publishers, civil society groups, regulators" → CONFIRMADO
- Crítica: Nate Hake, publisher que participou do grupo, diz que o trabalho está incompleto e há disputas não resolvidas → ppc.land → PARCIAL
- Contexto: relatório do workshop da IAB (RFC 9969) diz que o robots.txt é tratado de forma inconsistente por crawlers de IA → https://www.rfc-editor.org/rfc/rfc9969.html → PARCIAL
- "robots.txt é voluntário": argumento conhecido, sem atribuição confirmada → usar só como análise, sem atribuir

4. Jurídico
- Diretiva (UE) 2019/790, art. 4(3): a exceção de mineração de texto e dados só vale se o titular não reservou expressamente o uso; para conteúdo público online, por "meios legíveis por máquina" → https://eur-lex.europa.eu/eli/dir/2019/790/oj (eur-lex não abriu para o apurador; texto confirmado em https://www.legislation.gov.uk/eudr/2019/790/article/4) → CONFIRMADO no texto
- Google diz que a proposta é coerente com o Código de Práticas de IA de propósito geral do AI Act, que reconhece o robots.txt como método principal → CONFIRMADO como afirmação do Google
- Lei 9.610/98 (Brasil): NÃO CONFIRMADO, não afirmar

## Bloco D — números da semana e links

a) Desemprego
- 5,2% no trimestre jul–set/2026, divulgado em 30/10; menor taxa para o período (trimestre até setembro) desde 2012; 5,4% no tri até junho; 5,6% um ano antes; 5,6 milhões de desocupados, 417 mil a menos que um ano antes → https://www.estadao.com.br/economia/ibge-pnad-desemprego-setembro-2026/ → CONFIRMADO (imprensa). Escrever "menor para o período", não "menor da série". Página do IBGE: NÃO CONFIRMADA.
- FGV IBRE (Fernando de Holanda Barbosa Filho) e Inter (André Valério) veem perda de dinamismo → mesma URL → CONFIRMADO

b) DoorDash e agentes
- CEO Tony Xu na teleconferência do 3º tri: "maybe several hundred orders in total" de agentes de terceiros → https://techcrunch.com/2026/10/30/doordash-said-its-only-received-several-hundred-orders-from-ai-agents/ (30/10) → CONFIRMADO
- Total de pedidos do 3º tri/2026: 993 milhões, +28% a/a → https://www.sec.gov/Archives/edgar/data/0001792789/000179278926000062/proddashex991-pressrelease.htm → CONFIRMADO. "Several hundred" é "no total", sem período definido: comparar só como ordem de grandeza ("centenas" contra ~1 bilhão no trimestre).

c) Microsoft e OpenAI
- US$ 10 bi de acordos com a OpenAI sobre US$ 92,3 bi de receita no trimestre encerrado em 30/09/2026 (1º tri fiscal de 2027) = ~10,8%; dado de documento enviado a reguladores; não se sabe quanto é repasse e quanto é Azure → https://startups.com.br/negocios/big-techs/microsoft-tem-quase-11-da-receita-trimestral-vinda-da-openai/ (29/10) → CONFIRMADO na imprensa; 10-Q não verificado (não citar "10-Q")

d) Kalshi
- Avaliada em US$ 40 bi em rodada Série G de US$ 1 bi liderada por Sequoia e Wellington; avaliação anterior (maio): US$ 22 bi (+82%); Polymarket: US$ 21 bi; CEO Tarek Mansour diz que "houve discussões" sobre IPO → https://c-level.folha.uol.com.br/negocios/2026/10/kalshi-e-avaliada-em-us-40-bilhoes-e-se-aproxima-de-possivel-ipo.shtml (31/10, texto do NYT) → CONFIRMADO

e) Fujifilm
- Anúncio de 29/10: ~¥10 bi (~US$ 63 mi) para multiplicar por 5 a CAPACIDADE de produção de fita LTO (frente ao ano fiscal 2025), até o fiscal 2028; atribui a demanda à IA generativa → https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/ (30/10) → CONFIRMADO

f) Amazon
- Anúncios do 3º tri/2026: US$ 19,64 bi, +10,9% (contra +26% no 2º tri), efeito da mudança do Prime Day para junho; AWS US$ 45,98 bi, +39,3% → https://ppc.land/amazon-ad-revenue-growth-drops-to-11-after-prime-day-moves-to-june/ (29/10) → CONFIRMADO (imprensa especializada)

Links
1) nesformer: Drew Breunig pôs um emulador da CPU 6502 do NES nos pesos do Qwen3.5-4B; roda Super Mario Bros "very slowly"; fez com o Opus 5.5 usando testes de conformidade publicados há 15 anos → https://simonwillison.net/2026/Oct/30/nesformer/ (30/10) → CONFIRMADO. Repositório https://github.com/dbreunig/nesformer criado em 30/10/2026, 194 estrelas em 31/10 → CONFIRMADO. "~1 GB": NÃO CONFIRMADO, não usar.
2) "AI Isn't Replacing SREs. It's Deskilling Them." (SigNoz, 28/02/2026) → https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling → CONFIRMADO (não é da semana; vale como atemporal)
3) OpenAI "The future of the firm" → NÃO CONFIRMADO (403). Não usar.
4) The Verge, Lauren Feiner, 30/10: Wikimedia apresenta amicus brief nos processos de editoras (como o NYT) contra OpenAI e Microsoft: treinar seria fair use, regurgitar artigos não → https://www.theverge.com/policy/1022880/wikipedia-openai-new-york-times-copyright → CONFIRMADO (paywall variável)
5) Stratechery "The End of the Internet" (26/10) → PARCIAL (paywall parcial provável)
6) Simon Willison, vibe game development (28/10) → ver Bloco A, item F → CONFIRMADO

## Bloco C — histórias em andamento

1) Binance
- A maior parte saiu em cerca de 20 minutos em 29/10, segundo a TRM Labs; carteiras em pelo menos 10 blockchains esvaziadas; preparação começou "ao menos 36 horas antes", com testes do código em carteiras → https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/ (Matt Burgess, 30/10) → CONFIRMADO (atribuído à TRM)
- Autoria: TRM Labs e Chainalysis apontam o grupo norte-coreano TraderTraitor; Elliptic (Tom Robinson): "We think North Korea is likely responsible"; nem a Binance nem governos apontaram a Coreia do Norte → Wired e https://www.estadao.com.br/economia/hackers-ligados-a-coreia-do-norte-sao-apontados-como-responsaveis-por-ataque-bilionario-a-binance-npr/ → CONFIRMADO como atribuição de empresas privadas
- Se for a Coreia do Norte, quase dobraria tudo o que o regime já roubou em cripto (Elliptic) → Wired → CONFIRMADO
- Congelado: US$ 2,8 bi (44%), quase tudo stablecoins; US$ 3,3 bi em Bitcoin, Ether e XRP não congeláveis (Elliptic) → Wired → CONFIRMADO
- Binance: a investigação inicial apontou um laptop comprometido, mas a posterior "achou pontos adicionais de violação"; diz que cobrirá todas as perdas → Wired → CONFIRMADO
- Saques retomados: NÃO CONFIRMADO

2) Anthropic IPO
- Segundo o FT, a Blackstone (âncora de um financiamento de chips da Anthropic) disse a investidores que espera nota "alta junk" (faixa BB, o topo do grau especulativo) depois do IPO; antes previa grau de investimento; Anthropic e Blackstone não comentaram → https://techcrunch.com/2026/10/30/anthropic-expected-to-receive-high-junk-rating-from-credit-agencies-following-ipo-report-says/ (30/10) → CONFIRMADO o relato da TechCrunch; "BB" e "US$ 63 bi" PARCIAL
- S-1 na SEC em 26/10 → https://www.anthropic.com/news/s1-sec → CONFIRMADO

3) OpenAI rodada
- WSJ (30/10): levantou menos da metade da meta de US$ 30 bi, a US$ 1,25 tri, abaixo dos US$ 1,4 tri buscados antes → https://www.wsj.com/tech/ai/openai-raises-less-than-half-of-30-billion-target-in-latest-round-91aecdc5 → PARCIAL (manchete e linha fina; corpo com paywall). Valor exato (US$ 11 bi): NÃO CONFIRMADO em veículo de referência.

4) Google Modo IA e Reddit
- Carta do 3º tri do Reddit: tráfego de busca caiu "meaningfully", acelerando no fim do tri; em outubro, mais de 1 milhão de referências a menos por semana, em média; DAUq podem cair "low-double-digit" no 4º tri; a carta não atribui à IA → https://ppc.land/reddit-ad-revenue-gains-54-to-847m-as-daily-users-stall-at-130-3m/ (29/10) → CONFIRMADO
- Na teleconferência, Steve Huffman disse que a hipótese principal é AI Overviews e AI Mode, que empurram os outros resultados para baixo → https://www.searchenginejournal.com/reddit-to-test-login-only-mode-as-google-search-traffic-drops/595270/ → PARCIAL (frase "does not drive traffic" é do título do SEJ, não citar como aspas de Huffman)
- 3º tri: anúncios US$ 847 mi (+54%); DAUq globais 130,3 mi, estáveis; nos EUA, de 53,2 mi para 50,7 mi → ppc.land → CONFIRMADO
- Login: primeiros testes em mercados selecionados fora dos EUA nos próximos meses → https://ppc.land/reddit-plans-to-make-logins-the-norm-after-20-years-of-open-browsing/ → CONFIRMADO
- Estudo de CTR ~0,9% em impressões de IA: Cyrus Shepard, estudo de caso de UM site que se tirou das AI Overviews/AI Mode; os cliques orgânicos também caíram ao desligar → https://www.seroundtable.com/google-ai-overviews-mode-ctr-42421.html (30/10) → CONFIRMADO (amostra de um site; não generalizar)

5) Bolsa brasileira
- Sexta 30/10: Ibovespa −0,75%, a 167.922 pontos; semana −18,12%, pior desde março de 2020; dólar a R$ 5,44, +9% na semana; segunda 26/10 −14% com circuit breaker; outubro −9,88%; DI jan/2028 a 14,48% → https://investnews.com.br/investimentos/ibovespa-afunda-18-e-tem-pior-semana-desde-2020-dolar-salta-9/ → CONFIRMADO
- −18,12% está entre as 4 maiores quedas semanais do século; a maior foi a de 10/10/2008 (−20,01%); 20/03/2020 foi −18,88% → https://www.infomoney.com.br/mercados/maiores-quedas-semanais-ibovespa-2008-covid-11-setembro-eleicao/ → CONFIRMADO
- Fundos perderam R$ 157,5 bi em patrimônio do dia seguinte à eleição até 28/10 (Economática) → https://c-level.folha.uol.com.br/financas/2026/10/fundos-de-investimento-perdem-r-1575-bilhoes-apos-reeleicao-de-lula.shtml → CONFIRMADO
- Itaú: PIB 2027 de 1,2% para 0,5%; IPCA 2027 de 4,6% para 6,1% (teto da meta 4,5%); Selic em 13,75% em todo 2027 → https://www1.folha.uol.com.br/mercado/2026/10/itau-corta-projecao-do-pib-de-2027-para-05-e-ve-inflacao-acima-da-meta.shtml → CONFIRMADO

6) Raízen
- Assembleia de 30/10 aprova recuperação extrajudicial; passivo de R$ 65 bi; credores ficam com ~80% do capital (dívida de ~R$ 30 bi vira participação); Shell fica com 13% a 15% e aporta R$ 3,5 bi; Rubens Ometto sai do comando; divisão em Raízen Energia e Raízen Combustíveis, cisão na 2ª quinzena de dezembro → https://neofeed.com.br/negocios/credores-viram-socios-na-raizen-e-abrem-caminho-para-fim-de-maior-recuperacao-extrajudicial-do-brasil/ → CONFIRMADO
- R$ 39,8 bi de capitalização: NÃO CONFIRMADO

7) Kimi K3.1 Pro
- Pesos não publicados até 31/10 na conta oficial da Moonshot no Hugging Face (mais recente: Kimi-K3, 02/09) → https://huggingface.co/moonshotai → CONFIRMADO; prazo prometido de 4/11 (já publicado em 24/10 com https://www.kimi.ai/blog/kimi-k3-1-pro)

8) Meta termos comerciais: nada de novo na semana; seguem para 20/11 → https://ppc.land/meta-delays-website-crawling-terms-to-nov-20-after-publisher-complaints/ → CONFIRMADO

## Adendos da revisão
- Itaú (Folha, 30/10): motivos da revisão incluem a volta do PIS/Cofins sobre a gasolina, o fim da subvenção ao diesel, ICMS, reforma tributária, fim da 6x1 e dólar mais caro; espera Selic em 13,75% em todo 2027 → https://www1.folha.uol.com.br/mercado/2026/10/itau-corta-projecao-do-pib-de-2027-para-05-e-ve-inflacao-acima-da-meta.shtml → CONFIRMADO
- Fujifilm (Ars Technica): linha fina "Low costs and offline security mean magnetic tape still has a job" → CONFIRMADO
- Binance US$ 6,3 bi: confirmado na edição nº 12 (https://exame.com/future-of-money/caso-binance-corretora-diz-que-ataque-hacker-atingiu-us-63-bilhoes/) e no título da Wired → CONFIRMADO
