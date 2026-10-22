# Verificação, parte 1 (do "bom dia" ao fim de O EXPLICADOR) — Economia, 2026-10-22

Escopo: front matter, "bom dia", `<!-- painel -->` (ignorado, só conferi os números citados "no painel") e "O EXPLICADOR". A edição chega às 06:00 de quinta, 22/10/2026.

Como conferi: Guardian, Money Times (Fitch e XP), Folha, InfoMoney, Valor (CNI) e Euronews abertos com o `ler.py`; o Banco da Inglaterra abriu normal; a página do BC (`historicotaxasjuros`) depende de JavaScript, então conferi a série pela API do próprio BC (a mesma que a página mostra); o FT, pelo resumo do feed (aceito pelo pedido). Os números do painel conferem com `painel.md` e com as APIs do BC (SGS 13522, 433, 13762; Focus via Olinda). Fatos extras que usei para checar o "bom dia": comunicado do Fed de 16/09/2026, tabela de juros do BCE e levantamento da Reuters/BNN Bloomberg de 18/09/2026 (links no fim).

## Tabela de conferência

### Front matter

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| `assunto`: "o mundo sobe o juro, o brasil desce" (minúsculas, 7 palavras) | Fed, BCE, BC (abaixo) | confirmada | nenhuma (mas ver item 6 sobre o Reino Unido) |
| `previa`: "+ o imposto dos dividendos rendeu metade do previsto" | título do O Globo ("metade da previsão do governo para 2026") | confirmada (item da parte 2, coerente com o título da fonte) | nenhuma |
| Título da história 1: "Copom cortou a Selic de 14,50% para 13,75% desde junho" | API do BC (reuniões do Copom) | confirmada | nenhuma |
| Mesmo título: "enquanto Reino Unido e Europa sobem juros com a guerra no Irã" | BoE (set/2026): juro mantido em 3,75%, 6 a 3; Guardian: BoE "vai subir" só em novembro | corrigir | O Reino Unido ainda não subiu. Ver correção 6. |

### Bom dia

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| "Metade do mundo rico voltou a subir os juros por causa do petróleo" | Sem link na edição. Reuters/BNN Bloomberg (18/09): Fed, BCE, Austrália, Nova Zelândia e Japão subiram em 2026; BoE, Canadá, Suécia e Suíça mantiveram. Comunicado do Fed (16/09): alta de 0,25 p.p. para 3,75%-4%. | confirmada no mérito, mas sem fonte e sem apoio no corpo (o texto só mostra o BCE) | Ver correção 3. O comunicado do Fed não cita petróleo (diz "inflação elevada" e "incerteza geopolítica"); a ligação com a energia vem da reportagem. |
| "o Brasil segue cortando" | API do BC: 17/06 (14,25%), 05/08 (14,00%), 16/09 (13,75%) | confirmada | nenhuma |
| "Não é teimosia: é o ponto de partida." | tese do autor | confirmada como moldura | Julgamento leve, aceitável no "bom dia"; ver sugestão S2 se quiser selo. |

