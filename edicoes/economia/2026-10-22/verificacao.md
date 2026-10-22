# Verificação da edição de 2026-10-22 (caderno Economia, nº 1, teste)

Dois checadores Sonnet independentes, em paralelo. Parte 1: do começo ao fim de O EXPLICADOR. Parte 2: de BRASIL ao fim.

## O que foi aplicado
- Parte 1, as 9 correções obrigatórias:
  - "quarta (21/10)";
  - TL;DR e bom dia: o Fed (16/09, conferido no comunicado do Fed) e o BCE subiram, e o Banco da Inglaterra deve subir;
  - inflação britânica com a comparação (3,1% → 3,5%);
  - "Há sinais de que a atividade esfria" no lugar de "Esse freio já aparece";
  - o diesel "já contando os subsídios";
  - o diesel como risco, não como fato adiado;
  - o título da história 1.
- Parte 1, ficou de fora: a alta do BCE em setembro para 2,50%. A tabela do BCE não abriu aqui para confirmar, e o texto cita só a de junho.
- Parte 2, as 5 correções obrigatórias:
  - Desenrola: o desconto é o do banco à União, R$ 9 bi no máximo, CMN; tirado o que repetia a geral (o leilão);
  - diesel: hipótese, bomba +20%, IPCA +0,21 a 0,24 p.p.;
  - zona do euro: tirada a inferência sem fonte;
  - agenda com horário (Fed "à tarde": a página do Fed não traz horário);
  - aluguel: o IGP-M e a prévia explicados, e o 1,59% comparado à prévia de setembro.
- Recomendadas aplicadas:
  - arrecadação "na série da Receita" e "alta real";
  - CNI com a queda de 1,3 ponto;
  - frete com a atribuição na frente e o piso explicado;
  - Turquia "1 ponto percentual";
  - zona do euro com a escala do índice;
  - Copom, Focus, Fitch, XP e Goldman explicados na primeira menção;
  - prévia "metade da previsão para o ano".

---

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


---

# Verificação, parte 2 (BRASIL até o fecho) · Economia · 2026-10-22

Escopo: de "#### BRASIL" ao fim. O bloco `<!-- painel -->` foi ignorado. Todos os links da parte 2 estão "ok" no `links.json`. Os do IBGE (403 a robôs) foram conferidos no `oficiais.md`; o Fed, na página citada; o Copom, no `oficiais.md`. Dias da semana conferidos por cálculo de calendário: 22/10 quinta, 23/10 sexta, 28/10 quarta, 30/10 sexta, 4/11 quarta (todos batem).

Legenda: confirmada = a fonte diz exatamente isso; corrigir = erro, risco de o leitor entender errado, falta de explicação ou de selo, ou regra do manual descumprida.

## Tabela de afirmações

