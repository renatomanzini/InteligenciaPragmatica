# Apuração: edição nº 6 (21/10/2026)

Quatro agentes (Sonnet) em paralelo. Fichas resumidas; status: CONFIRMADO / PARCIAL / NÃO CONFIRMADO.

## (a) Matéria principal: rascunho do S-1 da Anthropic
- Documento NÃO é público: rascunho confidencial visto pelo WSJ; sem S-1 da Anthropic na EDGAR → https://www.sec.gov/cgi-bin/browse-edgar?company=anthropic&type=S-1 → CONFIRMADO
- Receita 1S26 US$ 16,3 bi vs US$ 1,1 bi no 1S25 → TechCrunch https://techcrunch.com/2026/10/20/anthropics-cloud-partnerships-are-getting-messy/ ; Investing.com https://www.investing.com/news/stock-market-news/anthropic-revenue-hits-163-billion-as-preliminary-s1-outlines-ipo-risks--wsj-4960928 → CONFIRMADO (secundária; WSJ com paywall)
- Prejuízo líquido 1S26 US$ 80,7 bi; ~US$ 72 bi são ajustes contábeis não caixa (conversíveis e instrumentos financeiros) → Investing.com → CONFIRMADO (secundária)
- Gasto com computação/infra de quase US$ 9 bi no 1S26 vs US$ 7,3 bi em todo 2025 → Investing.com → CONFIRMADO (secundária)
- Dois clientes ≈ 20% da receita do 1S → TechCrunch, Investing.com → CONFIRMADO
- Compromissos de nuvem ~US$ 450 bi em ~10 anos (Google US$ 111 bi, AWS US$ 110 bi, Microsoft US$ 31 bi) → Investing.com → CONFIRMADO (secundária)
- Pediu mais capacidade do que AWS, Google e Microsoft aceitaram dar; aluga data centers e usa operadores com "limited operating history" → TechCrunch → CONFIRMADO (secundária)
- Risco de responsabilidade por dano da IA acima do seguro → TechCrunch → CONFIRMADO (secundária)
- 3T26 US$ 16,8 bi dito a investidores (não vem do S-1) → TechCrunch → CONFIRMADO
- Meta de IPO em novembro (WSJ via TechCrunch) → PARCIAL
- Eric Schmidt ~1% (Bloomberg) vs Dario ~2% (Reuters) → TechCrunch https://techcrunch.com/2026/10/20/eric-schmidt-reportedly-owns-about-half-as-much-of-anthropic-as-ceo-dario-amodei/ → PARCIAL (estimativas de imprensa)
- Dario e Daniela Amodei com salário-base ~US$ 655 mil em 2025 → Investing.com → CONFIRMADO (secundária)
- S-1 cita China como risco → NÃO CONFIRMADO (fora)
- Claude Code "estacionou desde junho" (Reddit) → NÃO CONFIRMADO (fora)
- Prejuízo 1S25 ~US$ 13 bi → PARCIAL (fora)
- Anthropic /news: nada de 19–21/10; /research: "How Claude designed protein binders against scorpion neurotoxins", 20/10 → CONFIRMADO

## (b) IA na prática: reduzir a superfície de ataque
- Post "Using Claude to reduce the attack surface of code", 20/10/2026, Chris Rohlf (Frontier Red Team) → https://www.anthropic.com/research/attack-surface-reduction → CONFIRMADO
- 25 projetos open source, +5 milhões de linhas; +17.000 opções de configuração, 3.842 relevantes para segurança; 493 problemas → CONFIRMADO
- 162 combinações sensíveis aceitas sem erro/aviso/documentação; 94 desligavam controle de segurança → CONFIRMADO
- Em 4 projetos, com DNS reverso desligado, regras de negação por hostname nunca casavam (falha aberta); conflito de 21 anos derrubava exigência de certificado de cliente → CONFIRMADO
- OpenSSH 10.4: ~4.500 linhas de código experimental ML-DSA-44 alcançáveis sem autenticação, ~16% do código pré-autenticação; 10.6 completou correção → CONFIRMADO (no post)
- Limites: "pesquisa inicial"; muitos achados não "imediatamente exploráveis"; não diz quantos corrigidos; sem prompt literal → CONFIRMADO
- HN: críticas sobre restrições de cibersegurança do Claude → https://news.ycombinator.com/item?id=50175779 → CONFIRMADO
- eMudhra: chaves privadas de 8 CAs intermediárias comprometidas, "incorretamente geradas"; Firefox/Chrome bloqueiam desde 17/10, Apple 19/10, Microsoft 20/10; sem registros de CT, navegadores com CT não poderiam ter sido atacados → https://emudhra.we-have-a-problem.com/ ; https://simonwillison.net/2026/Oct/20/emudhra-certificates/ → CONFIRMADO
- PHP patches de emergência → NÃO CONFIRMADO (fontes 502/403; fora)
- Arkose 97,7% → PARCIAL (fora)

