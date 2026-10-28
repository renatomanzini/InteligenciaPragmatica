# Verificação, parte 1 (início até o fim de "### Mundo"), edição de 2026-10-28

Datas conferidas: 26/10 segunda, 27/10 terça, 28/10 quarta, 03/11 terça, 04/11 quarta. Todas certas.
IBGE: a edição só usa o IPCA do painel (4,58%, teto 4,5%), que bate com `painel_economia.md`. A API do SIDRA ainda não traz setembro de 2026, então não há conferência independente; o painel é gerado por código.

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| Ibovespa -0,51%, 175.710 pts; máxima acima de 178 mil; BB caiu depois de -29% na segunda; Natura -6,4% | Valor Investe (11); Money Times (17) dá Natura -6,94% | OK | Nenhuma |
| Dólar comercial -1%, R$ 5,35; maior salto diário desde 1999 | Valor Investe (11); Agência Brasil (1) | OK | Nenhuma |
| "Queda de 3,02% do painel é da PTAX" (painel: R$ 5,33, -3,02%) | painel.md | OK, grafia igual | Nenhuma |
| Wall Street: alta com petróleo mais barato e chips; Nasdaq +1,18%, S&P +0,60%, "segundo dia seguido de ganho" | Money Times (17) | Parcial | A fonte diz que o S&P 500 engatou o segundo dia de ganhos; não diz isso do Nasdaq. Ver correção 1 |
| Segunda (26): Ibovespa -13,88%, 176.608 pts; mínima -17%; dólar +8,21%, R$ 5,403; reeleição de Lula | Agência Brasil (1) | OK | Nenhuma |
| "Contra a aposta da maior parte do mercado" | Agência Brasil: "parte do mercado"; Valor: "preferido pelo mercado" | OK, um pouco forte | Opcional: "contra a aposta de boa parte do mercado" |
| Maior queda diária desde a pandemia | InfoMoney (15); Agência Brasil (1) | OK | Nenhuma |
| Morgan Stanley reduziu posições em B3, BTG, XP, Nubank, Mercado Livre e Sabesp; Bradesco BBI projeta PIB mais fraco e mais desemprego em 2027 | InfoMoney (15) | Parcial | Isso é mudança na carteira recomendada (modelo) dos bancos e foi feita "nas últimas sessões", não só na terça. O Bradesco BBI é banco brasileiro, e o TL;DR diz "bancos estrangeiros". Ver correção 2 |
| "Exposição ao Brasil" | | Termo técnico sem explicação | Ver correção 2 |
| Tesouro cancelou todos os leilões da semana; recomprou cerca de R$ 10 bi na segunda | Money Times (18) | OK pelo título. O corpo só diz que o LFT de terça foi cancelado e que as ofertas de prefixados e IPCA foram suspensas na segunda | "Recompra" sem explicação. Ver correção 3 |
| Analistas: turbulência até o governo assumir compromissos fiscais; mercado espera o ministro da Fazenda | Valor Investe (11) | OK | Nenhuma |
| Tesouro Prefixado 2029: 14,79% (15,26% na segunda); IPCA+ 2040: 7,53% (7,29%) | Valor Investe (12) | Números OK. Enquadramento enganoso | O Prefixado 2029 teve taxa MENOR na terça (a fonte titula "prefixados recuam"). "Taxa maior na compra" só vale contra o pré-eleição (12,79% em 22/10, edição de 23/10). Prefixado e IPCA+ sem explicação. Ver correção 4 |
| Contas públicas: Durigan, projeto de lei, centro da meta 2027, superávit de R$ 73,2 bi, 0,5% do PIB | g1 (7) | OK | "Isso pode obrigar a bloquear" é mais forte que o g1 ("em tese ... poderá precisar"). Ver correção 5 |
| "Déficit de 0,62% do PIB em 12 meses até agosto" | painel_economia.md | OK, grafia igual | Nenhuma |
| Imposto Seletivo: MP "provavelmente esta semana" | Agência Brasil (2) | OK | Nenhuma |
| Crédito: 20,3 mi, +75% em cinco anos, 17% dos devedores, 42% da renda até dois salários mínimos, BC promete medidas sobre o rotativo | Agência Brasil (3) | Números OK. Termo trocado | O BC fala em "endividamento de risco" (2 de 4 critérios; a fonte diz que não são todos inadimplentes). "Superendividados" é o título da Agência Brasil, não o termo do BC. Falta o mês (junho de 2026). Ver correção 6 |
| Diesel: subvenção renovada por um mês, R$ 2,12 por litro | Agência Brasil (2) | OK. "Petróleo caro" é inferência. "Subvenção" sem explicação. R$ 2,12 sem escala | Ver correção 7 |
| Hypera: lucro +16,1%, R$ 527 mi no 3º tri; Semavy; 93 mil unidades no primeiro mês | Folha (5) | Números OK (lucro líquido das operações continuadas; 93 mil em setembro, dados da IQVIA) | "Caneta mais barata virou negócio" é opinião sem selo, e a fonte não diz "mais barata" (R$ 676 a R$ 697). A Folha atribui a alta também às vendas nas farmácias e lembra que nem todo o resultado veio das canetas (despesa financeira -35,3%). Ver correção 8 |
| Frango: terceiro foco em SC (Nova Erechim); Uruguai suspendeu importação de produtos avícolas do Brasil, exceto tratados | Folha (4); Estadão (13) | OK | Nenhuma obrigatória. Opcional: o Uruguai é o sexto país com restrição (México, Chile, China, Arábia Saudita e Malásia já tinham) |
| Fed: manter 3,75% a 4,00%; alta de 0,25 em setembro; FedWatch 90,6%; inflação ao consumidor 3,7% em 12 meses | InfoMoney (14) | Parcial | A fonte diz que o CPI "acelerou para 3,7% em setembro" e não escreve "em 12 meses". "Fed" e "FedWatch" sem explicação. A frase "Na prática, juro alto lá fora..." é do InfoMoney e está sem atribuição. Repete a AGENDA com a mesma informação. Ver correção 9 |
| Argentina: terceira revisão, programa de US$ 20 bi de 2025, cerca de US$ 900 mi, já desembolsou US$ 15,8 bi | g1 (6) | Números OK, mas omite que o repasse ainda depende do conselho executivo do FMI | "Fecharam" passa a ideia de dinheiro liberado. Ver correção 10 |
| Selic: probabilidade de corte de 0,25 foi de 76% para 28%; manutenção de 17,5% para 62%; sequência de cortes desde março | Valor Investe (10) | OK. O 76% é de 23/10 e não aparece na edição. O texto diz "a maioria das apostas" (76%, certo) | Nenhuma obrigatória |
| Cadeia causal do explicador ("dúvida fiscal » prêmio de risco » ... » BC com menos espaço") | Valor Investe (10): Sueishi e Rosário | Inferência sem dono | Atribuir. Ver correção 11 |
| IPCA 4,58% acima do teto de 4,5% (painel); Focus de 23/10: Selic 13,25% no fim de 2026 | painel_economia.md | OK, grafia igual | Nenhuma |
| "No bolso": "CDB e poupança seguem rendendo o que rendem hoje, e o crédito não barateia tão cedo" | Sem fonte com número. O Valor Investe (10) diz que a pausa mantém o crédito caro | Inferência sem selo, sem número e sem fonte | Ver correção 12 |
| Copom, Focus, juros futuros no explicador | | Termos sem explicação | Ver correção 13 |