### TL;DR e abertura

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| TL;DR: "a guerra no Irã empurrou os juros para cima no Reino Unido e na Europa" | BoE: Bank Rate mantido em 3,75% em 16/09 (3 votos por alta). Guardian: alta só "mais provável" em novembro. BCE subiu em jun. e set. | corrigir | No Reino Unido o juro básico não subiu; subiu o juro de mercado (financiamento imobiliário de 2 anos ~0,95 p.p. mais caro, segundo a BoE). Ver correção 2. |
| TL;DR: Selic de 13,75% "mais de 9 pontos" acima da inflação | 13,75 − 4,58 = 9,17 (conta simples); IPCA 12 meses 4,58% no painel e no SGS 13522 | confirmada | Observação: pela fórmula exata ((1,1375 / 1,0458) − 1) o juro real dá 8,77%. A edição define juro real como "o que sobra do juro depois de descontada a inflação" e usa a mesma subtração para o Reino Unido, então é coerente; ver S3. |
| TL;DR: "A folga existe; o que ameaça os próximos cortes são as expectativas de inflação e as contas públicas" | Fitch: autoridades preocupadas com expectativas e serviços; ajuste fiscal poderia permitir cortes maiores | confirmada como síntese, mas é juízo sem selo nem atribuição | Ver S2. |
| "Na terça (21/10), o Reino Unido soube que a inflação subiu" | Guardian publicado em 2026-10-21; 21/10/2026 é quarta-feira | corrigir | "terça" por "quarta". Ver correção 1. |
| inflação "subiu para 3,5% em setembro" | Guardian: "annual inflation rose from 3.1% in August" a 3,5% | confirmada, falta a comparação | Falta "em 12 meses" e o ponto de partida (3,1% em agosto). Ver correção 4. |
| "acima dos 3,4% que o mercado esperava" | Guardian: previsões da City de 3,4% | confirmada | nenhuma |
| "puxada pelo combustível" | Guardian: combustíveis foram o maior fator da alta em setembro (ONS) | confirmada | nenhuma |
| "O número reforçou a aposta numa alta de juros do Banco da Inglaterra em novembro" | FT (resumo do feed): "will cement expectations of Bank of England rate rise in November"; Guardian: reunião do MPC em 5/11 | confirmada | nenhuma |
| "O BCE já tinha subido em junho, pela primeira vez em três anos" | Euronews: depósito de 2% para 2,25%, "primeira vez em quase três anos" (a última alta foi em set/2023); tabela do BCE: 2,25% em 17/06 e 2,50% em 16/09 | confirmada, mas incompleta e arredondada | O BCE subiu de novo em 10/09 (2,50%). "Quase três anos" é mais exato (2 anos e 9 meses). Ver correção 5. |
| "petróleo e gás dispararam desde o fim de fevereiro, quando EUA e Israel atacaram o Irã" | Guardian | confirmada | nenhuma |
| "o Copom ... cortou a Selic três vezes desde junho, de 14,50% para 13,75%" | API do BC: 29/04 corta para 14,50% (vale desde 30/04); 17/06 → 14,25%; 05/08 → 14,00%; 16/09 → 13,75% | confirmada | Observação: contando desde março foram cinco cortes (15,00% → 13,75%); "desde junho" está certo. "Copom" não é explicado (ver S1). |

### "A diferença está no ponto de partida"

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| juro real = "o que sobra do juro depois de descontada a inflação" | conceito; Fitch usa "taxas reais – descontada a inflação" | confirmada | nenhuma |
| "No Reino Unido, o juro básico está em 3,75%" | BoE, set/2026; Guardian: reunião seguinte em 5/11, sem mudança até hoje | confirmada | nenhuma |
| "e a inflação em 3,5%" | Guardian | confirmada | nenhuma |
| "Sobra 0,25 ponto" | 3,75 − 3,50 = 0,25 | confirmada | Ver S3 sobre "ponto" x "ponto percentual". |
| "pouco para segurar um choque de preços. Por isso, lá, a conversa é de subir." | BoE: 3 dos 9 membros votaram por alta em setembro; "riscos de inflação inclinados para cima" | confirmada como análise (apoiada) | Sugestão: citar o fato (S4). |
| "Selic de 13,75% contra uma inflação de 4,58% em 12 meses (no painel) deixa 9,17 pontos" | painel.md e SGS 13522 (4,58%); 13,75 − 4,58 = 9,17 | confirmada | nenhuma |
| Fitch: "juros reais brasileiros estão muito acima do padrão histórico há vários anos" | Money Times/Fitch: "estão muito acima dos padrões históricos há vários anos" | confirmada | nenhuma |
| Cadeia "Juro real alto » crédito caro » família e empresa gastam menos » os preços sobem menos" | mecanismo geral (Fitch: juros elevados encarecem o financiamento) | confirmada | nenhuma |
| "Esse freio já aparece: a indústria está com a pior satisfação com a margem de lucro desde 2020 ... e a XP vê a arrecadação perdendo fôlego com a atividade mais fraca" | Valor/CNI: 42,2 pontos, "menor desde o 2º trimestre de 2020", causa dada: custos (guerra) e demanda menor. XP: "perda de força ... atividade econômica mais fraca". | os números estão confirmados; a ligação com o juro real não confirmada | Nem a CNI nem a XP atribuem o quadro ao juro alto (a CNI fala em guerra e demanda). É inferência do autor apresentada como fato. Ver correção 7. |

