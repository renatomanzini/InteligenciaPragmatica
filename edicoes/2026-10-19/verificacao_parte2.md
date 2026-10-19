# Verificação, parte 2 (ECONOMIA até o fim) — edição 2026-10-19

Método: WebFetch em cada link; `curl` quando bloqueado (Estadão); API do BCB (Olinda) para o Focus; WebSearch para o FXStreet (403 no fetch e no curl por Cloudflare).

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Focus: PIB 2026 de 1,85% para 1,83% | Exame; BCB Olinda (mediana 1,8551 em 08/10 e 1,8301 em 16/10) | confirmada | nenhuma |
| 2 | Focus: IPCA 2027 de 4,30% para 4,32% | Exame; BCB (4,3000 em 15/10, 4,3206 em 16/10) | confirmada | nenhuma |
| 3 | Selic esperada no fim do ano 13,25% | Exame (não rotula como "fim do ano"); BCB: Selic 2026 mediana 13,25 | confirmada (na origem) | opcional: "Selic esperada para 2026" |
| 4 | "crescer menos com juro igual" | Focus (Selic 13,25 estável na semana, BCB) | confirmada, mas é interpretação | sem selo `**Opinião:**`; "na prática" ok, mas o selo é mais seguro |
| 5 | Ibovespa +0,54% a 205.430 pontos na sexta (16); semana -1,74% | InfoMoney (205.430,33; +0,54%; -1,74%) | confirmada | nenhuma |
| 6 | Dólar perto de R$ 5,07 | InfoMoney (R$ 5,072/5,073) | confirmada | nenhuma |
| 7 | China PIB 3º tri 4,5%, 2º tri 4,3% | Xinhua | confirmada | nenhuma |
| 8 | "um pouco acima dos 4,4% esperados" | FXStreet | confirmada (por busca; página bloqueada, trecho do FXStreet indica 4,5% vs 4,4% esperado) | nenhuma |
| 9 | Brent -1,8% para US$ 107,88 | O Econômico (04h27 GMT, queda de US$ 1,98) | confirmada | nenhuma |
| 10 | "na manhã desta segunda" | O Econômico: 04h27 GMT = 01h27 em Brasília | errada (leve) | "no início do pregão desta segunda" ou "na madrugada desta segunda (Brasília)" |
| 11 | Trump assinou "na sexta à noite" | O Econômico diz só "na sexta-feira" | não confirmada ("à noite") | cortar "à noite": "assinou na sexta (16)" |
| 12 | A ordem "suspende sanções contra a Rússia" | O Econômico: suspende grandes sanções e tarifas (Graham Act); Rubio fala em até 60 dias de avaliação | confirmada, mas incompleta | opcional: "suspende grandes sanções e tarifas" |
| 13 | "Na sexta, a gente contou o Brent a US$ 109,86" | edição 16/10 (verificacao.md); O Econômico: 107,88+1,98 = 109,86 fechamento de sexta | confirmada com ressalva | A edição de sexta saiu antes do fechamento de sexta. Para não confundir, escrever "o fechamento de sexta" com o link, ou "a edição de sexta (16) trouxe US$ 109,86". Conferir se a edição de 16/10 tratava o fechamento de quinta |
| 14 | Ri Happy pediu recuperação extrajudicial no domingo (18) | Exame | confirmada | nenhuma |
| 15 | ~48 dias depois de comprada pela BluSun | Exame: 48 dias contados do anúncio da troca de controle em 31/08 (31/08 + 48 = 18/10) | confirmada | opcional: "48 dias depois de anunciar a venda" (a conta é do anúncio) |
| 16 | Héctor Núñez volta à presidência; dívida não divulgada | Exame | confirmada | nenhuma |
| 17 | FIP Shine (ligado à IG4) com 50,11% do capital votante | InvestNews | confirmada | nenhuma |
| 18 | "contra cerca de 47% da Petrobras" | InvestNews (~47% do votante) | confirmada | nenhuma |
| 19 | Liquidação na quarta (21) | InvestNews (21/10, quarta) | confirmada | nenhuma |
| 20 | Petrobras montou grupo para medir impacto do fim da 6x1 | Estadão (curl): "criou um grupo de trabalho" sobre contratos de serviços | confirmada | nenhuma |
| 21 | Quase 130 mil terceirizados; cerca de 50 mil próprios, não afetados | Estadão (curl) | confirmada | nenhuma |
| 22 | "mais que o dobro" | 130/50 = 2,6 | confirmada | nenhuma |
| 23 | "o custo chega pelos contratos de serviço" | Estadão: impacto nos contratos de prestação de serviços; "custo" é inferência | não confirmada (inferência) | marcar como `**Opinião:**` ou trocar por "o impacto chega pelos contratos" |
| 24 | Disney oferecerá emprego a pelo menos 60 funcionários da Character.AI, em falência | TechCrunch | confirmada | nenhuma |
| 25 | Pacote estimado em US$ 60 mi por ano | TechCrunch ("estimated $60 million in total annual pay") | confirmada | nenhuma |
| 26 | "Antes, já tinha acertado comprar ativos por US$ 20 mi" | TechCrunch: a própria Character.AI disse antes que a Disney compraria alguns ativos por US$ 20 mi; é lance inicial (stalking horse), outro comprador pode cobrir | confirmada com ressalva | "A Character.AI disse antes que a Disney compraria parte dos ativos por US$ 20 mi, num lance inicial que outro comprador ainda pode superar" |
| 27 | Replit: Masad pôs OpenAI como padrão; Claude segue como opção | TechCrunch | confirmada | nenhuma |
| 28 | "A Replit estava entre os cinco maiores clientes da Anthropic" | TechCrunch: é declaração de Masad ("recentemente um dos cinco maiores") | confirmada, mas falta atribuição | "segundo Masad, estava entre os cinco maiores clientes..." |
| 29 | Fonte anônima contestou a versão dele | TechCrunch | confirmada | nota: Masad disse que a Replit "não trabalha mais" com a Anthropic; a edição suaviza. Pode somar |
| 30 | Stablecoins US$ 482 bi (~R$ 2,4 tri) jan-set, +45%, segundo a Allium | InvestNews | confirmada | nenhuma |
| 31 | LinkedIn "lançou" consultas pagas, Business Premium nos EUA | LinkedIn (Advice Sessions, no ar para elegíveis nos EUA) | confirmada | nenhuma |
| 32 | "o perfil vira balcão de consultoria" | interpretação | não é fato | marcar `**Opinião:**` ou cortar |
| 33 | EUA: US$ 1,05 tri de juros líquidos no ano fiscal 2026, terminado em setembro | InvestNews/Bloomberg (Tesouro) | confirmada | nenhuma |
| 34 | Ano anterior US$ 970 bi | InvestNews | confirmada | nenhuma |
| 35 | 3,2% do PIB, recorde acima de 1991, estimativa da Peterson Foundation | InvestNews | confirmada | nenhuma |
| 36 | "cerca de US$ 2,9 bi por dia, pela nossa conta" | recalculei: 1,05e12 / 365 = US$ 2,877 bi | confirmada | nenhuma (2,9 é arredondamento correto) |
| 37 | Taxa média da dívida negociável de 1,47% para 3,52% em cinco anos | InvestNews | confirmada | nenhuma |
| 38 | TD Securities: 1 ponto a mais somaria US$ 310 bi à conta de 2027 | InvestNews ("em todos os prazos") | confirmada | opcional: acrescentar "em todos os prazos" |
| 39 | Cadeia "cada título que vence é trocado por um mais caro » ... a dívida cresce" | mecanismo; a fonte diz que o EUA não está em crise e que o PIB nominal (6,3%) ainda supera os juros | não confirmada (mecanismo é explicação editorial) | considerar uma frase de contrapeso: economistas dizem que não é crise (fonte) |
| 40 | Para ler: MIT Tech Review, Claude em ilha deserta virtual, "brincar", especialistas duvidam | MIT TR | confirmada | nenhuma |
| 41 | Import AI 477: Jack Clark, cofundador da Anthropic, diz ao FMI que a singularidade já começou | Import AI (palestra Per Jacobsson, reunião do FMI em Bangkok, 17/10; "I believe that this year we have gained convincing evidence that it has now begun"; "The singularity is here"). Cofundador confirmado no próprio post | confirmada | sugestão: "em palestra na reunião do FMI" em vez de "ao FMI". Nota: "já começou" é a tese dele, convém "diz que" (já está assim) |
| 42 | Saarinen: software feito por agentes sem alguém com julgamento vira média | karrisaarinen.com | confirmada | nenhuma |
| 43 | Estrutura "- [Para ler] [título](url)" sob o cabeçalho "Para ler:" | manual (formato `🔗`/lista) | formatação | repete "Para ler"; remover o prefixo `[Para ler]` de cada item |