## (c) Economia e rodadas
- Brasil "devedor internacional após 19 anos" → Estadão bloqueado; dado do BC não achado → NÃO CONFIRMADO (fora; STATS trocado)
- Ibovespa 20/10 +1,57%, a 208,3 mil pontos; dólar -0,58%, a R$ 5,019 → https://www.infomoney.com.br/mercados/ibovespa-hoje-bolsa-de-valores-ao-vivo-20102026/ → CONFIRMADO (lido pela redação)
- Panda bonds: ~10 bi de yuans (US$ 1,5 bi) depois do 2º turno, segundo a Bloomberg; Tesouro não comentou → https://investnews.com.br/economia/brasil-prepara-primeira-emissao-de-panda-bonds-para-depois-da-eleicao-presidencial/ → PARCIAL (fonte anônima)
- Agenda 21/10: WEG antes da abertura; Meta e Tesla divulgam hoje; IGP-M 2ª prévia às 8h → https://www.infomoney.com.br/mercados/pesquisa-quaest-balancos-weg-meta-tesla-21102026/ → CONFIRMADO
- SpaceX 3º tri: receita US$ 14,6 bi; IA = 52% (US$ 7,5 bi), lucro da IA US$ 431 mi; ~US$ 1 bi de receita ligada a Bitcoin e partes relacionadas; capex US$ 19,6 bi; capex de US$ 35–40 bi previsto no 4º tri; lucro líquido US$ 4,4 bi → https://techcrunch.com/2026/10/20/spacexs-ai-business-is-beating-expectations/ → CONFIRMADO (lido pela redação)
- Fusão SpaceX-Tesla → NÃO CONFIRMADO (fora); Brent de 20/10 → NÃO CONFIRMADO (fora); data do Fed → NÃO CONFIRMADO (fora)
- iFood Benefícios compra a Caju; valor não divulgado oficialmente, NeoFeed diz mais de R$ 1,2 bi; notificado ao Cade; 1,7 mi + 1,3 mi de usuários → https://neofeed.com.br/startups/ifood-beneficios-compra-caju-por-mais-de-r-12-bilhao/ → PARCIAL (valor), CONFIRMADO (negócio)
- Ânima: ação -9% em 20/10; R$ 150 mi iniciais; BTG estima custo total acima de R$ 600 mi; 15 cursos de medicina por 20 anos → https://investnews.com.br/negocios/r-600-milhoes-em-jogo-por-que-o-mercado-reagiu-mal-ao-acordo-da-anima-com-o-einstein/ → CONFIRMADO
- Patria/Atacadão 22 lojas ~R$ 1 bi (fontes de mercado; sale and leaseback) → NeoFeed → PARCIAL
- Salesforce compra Braze: US$ 47,50 por ação, ~US$ 5,66 bi, fechamento a partir de fev/2027 → https://ppc.land/salesforce-agrees-to-buy-braze-for-5-66bn-in-cash/ → CONFIRMADO
- Yelp Smart Lead Reply US$ 30/mês em novembro; Receptionist US$ 99/mês → https://ppc.land/yelp-charges-30-a-month-for-ai-agent-that-answers-and-qualifies-leads-2/ → CONFIRMADO
- Projeto de lei da Anthropic: risco "previsível e iminente" a mais de 50 pessoas ou mais de US$ 1 bi; só juiz federal pode suspender lançamento; agências proibidas de bloquear sozinhas → https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed/ → CONFIRMADO (secundária)
- Otter US$ 320 mi do Customer Value Fund da General Catalyst (financiamento, não venda de ações) → startups.com.br → PARCIAL
- Spotify 50 mi de faixas; Shopee x ML → NÃO CONFIRMADO (fora)

## (d) Curiosidade, links, Muse
- Deepwater Horizon: queda de 60% a 85% na abundância de peixes, crustáceos e cefalópodes de profundidade em 3,5 anos, sem recuperação em mais de uma década; autores não provam causalidade → https://e360.yale.edu/digest/deepwater-horizon-deep-sea-recovery ; PNAS https://www.pnas.org/doi/full/10.1073/pnas.2616554123 → CONFIRMADO
- Steve Krouse, "What Shall I Teach My Son?" → https://stevekrouse.com/ends → CONFIRMADO
- Simon Willison, Battle Drones: 321 commits, feito quase todo por agentes (principalmente Claude Code) → https://simonwillison.net/2026/Oct/20/battledrones/ → CONFIRMADO
- MIT TR, "We can do impossible things", Corinne Iozzio → CONFIRMADO
- Meta pausou compartilhamento do Muse; Claroc achou ~6.800 links → The Verge https://www.theverge.com/tech/1014627/meta-muse-ai-sharing-ai-chats → CONFIRMADO
- Kernel Linux "deixou de exigir" declaração de IA → NÃO CONFIRMADO (doc ainda exige; fora)
