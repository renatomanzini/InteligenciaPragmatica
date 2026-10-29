# Apuração — 2026-10-29

## (b) IA na prática — DAYJOB: Tax (Surge AI)
Fontes primárias: blog https://surgehq.ai/blog/dayjob-tax (27/10/2026); leaderboard https://surgehq.ai/benchmarks/dayjob-tax; HN https://news.ycombinator.com/item?id=50275626

- 50 tarefas em 8 áreas (pessoa física/família, pequenos negócios, sociedades, propriedade e investimentos, espólios/doações/trusts, internacional, transações corporativas, revisão e disputas) → blog → CONFIRMADO
- O agente recebe o pedido do cliente e os documentos e entrega declaração, papéis de trabalho, revisão técnica ou parecer; a Surge mede também se ele acha problema que o cliente não levantou, resolve evidência conflitante, reconhece informação insuficiente → blog → CONFIRMADO
- Métrica: pass@1, passa quem cumpre pelo menos 95% dos critérios da rubrica → blog → CONFIRMADO
- 1.789 arquivos, mediana de 30 por tarefa, máximo de 123; 1.487 PDFs, 117 planilhas, 38 Word, mais e-mails, imagens etc. → blog → CONFIRMADO
- Tarefas feitas por especialistas em tributação (ex-PwC, Deloitte, EY, Baker Tilly; anônimos), revisão em três camadas → blog → CONFIRMADO. Nº de especialistas e se a correção é humana ou por modelo-juiz → NÃO CONFIRMADO
- Notas (pass@1, limiar 95%), leaderboard → CONFIRMADO: Claude Sonnet 5.5 10,8%; Claude Fable 5.1 9,6%; Claude Opus 5.5 9,2%; Muse Wonder 1.0 (Meta) 6,0%; Grok 4.7 5,0%; GPT 6 Astra 4,8%; GPT 6.1 Sol 4,0%; Muse Spark 1.3 3,6%; Gemini 4 Argon 3,2%; Hy4 Preview (Tencent) 1,6%; DeepSeek V4.1 Flash 1,2%; Gemini 3.8 Flash 0,8%; GLM 5.3 0,4%; Kimi K3, Mistral Large 4, Qwen 3.8 Max 0%. 16 modelos.
- Comparação: no mesmo site, o Sonnet 5.5 lidera o teste de programação sudo L7 com 50,6% → leaderboard → CONFIRMADO
- Caso da venda de imóvel (exclusão de ganho de até US$ 250 mil): GPT 6 Astra não identificou, em 5 tentativas, o prazo de perda da elegibilidade; o Opus identificou nas 5 → blog → CONFIRMADO
- Caso do casal (Roth IRA e 401(k)): o Opus 5.5 assumiu nas 5 tentativas que o casal não era casado, apesar de indícios; o Astra pediu confirmação do estado civil em 4 de 5 → blog → CONFIRMADO
- Armadilhas: recibo manuscrito, recibo citado no razão mas ausente (o agente deveria sinalizar) → blog → CONFIRMADO
- Conclusão da Surge: "Agents haven't yet passed the audit." → blog → CONFIRMADO
- Outros testes (TaxBench, TaxCalcBench) partem de problema definido; o DAYJOB mede se o agente percebe qual é o problema → blog → CONFIRMADO
- Custo/tempo em números → NÃO CONFIRMADO; linha de base humana → NÃO CONFIRMADO; intervalos de confiança não publicados → CONFIRMADO (ausência)
- Críticas no HN: diferença entre os 3 primeiros pode estar dentro do erro (usuário WhitneyLand); pergunta sem resposta sobre linha de base humana → CONFIRMADO como comentário
- Conflito de interesse: a Surge vende dados de treino e avaliação para laboratórios de IA (site) → CONFIRMADO como fato; benchmark não totalmente reprodutível (acesso por pedido) → CONFIRMADO
- Relatos anedóticos no HN (usuário usa Claude para revisar declaração e achou taxa de câmbio errada) → PARCIAL
- Legora/OpenAI → NÃO CONFIRMADO (página não abriu). Fora.

