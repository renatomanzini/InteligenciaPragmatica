# Apuração: edição nº 4, 19/10/2026

Fichas dos apuradores (modelo Sonnet), condensadas. Status: CONFIRMADO / PARCIAL / NÃO CONFIRMADO.

## (a) Principal: Anthropic Public Benefit Fund
- Anúncio em 18/10/2026 → https://www.anthropic.com/news/public-benefit-fund → CONFIRMADO
- 5% das ações, "sujeito à aprovação dos acionistas" (ainda não aprovada) → idem → CONFIRMADO
- +2% a critério do conselho a cada alta de 50% no valor acima de uma base; base não divulgada → idem → CONFIRMADO (base NÃO CONFIRMADA)
- Veículo: LLC integralmente da Anthropic, não 501(c)(3); patrimônio não pode ir para lobby ou doação política → idem → CONFIRMADO
- Cofundadores prometeram 80% do patrimônio, na fundação → idem → CONFIRMADO
- Matching de doação de ações; cerca de metade dos funcionários participa → idem → CONFIRMADO
- ~20% das ações ao todo para o bem público (soma; composição não detalhada) → idem → CONFIRMADO (composição PARCIAL)
- Governança, estrutura e marcos "nos próximos meses" + relatório de benefício público; TechCrunch: não disse quem decide o que será financiado → anthropic.com + https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/ → CONFIRMADO
- US$ 200 mi anteriores para estudar impacto da IA no trabalho → ambas → CONFIRMADO
- Série H: US$ 65 bi a US$ 965 bi pós-money, 29/05/2026, liderada por Altimeter, Dragoneer, Greenoaks, Sequoia; Série G de fev/2026 a US$ 380 bi → https://www.orrick.com/en/News/2026/05/Anthropic-Raises-65B-Series-H-at-965B-Post-Money-Valuation (verificado pelo editor via busca) → CONFIRMADO
- Contas (nossas, sobre US$ 965 bi): 5% ≈ US$ 48 bi; 2% ≈ US$ 19 bi; 20% ≈ US$ 193 bi → cálculo
- LTBT: página de 19/09/2023; cinco trustees; trust de propósito de Delaware; ações Class T; "will elect a majority of the board within 4 years"; cláusulas failsafe permitem mudar os poderes do trust com supermaioria de acionistas, sem consentimento dos trustees; Ben Bernanke entrou em jul/2026 → https://www.anthropic.com/news/the-long-term-benefit-trust → CONFIRMADO
- PBC; conselho eleito por acionistas e pelo LTBT → https://www.anthropic.com/company → CONFIRMADO
- DGCL §362(a) definição de PBC; §365(a) conselho equilibra interesses dos acionistas, dos afetados e do benefício público; §366(b) relatório ao menos bienal → https://delcode.delaware.gov/title8/c001/sc15/index.html → CONFIRMADO
- WSJ (fundo e "trust obscuro" no IPO) → paywall/captcha → NÃO CONFIRMADO (não atribuir detalhe)
- US$ 16,8 bi no 3º tri: já publicado em 17/10 como relato de investidor (Reuters via DealStreetAsia) → mantido como relato
- Pledge 1%: ~20 mil empresas; Reddit dedicou 1% das ações no IPO → https://pledge1percent.org/ → CONFIRMADO
- OpenAI Foundation 26% da OpenAI Group PBC (reestruturação 28/10/2025) → imprensa via busca → PARCIAL
- Críticas: análise que o trust pode ser quase sem poder (supermaioria pode alterá-lo) — a própria página do LTBT confirma o mecanismo failsafe → CONFIRMADO (mecanismo); críticos nomeados → PARCIAL
- Nenhuma reação independente ao fundo encontrada → NÃO CONFIRMADO