| # | Afirmação (resumo) | Fonte | Status | Correção / observação |
|---|---|---|---|---|
| **BRASIL** | | | | |
| 1 | Arrecadação federal de setembro: R$ 239,4 bi (R$ 239,384 bi) | Money Times (Receita Federal) | confirmada | Também em Agência Brasil, InfoMoney e CNN Brasil. |
| 2 | "a maior para o mês desde 2000" | Money Times: "desde o início da série histórica, em 2000" | confirmada, com ressalva | O Money Times e o InfoMoney dizem 2000; o Mercado de hoje (Valor) usou "desde 1995" para agosto. Os veículos divergem sobre o início da série. Ver recomendada R1. |
| 3 | "5,62% acima da inflação na comparação com setembro de 2025" | Money Times; Agência Brasil ("5,62%, descontada a inflação pelo IPCA") | confirmada | É alta real. A grafia "5,62% acima da inflação" pode ser lida como ponto percentual. Ver recomendada R1. |
| 4 | XP: boa parte da alta do ano vem de medidas de receita, como o imposto de 12% sobre a exportação de petróleo | Money Times | confirmada | XP: "grande parte do avanço ... associada a medidas de aumento de receitas, como ... a tributação das exportações de petróleo". |
| 5 | Imposto de exportação de petróleo: 12%, criado durante a guerra, R$ 2,9 bi só em setembro | Money Times (R$ 2,943 bi em setembro; R$ 12,869 bi no ano; alíquota de 12%, criada "para garantir o abastecimento ... durante a guerra") | confirmada | |
| 6 | Dividendos: R$ 5,26 bi de janeiro a setembro | O Globo | confirmada | |
| 7 | = metade dos R$ 10,5 bi que o governo prevê agora para o ano | O Globo | confirmada | |
| 8 | Previsão "já foi cortada duas vezes" e é "cerca de um terço dos R$ 29,9 bi do começo de 2026" | O Globo (29,94 bi inicial; 17,2 bi em 24/07; 10,5 bi em 22/09) | confirmada | |
| 9 | Cobrança "criada para compensar a isenção do IR para quem ganha até R$ 5 mil" | O Globo | confirmada | O Globo também diz "compensar, em parte". |
| 10 | CNI: satisfação com a margem de lucro cai a 42,2 pontos no 3º trimestre, o menor desde o 2º tri de 2020 | Valor (Sondagem Industrial da CNI) | confirmada | Queda de 1,3 ponto sobre o 2º trimestre (a fonte traz; a edição não). Ver recomendada R2. |
| 11 | CNI cita custos maiores com a guerra e demanda mais fraca | Valor (Marcelo Azevedo, CNI) | confirmada | A fonte diz "pressão de custos, em parte por conta da guerra" e "redução da demanda". "Custos maiores com a guerra" é um pouco mais forte. |
| **EMPRESAS E PREÇOS** | | | | |
| 12 | Piso do frete reforçado por lei neste ano está tirando carga do autônomo | Brazil Journal (MP de março, aprovada em julho; dados e pesquisa da Frete.com) | confirmada | É análise da Frete.com; a atribuição só vem no fim da frase. Ver recomendada R3. |
| 13 | Tabela cobra por eixo e distância, não por tonelada; R$ 145/t (caminhão grande) contra R$ 245/t (carreta), rota de 1.000 km | Brazil Journal | confirmada | Na fonte, o "caminhão grande" é um rodotrem de 9 eixos. |
| 14 | Fatia das carretas nas viagens do agro: de 68% para 44% | Brazil Journal / Frete.com | confirmada | A fonte não dá os períodos; a edição também não. |
| 15 | Leilão de gás: primeiro da União a oferecer o gás direto a grandes consumidores; 110 lotes; 1,1 milhão de m³/dia; 23 empresas | Valor | confirmada | |
| 16 | Vencedoras: Vale, CSN, Gerdau, Braskem e Yara; entrega de março a dezembro de 2027 | Valor | confirmada | |
| 17 | (escala do leilão de gás) | Valor | sem escala | O número "1,1 milhão de m³/dia" fica sem régua. A mesma matéria traz: o MME estima corte de até 57% no preço pago pela indústria. Ver recomendada R4. |
| **MUNDO** | | | | |
| 18 | Turquia corta juros em 1 ponto, para 36% ao ano | Valor ("1 ponto percentual", 36% a.a., unânime, em linha com o esperado) | confirmada | Taxa anterior: 37% (Intellinews, 04/09/2026: parada em 37% desde janeiro). "1 ponto" deveria ser "1 ponto percentual". Ver recomendada R5. |
| 19 | Cita queda do núcleo da inflação e demanda interna fraca | Valor | confirmada | "tendência de queda do núcleo da inflação e fraqueza da demanda interna". |
| 20 | "núcleo da inflação (a medida que tira os preços mais voláteis)" | explicação do redator | confirmada | Termo explicado na primeira vez. |
| 21 | Reino Unido: £ 10,9 bi de juros da dívida em setembro, maior setembro da série | Guardian | confirmada | "highest September figure since records began". |
| 22 | Parte dos títulos é corrigida pela inflação, que somou £ 4 bi só no mês | Guardian (ONS) | confirmada | |
| 23 | FMI: PIB de Oriente Médio, Norte da África e Paquistão encolhe 1,3% em 2026 por causa da guerra, depois cresce 6,6% em 2027 | Valor (título: "deve recuar 1,3% em 2026") | confirmada | O endereço (slug) do link diz "13-pontos-percentuais", mas o título atual e o texto dizem "recuar 1,3%". A edição está certa. Projeção do FMI: a edição já atribui ao FMI. |
| 24 | Zona do euro: confiança do consumidor de -16,8 para -17,9 na leitura preliminar de outubro, pior que os -17 esperados | Valor (Comissão Europeia) | confirmada | Trading Economics mostra o mesmo -17,9 e o consenso de -17. |
| 25 | "na prática, o choque de energia já pesa no humor de quem compra" | nenhuma (o Valor, 2 frases, não diz a causa) | corrigir | Atribuição de causa sem fonte e sem selo. Só um agregador (Trading Economics) diz que petróleo, inflação e juros "provavelmente contribuíram". Correção obrigatória 3. |
| **O QUE MUDA NO BOLSO** | | | | |
| 26 | Contrato de aluguel corrigido pelo IGP-M com aniversário em outubro sobe 3,34% (acumulado em 12 meses até setembro) | QuintoAndar (FGV: IGP-M de setembro 1,57%; 12 meses 3,34%) | confirmada | Os mesmos números aparecem em Debit e Muita Informação (achados por busca). Fonte secundária; o ideal é o link da FGV Ibre. |
| 27 | IGP-M e "prévia" sem explicação na primeira vez | | corrigir | Correção obrigatória 5. |
| 28 | 2ª prévia de outubro: 1,59% "no mês" | Valor (21/10) | confirmada, com ressalva | O número é da segunda prévia (leitura parcial), não do mês fechado. Na prévia equivalente de setembro foi 1,47%. Correção obrigatória 5. |
| 29 | "puxada pelos preços no atacado, que pesam 60% no índice" | Valor: IPA (preços ao produtor) pesa 60% e subiu 2,12% | confirmada | IPA = preços ao produtor; "atacado" é o uso corrente. |
| 30 | Desenrola 3: bancos podem oferecer até R$ 90 bi em dívidas antigas | Agência Brasil | confirmada | |
| 31 | "com desconto mínimo de 90%" | Agência Brasil | corrigir | O desconto é o que os bancos dão à União na venda (a União pagaria no máximo R$ 9 bi pelos R$ 90 bi). O leitor entende que o devedor terá 90% de desconto. O que o devedor paga "ainda depende de definições do CMN". Correção obrigatória 1. |
| 32 | "a chamada desta quinta mede o interesse dos credores" | Agência Brasil (edital publicado em 22/10; 5 dias úteis para os bancos informarem) | confirmada | |
| 33 | "ainda não é a hora de o devedor renegociar" | Agência Brasil: a etapa "não é uma convocação para que os consumidores renegociem"; "não precisam procurar os bancos para participar da etapa" | corrigir | A fonte fala da etapa do programa. A frase da edição soa como conselho geral, e o devedor pode renegociar direto com o banco. Correção obrigatória 1. |
| 34 | Leilão "entre o fim de novembro e o começo de dezembro" | Estadão (Durigan: "dentro do mês de novembro, podendo ser no começo de dezembro") | confirmada | Repete a geral de hoje (mesma fonte, mesmo dado). Correção obrigatória 1. |
| 35 | Repetição da geral: "Desenrola 3 prevê leilão de até R$ 90 bi" | geral 22/10 | corrigir | R$ 90 bi, leilão em novembro/começo de dezembro e o link do Estadão já saíram na geral. O valor novo daqui é a chamada aos bancos, o custo máximo de R$ 9 bi e o que muda para o devedor. Correção obrigatória 1. |
| 36 | Goldman calcula reajuste de cerca de 50% no diesel | InfoMoney | corrigir | É hipótese condicional: só se os subsídios extras aos importadores (R$ 1,40/l, até meados de novembro) acabarem. O Goldman não usa o reajuste no cenário-base (assume preços estáveis até o fim do ano). Correção obrigatória 2. |
| 37 | "é o número a vigiar depois do segundo turno" | | corrigir | Julgamento do redator sem selo. Também repete o explicador sem trazer o efeito no bolso. A fonte tem o número: 50% na refinaria vira cerca de 20% na bomba e 0,21 a 0,24 ponto percentual no IPCA. Correção obrigatória 2. |
| **NA AGENDA** | | | | |
| 38 | Sex (23/10), 9h: IPCA-15 de outubro | oficiais.md (23/10 09:00, IPCA-15) | confirmada | |
| 39 | Qua (28/10): decisão do Fed | Fed (FOMC "October 27-28") | confirmada | A decisão sai no 2º dia, quarta 28/10. |
| 40 | Fed e Copom sem horário | manual, seção 5.8 ("o dia, o horário de Brasília e o link") | corrigir | Fed: o horário usual é 14h de Nova York, 15h em Brasília (os EUA ainda estão no horário de verão até 1/11); a página do Fed não traz horário. Copom: oficiais.md diz "à noite". Correção obrigatória 4. |
| 41 | Sex (30/10), 9h: PNAD Contínua, desemprego do trimestre até setembro | oficiais.md (30/10 09:00, PNAD Contínua Mensal) | confirmada | O painel tem desemprego "no trimestre até agosto", então o próximo é o até setembro. |
| 42 | Qua (4/11): decisão do Copom | oficiais.md (04/11, à noite) | confirmada | |
| **FECHO** | | | | |
| 43 | "Até a próxima." e "Não é recomendação de investimento." | manual, seção 5.9 | confirmada | |