## Outros pontos conferidos
- Pesquisa eleitoral: não há. Recomendação de investimento: não há (só relato de recomendações de bancos). O rodapé está presente.
- Repetição com a geral ou com o Mercado de hoje: a geral de 28/10 já cobre a recompra do Tesouro (R$ 31,6 bi) e o Brent. O bloco ECONOMIA não repete esses itens. O Frango repete a pauta de 23/10, mas traz valor novo (terceiro foco e Uruguai) e diz "o que mudou desde 23/10". O Fed aparece em Mundo e na AGENDA com a mesma informação, o que é duplicado (correção 9).

## Correções obrigatórias (texto exato a trocar e texto novo)

1. Wall Street
   - Trocar: `o Nasdaq subiu **1,18%** e o S&P 500, **0,60%**, no segundo dia seguido de ganho, à espera do Fed`
   - Por: `o Nasdaq subiu **1,18%** e o S&P 500, **0,60%**, o segundo dia seguido de ganho do S&P, à espera do Fed (o banco central dos EUA)`

2. Bancos (história do dia)
   - Trocar no TL;DR: `bancos estrangeiros cortaram a exposição ao Brasil`
   - Por: `bancos como Citi e Morgan Stanley reduziram o peso do Brasil nas carteiras que recomendam`
   - Trocar: `Na terça, o pregão foi de acomodação, mas os grandes bancos mexeram nas carteiras. Segundo o InfoMoney, o Morgan Stanley reduziu posições em`
   - Por: `Na terça, o pregão foi de acomodação, mas, nos últimos dias, grandes bancos cortaram o peso do Brasil (a "exposição", quanto do dinheiro de uma carteira fica no país) nas carteiras que recomendam. Segundo o InfoMoney, o Morgan Stanley reduziu posições em`
   - Também no front matter, o título da história diz "bancos globais". Trocar por `bancos reduzem a exposição ao Brasil` ou manter só se o Bradesco BBI sair da frase.