## (b) IA na prática: Qwen3-4B "deslop"
- Autor Erik Markus Kannike, out/2026; ajuste fino do Qwen3-4B-Instruct-2507 para tirar tiques de escrita de IA (travessão, "não X, mas Y", listas de três) → https://100toolkit.com/blog/deslop-model/ → CONFIRMADO (alegação do autor)
- Método: destilação de respostas filtradas de um modelo professor + adaptador LoRA + edição de 4 neurônios; feito num MacBook Air M2 → idem → CONFIRMADO
- Pesos: https://huggingface.co/erikkannike/qwen3-4b-deslop-v4 ; licença Apache-2.0 no HF → CONFIRMADO / PARCIAL
- GGUF Q4_K_M ≈ 2,5 GB; adaptador LoRA 126 MB; roda em llama.cpp/Ollama → blog → PARCIAL (desempenho em 8 GB não testado)
- Avaliação do autor (regex do próprio guia, por 1.000 palavras): 121 → 12,5 em 40 prompts reservados; travessões 20,5 → 0; 30/30 perguntas factuais certas → blog → CONFIRMADO como alegação; dado de treino filtrado pelas mesmas checagens (admitido)
- Limites: voz "plana"; inventa nomes e lugares; respostas longas; testado só em prosa curta em inglês → blog → CONFIRMADO
- 31 downloads no mês, 1 curtida → HF → CONFIRMADO
- Alternativas descartadas: WhatsApp MCP (biblioteca não oficial Baileys, contra os termos do WhatsApp, "free" exige plano pago; https://github.com/finereli/whatsapp-mcp); Stripe 38x (https://stripe.com/blog/helping-personal-agents-shop-more-intelligently-and-reliably-with-link, 29/09, sem base de comparação)

## (d) STATS, HEA e links
- PLD +2.409% (NeoFeed, resumo gerado por IA; R$ 57,31 → R$ 1.437/MWh em 15/10; sem fonte primária da CCEE; parte do piso) → PARCIAL → descartado como número do dia
- Juros líquidos da dívida dos EUA: US$ 1,05 tri no ano fiscal 2026 (até set), contra US$ 970 bi em 2025; 3,2% do PIB, recorde acima de 1991 (Peterson Foundation); taxa média 3,52% vs 1,47% cinco anos antes; dívida > US$ 32 tri → https://investnews.com.br/economia/nao-e-so-no-brasil-divida-publica-dos-eua-custa-us-1-trilhao-so-em-juros-e-ameaca-virar-bola-de-neve/ (Bloomberg) → CONFIRMADO na reportagem
- Cães e bouba/kiki: Proc. R. Soc. B, DOI 10.1098/rspb.2026.1209, 14/10/2026, Biffi et al. (Univ. de Parma) → https://www.sciencealert.com/dogs-seem-to-agree-with-humans-that-bouba-is-round-and-kiki-is-spiky → CONFIRMADO
- MIT TR, Amit Katwala, 19/10: cópias do Claude Opus 4.7 sozinhas numa ilha simulada por 30 h inventaram jogos; especialistas questionam se é "brincar" → CONFIRMADO
- Import AI 477, Jack Clark, 19/10: no FMI, diz que a singularidade começou → CONFIRMADO
- Karri Saarinen, "Someone behind the software", 15/10 → CONFIRMADO
- 3Blue1Brown, vídeo existe; data não obtida → PARCIAL
- Ars (OpenAI e carteira cripto): já coberto em 16/10 → fora

## (c) Economia e rodadas
- Focus 19/10 (BCB, API Olinda; Exame): IPCA 2026 5,22% (mediana 5,219 vs 5,2245: praticamente estável); IPCA 2027 4,32% (4,30%); PIB 2026 1,83% (1,85%); PIB 2027 1,32% (1,40%); Selic fim 2026 13,25% (estável); câmbio fim 2026 R$ 5,13 (5,15) → https://exame.com/economia/boletim-focus-mercado-reduz-projecao-do-pib-para-183-em-2026/ → CONFIRMADO
- Sexta 16/10: Ibovespa 205.430,33 (+0,54%; −1,74% na semana); dólar ~R$ 5,07 (−0,28%; +1,75% na semana) → https://www.infomoney.com.br/mercados/ibovespa-hoje-bolsa-de-valores-ao-vivo-19102026/ → CONFIRMADO (imprensa, via resumo)
- China PIB 3º tri: 4,5% a/a (2º tri 4,3%; 9 meses 4,6%) → https://english.news.cn/20261019/89cd3cbf51d94ed7bc3156fa7c628667/c.html → CONFIRMADO; esperado 4,4% → https://www.fxstreet.com/news/breaking-chinas-gdp-expands-by-45-yoy-in-q3-vs-44-expected-202610190200 → PARCIAL
- Petróleo: Trump assinou na sexta (16/10) à noite ordem suspendendo sanções à Rússia; Brent recua ~1,8% para US$ 107,88 na manhã de 19/10 → https://www.oeconomico.com/brent-recua-18-para-us-10788-apos-trump-aliviar-sancoes-a-russia/ → PARCIAL (valor varia por horário)
- França juros longos (Valor, paywall, só lead) → PARCIAL → fora
- Ri Happy: recuperação extrajudicial em 18/10, ~48 dias após a compra pela BluSun (anúncio 31/08); Héctor Núñez volta à presidência; dívida não divulgada → https://exame.com/negocios/ri-happy-pede-recuperacao-extrajudicial-48-dias-apos-mudar-de-dono/ → CONFIRMADO
- Braskem: FIP Shine (IG4) fica com 50,11% do capital votante e 34,33% do total; liquidação em 21/10; Petrobras ~47% do votante; recuperação extrajudicial de 24/08 para ~US$ 10,9 bi → https://investnews.com.br/negocios/fip-shine-conclui-aquisicao-de-acoes-e-assume-mais-de-50-de-votos-na-braskem/ → CONFIRMADO
- Petrobras: grupo de trabalho para o impacto do fim da 6x1 em quase 130 mil terceirizados; ~50 mil empregados próprios não afetados → https://www.estadao.com.br/economia/coluna-da-broad/petrobras-avalia-impactos-do-fim-da-escala-6x1-a-130-mil-terceirizados/ → CONFIRMADO
- Stablecoins (Allium, global): US$ 482 bi (~R$ 2,4 tri) em pagamentos de jan a set/2026, +45% a/a; 1,04 bi de transações (+71%) → https://investnews.com.br/financas/stablecoins-ja-movimentaram-r-24-trilhoes-em-pagamentos-no-ano/ → CONFIRMADO (imprensa)
- STJ usucapião de domínio: sem turma, relator, processo (paywall) → PARCIAL → fora
- Disney: ofertas a pelo menos 60 funcionários da Character.AI (a maioria), ~US$ 60 mi/ano em remuneração; Character.AI em falência; Disney é stalking horse, já acordou comprar ativos por US$ 20 mi → https://techcrunch.com/2026/10/18/disney-agrees-to-hire-the-majority-of-character-ais-workforce/ → CONFIRMADO
- Replit: Amjad Masad disse em 15/10 que deixou de trabalhar com a Anthropic; depois esclareceu que OpenAI é o padrão do Replit Agent e Claude segue selecionável; era cliente "top cinco"; fonte anônima contestou → https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/ → CONFIRMADO
- Microsoft/Nscale (WSJ bloqueado) → NÃO CONFIRMADO → fora
- Google Ads Data Manager sem hash (e-mail repassado no LinkedIn) → PARCIAL → fora
- LinkedIn: consultas pagas 1:1 a partir do perfil, para Business Premium nos EUA, anúncio de 15/10 → https://news.linkedin.com/2026/new-ways-to-build-meaningful-connections → CONFIRMADO