## Aspas e opiniões
- Nenhuma aspa direta nesta parte; nada inventado.
- Sem selo `**Opinião:**`: itens 4, 23, 32 (interpretações "na prática").
- Números atribuídos ao link errado: nenhum encontrado.

## Correções obrigatórias
1. Petróleo: cortar "à noite" ("assinou na sexta à noite"); a fonte diz só "na sexta-feira".
2. Petróleo: "na manhã desta segunda" está errado (04h27 GMT = 01h27 em Brasília). Trocar por "no início do pregão desta segunda".
3. Petróleo: deixar claro que US$ 109,86 foi o que a edição de sexta publicou e que é igual ao fechamento de sexta citado pela fonte; reescrever ("o fechamento de sexta foi US$ 109,86") para não sugerir que a edição de sexta já tinha o fechamento.
4. Replit: atribuir a Masad "entre os cinco maiores clientes" ("segundo Masad").
5. Disney: atribuir os US$ 20 mi à própria Character.AI e avisar que o lance inicial pode ser superado.
6. Colocar selo `**Opinião:**` (ou cortar) em "na prática, o custo chega pelos contratos" (Petrobras), "na prática, o perfil vira balcão de consultoria" (LinkedIn) e, se quiser manter, "na prática, crescer menos com juro igual" (Focus).
7. Stats: considerar uma frase com o contrapeso da própria fonte (não há crise; PIB nominal acima dos juros), pois a cadeia sozinha é uma leitura unilateral.
8. Links: remover o prefixo redundante `[Para ler]` dos três itens; no Import AI, trocar "diz ao FMI" por "em palestra na reunião do FMI".

Todos os números centrais (Focus, Ibovespa, China, Brent, Braskem, Petrobras, Disney, stablecoins, juros dos EUA e a conta 1,05 tri / 365 = 2,9 bi) foram confirmados.
