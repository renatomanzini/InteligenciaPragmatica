# Verificação 2026-10-29

# Verificação parte 1 (front matter até A HISTÓRIA DO DIA) — Mercado 2026-10-29

Fontes abertas e lidas em 29/10. Abreviações: V1 = Valor (Ibovespa cai pela 3ª sessão), V2 = Valor (dólar à vista recua), V3 = Valor Investe (Ibovespa flerta), IN = InvestNews (Tesouro IPCA+), V5 = Valor Investe (IOF).

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| Ibovespa caiu 2,68%, a 171.006 pts, 3ª queda seguida, puxada pelos bancos | V1; painel (171.006 ▼ 2,68%) | OK | - |
| Pesaram boatos sobre nomeações para BC e TCU | V1 | OK | - |
| Dólar à vista subiu boa parte do dia, virou à tarde, fechou em leve queda (-0,19%, R$ 5,3401), acompanhando o dólar global mais fraco após o Fed | V2 | OK | - |
| "A alta de 0,14% do painel é a da PTAX" | painel (R$ 5,34 ▲ 0,14%, PTAX de 28/10) | OK (grafia igual). PTAX explicada no próprio texto | - |
| Fed manteve juros entre 3,75% e 4% | V1 | OK | - |
| S&P 500 +0,28%, Nasdaq +0,27% | V1; painel | OK (grafia igual) | - |
| Bom dia: bolsa caiu pelo 3º pregão seguido, perdeu quase 17% "desde a eleição"; Fed parado; Wall Street subiu pouco | V1 | OK | - |
| Ibovespa -16,6% na semana, -8,2% no mês, +6,1% no ano | V3 | OK | - |
| 171.006 pts perto do menor nível desde 20/8 (167.927) | V3 | OK | - |
| "Em três pregões depois da reeleição ... Os estrangeiros retiraram cerca de R$ 7 bilhões da bolsa" | V3: saques de R$ 1,03 bi (22/10), R$ 2,94 bi (23/10) e R$ 2,8 bi (26/10), "quase R$ 7 bilhões" em três sessões; a saída começou ANTES do 2º turno | IMPRECISO: no contexto parece que foram os 3 pregões pós-eleição; só 1 foi | Correção 1 |
| Tesouro IPCA+ 2032 a IPCA + 7,97% ao ano, última vez em setembro | IN | OK | - |
| Prefixado 2032 a 15,27% ao ano | IN | OK | - |
| Quem já tinha os títulos viu o preço cair (marcação a mercado) | IN (taxa sobe, preço cai) | OK; "marcação a mercado" só é explicada na prática, aceitável | - |
| "O medo com as contas públicas também empurra para cima os juros pagos pelo governo" | IN (prêmio de risco fiscal volta aos preços) | OK, é a explicação da fonte | - |
| Segundo O Globo, equipe econômica estuda IOF sobre LCI, LCA, CRI, CRA e debêntures incentivadas, hoje isentas de IR para PF | V5 | OK | - |
| IOF pode mudar por decreto, sem Congresso | V5 | OK | - |
| "Nada foi anunciado" | V5 (apuração do jornal, "avalia") | OK | - |
| TL;DR: títulos voltaram a pagar perto de 8% + inflação | IN (IPCA+ 2032 7,97%; 2040 7,57%) | OK | - |
| "Se o IOF sair, LCI e LCA ficam menos vantajosas do que hoje" | nenhuma fonte; inferência (alíquota, prazo e valor desconhecidos) | SEM SELO / sem atribuição | Correção 4 |
| "Quem leva um título do Tesouro até o vencimento recebe a taxa contratada; quem vende antes sente a oscilação" | IN | OK (não é recomendação) | - |
| Front matter: títulos das histórias (Ibovespa -2,68%, quase 17%, 7,97%; Alphabet -25%; Microsoft +32%) | V1, V3, IN, Valor Investe Alphabet (25,2%, ~10% no pós-mercado) e Microsoft (32%) | OK | - |

## Outras checagens
- Pesquisa eleitoral: nenhuma. A eleição aparece só como efeito no preço ("depois da reeleição de Lula"). OK.
- Recomendação de investimento: nenhuma frase de "compre/venda". O rodapé existe. OK (ver correção 4 para a inferência).
- Opinião sem selo: só a inferência da correção 4.
- Termos técnicos sem explicação na primeira vez (manual, seções 2 e 8): IOF, LCI/LCA/CRI/CRA, debêntures incentivadas, Tesouro IPCA+ e Prefixado, "dólar à vista". Explicados: Fed, PTAX, marcação a mercado (parcial). Ver correções 2, 3 e 5.