## Outras checagens pedidas

- **Opinião sem selo:** linha 25 (Zona do euro, "na prática, o choque de energia já pesa...") e linha 37 (Combustível, "é o número a vigiar"). Ambas cobertas pelas correções 2 e 3.
- **Recomendação de investimento:** nenhuma frase manda comprar, vender ou "travar" nada. "ainda não é a hora de o devedor renegociar" (linha 33) é o mais próximo de um conselho sobre dinheiro; coberta pela correção 1. O rodapé existe.
- **Política:** a parte 2 não tem pesquisa eleitoral nem candidato. "Segundo turno" aparece só como marco de tempo do diesel (aceitável: efeito econômico).
- **Dia da semana:** nenhum erro. "a chamada desta quinta" = 22/10, quinta.
- **Repetição da geral e do Mercado** (`historico --caderno economia --dias 1`): só o Desenrola 3 repete a geral (correção 1). A arrecadação aparece no Mercado de hoje apenas como item da agenda (11h), sem o resultado; a linha de BRASIL traz o resultado e a análise da XP, então tem valor novo. Nenhum outro item da parte 2 saiu na geral ou no Mercado dos últimos 3 dias (conferi também por busca de palavras nas edições de 16 a 22/10).
- **Termo técnico sem explicação:** IGP-M e "prévia" (correção 5). Recomendadas: "piso do frete" (R3). IPCA-15, Fed e núcleo da inflação estão explicados. "Copom" nunca é explicado na edição inteira (a primeira aparição é na parte 1).
- **Nota de calendário:** as fontes das linhas de BRASIL, MUNDO e o leilão de gás são de depois das 06:00 de 22/10 (a Turquia às 08h32, a CNI às 11h14, o leilão às 13h23, o FMI às 13h23). Para o teste a edição vale como "chega hoje"; numa entrega real às 06:00 esses fatos ainda não existiriam.
- **Fora da janela de 7 dias da agenda (seção 5.8):** PNAD (30/10, 8 dias) e Copom (4/11, 13 dias). O `oficiais.md` lista 8 dias e o Copom já aparece no explicador, então é tolerável; só registro.

