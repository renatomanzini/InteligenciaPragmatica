# Log de verificação: edição nº 2 (17/10/2026)

Checagem independente feita por dois agentes Sonnet. **Todas as correções obrigatórias (7 da parte 1 e 12 da parte 2) foram aplicadas na edicao.md**, junto com a maioria das recomendadas.

## Verificação da edição nº 2 (17/10/2026), PARTE 1

Escopo: do "bom dia" até antes de "O QUE MUDOU DESDE ONTEM" (descompilação por IA, Claude Haiku 5.5, Gemini 4 Argon).
Método: cada fonte citada foi aberta uma vez. A apuração.md foi tratada como pista, não como prova.
Dia da semana conferido no sistema: 07/10/2026 = quarta, 13/10 = terça, 14/10 = quarta, 15/10 = quinta, 17/10 = sábado.

Legenda de status: confirmada / confirmada por fonte alternativa / não confirmada / errada. "Confirmada (ressalva)" = o fato bate, mas o texto precisa de ajuste de precisão.

## 1. Tabela

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|-----------|-------|--------|-------------------|
| 1 | Bom dia: "a semana em que abrir software ficou coisa de dias" | Popcar | Confirmada (ressalva) | A evidência é de jogos. A frase sobre "qualquer software" é palpite do Popcar. Sugestão: "abrir jogos antigos". |
| 2 | Bom dia: "a semana em que usar IA ficou bem mais barato" | Anthropic (Haiku 5.5, 7/10) | Errada (tempo) | O Haiku 5.5 saiu na quarta 7/10, na semana passada. O próprio item 2 diz "antes desta newsletter existir". Ver correção obrigatória 6. |
| 3 | Bom dia: "a semana em que a OAB foi à Justiça" | OAB-SP: "ajuizou nesta quarta-feira (7)" | Errada (tempo e sujeito) | Foi em 07/10 (semana passada) e foi a OAB-SP, uma seccional. Ver correção obrigatória 6. |
| 4 | TL;DR: agentes de IA descompilam jogos e programas "em dias"; antes eram "anos de trabalho de comunidade" | Popcar ("a matter of days, or maybe less"; "took years"; "massive community efforts"); decomp.dev ("on the scale of years") | Confirmada | Nenhuma. |
| 5 | Definição: descompilar é reconstruir como o programa foi escrito | Popcar ("reverse-engineering it from a compiled version back to source code") | Confirmada (ressalva) | Opcional: "reconstruir um código-fonte que faça o mesmo", porque o original não volta idêntico. |
| 6 | "Quem fazia isso eram especialistas ou comunidades inteiras, ao longo de anos" | Popcar; decomp.dev | Confirmada | Nenhuma. |
| 7 | "Na terça (14), o desenvolvedor indie Popcar listou o que mudou" | Popcar (post de "14 Oct, 2026") | Errada | 14/10/2026 foi quarta-feira. Ver correção obrigatória 1. |
| 8 | Popcar é "desenvolvedor indie" | Simon Willison ("Indie game developer Popcar") | Confirmada por fonte alternativa | Nenhuma. |
| 9 | The Binding of Isaac "agora em 1440p e 165 FPS" | Popcar ("native 1440p, smoothly interpolated to 165FPS") | Confirmada (ressalva) | É a versão original em Flash (2011), não o remake, e os 165 FPS são interpolados. Sugestão: "a versão original em Flash, agora em 1440p e 165 FPS". |
| 10 | Colin McRae Rally 2.0 e Final Fantasy Tactics Advance saíram "em dias" | Popcar | Confirmada (ressalva) | Só o Isaac tem prazo explícito ("a few days"). Para os outros dois há só a regra geral. Sugestão: "saíram versões novas de ...; o port do Isaac levou alguns dias, segundo ele". |
| 11 | Título do texto: "awesome and scary" | Popcar ("That's both awesome and scary") | Confirmada | Nenhuma. |
| 12 | Link do Simon Willison (14/10) | simonwillison.net/2026/Oct/14/... | Confirmada | Nenhuma. |
| 13 | "No dia seguinte" (15/10) o decomp.dev anunciou | 404 Media (Jason Koebler, 15/10, 12:31; "said Thursday"). O decomp.dev não traz data. | Confirmada por fonte alternativa | Vale com "quarta (14)" na frase anterior. 15/10 foi quinta. |
| 14 | O decomp.dev "anunciou que vai fechar" | decomp.dev, post "Sunsetting decomp.dev": o site "will continue to track existing projects and serve individual project pages and historical data, but the main index and adding new projects are disabled" | Confirmada (ressalva) | Não fecha por completo. O 404 Media diz "shutting down", mas a fonte primária diz que o site fica no ar como arquivo. Ver correção obrigatória 5. |
| 15 | O decomp.dev é o "ponto de encontro dessa comunidade" | decomp.dev (índice e placar público de progresso) | Confirmada (ressalva) | Era um índice e placar de progresso, não um fórum. Sugestão no texto da correção 5. |
| 16 | Dizendo que a IA "quebrou" o lado comunitário | decomp.dev ("the community aspect of decompilation has been broken", culpando maus atores que abusam de projetos abertos com IA); 404 Media ("broken by AI") | Confirmada por fonte alternativa (ressalva) | "quebrou" entre aspas é tradução, não citação literal. O site atribui a quebra a oportunistas que usam IA. Ver recomendada R2. |
| 17 | REA "liga o agente de IA a programas de inspeção como o Ghidra e roda na máquina do usuário" | README do REA ("Hopper, Ghidra, or IDA"; "Analysis runs locally") | Confirmada | Nenhuma. |
| 18 | "Uma das ferramentas da onda é o REA" | README do REA (não cita jogos nem a onda do Popcar) | Não confirmada | Nenhuma fonte liga o REA a essa onda. Ver correção obrigatória 3. |
| 19 | REA "tem 308 mil estrelas" | `main.py github morluto/rea`: 308.744 estrelas, 78.142 forks | Confirmada (ressalva) | 308.744 arredonda para 309 mil. Sugestão: "mais de 308 mil". |
| 20 | O repositório "existe desde abril" | Mesmo comando: criado em 2026-04-14 | Confirmada | Nenhuma. |
| 21 | Popcar afirma que descompilar é "completamente legal" | Popcar ("Decompiling software is completely legal") | Confirmada (ressalva) | Está atribuído e como opinião dele, correto. As aspas traduzem o inglês. Ver recomendada R2. |
| 22 | Lei 9.609/98 "não fala em descompilação nem em engenharia reversa" | Planalto, texto integral (0 ocorrências de "descompil", "decompil", "engenharia reversa", "reversa") | Confirmada | Nenhuma. |
| 23 | Art. 2º põe o software sob o regime do direito autoral | Art. 2º ("regime de proteção... conferido às obras literárias pela legislação de direitos autorais") | Confirmada | Nenhuma. |
| 24 | Art. 6º não cita descompilação; "integração" do inciso IV vale só para uso exclusivo de quem a fez | Art. 6º, IV ("a integração de um programa... desde que para o uso exclusivo de quem a promoveu") | Confirmada | "a mais próxima" é leitura nossa. Ver recomendada R7. |
| 25 | "Violar o direito do autor de programa é crime (art. 12)" | Art. 12 ("Violar direitos de autor de programa de computador: Pena - Detenção de seis meses a dois anos ou multa") | Confirmada | Opcional: acrescentar a pena. |
| 26 | "Na prática, a resposta depende da licença do software e da finalidade" | Nenhuma. O Planalto não diz isso. | Não confirmada (opinião sem selo) | Ver correção obrigatória 4. |
| 27 | "O próprio REA avisa que é para software que você possui ou está autorizado a examinar" | README do REA ("analysis of software you own or are authorized to examine") | Confirmada | A frase vem logo depois do link do Planalto. Falta link próprio. Ver recomendada R6. |
| 28 | 🚨 "o custo... despencou de anos de especialista para dias de agente" | Popcar (tempo); nenhuma fonte dá custo | Confirmada (ressalva) | Justificativa editorial aceita pelo formato, mas as fontes medem tempo, não custo. Sugestão: "o tempo". |
| 29 | TL;DR 2: Haiku 5.5 custa "cerca de 75% menos" na média | Anthropic ("On average, it now costs around 75% less to run") | Confirmada | Nenhuma. |
| 30 | TL;DR 2: "erra bem menos em tarefas de computador" | Anthropic (OSWorld 2.1, subconjunto offline: 72,4% contra 15,7%) | Confirmada (ressalva) | A fonte mede acerto, não erro. Sugestão: "acerta bem mais em tarefas de computador". |
| 31 | Título: "4 vezes mais barata" | Derivado: 100% − 75% = 25% do custo = 1/4 | Confirmada (cálculo) | Nenhuma. Ver R4 sobre a diferença com o exemplo de US$ 7,50 e US$ 1. |
| 32 | "Saiu em 7/10" | Anthropic (7 de outubro de 2026) | Confirmada | Nenhuma. |
| 33 | "Antes desta newsletter existir" | `main.py historico`: a nº 1 é de 16/10 | Confirmada | Nenhuma. |
| 34 | US$ 0,10 contra US$ 1,00 por milhão de tokens de entrada | Anthropic e página de preços (Haiku 5.5: US$ 0,10 para prompts até 100 mil tokens, US$ 0,50 acima; Haiku 4.5: US$ 1) | Confirmada (ressalva) | Falta o limite. Sugestão: "(para prompts de até 100 mil tokens)". Ver R3. |
| 35 | "Conta o mesmo texto em cerca de 30% mais tokens" | Guia de migração ("approximately 30% more tokens") | Confirmada | Nenhuma. |
| 36 | "A própria Anthropic fala em ~75% de economia média" com o link do guia | O 75% está na página de lançamento (Anthropic), não no guia. A nota 2 dela diz que o cálculo mistura corte de 90% (até 100 mil tokens), corte de 50% (acima) e o tokenizador. | Errada (link errado e explicação incompleta) | Ver correção obrigatória 2. |
| 37 | 1.000 contratos: "cerca de US$ 7,50" no antigo | 1.000 × (5.000 entrada × US$ 1/M + 500 saída × US$ 5/M) = US$ 5,00 + US$ 2,50 = US$ 7,50 | Confirmada (cálculo) | Falta declarar as premissas. Ver R3. |
| 38 | 1.000 contratos: "US$ 1" no novo | Com 30% mais tokens: 6,5M × US$ 0,10 + 0,65M × US$ 0,50 = US$ 0,975. A preço de tabela sem o ajuste: US$ 0,75. | Confirmada (cálculo) | O US$ 1 já embute os 30% extras, e o texto não diz. Ver R3. |
| 39 | Teste de uso de computador: de 15,7% para 72,4% de acerto | Anthropic (OSWorld 2.1, subconjunto offline; Haiku 4.5 15,7%, Haiku 5.5 72,4%) | Confirmada | Opcional: citar "OSWorld 2.1, subconjunto offline". |
| 40 | "Os números são da Anthropic" | Anthropic (benchmarks autorrelatados) | Confirmada | Nenhuma. |
| 41 | Gemini 4 Argon lançado em 13/10 | Google (13 de outubro de 2026) | Confirmada | Nenhuma. |
| 42 | "Só está nos planos pagos" | Google: app para assinantes Ultra e Pro; API só no nível pago; página de preços: "not available on the Free tier" | Confirmada | Nenhuma. |
| 43 | "A partir de R$ 96,99/mês" | gemini.google/subscriptions (pt-BR): AI Pro R$ 96,99. O AI Plus (R$ 24,99) não inclui o Argon. | Confirmada | Nenhuma. |
| 44 | Na API, "custa o mesmo que o modelo anterior até 30/11" | Página de preços: Argon US$ 2 entrada e US$ 10 saída. Gemini 3.1 Pro Preview: US$ 2 e US$ 12 (prompts até 200 mil). O blog do Google não compara com nenhum modelo anterior. | Errada | Entrada igual, saída mais barata. Ver correção obrigatória 7. |
| 45 | "E depois dobra" | Blog e página de preços: US$ 4 e US$ 20 a partir de 1/12 (introdutório até 30/11) | Confirmada | Nenhuma. |
| 46 | "Transparência: escrita com modelos da Anthropic" | Declaração editorial da própria newsletter | Sem fonte externa (declaração de interesse) | Nenhuma. |
| 47 | Trecho copiado (mais de ~15 palavras iguais) | Cotejo com Popcar, decomp.dev, README, Anthropic, Google | Nenhum encontrado | Nenhuma. |
| 48 | Opinião sem selo | Leitura do texto inteiro da Parte 1 | Um caso (#26) | Ver correção obrigatória 4. |

## 2. Correções obrigatórias

### 1. Dia da semana errado ("terça (14)")
- Atual: "Na terça (14), o desenvolvedor indie Popcar listou o que mudou."
- Sugerido: "Na quarta (14), o desenvolvedor indie Popcar listou o que mudou."
- Motivo: 14/10/2026 foi quarta-feira. O "No dia seguinte" (quinta, 15/10) continua correto.

### 2. O 75% está no link errado e a explicação é incompleta
- Atual: "Como o modelo novo conta o mesmo texto em cerca de 30% mais tokens, a própria Anthropic fala em ~**75%** de economia média ([guia](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide))."
- Sugerido: "O preço de tabela cai 90% para prompts de até 100 mil tokens. Mas o modelo novo conta o mesmo texto em cerca de 30% mais tokens ([guia](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide)), e prompts acima de 100 mil tokens custam mais. Por isso a própria Anthropic fala em ~**75%** de economia média ([Anthropic](https://www.anthropic.com/news/claude-haiku-5-5))."
- Motivo: o guia só traz os 30%. O 75% e a nota sobre o corte de 90% e 50% estão na página de lançamento.

### 3. "Uma das ferramentas da onda é o REA" não tem fonte
- Atual: "Uma das ferramentas da onda é o **REA**, que liga o agente de IA a programas de inspeção como o Ghidra e roda na máquina do usuário."
- Sugerido: "Um exemplo de ferramenta do tipo é o **REA**, que liga o agente de IA a programas de inspeção como o Ghidra e roda na máquina do usuário."
- Motivo: o README descreve a ferramenta, mas nenhuma fonte a liga à onda de descompilação de jogos do Popcar.

### 4. Inferência jurídica sem selo de opinião
- Atual: "Na prática, a resposta depende da licença do software e da finalidade ([Planalto](https://www.planalto.gov.br/ccivil_03/leis/l9609.htm))."
- Sugerido: "A lei não resolve a questão. **Opinião:** na prática, a resposta tende a depender da licença do software e da finalidade. ([Planalto](https://www.planalto.gov.br/ccivil_03/leis/l9609.htm))"
- Motivo: o Planalto não diz isso. É conclusão nossa e precisa do selo (manual 14.6). O link fica só para os artigos citados.

### 5. decomp.dev não "fecha": está encerrando o índice
- Atual: "O **decomp.dev**, ponto de encontro dessa comunidade, anunciou que vai fechar, dizendo que a IA "quebrou" o lado comunitário do trabalho ([decomp.dev](https://decomp.dev); [404 Media](...))."
- Sugerido: "O **decomp.dev**, índice e placar da comunidade de descompilação, anunciou que vai encerrar o projeto: o índice principal e a entrada de novos projetos foram desativados, e as páginas dos projetos existentes ficam no ar como arquivo. O autor diz que o lado comunitário da descompilação "foi quebrado" por quem usa IA para bifurcar e portar projetos alheios ([decomp.dev](https://decomp.dev); [404 Media](https://404media.co/video-game-reverse-engineering-community-shuts-down-because-ai-has-made-it-too-easy))."
- Motivo: o post se chama "Sunsetting decomp.dev" e diz que o site continua servindo as páginas e o histórico. Só o 404 Media usa "shutting down". Ajustar também a frase da história em andamento no front matter ("encerra atividades" é aceitável).

### 6. Bom dia com tempo e sujeito errados
- Atual: "bom dia. Foi a semana em que abrir software ficou coisa de dias, e em que usar IA ficou bem mais barato. Também foi a semana em que a OAB foi à Justiça para dizer até onde ela pode ir."
- Sugerido: "bom dia. Foi a semana em que abrir jogos antigos ficou coisa de dias. E duas notícias da semana passada seguem rendendo: usar IA ficou bem mais barato, e a OAB-SP foi à Justiça para dizer até onde a IA pode ir."
- Motivo: o Haiku 5.5 (7/10) e a ação da OAB-SP (07/10) são da semana passada, e o item 2 já admite isso ("antes desta newsletter existir"). Quem entrou na Justiça foi a OAB-SP, não a OAB. O "ela" da última oração era ambíguo.

### 7. Preço da API do Gemini 4 Argon não é "o mesmo" do anterior
- Atual: "Na API, custa o mesmo que o modelo anterior até 30/11 e depois dobra ([Google](...); [planos](...); [preços](...))."
- Sugerido: "Na API, custa US$ 2 de entrada e US$ 10 de saída por milhão de tokens até 30/11 e depois dobra, para US$ 4 e US$ 20. O Gemini 3.1 Pro custa US$ 2 e US$ 12."
- Motivo: a entrada é igual à do 3.1 Pro, mas a saída é US$ 2 mais barata. Nenhum dos links chama o 3.1 Pro de "modelo anterior", então o nome deve aparecer no texto.

## 3. Recomendadas (não obrigatórias)

- **R1. Freio de realidade no item 1.** Falta o contraponto que as próprias fontes dão: o Popcar admite que o código "não fica tão limpo quanto o feito à mão" e que há ports bagunçados, e o decomp.dev diz que a IA ainda precisa de orientação, revisão humana e limpeza. Sugestão: "O próprio Popcar admite que o código não fica tão limpo quanto o feito à mão."
- **R2. Aspas de tradução.** "quebrou" e "completamente legal" são traduções entre aspas. Para não parecer citação literal, usar o original ("completely legal") ou escrever "(tradução nossa)".
- **R3. Premissas da conta do Haiku.** Acrescentar: "(contratos de ~5 mil tokens de entrada e 500 de saída; o US$ 1 já inclui os 30% a mais de tokens; a US$ 0,10 por milhão para prompts até 100 mil tokens)". Sem isso o leitor não reproduz o 7,50 e o 1. Com o preço de tabela puro, sem o ajuste de tokens, a conta daria US$ 0,75.
- **R4. Coerência entre 75% e o exemplo.** O título diz 4 vezes (75%) e o exemplo mostra 7,5 vezes (87%). Explicar em meia frase: "nessa conta específica a economia é maior, porque os prompts são curtos".
- **R5. 308 mil estrelas.** Trocar por "mais de 308 mil" (308.744 arredonda para 309 mil).
- **R6. Link do REA no aviso.** A frase "O próprio REA avisa..." vem logo depois do link do Planalto. Acrescentar ([GitHub](https://github.com/morluto/rea)) para não parecer que a lei diz isso.
- **R7. "A mais próxima" (art. 6º, IV).** É avaliação nossa. Sugestão: "a que mais se aproxima, na nossa leitura, é a 'integração' do inciso IV".
- **R8. Ordem do texto sobre o Isaac e prazos.** Ver linhas 9 e 10 da tabela (versão Flash original; "alguns dias" só vale para o Isaac).
- **R9. Link do decomp.dev.** A home é o próprio post de encerramento hoje, mas pode mudar. Se achar um permalink, trocar.

## Verificação da Parte 2: edição nº 2 (sábado, 17/10/2026)

Escopo: de "O QUE MUDOU DESDE ONTEM" até a pergunta. Cada link foi aberto uma vez. Fontes lidas: The Verge (2), página dos termos da Meta (versão em inglês e em português, no navegador), Planalto (EC 141, Lei 8.906, LC 95, Código Civil), Agência Câmara, DealStreetAsia/Reuters, Simon Willison, The Next Web, XBOW (post e post-companheiro), GitHub (`main.py github` e API), GitHub Blog, OpenAI (no navegador, o curl leva 403), Bloomberg Law, OAB-SP, Lawletter, Startups, Popcar, MIT Technology Review, Import AI 476. Também conferi a edição nº 1 (16/10) para as frases "ontem escrevemos...".

Status: **OK** = a fonte diz isso. **RESSALVA** = verdadeiro, mas falta contexto. **CORRIGIR** = a fonte não diz isso ou diz outra coisa. **SEM FONTE** = não está no link citado.

## 1. Tabela

| # | Afirmação (texto da edição) | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Meta "tirou dos novos termos a frase que permitia usar 'qualquer conteúdo' dos sites para 'treinar' produtos" | Verge; termos (EN) | **RESSALVA** | A frase "Meta may use any content from such domains... train..." sumiu da versão em **inglês** (confirmado). Mas (a) a versão em **português do Brasil** da mesma página ainda trazia a frase antiga ("A Meta pode usar qualquer conteúdo... treinar...") na noite de 17/10; (b) "any content" segue no trecho do rastreamento: "(and any content available through them)"; (c) "permitia" é forte demais: a Verge diz que a frase "may have allowed" e que "especialistas" a leram assim. Ver correção 5. |
| 2 | O robô "continua autorizado nos sites de clientes comerciais, agora para 'desenvolver, melhorar, pesquisar e manter' produtos de anúncio e negócio" | termos (EN) | **OK (com ressalva leve)** | Texto atual: "provide, develop, improve, research, and maintain advertising and business products". A edição omite "fornecer". A autorização cobre também páginas "disponibilizadas pelo uso dos produtos Meta por você ou pelos usuários", não só sites de clientes. Aceitável como resumo. |
| 3 | A Meta diz que "não é sobre raspar sites de notícia" | Verge | **OK** | Tradução de "This is not about scraping news sites" (porta-voz Daniel Roberts, em declaração à Verge de 17/10). Sugestão: dizer "um porta-voz da Meta" em vez de "A Meta", e que a frase vem traduzida. |
| 4 | "depois da reação" (Meta) | Verge | **OK** | "After backlash, Meta is updating its terms again". Publicado 17/10, 15h04 UTC (12h04 em Brasília). |
| 5 | Delta impede agentes de comprar passagens | Verge | **OK** | "preventing them from booking tickets on behalf of users". |
| 6 | JPMorgan e Schwab bloqueiam agentes nas contas | Verge | **OK** | "confirmed that they're blocking AI agents from accessing accounts due to security concerns". |
| 7 | Yelp só libera quem paga pela licença de dados | Verge | **OK** | A fala é do Yelp **ao TechCrunch**, relatada pela Verge. Opcional: "disse o Yelp ao TechCrunch". |
| 8 | "Ontem falamos de agente invadindo sistema" | Edição 16/10 | **OK** | Item 1 da edição nº 1 ("O agente aprontou"). |
| 9 | "Ontem escrevemos que a jornada de 42h valeria 'em 60 dias'" | Edição 16/10 | **OK** | Texto da nº 1: "Em 60 dias, a jornada máxima cai para 42h". |
| 10 | A emenda diz "2 meses após a publicação" | EC 141, art. 6º, I | **OK** | Art. 6º, I: "2 (dois) meses após a publicação". Publicada no DOU de 16/10/2026 (edição extra), data de 16/10 no texto. |
| 11 | "ou seja, a partir de **16/12/2026**" | EC 141 + contagem | **RESSALVA** | A emenda **não traz data**. É inferência nossa e a contagem tem duas leituras: **16/12** (fim do prazo, Código Civil art. 132, §3º: prazo de meses expira "no dia de igual número do de início") ou **17/12** (LC 95/98, art. 8º, §1º: conta-se com a inclusão do dia da publicação e do último dia, e a regra vale "no dia subsequente"). Ver correção 2. |
| 12 | "As 40h vêm um ano depois" | EC 141, art. 6º, II | **OK** | Art. 6º, II: "1 (um) ano após o decurso do prazo de que trata o inciso I". Ou seja, 12 meses depois dos 2 meses (14 meses da publicação). |
| 13 | "A Câmara **já adotou** a escala nova para ~1.700 terceirizados" | Agência Câmara 16/10 | **CORRIGIR** | A matéria diz que Motta "afirmou que a Casa **vai implementar** imediatamente" e que fará "os ajustes **a partir da próxima semana**". Não "já adotou". O número (~1.700 terceirizados na 6x1) está certo. Ver correção 1. |
| 14 | Anthropic: US$ 16,8 bi no 3º tri | Reuters (DealStreetAsia); Simon Willison (FT) | **OK** | Reuters e FT batem em US$ 16,8 bi. |
| 15 | "cerca de 45% acima do anterior" | Reuters | **OK** | Reuters: +45% (US$ 11,6 bi no 2º tri). O FT, via Simon Willison, diz "quase 50%" (US$ 11,5 bi). Opcional: citar a diferença. |
| 16 | "segundo investidores que estavam na apresentação da empresa" | Reuters; FT | **RESSALVA** | Reuters (texto do DealStreetAsia): "an investor who attended" (um investidor). O TNW diz que a Reuters citou dois presentes; o FT cita "pessoas com conhecimento do assunto". Plural defensável, mas o link da Reuters diz "um investidor". |
| 17 | "A empresa não publicou os números nem comentou" | Reuters; TNW/Bloomberg | **CORRIGIR** | Reuters: "did not **immediately** respond" (não respondeu de imediato). Quem diz que a empresa "não publicou" e "recusou comentar" é o TNW, citando a Bloomberg. A Anthropic **falou** aos investidores no evento. Ver correção 3. |
| 18 | "e o IPO pode vir em novembro" | (nenhum dos dois links) | **SEM FONTE** | Reuters: estreia "likely to be pushed until **after** the November US midterm elections". Quem fala em datas é a **Bloomberg**, via TNW: marketing "as early as the week of November 9", negociação "before Thanksgiving on November 26", e "plans remain fluid". Previsão precisa de quem aposta (manual 14.6). Ver correção 3. |
| 19 | XBOW: US$ 40 mil de gasto em IA | XBOW (post principal) | **OK** | "The compute we used over six days for the awarded chain cost $40,000". |
| 20 | "em 6 dias, um ataque completo ao Chrome" | XBOW | **RESSALVA** | De 2 a 7/08 (domingo a sexta) ✓. Mas o post-companheiro diz que a **primeira** cadeia levou ~2 meses e foi descartada (o Google já conhecia uma das falhas); os 6 dias foram a segunda montagem, "drawing on the earlier experience". Falta contexto. |
| 21 | "o Google pagou US$ 250 mil de recompensa" | XBOW | **RESSALVA** | XBOW: "won our company a $250,000 bounty" / "Google awarded this chain the first $250,000 Chrome full-chain reward". É a XBOW quem diz; o Google não confirmou publicamente. "Pagou" vira "concedeu, segundo a XBOW". |
| 22 | "A XBOW estima que, sem IA, seriam 4 pessoas por 6 a 9 meses" | XBOW (post principal) | **SEM FONTE** | **Não está no link citado.** Está no post-companheiro: "Pre-LLMs a Chrome full chain would take a team of four around 6-9 months to be produced, our first submission took 2 months. The awarded one? six days." (https://xbow.com/labs/research/zero-to-calc-in-six-days-inside-xbow-chrome-full-chain). Ver correção 4. O post principal só traz "seis meses" (fala de um veterano de inteligência) e "mais de meio ano". |
| 23 | "O relato é da própria empresa, e a falha já foi corrigida" | XBOW | **OK** | "The bugs are now fixed". O texto é autorrelato. |
| 24 | OpenClaw: 392 mil estrelas | GitHub (`main.py github`) | **OK** | `main.py`: 392.292 estrelas, 82.458 forks, criado em 2025-11-24. A API deu 392.291 e licença MIT (confirma "código aberto"). |
| 25 | "eram 388 mil no fim de agosto" | GitHub Blog | **OK** | "approximately 388,000 stars... by August 26, 2026". Mais exato: "em 26/08". |
| 26 | "O hype também estaciona." | (juízo) | **CORRIGIR (selo)** | Juízo sem `**Opinião:**`. Troque por fato: "Em sete semanas, ganhou só ~4 mil estrelas" (388 mil em 26/08 → 392 mil em 17/10), ou ponha o selo. |
| 27 | S&C criou com a OpenAI o Agreement Analyzer | OpenAI; Bloomberg Law | **OK** | "In collaboration with OpenAI, Sullivan & Cromwell developed Agreement Analyzer". |
| 28 | "Em Nova York" | OpenAI; Bloomberg Law | **RESSALVA** | As fontes não situam o projeto em Nova York. A OpenAI diz "North America"; a Bloomberg diz que o sócio Savva é de **Palo Alto** (a ferramenta foi apresentada em Nova York, num evento da OpenAI). Use "Nos EUA". |
| 29 | Advogado "põe a minuta, os precedentes e o 'playbook' do escritório" | OpenAI | **OK** | "a lawyer can add their own selected precedents and a playbook with firm and client positions". |
| 30 | "Agentes revisam por ângulos diferentes, e outros agentes **contestam** os achados" | OpenAI | **RESSALVA** | A OpenAI escreve "Savva describes an application in which agents develop conclusions and other agents challenge them" e "**In a potential use case**, specialized agents review...". O texto fala de um caso/aplicação descrito por Savva, não afirma sem ressalva que é o fluxo de produção. Atribua: "segundo a OpenAI, o sócio descreve...". |
| 31 | Saída: memorando com alterações em controle de alterações, que o advogado "revisa, adapta ou rejeita" | OpenAI | **OK** | "returns a memorandum and proposed tracked changes for a lawyer to review, adapt or reject". |
| 32 | "O caso americano é um estudo de caso publicado pela própria OpenAI e não traz nenhum número de desempenho" | OpenAI; Bloomberg | **OK** | Nenhum número de desempenho. Savva (Bloomberg): benefício é "análise mais minuciosa no mesmo prazo", não corte de tempo. Dado de contexto: a ferramenta foi apresentada em **17/09** (Bloomberg Law, 29/09); o estudo da OpenAI é de 15/10. |
| 33 | OAB-SP entrou em **07/10** com ação civil pública contra a Enter | OAB-SP; Lawletter | **OK** | "nesta quarta-feira (7)", 07/10/2026. |
| 34 | "Nesta semana, ela virou processo" (abertura da seção) | OAB-SP | **CORRIGIR** | 07/10 foi a quarta da **semana passada** (dez dias antes de 17/10). Regra de datas (manual 14.7). Ver correção 6. (A abertura da edição, "a semana em que a OAB foi à Justiça", repete o problema.) |
| 35 | Processo nº 5031169-20.2026.4.03.6100 | Lawletter | **OK** | "Processo: 5031169-20.2026.4.03.6100, em tramitação na 4ª Vara Cível Federal de São Paulo". O número não aparece no texto da página da OAB-SP. |
| 36 | Tese: plataforma pratica atos privativos da advocacia sem ser sociedade de advogados | Startups (petição); Lawletter | **OK** | Citação da petição no Startups: "ato privativo da advocacia por empresa não registrada na OAB como sociedade de advocacia". |
| 37 | Pedido: "que todo contrato tenha advogado responsável identificado, sob multa de **R$ 50 mil por contrato**" | Lawletter; OAB-SP | **CORRIGIR** | R$ 50 mil por contrato é a multa do **pedido de urgência** que impede **novos contratos ou ampliação dos existentes** sem identificação do advogado responsável e registro de revisão. (Também reaparece na hipótese subsidiária.) No pedido principal, a identificação é **por minuta**, com multa de R$ 1 mil por minuta. "Todo contrato" é exagero. Ver correção 7. |
| 38 | Pedido: "supervisão humana auditável" | OAB-SP | **OK** | "supervisão humana efetiva, verificável e auditável por advogados em todas as etapas". |
| 39 | Pedido: "R$ 1 milhão de dano moral coletivo" | Lawletter; Startups | **OK** | "R$ 1 milhão por danos morais coletivos, ou outro valor que venha a ser fixado pela Justiça", para o Fundo de Defesa de Direitos Difusos. |
| 40 | A Enter "nega que substitua advogados e diz que a revisão, a assinatura e o protocolo ficam com eles" | Lawletter; Startups | **OK** | Nota da Enter: revisão, assinatura, protocolo e responsabilidade ficam com advogados das empresas-clientes. |
| 41 | "Não há decisão até agora" | Lawletter | **CORRIGIR** | A única fonte com os autos (Lawletter) é de 07/10, 20h28: "ainda não consta decisão". Não achei notícia de decisão depois disso, mas isso é ausência de notícia, não prova. Escreva "Não encontramos decisão até 17/10". |
| 42 | "A base é o Estatuto da Advocacia: são privativas da advocacia a postulação ao Judiciário e a consultoria, a assessoria e a direção jurídicas (Lei 8.906/94, art. 1º)" | Planalto | **RESSALVA** | O texto do art. 1º está **correto**: "I - a postulação a qualquer órgão do Poder Judiciário e aos juizados especiais" (com "Vide ADIN 1.127-8"); "II - as atividades de consultoria, assessoria e direção jurídicas". Mas **nenhuma das três fontes da ação cita o art. 1º** (busca por "8.906", "Estatuto" e "art. 1" deu zero nelas). "A base é" afirma o que a petição invoca; é leitura nossa. Ver correção 8. |
| 43 | "O freio": a fronteira ferramenta × substituto "não foi julgada"; o brasileiro "não tem decisão" | Lawletter | **RESSALVA** | Mesma ressalva da linha 41. |
| 44 | "Quem cria legaltech: os pedidos da OAB-SP são, na prática, um checklist de produto" | (juízo) | **RESSALVA (selo)** | É leitura nossa, sem selo. Ponha `**Opinião:**` ou reescreva como "dá para ler os pedidos como checklist". "nada de vender como 'substituto'" bate com o pedido de suspender anúncios que apresentem o produto "como substitutos de advogados". |
| 45 | `**Opinião:**` do "Como isso vira serviço" | (juízo) | **OK** | Selo presente. |
| 46 | Para ler: texto do Popcar, em inglês, "com os dois lados" | Popcar | **OK** | "awesome and scary", com os dois lados. Observação editorial: é a mesma fonte principal do breakthrough nº 1. |
| 47 | Para ler: "Rins de porco 'congelados' por um ano voltaram a funcionar" | MIT TR | **CORRIGIR** | Foi **um** rim guardado por pouco mais de um ano; testado em máquina de perfusão (produziu urina "imediatamente"). Os transplantados em porcos estavam guardados por dias ou semanas e foram monitorados por 2 horas. Os rins produziram cerca de 2/3 da urina esperada e tinham sinais de lesão. Ver correção 9. |
| 48 | "Ainda é preprint" e "um órgão humano dura de 24 a 36 horas fora do corpo" | MIT TR | **OK** | "shared at the preprint server bioRxiv and has not yet been peer-reviewed"; "24 to 36 hours, which is the current limit". |
| 49 | Import AI 476, de Jack Clark: "por que os modelos abertos ocidentais seguem atrás dos chineses" | Import AI | **RESSALVA** | O texto (12/10) compara o Beam (EUA) e o Mistral Large 4 com o GLM-5.3 chinês e diz que os EUA saíram da fronteira dos abertos "largely because Meta stopped making good LLaMA models". Mas também fala em "America returns to open weight models" (o Beam seria uma chance de voltar). "Por que... seguem atrás" supera o texto. |
| 50 | "Clark é cofundador da Anthropic" | (sem link) | **SEM FONTE** | A página do Import AI não diz isso. É fato conhecido, mas a regra 14.1 pede link. Cite a página oficial da Anthropic (ou a Wikipedia) e mantenha a nota de transparência. |
| 51 | Pergunta da semana | — | **OK** | Sem afirmação factual. |

Links: todos os links da Parte 2 abriram (HTTP 200; OpenAI e Facebook só pelo navegador, que o curl não passa). Nenhum link quebrado. Não achei trecho copiado nem aspas inexistentes; as aspas sobre a Meta são tradução de falas em inglês (curtas, dentro do limite de 15 palavras).

## 2. Correções obrigatórias

### 1. Câmara: "já adotou" não procede
- **Atual:** "A Câmara já adotou a escala nova para ~1.700 terceirizados"
- **Sugerido:** "O presidente da Câmara, Hugo Motta, mandou aplicar já a escala nova aos ~1.700 terceirizados da Casa, a partir da próxima semana"
- **Motivo:** a Agência Câmara (16/10, 16h53) diz que a Casa "vai implementar imediatamente" e fará os ajustes "a partir da próxima semana". Tempo verbal errado (manual 14.7).

### 2. 6x1: a data 16/12 é conta nossa e tem duas leituras
- **Atual:** "A emenda diz **2 meses após a publicação**, ou seja, a partir de **16/12/2026**."
- **Sugerido:** "A emenda diz **2 meses após a publicação**. Publicada em 16/10, o prazo termina em **16/12/2026** (conta nossa: a emenda não traz a data, e há quem conte o início só a partir de 17/12)."
- **Resposta sobre a regra de contagem:** em meses, o prazo termina no dia de mesmo número do início (Código Civil, art. 132, §3º, exclui o dia da publicação), então **16/12/2026 dá**, como **fim do prazo**. Se aplicarmos, por analogia, a regra de vacância das leis (LC 95/98, art. 8º, §1º: inclui o dia da publicação e o último dia, e vale "no dia subsequente à consumação integral"), a regra passa a valer em **17/12/2026**. A Lei 810/49 (conceito de mês) não abriu no Planalto, então não foi conferida. Aplicar a LC 95 a uma emenda é analogia, e o art. 10, I da emenda ("após decorridos 2 meses de sua publicação") usa linguagem de vacância. Em qualquer leitura, as 40h caem no mesmo dia um ano depois (16 ou 17/12/2027). O "60 dias" que o Senado repetiu daria 15/12, por isso a correção de ontem é real, só que de 1 a 2 dias.
- **Ajuste também no front matter:** `titulo: "EC 141: 42h a partir de 2 meses da publicação (16/12)..."` para "(fim do prazo em 16/12)".

### 3. Anthropic: atribuição e data do IPO
- **Atual:** "segundo investidores que estavam na apresentação da empresa. A empresa não publicou os números nem comentou, e o IPO pode vir em novembro ([Reuters]; [Simon Willison])."
- **Sugerido:** "segundo um investidor que estava na apresentação (Reuters) e pessoas a par do assunto (FT, via Simon Willison). A Anthropic não publicou os resultados e não quis comentar à Bloomberg. A aposta da Bloomberg é que o marketing do IPO comece na semana de 9/11 e as ações negociem antes de 26/11, mas os planos podem mudar ([Reuters](https://www.dealstreetasia.com/?p=498196); [Simon Willison](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/); [The Next Web, citando a Bloomberg](https://thenextweb.com/news/anthropic-q3-revenue-16-8bn-ipo))."
- **Motivo:** "pode vir em novembro" não está em nenhum dos dois links. A Reuters diz que a estreia deve ficar para **depois** das eleições americanas de novembro; as datas vêm da Bloomberg (via TNW). "Nem comentou" é mais forte que "não respondeu de imediato" (Reuters).

### 4. XBOW: "4 pessoas por 6 a 9 meses" está em outro link
- **Atual:** "A XBOW estima que, sem IA, seriam 4 pessoas por 6 a 9 meses. O relato é da própria empresa... ([XBOW](https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit))"
- **Sugerido:** "A XBOW diz que, antes dos LLMs, uma equipe de 4 levaria de 6 a 9 meses; a primeira tentativa dela levou 2 meses e foi descartada, e a segunda, 6 dias. O relato é da própria empresa, e as falhas já foram corrigidas ([XBOW](https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit); [post técnico](https://xbow.com/labs/research/zero-to-calc-in-six-days-inside-xbow-chrome-full-chain))."
- Troque também "o Google pagou" por "o Google concedeu, segundo a XBOW,".

### 5. Meta: a mudança só está confirmada na versão em inglês
- **Atual:** "tirou dos novos termos a frase que permitia usar 'qualquer conteúdo' dos sites para 'treinar' produtos."
- **Sugerido:** "tirou dos novos termos (na versão em inglês) a frase que, para especialistas, podia permitir usar 'qualquer conteúdo' dos sites para 'treinar' produtos. A tradução em português ainda trazia a frase antiga na noite de 17/10. O trecho do rastreamento continua falando em 'qualquer conteúdo disponível' nas páginas."
- **Front matter:** `titulo: "Meta tira 'treinar' e 'qualquer conteúdo' dos termos..."` vira "Meta tira 'treinar' dos termos em inglês; robô segue autorizado para anúncios".
- **Motivo:** a página em português (pt-br.facebook.com) conserva "A Meta pode usar qualquer conteúdo desses domínios... para fornecer, desenvolver, melhorar, pesquisar, treinar e manter...". O leitor brasileiro que clicar em [termos] pode ver o contrário do que a edição diz. Cheque de novo antes de enviar; pode ser só atraso da tradução. Se já estiver atualizada, basta tirar a ressalva da tradução e manter o resto.
- A fala é do porta-voz Daniel Roberts: "um porta-voz da Meta diz".

### 6. Enter: data da semana
- **Atual:** "Nesta semana, ela virou processo."
- **Sugerido:** "Na semana passada, ela virou processo." (07/10 foi a quarta da semana anterior.) Ajuste o mesmo em "Também foi a semana em que a OAB foi à Justiça" na abertura.

### 7. Enter: o pedido dos R$ 50 mil
- **Atual:** "que todo contrato tenha advogado responsável identificado, sob multa de **R$ 50 mil** por contrato;"
- **Sugerido:** "que novos contratos (ou a ampliação dos atuais) só saiam com advogado responsável identificado e registro de revisão, sob multa de **R$ 50 mil** por contrato; e, no pedido principal, advogado responsável identificado em cada minuta;"
- Troque também "Não há decisão até agora" por "Não encontramos decisão até 17/10 (os autos que a Lawletter viu, em 07/10, não tinham)".

### 8. Enter: "A base é o Estatuto" é nossa leitura
- **Atual:** "⚖️ A base é o Estatuto da Advocacia: são privativas da advocacia..."
- **Sugerido:** "⚖️ A ideia de 'ato privativo' vem do Estatuto da Advocacia: são privativas a postulação a qualquer órgão do Poder Judiciário e as atividades de consultoria, assessoria e direção jurídicas (Lei 8.906/94, art. 1º). As matérias sobre a ação não citam o artigo."
- O texto da lei está correto.

### 9. Rins de porco: foi um rim
- **Atual:** "Rins de porco 'congelados' por um ano voltaram a funcionar"
- **Sugerido:** "Um rim de porco guardado por pouco mais de um ano a −150 °C voltou a funcionar (os outros ficaram dias ou semanas). Ainda é preprint, e os rins mostraram lesão e produziram cerca de 2/3 da urina esperada."

### 10. Sullivan & Cromwell: atribuir os "agentes que contestam"
- **Atual:** "**Em Nova York**, o escritório Sullivan & Cromwell criou com a OpenAI o **Agreement Analyzer**. ... Agentes revisam por ângulos diferentes, e outros agentes **contestam** os achados."
- **Sugerido:** "**Nos EUA**, o escritório Sullivan & Cromwell criou com a OpenAI o **Agreement Analyzer**, apresentado em 17/09. No estudo de caso da OpenAI, o sócio John Savva descreve agentes que revisam por ângulos diferentes e outros que contestam os achados."
- **Motivo:** a OpenAI diz "describes an application in which..." e "In a potential use case", e não situa o projeto em Nova York (Savva é de Palo Alto).

### 11. Opinião sem selo
- "O hype também estaciona." (OpenClaw): troque por fato ("em sete semanas, ganhou só ~4 mil estrelas") ou ponha `**Opinião:**`.
- "os pedidos da OAB-SP são, na prática, um checklist de produto" (legaltech): ponha `**Opinião:**` ou reescreva como "dá para ler os pedidos como um checklist".

### 12. Import AI e Jack Clark
- **Atual:** "por que os modelos abertos ocidentais seguem atrás dos chineses. Clark é cofundador da Anthropic."
- **Sugerido:** "mostra dois modelos abertos ocidentais novos (o Beam, dos EUA, e o Mistral Large 4, da Europa) ainda um pouco atrás do GLM-5.3, chinês. Clark é cofundador da Anthropic ([Anthropic](https://www.anthropic.com/company))." (O link da Anthropic é sugestão minha e não foi aberto; confira antes de usar.)

## 3. Pontos opcionais (não obrigatórios)
- **OAB-RJ:** um artigo de opinião da Migalhas (13/10) diz que a seccional do Rio pediu, dois dias depois do ajuizamento, para entrar no polo ativo. É texto de opinião e não foi confirmado em outra fonte; só entre se achar fonte noticiosa.
- **Duplicidade:** o primeiro "Para ler" repete o Popcar, que já é a fonte do breakthrough nº 1.
- **Anthropic:** citar que o FT fala em "quase 50%" ajuda a mostrar que o número depende da base do 2º tri (US$ 11,5 bi no FT, 11,6 bi na Reuters).