## (a) Principal — CBS de 11,3% (TCU, 28/10/2026)
Sem fonte primária vista (portal do TCU e Planalto não abriram; Jota com paywall). Base: imprensa de referência.
- TCU aprovou em 28/10 a alíquota de referência da CBS para 2027 → https://www.estadao.com.br/economia/aliquota-de-novo-imposto-da-reforma-tributaria-assusta-e-carga-tributaria-pode-subir-em-2027/ ; https://c-level.folha.uol.com.br/negocios/2026/10/tributo-da-reforma-maior-que-o-previsto-obriga-empresas-a-rever-planejamento-para-2027.shtml → CONFIRMADO
- Alíquota 11,3% (cálculo 11,3468%; Estadão usa 11,34%) → https://investnews.com.br/economia/aliquota-cbs-tcu-2027/ → CONFIRMADO. Usar "11,3%".
- Redutor de 44,2% para compras da administração pública → InvestNews; https://www.jota.info/tributos/tcu-aprova-aliquota-de-referencia-de-113-para-cbs-e-redutor-de-442 → PARCIAL (mecânica não vista)
- Estimativa anterior 9,21% → https://braziljournal.com/prepare-o-bolso-e-o-caixa-vem-ai-o-iva-de-pelo-menos-30 ; InvestNews → CONFIRMADO o número (autoria varia: "equipe econômica"/Comitê Gestor do IBS)
- CBS estimada em R$ 528,5 bi/ano; meta de receita ~4,99% do PIB → InvestNews → PARCIAL
- Fazenda: alíquota efetiva ~8,5% em 2027 (cesta básica zerada, cashback); 11,3% é "alíquota máxima" → Folha C-Level → CONFIRMADO como declaração
- IVA total ~30% (CBS 11,3% + IBS ~18,7% estimado) → Brazil Journal → PARCIAL (projeção). Bichara (Bichara Advogados) projeta pior caso de 34,2% → Estadão → CONFIRMADO como projeção dele. Jota: "até 29%".
- Teto da reforma: 26,5%; se ultrapassado, governo deve propor corte de benefícios a partir de 2032 → Folha → CONFIRMADO (imprensa)
- Hungria 27% (maior IVA hoje), nórdicos 25% → Brazil Journal → PARCIAL (Estadão fala em 26% para o segundo)
- Appy estimou IVA abaixo de 27% quando a reforma foi aprovada → Brazil Journal → CONFIRMADO
- CBS substitui PIS e Cofins a partir de janeiro de 2027 → InvestNews; Brazil Journal → CONFIRMADO
- Hoje no lucro presumido PIS/Cofins = 3,65% sobre a receita → Brazil Journal → PARCIAL; não cumulativo 9,25% → Folha (Fiemg) → PARCIAL
- Tese do Brazil Journal: no presumido, serviço com pouco crédito sai de 3,65% para 11,3% (carga "mais que triplicaria") → Brazil Journal → CONFIRMADO como análise do veículo; ressalva: redução de 30% para profissões regulamentadas e créditos podem diminuir
- Redução de 30% para profissionais liberais (profissões regulamentadas, com requisitos); 60% saúde/educação → InvestNews → PARCIAL. NÃO citar artigo.
- Simples Nacional: pode ficar no regime ou optar por apurar CBS/IBS por fora (híbrido) para gerar crédito ao cliente → InvestNews → PARCIAL
- IBS em teste a 0,1% em 2027–2028; transição até 2033 → InvestNews → PARCIAL
- Calendário: TCU tinha até 30/10 para enviar ao Senado; Senado fixa por resolução até 15/12; sem decisão, vale o cálculo do TCU → InvestNews → CONFIRMADO (imprensa)
- Imposto Seletivo sem lei de alíquotas; sem ele a CBS sobe (Daniel Loria, Loria Advogados) → Estadão → CONFIRMADO como análise
Quem critica:
- Paulo Skaf (Fiesp): decisão "quebra a premissa central" de manter a carga; tira mais de R$ 100 bi em 2027 → Folha → CONFIRMADO
- Bichara: "Você já viu imposto cair no Brasil?" → Estadão → CONFIRMADO
- Abcon (Felipe Cascaes): setor projetava ~9% e vai repassar às tarifas → Folha → CONFIRMADO
Quem defende/relativiza:
- Bernard Appy: 2027 é a alíquota "menos precisa" da transição; "a tendência é de que caia" → Estadão → CONFIRMADO
- Daniel Loria: Receita foi "conservadora" → Estadão → CONFIRMADO
- TCU: a alíquota não aumenta nem reduz a carga na média dos anos-base → Estadão → CONFIRMADO como posição