3. Recompra
   - Trocar: `depois de recomprar cerca de **R$ 10 bilhões** em títulos na segunda, para acalmar as negociações`
   - Por: `depois de recomprar cerca de **R$ 10 bilhões** em títulos na segunda (comprar de volta papéis que já vendeu, para dar liquidez e acalmar as negociações)`

4. "E no seu bolso?"
   - Trocar: `O susto chegou à renda fixa: na terça, o Tesouro Prefixado 2029 pagava **14,79%** ao ano (15,26% na segunda), e o Tesouro IPCA+ 2040 subiu para IPCA + **7,53%** (7,29% na véspera)`
   - Por: `O susto chegou à renda fixa: na terça, o Tesouro Prefixado 2029 (juro fixo, combinado na compra) pagava **14,79%** ao ano, abaixo dos 15,26% da segunda, mas bem acima dos 12,79% de 22/10; e o Tesouro IPCA+ 2040 (a inflação mais um juro fixo) subiu para IPCA + **7,53%** (7,29% na véspera)`
   - Trocar: `Taxa maior na compra, mas quem já tinha o título antes viu o preço dele cair`
   - Por: `Taxa maior do que antes da eleição para quem compra agora, mas quem já tinha o título antes viu o preço dele cair`

5. Contas públicas
   - Trocar: `na prática, isso pode obrigar a bloquear mais gastos dos ministérios ao longo do ano`
   - Por: `em tese, isso pode obrigar o governo a bloquear mais gastos dos ministérios ao longo de 2027`

6. Crédito
   - Trocar: `o Brasil tem **20,3 milhões** de superendividados, **75%** a mais que cinco anos antes e **17%** de todos os devedores do sistema financeiro, segundo o Relatório de Estabilidade Financeira do BC;`
   - Por: `em junho, o Brasil tinha **20,3 milhões** de pessoas em "endividamento de risco" (quem atende a pelo menos dois de quatro critérios, como atraso de mais de 90 dias ou mais de 50% da renda comprometida; não quer dizer que todos estejam inadimplentes), **75%** a mais que cinco anos antes e **17%** dos devedores do sistema financeiro, segundo o Relatório de Estabilidade Financeira do BC;`

