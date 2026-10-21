# Verificação: edição nº 6 (21/10/2026)

Dois checadores independentes (Sonnet). Todas as correções obrigatórias das duas partes foram aplicadas na edição, exceto: o US$ 1 bi da SpaceX ficou como 'receita engordada por ~US$ 1 bi', porque o TechCrunch diz literalmente 'top-line revenue number was also boosted by about $1 billion in income'. O formato Otimistas/Pessimistas é o padrão do manual (seção 5) e foi mantido sem selo. Links: 22 verificados, 19 ok, 0 quebrados, 3 inconclusivos (403 de investing.com, pnas.org e sec.gov; os três foram confirmados por outro caminho: WebFetch, Crossref e busca efts da SEC).

---

# Verificação da edição 2026-10-21 (Parte 1: abertura até IA NA PRÁTICA, mais as demais seções conferidas por extensão)

Método: cada link aberto com WebFetch ou curl. Investing.com e SEC (browse-edgar) devolveram 403 no curl; Investing foi lido pelo WebFetch, PNAS pelo Crossref, SEC pela busca full-text (efts). Conteúdo da web tratado como dado.

## 1. Abertura, Hoje eu aprendi, Nesta edição

| Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|
| "perdeu cinco vezes o que faturou" (80,7 / 16,3 = 4,95) | Investing.com | confirmada (conta ok) | nenhuma |
| 16 anos após Deepwater Horizon (2010 + 16) | Yale E360 | confirmada | nenhuma |
| Queda de 60% a 85% em 3,5 anos; "mais de uma década" | PNAS (Crossref: "declined by 60 to 85%", "3.5-y", "over a decade") | confirmada | Yale E360 não traz o intervalo 60-85%; ele só está no PNAS. Aceitável com os dois links. |
| "vida no fundo do Golfo do México" / "Peixes, crustáceos e lulas de profundidade" | PNAS | parcialmente errada | O estudo trata da coluna d'água profunda (deep-pelagic: peixes, crustáceos e cefalópodes, sobretudo krill e peixes-lanterna), não do leito. Trocar "no fundo" por "nas águas profundas". |
| "Os autores dizem que o vazamento é a explicação mais simples, mas não provam a causa" | PNAS ("most parsimonious explanation"); Yale | confirmada | nenhuma |
| "receita 15 vezes maior"; "prejuízo quase todo contábil" | Investing.com (US$ 16,3 bi vs US$ 1,1 bi; US$ 72 bi de US$ 80,7 bi) | confirmada | nenhuma |
| "a Anthropic achou 493 problemas apagando o que ninguém usa" | Anthropic | parcialmente errada | O post conta 493 achados de análise de superfície de ataque, não "problemas achados apagando". Reescrever: "achou 493 problemas de superfície de ataque em 25 projetos". |
| iFood/Caju; "mercado não gostou do preço que a Ânima vai pagar" ; SpaceX "fatura mais com IA do que com foguete" | InvestNews, TechCrunch | confirmada | nenhuma (ver itens abaixo) |

## 2. Matéria principal (IA)

| Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|
| WSJ viu rascunho do S-1 | Investing.com ("preliminary S-1", "WSJ") | confirmada | nenhuma |
| Receita do 1º semestre US$ 16,3 bi | TechCrunch e Investing | confirmada | nenhuma |
| "contra US$ 1,1 bi um ano antes", link TechCrunch | TechCrunch não traz o valor do ano anterior | número atribuído ao link errado | O US$ 1,1 bi está só no Investing.com. Citar o Investing nessa frase (ou os dois). |
| "Dá 15 vezes mais" (16,3 / 1,1 = 14,8) | conta | confirmada (arredondamento ok) | nenhuma |
| Na base da SEC não há S-1 da Anthropic (link browse-edgar) | SEC | confirmada indiretamente | O link browse-edgar dá 403 para robôs e não pode ser conferido por quem clica de fora. A busca full-text do EDGAR por "Anthropic PBC" em S-1/DRS não retorna nenhum S-1 da empresa (só fundos "X Anthropic LP"). Sugestão: dizer "não encontramos S-1 público" (um rascunho confidencial não aparece na base). |
| Contexto: dia 17, US$ 16,8 bi no 3º trimestre | edição de 17/10 (mesmo texto); TechCrunch 20/10 também diz US$ 16,8 bi, +45% | confirmada | Na ed. 17 foi dito "segundo um investidor que estava na apresentação". Aqui o texto soa como a empresa tendo dito. Ajustar: "teria dito a investidores". |
| Dia 19, prometeu 5% das ações a fundo de benefício público | edição de 19/10 | confirmada (interna) | nenhuma |
| Prejuízo US$ 80,7 bi no semestre | Investing.com | confirmada | nenhuma |
| "Cerca de US$ 72 bi" de ajustes contábeis (dívidas conversíveis e outros instrumentos), sem saída de caixa | Investing.com (US$ 72 bi, non-cash, convertible notes e financing instruments) | confirmada | nenhuma |
| "Sem eles, pela conta da gente, sobram uns US$ 9 bi" (80,7 - 72 = 8,7) | conta da gente | confirmada (arredondamento ok) | nenhuma |
| Computação: quase US$ 9 bi em 6 meses, mais que US$ 7,3 bi de 2025 inteiro | Investing.com | confirmada | Fonte fala em "compute and infrastructure spend"; ok. |
| ~US$ 450 bi em 10 anos: Google 111, AWS 110, Microsoft 31 | Investing.com | confirmada | Omite o que a fonte também diz: possível gasto de até US$ 750 bi com negociações em curso (TechCrunch: "more than $750 billion"). Sugestão: acrescentar para não passar impressão de teto. |
| Dois clientes ~20% da receita | TechCrunch e Investing | confirmada | nenhuma |
| "pediu mais capacidade do que AWS, Google e Microsoft aceitaram fornecer" | TechCrunch ("struggling to secure enough capacity", rivais veem como concorrente) | não confirmada (parafraseada além da fonte) | Trocar por: "teria dificuldade para garantir capacidade suficiente com AWS, Google e Microsoft, que a veem cada vez mais como concorrente". |
| Aluga data centers e usa operadores com "limited operating history" | TechCrunch | confirmada | A aspa existe na fonte. |
| Risco de responsabilização por danos acima do seguro | TechCrunch | confirmada | nenhuma |
| "US$ 450 bi é cerca de 14 vezes a receita do semestre em ritmo anual (US$ 32,6 bi)" (450 / 32,6 = 13,8) | conta da gente | aritmética confirmada | Conceito frágil: compara compromisso de 10 anos com receita de 1 ano, sem dizer isso. Explicitar "compromisso de dez anos ante um ano de receita". |
| "Se o 3º trimestre de US$ 16,8 bi se confirmar, um trimestre fatura mais do que o semestre inteiro" | 16,8 > 16,3 | confirmada (conta ok) | nenhuma |
| "Os otimistas / Os pessimistas" | sem fonte nomeada | opinião sem selo | Manual 14.6: previsão exige "a aposta é" e quem aposta. Rotular como análise da newsletter com `**Opinião:**` ou atribuir a analistas citados. |
| "E a empresa depende de rivais para ter máquina" | TechCrunch (rivais veem como concorrente) | confirmada em essência | nenhuma |
| "o Claude Code roda nessa conta. Quem vende serviço em cima de uma única ferramenta herda o risco do fornecedor: preço, limite de uso e fila" | nenhuma | opinião sem selo (o selo só cobre a última frase) | Mover o selo `**Opinião:**` para o início do trecho. |

## 3. IA NA PRÁTICA

| Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|
| 25 projetos abertos, mais de 5 milhões de linhas | Anthropic | confirmada | nenhuma |
| Mais de 17.000 opções de configuração, 3.842 de segurança, 493 problemas | Anthropic | confirmada | nenhuma |
| Post assinado por Chris Rohlf, "do time de segurança da empresa" | Anthropic (campo Team: Frontier Red Team) | parcialmente correta | Escrever "do Frontier Red Team da Anthropic". |
| 162 combinações aceitas sem erro, aviso ou documentação; 94 desligavam um controle | Anthropic | confirmada | nenhuma |
| OpenSSH 10.4, ~4.500 linhas de código experimental (ML-DSA-44) alcançáveis sem login, ~16% do código pré-autenticação | Anthropic | confirmada | Conferir o termo "código que roda antes da autenticação" (sshd em configuração padrão). Ok. |
| "A versão 10.6 terminou de corrigir" | Anthropic (corrigido na 10.6; a 10.5 deixou lacunas) | confirmada | nenhuma |
| "É pesquisa inicial, nas palavras do post" | Anthropic ("some of our initial research"; "only a very limited view") | confirmada com ressalva | A frase "pesquisa inicial" não é aspas literais; trocar "nas palavras" por "o post descreve como parte de pesquisa inicial". |
| "Muitos achados não eram exploráveis sozinhos" | Anthropic (só os 11 projetos "Gated" são descritos como "would not have been immediately exploitable on their own") | parcialmente confirmada | Restringir: "os achados do grupo Gated não eram exploráveis sozinhos". |
| "o post não diz quantos dos 493 foram corrigidos" | Anthropic | confirmada | nenhuma |
| "O método usa testes automáticos para conferir que nada quebrou" | Anthropic ("running the project's own test suite ... against the baseline") | confirmada | nenhuma |
| eMudhra: chaves de 8 intermediários | emudhra.we-have-a-problem.com; Simon Willison ("eight") | confirmada | Nuance: as chaves foram geradas de forma incorreta e podem ser recuperadas dos certificados; "vazaram" é impreciso. Sugestão: "foram comprometidas". |
| Firefox e Chrome bloquearam desde o dia 17, Apple dia 19, Microsoft dia 20 | emudhra.we-have-a-problem.com | confirmada | As datas estão só no site do incidente, não no post do Simon Willison (que não traz datas). Citar o site do incidente nessa frase. |
| "Com elas, daria para se passar por qualquer site" | emudhra.we-have-a-problem.com ("impersonate any website") | confirmada | Acrescentar que navegadores com Certificate Transparency não teriam sido atacados; o risco maior é em clientes fora do ecossistema de navegadores. |
| "Esta semana vazaram" | emudhra (certs de abril de 2025; reporte em 17/10; divulgação em 19/10) | parcialmente correta | Trocar por "esta semana foi revelado". |
| Aplicações para advogado ("vira prova de diligência"), e-commerce, clínica ("ainda é um caminho até o prontuário") | sem fonte | opinião/afirmação jurídica sem selo | Marcar com `**Opinião:**` ou suavizar ("pode ajudar a demonstrar diligência"). A frase do advogado é afirmação jurídica sem base. |
| "um vazamento custa mais, inclusive em LGPD" | sem fonte | não confirmada | Cortar "inclusive em LGPD" ou rotular como opinião. |

## 4. Seções seguintes (conferidas por extensão)

| Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|
| Ibovespa +1,57% a 208,3 mil; queda de 0,17% na véspera; dólar -0,58% a R$ 5,019 | InfoMoney (208.295,98; -0,17% em 19/10; R$ 5,019, -0,58%) | confirmada | nenhuma |
| Panda bonds: "primeira emissão ... cerca de 10 bi de yuans (US$ 1,5 bi)" | InvestNews/Bloomberg | parcialmente errada | A meta total é ~10 bi de yuans (US$ 1,5 bi); a emissão inaugural seria de 5 bi de yuans. A venda seria na semana após o 2º turno (25/10). Corrigir. |
| "o Tesouro não comentou" | InvestNews ("não havia respondido ao pedido de comentário") | parcialmente correta | Trocar por "não respondeu ao pedido de comentário". |
| Hoje: WEG antes da abertura; IGP-M 2ª prévia às 8h | InfoMoney | confirmada | nenhuma |
| SpaceX: lucro líquido US$ 4,4 bi, receita US$ 14,6 bi | TechCrunch | confirmada | nenhuma |
| "cerca de US$ 1 bi dessa receita veio da alta do Bitcoin e de partes relacionadas" | TechCrunch ("about $1 billion in income related to the recovery of Bitcoin prices" mais renda de partes relacionadas não quantificada) | errada | É resultado (income), não receita; e o US$ 1 bi é só do Bitcoin, partes relacionadas vêm à parte, sem valor. Corrigir: "cerca de US$ 1 bi do lucro veio da recuperação do Bitcoin, além de ganhos com partes relacionadas". |
| Meta e Tesla divulgam hoje; "é o próximo teste de quanto as big techs gastam com IA" | InfoMoney | datas confirmadas; frase final é opinião sem selo | Selar `**Opinião:**` ou cortar. |
| iFood Benefícios e Caju: 1,7 mi e 1,3 mi usuários; Cade e BC | NeoFeed | confirmada | "somando" sugere 3 mi, mas a fonte diz "antes de sobreposição". Ok. "o valor não foi divulgado, e o NeoFeed fala em mais de R$ 1,2 bi" ok (apuração própria). |
| Ânima: -9% ontem, 15 cursos, 20 anos, R$ 150 mi de entrada, BTG > R$ 600 mi | InvestNews | confirmada | nenhuma |
| Patria / HGRU11 / 22 lojas / ~R$ 1 bi / sem comentário | NeoFeed (22 ativos do Atacadão) | confirmada | "22 lojas": a fonte diz 22 ativos. Trocar por "22 ativos". |
| Salesforce/Braze: US$ 47,50 em dinheiro, ~US$ 5,66 bi; fechamento a partir de fev/2027 | PPC Land | confirmada | US$ 5,66 bi é enterprise value; o fechamento é esperado no ano fiscal 2028 (começa em 1/2/2027), sujeito a aprovações. |
| Yelp: US$ 30/mês a partir de novembro; atendente de telefone por IA custa US$ 99 | PPC Land | parcialmente confirmada | US$ 99 é o preço de lançamento do Yelp Receptionist (outono 2025); a fonte não traz o preço atual. Escrever "custava US$ 99 no lançamento, em 2025". |
| Meta pausou compartilhamento do Muse; Claroc achou ~6.800 links | The Verge ("more than 6,800 Muse links") | confirmada ("cerca de" vs "mais de") | Trocar "cerca de 6.800" por "mais de 6.800". |
| "alguns com dados de empresas e de bancos" | The Verge (receita de empresa de marketing, empréstimo de dono de pequeno negócio, agenda de empresa, notas de candidato) | errada | Não há dados de bancos. Corrigir: "alguns com dados de empresas e pedidos de empréstimo". Também: a Claroc viu centenas de conversas, não 6.800. |
| Anthropic/projeto de lei: só juiz federal suspende; >50 pessoas ou >US$ 1 bi; agências proibidas | TechCrunch | confirmada | A fonte diz que o Commerce teria de pedir a um juiz de Washington; risco "foreseeable, imminent". "em danos" é "em danos materiais". Adicionar "o Congresso ainda não adotou". |
| "na prática, quem decide é o Judiciário, não o regulador" | análise própria | opinião sem selo | Selar `**Opinião:**` (o Commerce ainda inicia o pedido). |
| STATS: 52%, US$ 7,5 bi de US$ 14,6 bi | TechCrunch ("52% of its income") | número da fonte confirmado, conta não fecha | 7,5 / 14,6 = 51,4%, ou seja 51%. A fonte diz 52% de "income". Corrigir para "pouco mais da metade (7,5 de 14,6 bi, 51%)" ou escrever "52%, segundo o TechCrunch" e avisar da diferença. Manchete e título da seção usam 52%. |
| "Super Intelligence" junta Grok, Cursor, aluguel de computação, 1,7 GW | TechCrunch | confirmada | Cursor "comprado há pouco" ok. |
| IA deu US$ 431 mi de lucro | TechCrunch | confirmada | Informar que seria maior sem US$ 1,2 bi de remuneração em ações ligada ao Cursor. |
| US$ 19,6 bi de investimento no trimestre, "mais do que faturou" | TechCrunch (capex) | confirmada (19,6 > 14,6) | nenhuma |
| "Para o 4º trimestre, a previsão é de US$ 35 bi a US$ 40 bi" | TechCrunch (é gasto em investimento, não receita) | enganosa | Escrever "a previsão de investimento para o 4º trimestre é de US$ 35 bi a US$ 40 bi". |
| "A cadeia: ... a conta só fecha se a demanda continuar subindo" | análise própria | opinião sem selo | `**Opinião:**` |
| Steve Krouse, "What Shall I Teach My Son?", Postman | stevekrouse.com | confirmada | nenhuma |
| Battle Drones: 321 commits, estilo C&C, multiplayer por som | Simon Willison | confirmada | A fonte diz que depois foi adicionado multiplayer online. |
| MIT Tech Review: edição sobre ideias impossíveis, sangue sintético, falar com animais | technologyreview.com | confirmada | A carta é de Corinne Iozzio, edição nov/dez ("Impossible issue"). "abre a edição" ok. |