## (d) MARKETING DIGITAL
1. Google — anúncios no Modo IA em 10 novos mercados (Austrália, Canadá, Índia, Quênia, Malásia, Nova Zelândia, Nigéria, Paquistão, Filipinas, Singapura), anunciado em 28/10; anúncios multiturno (em perguntas de acompanhamento) só nos EUA; Brasil, México e Reino Unido "ainda este ano", sem data → https://blog.google/products/ads-commerce/ads-in-ai-mode-global/ ; https://blog.google/intl/pt-br/produtos/estamos-expandindo-os-anuncios-no-modo-ia-para-novos-mercados/ → CONFIRMADO (Brasil: só planejado)
2. Perfil da Empresa no Google — restaurante pode desligar provedor de pedido de terceiros pelo painel (antes: pedido de remoção com 5 dias úteis). Fonte do Google só um post no LinkedIn; Ajuda oficial ainda não descreve; abrangência "all" em comentário informal → https://www.searchenginejournal.com/google-restaurants-opt-out-ordering-providers/594794/ → PARCIAL
3. Meta — três inovações no ranqueamento de anúncios (28/10): GenRecs (recuperação generativa baseada em LLM) no Feed do Facebook, "nearly +2%" de conversões em segmentos-alvo no 3º tri; Andromeda pontua mais de 1 bilhão de anúncios por segundo, +1,37% conversões no Facebook no 3º tri; GEM até 18,9% de melhora em conversões desde 2025; no 2º tri, ranqueamento deu 8,3% mais cliques; chegam automaticamente às contas, sem configuração. Todos números da Meta, sem auditoria → https://www.facebook.com/business/news/three-new-ai-innovations-in-ads-ranking → CONFIRMADO (como alegação da Meta)
4. Meta — Andy Stone diz que a consulta pode passar de 20/11 e, nesse caso, adia os novos termos; até lá valem os atuais → https://www.theverge.com/tech/1020769/meta-updated-business-terms-delay-indefinitely → CONFIRMADO
5. YouTube — teste de limite de pagamento de US$ 100 para US$ 20, grupo aleatório nos EUA, Índia e Indonésia, desde os pagamentos de outubro; Brasil fora → https://www.tubefilter.com/2026/10/28/youtube-partner-program-lower-payout-threshold-test/ → CONFIRMADO via veículos
6. Alphabet 3º tri: receita US$ 127,6 bi (+25%, contra US$ 102,3 bi); Google Search & other US$ 63,4 bi (+12%; foi +17% no 2º tri e +19% no 1º); YouTube ads US$ 11,2 bi (+9%); Cloud US$ 30,7 bi → https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm → CONFIRMADO. Na teleconferência, Philipp Schindler citou monetização menor do Modo IA como um de três fatores (câmbio foi o principal) → https://www.searchenginejournal.com/google-search-growth-slows-again-ai-mode/594862/ → PARCIAL. Queda das ações ~10% → NÃO CONFIRMADO
7. Estudo de TJ Robertson (TJ Digital, agência de SEO/GEO): 193.507 respostas de ChatGPT, Modo IA e AI Overviews a 4.167 perguntas; páginas citadas abriam com resposta direta em 20% dos casos, contra 5% das páginas do top 10 que a IA nunca puxou; associação, não causa; dados de clientes da agência → https://www.searchenginejournal.com/ai-cited-pages-more-often-got-straight-to-the-answer/594781/ → CONFIRMADO como descrito pelo SEJ
8. Mercado Livre prevê mais de R$ 100 mi em cupons ativados por dia no 11.11 e Black Friday, 37 milhões de anúncios em promoção (projeção da empresa, André Castilho) → https://www.meioemensagem.com.br/marketing/mercado-livre-explorara-cupons-para-11-11-e-black-friday → CONFIRMADO como projeção
9. Case Lush: em 2021 largou posts e anúncios em Instagram, Facebook, TikTok, Snapchat; em 2023 parou no X; verba para app próprio, colaborações, criadores, eventos e e-mail. Julia Hamfelt (Lush): app com 2,8 mi de usuários, e-mail com mais de 6 mi de alcance (PARCIAL, declaração). Receita do ano fiscal até jun/2025: £ 736,2 mi, contra ~£ 673 mi no ano anterior (que tinha caído 5%) → https://digiday.com/marketing/how-lush-quit-social-media-ads-and-still-drove-growth/ ; https://www.cosmeticsbusiness.com/lush-reports-full-year-2025-results → CONFIRMADO. A Lush não revela quanto gastava em social; não prova causa; marca com ~900 lojas.