7. Diesel
   - Trocar: `o governo renovou por mais um mês a subvenção ao diesel, de **R$ 2,12 por litro**, para conter a alta do preço com o petróleo caro`
   - Por: `o governo renovou por mais um mês a subvenção ao diesel (ajuda em dinheiro para segurar o preço), de **R$ 2,12 por litro**, para conter a alta dos preços`

8. Hypera
   - Trocar: `com o Semavy, a versão dela da semaglutida (o princípio ativo do Ozempic), que vendeu **93 mil** unidades no primeiro mês`
   - Por: `com a venda nas farmácias e o início do Semavy, a versão dela da semaglutida (o princípio ativo do Ozempic), que vendeu cerca de **93 mil** unidades em setembro, o primeiro mês, segundo a consultoria IQVIA`
   - Apagar: `A caneta mais barata virou negócio para a indústria nacional.`
   - Se quiser manter a ideia, trocar por: `O Itaú BBA estima que a caneta pode somar R$ 359 milhões à receita da Hypera no primeiro ano completo.` (da própria Folha)

9. Fed (Mundo)
   - Trocar: `com a inflação ao consumidor americana em **3,7%** em 12 meses ([InfoMoney](https://www.infomoney.com.br/economia/juros-eua-decisao-fed-fomc-impacto-selic-copom/)). Na prática, juro alto lá fora deixa menos espaço para o BC cortar aqui.`
   - Por: `e a inflação ao consumidor americana (CPI) acelerando para **3,7%** em setembro ([InfoMoney](https://www.infomoney.com.br/economia/juros-eua-decisao-fed-fomc-impacto-selic-copom/)). A FedWatch mede as apostas do mercado em contratos futuros. Para o InfoMoney, juro alto lá fora deixa menos espaço para o BC cortar aqui.`
   - Trocar também: `o Fed decide hoje` por `o Fed, o banco central dos EUA, decide hoje`.
   - Duplicação: a AGENDA repete o Fed com a mesma informação. Cortar a linha da AGENDA ou deixar só uma frase curta lá. Isso é da parte 2, mas está aqui por causa do Mundo.

10. Argentina
    - Trocar: `o FMI e a Argentina fecharam a terceira revisão do programa de **US$ 20 bilhões** de 2025, o que pode liberar cerca de **US$ 900 milhões**; o Fundo já desembolsou **US$ 15,8 bilhões**`
    - Por: `o FMI e a Argentina chegaram a um acordo na terceira revisão do programa de **US$ 20 bilhões** de 2025, o que pode liberar cerca de **US$ 900 milhões**, se o conselho executivo do FMI aprovar; o Fundo já desembolsou **US$ 15,8 bilhões**`

11. Explicador, cadeia causal
    - Trocar: `O mecanismo é a dúvida fiscal virando preço:`
    - Por: `O mecanismo, segundo os especialistas ouvidos pelo Valor Investe, é a dúvida fiscal virando preço:`
    - E trocar `juros futuros e dólar sobem` por `juros futuros (as taxas que o mercado cobra hoje para emprestar por prazos mais longos) e dólar sobem`.

12. Explicador, "No bolso"
    - Trocar: `se a Selic parar em 13,75%, o CDB e a poupança seguem rendendo o que rendem hoje, e o crédito não barateia tão cedo.`
    - Por: `se a Selic parar em 13,75%, a remuneração de aplicações atreladas a ela, como o Tesouro Selic, não cai, e, segundo o Valor Investe, o crédito segue caro por mais tempo.`
    - Motivo: CDB e poupança não têm número nem fonte na edição, e a frase soa como orientação.

13. Explicador, termos
    - Trocar: `a cada reunião do Copom desde março` por `a cada reunião do Copom (o comitê do BC que define a Selic) desde março`
    - Trocar: `O Focus de 23/10, feito antes da eleição` por `O Focus de 23/10 (a pesquisa semanal do BC com economistas), feito antes da eleição`