## Correções obrigatórias

1. SpaceX, linha "Lá fora": o US$ 1 bi é lucro (income) da recuperação do Bitcoin, não "receita ... e de partes relacionadas".
2. STATS: 7,5 / 14,6 = 51%, não 52%. Ou explicar que 52% é o número da fonte sobre "income", ou usar "mais da metade".
3. STATS: US$ 35-40 bi no 4º trimestre é previsão de investimento, não de receita; dizer isso.
4. Meta/Muse: tirar "bancos" (não está na fonte); trocar "cerca de 6.800" por "mais de 6.800".
5. Matéria principal: US$ 1,1 bi do ano anterior não está no TechCrunch; apontar o Investing.com nessa frase.
6. Matéria principal: "pediu mais capacidade do que ... aceitaram fornecer" não está na fonte; reescrever como "teria dificuldade para garantir capacidade".
7. Panda bonds: a emissão inaugural é de 5 bi de yuans; 10 bi de yuans (US$ 1,5 bi) é a meta total. "Não comentou" vira "não respondeu".
8. Hoje eu aprendi: "no fundo do Golfo" vira "nas águas profundas" (o estudo trata da coluna d'água).
9. Nesta edição: "achou 493 problemas apagando o que ninguém usa" distorce o post; reescrever.
10. IA NA PRÁTICA: "Muitos achados não eram exploráveis sozinhos" deve ser restringido aos achados do grupo Gated; "nas palavras do post" não é citação literal.
11. Opinião sem selo (manual 14.6): "Os otimistas / Os pessimistas", frase do risco de fornecedor única, aplicações para advogado ("prova de diligência"), "inclusive em LGPD", "é o próximo teste ... big techs", "quem decide é o Judiciário", "a conta só fecha se...".
12. Yelp: US$ 99 é o preço do lançamento em 2025, não o atual.
13. eMudhra: datas dos bloqueios só estão no site do incidente (não no Simon Willison); trocar "vazaram" por "foram comprometidas".
14. Patria: "22 lojas" vira "22 ativos". Contexto 17/10: "disse a investidores" deveria ser "teria dito".
15. Salesforce/Braze: US$ 5,66 bi é valor da empresa (enterprise value); dizer isso.

## Pontos de atenção (não obrigatórios)

- Compromisso de ~US$ 450 bi: a fonte também cita até US$ 750 bi com negociações em curso (TechCrunch); a razão de "14 vezes" compara 10 anos de compromisso com 1 ano de receita, e isso deve ficar explícito.
- Link browse-edgar da SEC não abre para quem usa robô (403); considerar linkar a página de busca do EDGAR em navegador ou reescrever a frase como "não encontramos".
- Verge: a Claroc revelou centenas de conversas legíveis, não 6.800.

---

# Verificação parte 2 (Economia até Pergunta) - edição 2026-10-21

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Ibovespa +1,57%, 208,3 mil pts, em 20/10 | InfoMoney | confirmada (fecha 208.295,98) | - |
| 2 | Queda de 0,17% da véspera; "devolveu com sobra" | InfoMoney | confirmada | - |
| 3 | Dólar -0,58%, R$ 5,019 | InfoMoney | confirmada | - |
| 4 | Panda bonds: ~10 bi de yuans (US$ 1,5 bi), após o 2º turno, Bloomberg | InvestNews | confirmada, com ressalva | A primeira emissão seria de 5 bi de yuans; os 10 bi são o total buscado. Fonte única anônima. A fonte diz que o Tesouro "não respondeu de imediato", não que "não comentou". Trocar por "o Tesouro não respondeu até a publicação". |
| 5 | WEG divulga balanço do 3T antes da abertura; 2ª prévia do IGP-M às 8h | InfoMoney (21/10) | confirmada | - |
| 6 | Meta e Tesla divulgam balanços do 3T hoje | InfoMoney | confirmada | - |
| 7 | "na prática, é o próximo teste de quanto as big techs gastam com IA" | - | opinião sem selo | Pôr `**Opinião:**` ou cortar. |
| 8 | SpaceX: lucro líquido US$ 4,4 bi, receita US$ 14,6 bi | TechCrunch | confirmada | - |
| 9 | "cerca de US$ 1 bi dessa receita veio da alta do Bitcoin e de partes relacionadas" | TechCrunch | errada (imprecisa) | A fonte fala em ganho não operacional de ~US$ 1 bi, não em receita. Escrever: "cerca de US$ 1 bi do lucro veio de ganho não operacional (recuperação do Bitcoin e receitas de partes relacionadas)". |
| 10 | iFood Benefícios compra a Caju, 1,7 mi e 1,3 mi de usuários | NeoFeed | confirmada | Fonte diz "mais de 1,3 mi" de trabalhadores na Caju. |
| 11 | "valor não foi divulgado"; NeoFeed fala em mais de R$ 1,2 bi; depende de Cade e BC | NeoFeed | confirmada | Deixar claro que o R$ 1,2 bi é apuração do NeoFeed (a frase atual já diz isso). Cade foi notificado em 20/10. |
| 12 | Ânima cai 9% ontem; marca Einstein em 15 cursos de medicina por 20 anos; R$ 150 mi de entrada; BTG > R$ 600 mi | InvestNews | confirmada | A entrada exclui comissões e outros pagamentos; o R$ 600 mi é em valores de hoje. |
| 13 | Patria/HGRU11 compra 22 lojas do Atacadão, ~R$ 1 bi, sale-leaseback, Patria não comenta | NeoFeed | confirmada | - |
| 14 | Salesforce compra Braze por US$ 47,50/ação em dinheiro, ~US$ 5,66 bi | PPC Land | confirmada, com ressalva | US$ 47,50 é por ação Classe A; US$ 5,66 bi é valor da empresa (enterprise value). Dizer "valor da empresa". |
| 15 | Fechamento esperado a partir de fevereiro de 2027 | PPC Land | confirmada, com ressalva | A fonte diz "ano fiscal 2028", que começa em 1/2/2027; depende de acionistas e reguladores. Escrever "no ano fiscal de 2028 da Salesforce (a partir de fev/2027)". |
| 16 | Yelp: US$ 30/mês, a partir de novembro, agente que responde e qualifica pedidos de orçamento | PPC Land | confirmada | - |
| 17 | Atendente de telefone por IA custa US$ 99 | PPC Land | não confirmada | A fonte cita US$ 99 como preço do Receptionist no lançamento (outono de 2025) e diz que pode estar defasado. Cortar ou escrever "custava US$ 99 no lançamento". |
| 18 | Meta pausou o compartilhamento do Muse; pesquisadores da Claroc; cerca de 6.800 links | The Verge (via curl; WebFetch bloqueado) | confirmada, com ressalva | A fonte diz "mais de 6.800" (via registros DNS públicos). Trocar "cerca de" por "mais de". |
| 19 | Links com "dados de empresas e de bancos" | The Verge | não confirmada | Os exemplos citados são: revisão de receita de uma agência de marketing, pedido de empréstimo de um dono de pequeno negócio, calendário de equipe e notas de candidato. Nada sobre bancos. Trocar por "dados de empresas e pedidos de empréstimo". |
| 20 | Anthropic mostra a congressistas rascunho de lei; só um juiz federal pode suspender; >50 pessoas ou >US$ 1 bi; agências proibidas de barrar sozinhas | TechCrunch (citando Politico) | confirmada, com ressalva | O fluxo: avaliadores independentes registrados no Commerce Dept. avisam o Commerce em 72 h, que pede a um juiz de Washington D.C. a suspensão. O US$ 1 bi é em danos materiais. É um rascunho "reportado" (Politico), então atribuir: "segundo o Politico". |
| 21 | "na prática, quem decide é o Judiciário, não o regulador" | - | opinião sem selo | O Commerce é quem aciona o juiz. Pôr `**Opinião:**` ou reescrever como fato: "o Commerce teria de pedir a um juiz". |
| 22 | STATS: IA = 52% da receita da SpaceX, US$ 7,5 bi de US$ 14,6 bi | TechCrunch | confirmada, com ressalva | 7,5/14,6 dá 51,4%. A fonte diz "52% of income". Manter 52% atribuído à TechCrunch, ou escrever "cerca de metade". |
| 23 | Segmento "Super Intelligence": Grok, Cursor (comprado há pouco) e computação; 1,7 GW | TechCrunch | confirmada | A fonte chama de "neocloud". |
| 24 | "já fatura mais com IA do que com todo o resto junto" | TechCrunch | confirmada (inferência de 52%) | Aceitável, mas depende do arredondamento (item 22). |
| 25 | IA deu US$ 431 mi de lucro | TechCrunch | confirmada | A fonte diz que seria maior sem US$ 1,2 bi de remuneração em ações ligada ao Cursor. Vale uma ressalva. |
| 26 | US$ 19,6 bi de investimento no trimestre, mais do que faturou | TechCrunch | confirmada | - |
| 27 | "Para o 4º trimestre, a previsão é de US$ 35 bi a US$ 40 bi" | TechCrunch | errada (ambígua) | São novos investimentos de capital (capex), não receita. A frase solta lê-se como receita. Escrever "a previsão de investimento (capex) para o 4º trimestre é de US$ 35 a 40 bi". |
| 28 | "A cadeia: ... a conta só fecha se a demanda continuar subindo. É a mesma aposta da matéria principal" | - | opinião sem selo | Pôr `**Opinião:**`. |
| 29 | Krouse: programador prestes a ser pai pergunta para que serve a escola | stevekrouse.com/ends | confirmada | - |
| 30 | "Parte de *The End of Education*, de Neil Postman" | stevekrouse.com/ends | errada | O ensaio é uma reflexão inspirada no livro de Postman, não parte dele. Escrever "inspirado em *The End of Education*, de Neil Postman". |
| 31 | Battle Drones: estilo Command & Conquer, quase todo por agentes, 321 commits, multiplayer por som | simonwillison.net | confirmada | - |
| 32 | MIT TR: "abre a edição" sobre ideias impossíveis, de sangue sintético a conversar com animais | technologyreview.com | confirmada | É a carta da editora (Corinne Iozzio) da edição nov/dez 2026. Opcional citar. |
| 33 | Pergunta do dia | - | sem afirmação factual | - |

## Correções obrigatórias
1. SpaceX, item 9: o ~US$ 1 bi é ganho não operacional (Bitcoin e partes relacionadas), não parte da receita.
2. SpaceX, item 27: US$ 35 a 40 bi é capex previsto, não receita; deixar explícito.
3. Yelp, item 17: o US$ 99 do atendente telefônico é preço de lançamento, possivelmente defasado. Cortar ou qualificar.
4. Meta, item 19: cortar "bancos"; a fonte não menciona. Item 18: "mais de 6.800", não "cerca de".
5. Para ler, item 30: o ensaio de Krouse é inspirado no livro de Postman, não "parte" dele.
6. Selo `**Opinião:**` faltando em: "na prática, é o próximo teste..." (Lá fora, Hoje), "na prática, quem decide é o Judiciário..." (Anthropic) e o parágrafo "A cadeia..." (STATS).
7. Panda bonds, item 4: a primeira emissão é de 5 bi de yuans (10 bi é o total buscado); o Tesouro "não respondeu de imediato".
8. Anthropic, item 20: atribuir o rascunho ao Politico (via TechCrunch) e descrever o papel do Commerce Dept.

## Ressalvas menores (recomendadas)
- Braze: dizer "valor da empresa" e "ano fiscal 2028 da Salesforce (a partir de fev/2027)".
- STATS: 52% (fonte) versus 51,4% (7,5/14,6); manter atribuído ou usar "cerca de metade".
- SpaceX: citar a ressalva de US$ 1,2 bi em remuneração em ações do Cursor no lucro de US$ 431 mi.
- The Verge bloqueou o WebFetch; a conferência foi feita com curl.