## (c) Economia, rodadas, STATS, links
- Ibovespa caiu 2,68% em 28/10, a 171.006 pontos, 3º pregão seguido de queda, menor nível desde 20/08 → https://www.cnnbrasil.com.br/economia/money/mercado/mercado-financeiro-ibovespa-dolar-28-outubro-2026/ → CONFIRMADO. Acumulado de −16,6% nos três pregões desde a reeleição → https://braziljournal.com/a-bolsa-caiu-16-com-lula-ate-agora-mas-o-estrago-e-maior-do-que-parece → CONFIRMADO. Casas Bahia −20% no dia → Brazil Journal → CONFIRMADO. Dólar ~R$ 5,34 (fontes divergem na casa decimal) → PARCIAL.
- Petrobras 3º tri: 3,51 mi boed, +11,7% sobre o 3º tri de 2025, recorde; diesel recorde 769 mil bpd → https://valor.globo.com/empresas/noticia/2026/10/28/petrobras-tem-producao-media-de-oleo-lgn-e-gas-recorde-no-terceiro-trimestre.ghtml → CONFIRMADO (imprensa)
- Santander Brasil 3º tri: lucro R$ 2,9 bi, −28% a/a, 7% abaixo do consenso; ROE 11,9% (17,5% um ano antes) → https://braziljournal.com/lucro-do-santander-cai-28-e-fica-abaixo-do-consenso-roe-vai-a-11-9 → CONFIRMADO
- Fed manteve 3,75%–4,00% em 28/10, por 10 a 2; Lisa Cook e Beth Hammack votaram por alta de 0,25 p.p. → https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm → CONFIRMADO
- Brent: fechou em alta em 28/10 (~US$ 111,6 contrato de janeiro; fontes divergem) → PARCIAL. Usar só "acima de US$ 100" com https://www.wsj.com/finance/commodities-futures/oil-is-gushing-out-of-the-gulf-why-are-prices-still-above-100-a-barrel-3ccff61d (paywall, não lido) → evitar número.
- Raízen: acordo com PGFN e Receita para regularizar R$ 22,4 bi (R$ 16,7 bi da Raízen, R$ 5,7 bi dos controladores); desconto de R$ 8,5 bi sobre a parte da companhia; condição para reestruturar ~R$ 65 bi; assembleia em 30/10 → https://investnews.com.br/negocios/raizen-acordo-tributario-com-a-uniao/ → CONFIRMADO
- Vivo avalia comprar a Vero (1,3 mi de clientes em 425 cidades; dívida líquida R$ 3 bi), sem acordo, segundo fontes da Coluna do Broadcast → https://www.estadao.com.br/economia/coluna-da-broad/vivo-negocia-compra-da-vero-provedora-de-banda-larga/ → CONFIRMADO como "avalia"
- DeltaAI, legaltech apoiada pela Aleve, quer prever decisões judiciais; diz estar perto de R$ 1 mi de faturamento com 3 produtos lançados em março; projeta R$ 3 mi em 2027 → https://startups.com.br/negocios/legaltech/legaltech-apoiada-pela-aleve-quer-prever-decisoes-de-juizes/ → PARCIAL (autodeclarado)
- Anatel exige validação facial para ativar e manter linhas (PF e MEI); base existente até 31/12/2028; linhas irregulares podem ser suspensas a partir de 2029 → https://investnews.com.br/negocios/anatel-exige-reconhecimento-facial-para-ativar-e-manter-linhas-de-celular/ → PARCIAL (ato não visto)
- Weil Gotshal: comitê de gestão recomendou aos sócios em 28/10 uma liquidação ordenada; sócios votam nos próximos dias; receita ~US$ 2,1 bi; 95 anos; saídas de sócios e fusão fracassada com a Willkie → https://news.bloomberglaw.com/business-and-practice/weil-gotshal-to-wind-down-in-stunning-fall-for-heavyweight-firm ; https://abovethelaw.com/2026/10/after-95-years-weil-gotshal-is-winding-down/ → PARCIAL (escrever "recomenda encerrar")
- Microsoft: US$ 10 bi de receita da OpenAI no tri até 30/09, ~11% dos US$ 92,3 bi → https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/ → CONFIRMADO. Azure US$ 33,2 bi, +48%, primeira vez em dólares → https://techcrunch.com/2026/10/28/microsoft-just-shared-azures-actual-revenue-in-dollars-33-2-billion/ → CONFIRMADO
- Gemini 4 Carbon: acesso só para grupo restrito de defensores de cibersegurança; público e desenvolvedores "em breve", sem data; 1º no Artificial Analysis Index (segundo o Google) → https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ ; https://arstechnica.com/ai/2026/10/google-announces-gemini-4-carbon-its-latest-frontier-ai-model-that-you-cant-use/ → CONFIRMADO
- Warren envia carta de 4 páginas a Dario Amodei sobre riscos citados no S-1; prazo de resposta 3/11 → https://aiweekly.co/alerts/warren-gives-anthropic-until-november-3-to-answer-four-pages-of-s-1-existential ; https://www.wsj.com/finance/regulation/elizabeth-warren-demands-answers-from-anthropic-on-existential-risks-5362f009 → PARCIAL
STATS
- Stack Overflow: 1.442 perguntas em julho de 2026, contra 207.204 no pico de março de 2014 (−99%), dados do Data Explorer segundo o PPC Land → https://ppc.land/stack-overflow-drops-to-1-442-questions-in-july-down-99-from-2014-peak/ → PARCIAL (via secundária). "Menos de 1.000 por mês" → NÃO CONFIRMADO. Declínio começou antes do ChatGPT, segundo comentários no HN → opinião.
HOJE EU APRENDI
- O ganso-de-cabeça-listrada tem fama de sobrevoar o Everest, mas GPS em 91 gansos (Hawkes et al., 2013) registrou voo máximo de 7.290 m; eles seguem os vales → https://wetlands.bangor.ac.uk/news/high-flying-geese-take-low-profile-over-himalayas-11065 → PARCIAL (resumo; checar)
LINKS
- https://simonwillison.net/2026/Oct/28/vibe-game-development/ → Willison: ponto de virada no "vibe coding" de jogos → CONFIRMADO
- https://www.technologyreview.com/2026/10/20/1145399/emacs-turns-50/ → Emacs faz 50 anos (Simson Garfinkel) → CONFIRMADO
- https://www.quantamagazine.org/how-spiders-spin-silk-dope-into-natures-toughest-material-20261028/ → como a aranha transforma proteína embolada em fibra resistente → CONFIRMADO (abre, 200)
- OpenAI "future of the firm" → 403, fora.