### "O que pode parar a tesoura"

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| Focus IPCA 2026 "subiu de 4,92% para 5,22%" em quatro semanas | painel.md (16/10 x 18/09); Olinda: 4,9205 e 5,219 | confirmada | nenhuma |
| IPCA 2027 "4,32%, longe da meta de 3%" | painel.md; Olinda 4,3206; meta de 3% (teto 4,5%) | confirmada | "Longe" é adjetivo: o número está 1,32 p.p. acima da meta e dentro do teto de 4,5%. Ver S5. |
| "O Focus é a pesquisa semanal do BC com as apostas do mercado" | definição do Focus | confirmada | nenhuma |
| Goldman: "a Petrobras vende diesel 21% abaixo do preço internacional" | InfoMoney: "preço realizado do diesel pela Petrobras (incluindo subsídios do governo)" 21% abaixo da paridade (R$ 5,43 contra R$ 6,89; 5,43 / 6,89 = 0,79) | corrigir | Falta "incluindo subsídios". Sem isso, 21% abaixo e "subir 50%" se contradizem (fechar 21% pediria ~27%). A venda às distribuidoras é a R$ 3,31/l. Ver correção 8. |
| subsídio extra aos importadores "R$ 1,40 por litro, válido até meados de novembro" | InfoMoney: "subsídios adicionais de R$ 1,40/litro ... devem ser válidos até meados de novembro" | confirmada | nenhuma |
| se acabar depois da eleição, Petrobras "teria de subir o diesel às distribuidoras em cerca de 50%, ou R$ 1,50 por litro" | InfoMoney: "cerca de 50% (aproximadamente R$ 1,50/litro)" | confirmada | Sugestão S6: dar a escala (base R$ 3,31/l; ~20% na bomba; IPCA +0,21 a 0,24 p.p.). |
| "O banco não conta com esse reajuste no cenário principal" | InfoMoney: "não incorpora um reajuste em seu cenário-base" | confirmada | nenhuma |
| "A dívida bruta está em 82,9% do PIB (no painel)" | painel.md; SGS 13762: 82,87% (agosto); Folha também traz 82,9% | confirmada | Sem comparação. Ver S7. |
| Grupo Parlatório "de 380 empresários, executivos e representantes da sociedade civil" | Folha | confirmada | nenhuma |
| "escreveu aos dois candidatos" | Folha: carta a Lula e Flávio Bolsonaro | confirmada | O candidato não é o protagonista; ok. |
| "dá para levar a Selic a 7,5% até dezembro de 2027" | Folha: "queda da Selic a 7,5% ao ano e da inflação a 3% já em dezembro de 2027" | confirmada | nenhuma |
| "superávit primário ... de pelo menos 1% do PIB no ano que vem" | Folha: "superávit primário de pelo menos 1% do PIB no próximo ano" | confirmada | A Folha não diz de qual perímetro é a meta de 1% (governo central ou setor público); a edição compara com o setor público consolidado. Ver S8. |
| superávit primário = "receitas maiores que despesas, sem contar os juros" | definição | confirmada | nenhuma |
| "déficit primário de 0,62% do PIB em 12 meses (no painel)" | painel.md ("até agosto") | confirmada | nenhuma |
| Fitch: "PIB de 1,9% em 2026 e de 1,4% em 2027" | Money Times/Fitch | confirmada | A Fitch usa esses números para dizer que há "espaço limitado" para cortar; a edição os põe do lado de "Quem acha que dá para seguir cortando". Ver S9. |
| "a inflação de serviços está perto de 6% há um ano, segundo a Fitch" | Fitch: "estacionada em 6% há um ano" | confirmada | nenhuma |
| "o choque do diesel só foi adiado" | Goldman: cenário-base é preço estável até o fim do ano; reajuste é "risco" | não confirmada (previsão sem selo) | Ver correção 9. |
| Fitch vê Selic em 13,50% no fim do ano ("mais um corte de 0,25 ponto") | Money Times/Fitch: de 13,75% para 13,50%; 13,75 − 13,50 = 0,25 | confirmada | nenhuma |
| Focus: 13,25% ("mais dois") | painel.md; Olinda 13,25; 13,75 − 13,25 = 0,50 = dois cortes de 0,25 | confirmada | nenhuma |
| IPCA-15 de outubro sai sexta (23/10), 9h; "prévia da inflação oficial" | oficiais.md (23/10 09:00) | confirmada | O IBGE dá 403 a robôs; conferido no `oficiais.md`. |
| Próxima decisão do Copom em 4/11 | oficiais.md; calendário do Copom (3 e 4/11, anúncio à noite de 4/11) | confirmada | nenhuma |

### Regras de redação