## Correções obrigatórias

1. Estrangeiros (linha da história, parágrafo 1). Trocar:
`Os estrangeiros retiraram cerca de **R$ 7 bilhões** da bolsa ([Valor Investe]`
por:
`Os estrangeiros retiraram quase **R$ 7 bilhões** da bolsa em três sessões, desde 22/10, a véspera do segundo turno ([Valor Investe]`

2. Termos do Tesouro (parágrafo 2). Trocar:
`o Tesouro IPCA+ 2032 pagava inflação mais **7,97%** ao ano, nível visto pela última vez em setembro, e o Prefixado 2032, **15,27%** ao ano`
por:
`o Tesouro IPCA+ 2032 (que paga a inflação oficial, o IPCA, mais uma taxa fixa) pagava IPCA mais **7,97%** ao ano, nível visto pela última vez em setembro, e o Prefixado 2032 (de taxa combinada na compra) pagava **15,27%** ao ano`

3. Termos do IOF (parágrafo 3). Trocar:
`segundo O Globo, a equipe econômica estuda cobrar IOF de LCI, LCA, CRI, CRA e debêntures incentivadas, hoje isentas de Imposto de Renda para pessoa física.`
por:
`segundo O Globo, a equipe econômica estuda cobrar IOF (Imposto sobre Operações Financeiras) de LCI e LCA (letras de crédito imobiliário e do agronegócio), CRI e CRA (certificados de recebíveis) e debêntures incentivadas (títulos de dívida de empresas para obras de infraestrutura), hoje isentas de Imposto de Renda para pessoa física.`

4. Inferência sem selo (E no seu bolso?). Trocar:
`Se o IOF sair, LCI e LCA ficam menos vantajosas do que hoje, mas por enquanto é só um estudo.`
por:
`Se o IOF sair, o rendimento líquido de LCI e LCA tenderia a cair em relação ao de hoje (o tamanho dependeria da alíquota, que não existe ainda), mas por enquanto é só um estudo do governo, segundo O Globo.`

5. "Dólar à vista" sem explicação (O QUE MEXEU, Dólar). Trocar:
`o à vista subiu boa parte do dia`
por:
`o à vista (a cotação negociada ao longo do dia) subiu boa parte do dia`

Observação: as correções 2 e 3 aumentam o texto da história; confira o limite de 150 a 250 palavras (manual, seção 5) e corte frase de baixo valor se passar.

# Verificação parte 2 (AGENDA DE HOJE até o rodapé)

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| BCE decide os juros hoje (29/10), com entrevista coletiva | BCE (calendário) | OK (a página lista a entrevista de 29/10/2026); o link é a página geral do calendário e não traz horário | opcional: horário de Brasília |
| Vale divulga o balanço do 3T hoje, depois do fechamento | InfoMoney | OK | nenhuma |
| Itaú BBA espera Ebitda de US$ 2,66 bi em ferrosos, 13% abaixo do trimestre anterior, minério mais barato | InfoMoney | OK | nenhuma |
| Ebitda explicado | n/a | OK | nenhuma |
| Fed manteve juros, dois votos contrários (Cook e Hammack), queriam alta de 0,25 p.p., por causa da inflação | InvestNews | OK | nenhuma |
| Alphabet: lucro -25,2%, US$ 26,2 bi, abaixo do esperado, ação -quase 10% no pós-mercado | Valor Investe | OK nos números. "Pós-mercado" sem explicação. A fonte diz que a queda do lucro teve peso de perda de US$ 8,7 bi com participações acionárias | explicar "pós-mercado" |
| Microsoft: lucro +32%, US$ 36,6 bi, acima do esperado | Valor Investe | OK (nota: é o 1º trimestre fiscal) | nenhuma |
| Santander Brasil: lucro -28%, R$ 2,885 bi, inadimplência de PF 4,2% para 5,5% em 12 meses, atraso acima de 90 dias | Valor Investe | OK | nenhuma |
| Opinião/previsão sem selo | n/a | Nenhuma encontrada; a previsão da Vale está atribuída ao Itaú BBA | nenhuma |
| Recomendação de investimento / pesquisa eleitoral | n/a | Nenhuma | nenhuma |
| Números do painel citados | painel.md | A parte 2 não cita número do painel | nenhuma |

## Correções obrigatórias

1. Termo técnico sem explicação (RADAR, Big techs).
   - Trocar: `e a ação desabou quase **10%** no pós-mercado (`
   - Por: `e a ação desabou quase **10%** no pós-mercado (a negociação depois do fechamento do pregão) (`

Todas as correções obrigatórias das duas partes foram aplicadas.