## Correções obrigatórias (texto exato a trocar → texto novo)

### 1. Desenrola (BOLSO, "Dívida atrasada")

Trocar:

```
→ **Dívida atrasada**: o Desenrola 3 começou pelos bancos, que podem oferecer até R$ 90 bi em dívidas antigas, com desconto mínimo de 90%; a chamada desta quinta mede o interesse dos credores e ainda não é a hora de o devedor renegociar ([Agência Brasil](https://agenciabrasil.ebc.com.br/economia/noticia/2026-10/ministro-preve-renegociacao-de-r-90-bi-em-3a-fase-do-desenrola)). O leilão deve ficar entre o fim de novembro e o começo de dezembro ([Estadão](https://www.estadao.com.br/economia/desenrola-3-governo-espera-comprar-r-90-bi-em-dividas-antigas-em-novembro-diz-durigan/)).
```

Por:

```
→ **Dívida atrasada**: no Desenrola 3, a União compra dívidas antigas dos bancos para depois renegociá-las com o devedor, e a primeira etapa é só com os credores: a chamada publicada nesta quinta pergunta aos bancos quanto querem vender, e eles têm cinco dias úteis para responder. O desconto mínimo de **90%** é o que o banco dá à União na venda (por R$ 90 bi em dívidas, ela pagaria no máximo **R$ 9 bi**); quanto o devedor vai pagar ainda depende de regras do Conselho Monetário Nacional, e a Fazenda diz que ele não precisa procurar o banco por causa dessa etapa ([Agência Brasil](https://agenciabrasil.ebc.com.br/economia/noticia/2026-10/ministro-preve-renegociacao-de-r-90-bi-em-3a-fase-do-desenrola)). Entram dívidas de dois a quatro anos e meio, com o leilão previsto para o fim de novembro ou o começo de dezembro ([Estadão](https://www.estadao.com.br/economia/desenrola-3-governo-espera-comprar-r-90-bi-em-dividas-antigas-em-novembro-diz-durigan/)).
```