| Item | Resultado |
|---|---|
| Opinião sem selo | Pontos: "Esse freio já aparece" (correção 7), "o choque do diesel só foi adiado" (correção 9) e, mais leve, a última frase do TL;DR (S2). |
| Recomendação de investimento | Nenhuma na parte 1. |
| Pesquisa eleitoral / candidato protagonista | Nenhuma. O Grupo Parlatório é o sujeito; a eleição entra só como efeito (fim do subsídio do diesel). |
| Termo técnico sem explicação | Explicados: juro real, Focus, superávit primário, IPCA-15 (e Selic, IPCA, meta e resultado primário no painel). Sem explicação: "Copom" (S1); "Fitch", "XP" e "Goldman Sachs" aparecem sem dizer o que são (S1). |
| Número sem escala ou comparação | 3,5% sem "em 12 meses" e sem o ponto de partida (correção 4); 82,9% sem comparação (S7); "50%" sem a base (S6). |
| % x ponto percentual | "9 pontos", "0,25 ponto", "corte de 0,25 ponto" estão certos como diferença de taxas, mas o manual pede "ponto percentual" (S3). |
| Repetição da geral ou do Mercado (`historico --dias 1`) | Sem repetição. O Mercado de hoje deu Brent a US$ 111,95 e o juro da França; a edição não usa. O Focus foi notícia na geral de 19/10 (PIB 1,83% e IPCA 2027 4,32%); aqui entra como argumento, com valor novo (comparação de quatro semanas, meta e mecanismo). Reino Unido, BCE, Fitch, Goldman e Parlatório não saíram em nenhum outro caderno nos últimos 3 dias. |
| Tamanho do explicador | Cerca de 660 palavras (sem as URLs); o manual pede de 350 a 550. Ver S10. |

## Correções obrigatórias

**1. Dia da semana.**
Trocar: `Na terça (21/10), o Reino Unido soube`
Por: `Na quarta (21/10), o Reino Unido soube`
(21/10/2026 é quarta-feira; o Guardian publicou em 21/10 e a própria edição trata 23/10 como sexta.)

**2. TL;DR: o Reino Unido ainda não subiu o juro básico.**
Trocar: `a guerra no Irã empurrou os juros para cima no Reino Unido e na Europa, mas o Brasil partiu de muito mais alto: a Selic de **13,75%** está mais de **9 pontos** acima da inflação.`
Por: `a guerra no Irã empurrou os juros para cima na Europa e nos EUA, e o Banco da Inglaterra deve ir atrás em novembro, mas o Brasil partiu de muito mais alto: a Selic de **13,75%** está mais de **9 pontos percentuais** acima da inflação.`

**3. "Bom dia": a afirmação "metade do mundo rico" não tem fonte nem apoio no corpo do texto.**
Trocar: `Metade do mundo rico voltou a subir os juros por causa do petróleo, e o Brasil segue cortando.`
Por: `O Fed e o Banco Central Europeu voltaram a subir os juros com o petróleo nas alturas, o Banco da Inglaterra deve ir atrás, e o Brasil segue cortando.`
(Fed e BCE ganham link no parágrafo da correção 5. Se preferir manter "metade", acrescentar no corpo, com o link da Reuters/BNN Bloomberg, que cinco dos dez bancos centrais do G10 já subiram juros em 2026 e explicar "G10" em meia frase; não fiz essa troca porque aumenta o texto.)

**4. Inflação do Reino Unido sem a comparação.**
Trocar: `a inflação subiu para **3,5%** em setembro, acima dos 3,4% que o mercado esperava, puxada pelo combustível`
Por: `a inflação em 12 meses subiu de 3,1% em agosto para **3,5%** em setembro, acima dos 3,4% que o mercado esperava, puxada pelo combustível`

**5. BCE incompleto e Fed ausente.**
Trocar: `O Banco Central Europeu já tinha subido em junho, pela primeira vez em três anos ([Euronews](https://www.euronews.com/business/2026/06/11/ecb-raises-interest-rates-for-the-first-time-in-three-years-as-iran-war-fuels-inflation)).`
Por: `O Banco Central Europeu já subiu duas vezes: em junho, pela primeira vez em quase três anos ([Euronews](https://www.euronews.com/business/2026/06/11/ecb-raises-interest-rates-for-the-first-time-in-three-years-as-iran-war-fuels-inflation)), e de novo em setembro, para 2,50% na taxa de depósito ([BCE](https://www.ecb.europa.eu/stats/monetary/rates/html/index.en.html)). O Fed também subiu, em 16/09, para a faixa de 3,75% a 4% ([Fed](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)).`

**6. Front matter: título da história 1.**
Trocar: `Copom cortou a Selic de 14,50% para 13,75% desde junho, enquanto Reino Unido e Europa sobem juros com a guerra no Irã`
Por: `Copom cortou a Selic de 14,50% para 13,75% desde junho, enquanto Fed e BCE sobem juros e o Reino Unido deve subir, com a guerra no Irã`

**7. "Esse freio já aparece" liga à força um quadro que as fontes atribuem a outras causas.**
Trocar: `Esse freio já aparece: a indústria está com a pior satisfação com a margem de lucro desde 2020 (veja abaixo), e a XP vê a arrecadação perdendo fôlego com a atividade mais fraca`
Por: `Há sinais de que a atividade esfria: a indústria está com a pior satisfação com a margem de lucro desde 2020, por custos maiores com a guerra e demanda mais fraca (veja abaixo), e a XP vê a arrecadação perdendo fôlego com a atividade mais fraca`
(manter o link do Money Times no fim da frase. Se o autor quiser manter a ideia de que o juro alto é a causa, precisa escrever como **Opinião:**.)

**8. Diesel: o "21%" é com subsídio.**
Trocar: `a Petrobras vende diesel **21%** abaixo do preço internacional`
Por: `o preço que a Petrobras recebe pelo diesel, já contando os subsídios do governo, está **21%** abaixo do preço internacional`

**9. "O choque do diesel só foi adiado" é previsão sem selo e contradiz o cenário-base do Goldman.**
Trocar: `e o choque do diesel só foi adiado.`
Por: `e o diesel segue como risco: o Goldman vê um reajuste de cerca de 50% às distribuidoras como possível depois da eleição, embora não o ponha no cenário principal.`

## Sugestões (não obrigatórias)

- **S1. Termos.** Na primeira vez: "o Copom, o comitê do BC que define a Selic"; "a agência de risco Fitch"; "a XP" e "o Goldman Sachs" com "banco" ou "casa de análise" na frente.
- **S2. Juízo sem selo.** Atribuir a última frase do TL;DR: `A folga existe; segundo a Fitch, o que limita os próximos cortes são as expectativas de inflação e as contas públicas.` (a Fitch fala das expectativas e do aperto fiscal). O "Não é teimosia" do "bom dia" é aceitável como moldura.
- **S3. Ponto percentual.** Já está em 9 pontos percentuais no TL;DR (correção 2). Na primeira ocorrência do corpo: `Sobra 0,25 ponto percentual`. Sobre o juro real: se quiser blindar a conta, escrever "cerca de 9 pontos" (a fórmula exata dá 8,77%).
- **S4. Reino Unido.** Depois de "a conversa é de subir", acrescentar o fato: `três dos nove membros do comitê do BoE já votaram por subir em setembro ([Banco da Inglaterra](https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/september-2026))`.
- **S5. Focus 2027.** Trocar "longe da meta de 3%" por "1,32 ponto percentual acima da meta de 3%" (o teto da meta é 4,5%, então ainda está dentro dele).
- **S6. Escala do diesel.** Depois de "cerca de 50%, ou R$ 1,50 por litro", acrescentar: `(hoje a Petrobras vende a R$ 3,31 por litro; na bomba, a alta seria de cerca de 20% e empurraria o IPCA em 0,21 a 0,24 ponto percentual, pelas contas do banco)`. Atenção para a parte 2: a linha "Combustível" do bolso fala em "reajuste de cerca de 50%" sem dizer que é no preço às distribuidoras; na bomba o Goldman calcula ~20%.
- **S7. Dívida bruta.** Dar a régua: `82,9% do PIB em agosto, contra 82,6% em julho (no painel)`; ou a meta do grupo (abaixo de 70% até 2030, Folha).
- **S8. Perímetro do 1% do PIB.** A Folha não especifica; se o autor souber que é o setor público consolidado, tudo bem; se não, trocar "o setor público como um todo" por "as contas públicas hoje".
- **S9. Fitch nos dois lados.** Em "Quem acha que dá para seguir cortando diz", acrescentar ao fim: `A Fitch projeta PIB de 1,9% em 2026 e de 1,4% em 2027, mas mesmo assim vê pouco espaço para cortar.`
- **S10. Tamanho.** O explicador tem cerca de 660 palavras; o manual pede de 350 a 550. As correções 5 e 8 e as sugestões S4 e S6 aumentam o texto, então vale cortar uns 100 a 150 palavras: por exemplo, juntar "Aqui, o Copom fez o contrário..." ao TL;DR, enxugar a frase do Parlatório e remover a segunda metade do parágrafo da cadeia `»` (já reescrita na correção 7).

## Fontes extras usadas só para checar o "bom dia"
- Fed, 16/09/2026: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
- BCE, tabela de juros: https://www.ecb.europa.eu/stats/monetary/rates/html/index.en.html
- Reuters/BNN Bloomberg, 18/09/2026: https://www.bnnbloomberg.ca/business/economics/2026/09/18/major-central-banks-on-tightening-path-amid-energy-price-shock/
- API do BC (reuniões do Copom): https://www.bcb.gov.br/api/servico/sitebcb/historicotaxasjuros