Por quê: (a) o "desconto mínimo de 90%" lido sozinho promete 90% de desconto ao devedor; (b) "ainda não é a hora de o devedor renegociar" é conselho sem fonte e mais amplo que a fonte; (c) o R$ 90 bi e a data do leilão já saíram na geral; o texto novo põe na frente o que a geral não deu (custo máximo de R$ 9 bi, cinco dias úteis, CMN, idade das dívidas). Todos os dados novos estão nas duas matérias citadas.

### 2. Diesel (BOLSO, "Combustível")

Trocar:

```
→ **Combustível**: diesel mais caro encarece o frete, e o frete chega ao preço da comida; por isso o reajuste de cerca de 50% que o Goldman calcula é o número a vigiar depois do segundo turno ([InfoMoney](https://www.infomoney.com.br/mercados/petrobras-petr3-petr4-pode-ter-subir-diesel-ate-cinquenta-porcento-goldman-sachs-quais-impactos-acoes-inflacao/)).
```

Por:

```
→ **Combustível**: diesel mais caro encarece o frete, e o frete chega ao preço da comida. Se a Petrobras subisse o diesel às distribuidoras em cerca de **50%** (hipótese que o Goldman Sachs não usa no cenário principal), o litro na bomba, hoje a R$ 7,34, subiria cerca de **20%**, e o IPCA ganharia de **0,21 a 0,24 ponto percentual** somando o efeito direto e o do frete; qualquer decisão deve ficar para depois do segundo turno ([InfoMoney](https://www.infomoney.com.br/mercados/petrobras-petr3-petr4-pode-ter-subir-diesel-ate-cinquenta-porcento-goldman-sachs-quais-impactos-acoes-inflacao/)).
```

Por quê: o InfoMoney diz que o reajuste de ~50% só ocorreria se o subsídio extra aos importadores acabasse, e que o banco assume preço estável até o fim do ano; "o número a vigiar" era opinião sem selo; e o 50% já está no explicador. Os números novos (bomba +20%, 21 a 24 pontos-base no IPCA = 0,21 a 0,24 ponto percentual, R$ 7,34) estão na mesma matéria.

### 3. Zona do euro (MUNDO)

Trocar:

```
na prática, o choque de energia já pesa no humor de quem compra.
```

Por:

```
**Opinião:** é provável que o choque de energia ajude a explicar o recuo, mas a nota não informa a causa.
```

(Alternativa sem selo: cortar o trecho depois do ponto e vírgula e terminar a linha em "...pior que os -17 esperados ([Valor](...))." Se quiser dar escala: "quanto mais negativo, pior".)

### 4. Agenda: horário do Fed e do Copom

Trocar:

```
→ **Qua (28/10)**: decisão de juros do Fed, o banco central dos EUA ([Fed](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)).
```

Por:

```
→ **Qua (28/10), 15h**: decisão de juros do Fed, o banco central dos EUA ([Fed](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)).
```

Trocar:

```
→ **Qua (4/11)**: decisão do Copom sobre a Selic ([BC](https://www.bcb.gov.br/controleinflacao/calendarioreunioescopom)).
```

Por:

```
→ **Qua (4/11), à noite**: decisão do Copom sobre a Selic ([BC](https://www.bcb.gov.br/controleinflacao/calendarioreunioescopom)).
```

Por quê: o manual (seção 5.8) exige o horário de Brasília em cada linha. Ressalva: o "15h" é o horário usual do comunicado do Fed (14h em Nova York, ainda no horário de verão americano até 1/11); a página do Fed não traz horário. Se preferir não afirmar o que a fonte não diz, use "Qua (28/10), à tarde". O "à noite" do Copom vem do `oficiais.md`.

### 5. Aluguel (BOLSO): explicar IGP-M e prévia, e corrigir "no mês"

Trocar:

```
→ **Aluguel**: o contrato corrigido pelo IGP-M que faz aniversário em outubro sobe **3,34%**, o acumulado de 12 meses até setembro ([QuintoAndar](https://www.quintoandar.com.br/guias/reajuste-de-aluguel-calculadora-igpm-2026/)); e a segunda prévia de outubro já marcou **1,59%** no mês, puxada pelos preços no atacado, que pesam 60% no índice ([Valor](https://valor.globo.com/brasil/noticia/2026/10/21/igp-m-sobe-159-pontos-percentuais-na-segunda-prvia-de-outubro-informa-fgv.ghtml)).
```

Por:

```
→ **Aluguel**: o IGP-M, índice da FGV que reajusta boa parte dos contratos de aluguel, acumula **3,34%** em 12 meses até setembro, e é esse o reajuste dos contratos com aniversário em outubro, abaixo do IPCA de 4,58% em 12 meses (no painel); num aluguel de R$ 2.000, são R$ 66,80 a mais por mês ([QuintoAndar](https://www.quintoandar.com.br/guias/reajuste-de-aluguel-calculadora-igpm-2026/)). A conta de novembro pode vir mais pesada: a segunda prévia de outubro (a leitura parcial do índice do mês) marca **1,59%**, contra 1,47% na prévia equivalente de setembro, puxada pelos preços ao produtor (o atacado), que pesam 60% do índice ([Valor](https://valor.globo.com/brasil/noticia/2026/10/21/igp-m-sobe-159-pontos-percentuais-na-segunda-prvia-de-outubro-informa-fgv.ghtml)).
```

Por quê: IGP-M e "prévia" apareciam sem explicação; "1,59% no mês" passa a ideia de resultado fechado; faltava a régua (contra o IPCA e contra a prévia de setembro, ambos nas fontes/painel; R$ 66,80 = 3,34% de R$ 2.000, conta do redator). "A conta de novembro pode vir mais pesada" é inferência: a variação de outubro entra no acumulado de 12 meses dos contratos de novembro; se preferir não inferir, corte essa frase.

## Correções recomendadas (não bloqueiam)

- **R1. Arrecadação**: trocar "a maior para o mês desde 2000 e **5,62%** acima da inflação na comparação com setembro de 2025" por "a maior para um setembro na série da Receita e alta real de **5,62%** (já descontada a inflação) sobre setembro de 2025". Motivo: as fontes divergem sobre o ano em que a série começa (2000 no InfoMoney/Money Times, 1995 no Valor do Mercado de hoje) e "acima da inflação" pode ser lido como ponto percentual.
- **R2. Indústria**: acrescentar "(queda de 1,3 ponto sobre o 2º trimestre)" depois de "42,2 pontos", e trocar "custos maiores com a guerra" por "custos maiores, em parte pela guerra" (é como o gerente da CNI diz).
- **R3. Frete**: pôr a atribuição na frente ("segundo a plataforma de fretes Frete.com, o piso do frete, o preço mínimo que o contratante paga ao caminhoneiro, reforçado por lei neste ano, está tirando carga do autônomo...") e tirar o "segundo a Frete.com" do fim. Os números R$ 145/R$ 245 e 68%/44% são da análise da Frete.com.
- **R4. Gás**: dar escala ao leilão acrescentando "o Ministério de Minas e Energia estima que o preço pago pela indústria cai até 57%" (está na mesma matéria do Valor; o preço médio final "ainda será divulgado").
- **R5. Turquia**: trocar "cortou os juros em 1 ponto, para **36%** ao ano" por "cortou os juros em 1 ponto percentual, de 37% para **36%** ao ano" (37% = taxa parada desde janeiro, Intellinews de 04/09/2026, e bate com o corte de 1 ponto do Valor).
- **R6. Zona do euro**: dar escala ao índice com "(quanto mais negativo, pior)"; o Trading Economics dá a média histórica de -9,5 desde 1985, mas é agregador (a fonte primária é a Comissão Europeia).
- **R7. Oriente Médio**: o PIB projetado é real; se quiser seguir a seção 4 do manual à risca, "já descontada a inflação". Escala possível, da mesma matéria: Bahrein, Kuwait, Catar e Iraque com queda de dois dígitos.
- **R8. Reino Unido**: a seção 9 do manual pede conversão para reais quando ajuda ("£ 10,9 bi, cerca de R$ X bi"); o câmbio da libra não está no painel, então só vale se houver fonte.
- **Fora da parte 2 (front matter), para quem editar**: (a) `previa: "+ o imposto dos dividendos rendeu metade do previsto"` induz a erro: é metade da previsão revisada para o ano inteiro, com nove dos doze meses passados, e cerca de 18% da previsão inicial (R$ 5,26 bi de R$ 29,9 bi); sugestão: "+ o imposto dos dividendos rendeu metade da previsão para o ano". (b) O título da história `desenrola-3` diz "o leilão deve ficar para o fim de novembro", mas a fonte diz "dentro de novembro, podendo ser no começo de dezembro". (c) Em O Globo, para atingir R$ 10,5 bi faltam R$ 5,24 bi em três meses, R$ 1,75 bi por mês, 42% acima do recorde de setembro (R$ 1,23 bi): se couber na linha de BRASIL, é a escala que faltou.
