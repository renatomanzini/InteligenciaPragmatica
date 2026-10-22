# Verificação: Mercado de 22/10/2026 (quinta), nº 1, teste

Checagem independente do `edicao.md` (escrito por volta das 09:20). Fontes lidas em 22/10/2026, depois das 09:26.

**Como foi feito.** Os 13 links foram abertos. WebFetch funcionou no InfoMoney, no Money Times e no Exame de 21/10; deu 403 na CNBC e no Exame de 22/10, e o Valor está bloqueado. Nesses casos baixei com `curl -sL -A "Mozilla/5.0"` e li o texto. O Valor de "NY sobe com techs" é paywall: só o lead (título, subtítulo e 1º parágrafo) abriu. Li também a matéria do Valor sobre Ormuz (`valor.globo.com/mundo/noticia/2026/10/22/ir-relata-ataques-a-sete-petroleiros-...`), que não é citada na edição, só para checar a frase "sem confirmação independente".

**Dias da semana (`date`):** 21/10/2026 = quarta; 22/10/2026 = quinta; 25/10/2026 = domingo (segundo turno). Tudo certo na edição.

**Painel x texto:** todo número do painel citado no texto tem a mesma grafia (Ibovespa 0,86%; S&P 500 0,58%; Nasdaq 1,05%; Dow Jones 0,69%; VIX 8,45%; dólar 0,43%; Brent US$ 111,95; bitcoin 3,15% e US$ 81.778). Nenhum foi reescrito.

**Contagem:** 727 palavras fora o painel (alvo 450 a 750: ok). A história do dia tem 233 palavras sem título e TL;DR, 260 com o TL;DR e 277 com tudo (alvo 150 a 250: no limite, depende de como se conta).

## Tabela de afirmações

Resumo: 55 afirmações conferidas. 39 confirmadas, 12 confirmadas com ressalva, 4 não confirmadas (linhas 2, 11, 30 e 38), 0 erradas de fato, 0 opiniões sem selo. As ressalvas e as "não confirmadas" viram as correções abaixo.

### Abertura

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Cautela às vésperas do segundo turno | InfoMoney (título: "cautela eleitoral"; "a quatro dias do segundo turno"); Exame 22/10 ("cautela eleitoral ... às vésperas do segundo turno, marcado para domingo, 25") | confirmada | nenhuma |
| 2 | "cautela **de sempre**" | nenhuma das duas diz que é recorrente | não confirmada | tirar "de sempre": "a cautela às vésperas do segundo turno" |
| 3 | "A bolsa daqui ainda nem abriu" | InfoMoney fala do Ibovespa futuro nos "primeiros negócios"; a abertura da B3 às 10h não está na fonte, mas é horário público | confirmada, com ressalva | nenhuma |

### O que mexeu ontem (21/10)

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 4 | Ibovespa caiu 0,86% | Exame 21/10 ("recuou 0,86%, aos 206.495,23 pontos"); painel | confirmada | nenhuma |
| 5 | 46 das 76 ações do índice no vermelho | Exame 21/10 ("Das 76 ações que compõem o índice, 46 terminaram o dia em baixa") | confirmada | nenhuma |
| 6 | WEG despencou 7,34% depois de balanço abaixo do esperado | Exame 21/10 (WEG -7,34%; lucro R$ 1,67 bi contra R$ 1,71 bi esperados, margens abaixo do esperado) | confirmada | nenhuma. Acertou em não citar o lucro: Money Times diz R$ 1,66 bi |
| 7 | Vale perdeu 2,15% | Exame 21/10 | confirmada | nenhuma |
| 8 | O dia foi de cautela com o segundo turno | Exame 21/10 ("cautela provocada pelo cenário eleitoral") | confirmada | nenhuma. Sem pesquisa nem nomes no texto |
| 9 | S&P 500 +0,58%, Nasdaq +1,05%, Dow +0,69% | painel; Exame 21/10 (7.757,17; 26.702,86; 52.856,09). **O Valor linkado não traz esses números** (só o lead abriu) | confirmada, com ressalva | opcional: citar o Exame também, que traz os três números |
| 10 | Subiram "com os primeiros balanços de tecnologia" | Valor, lead: "início da temporada de balanços", "impulso do setor de tecnologia" | confirmada, com ressalva | "com o início da temporada de balanços, puxado pela tecnologia" |
| 11 | Fecharam longe das máximas "**por causa de** novos ataques no Oriente Médio" | Valor, lead: "afastados das máximas, **em meio a** novos ataques no Oriente Médio" | não confirmada (a fonte não faz a ligação de causa) | trocar "por causa de" por "em meio a" |
| 12 | VIX subiu 8,45% (índice do medo nas opções do S&P 500) | painel; explicação de meia frase presente | confirmada | nenhuma |
| 13 | Brent +0,03%, a US$ 108,82 | Exame 21/10 (contrato de dezembro, ICE) | confirmada | nenhuma |
| 14 | Dividido entre expectativa de avanço diplomático EUA-Irã e risco de oferta | Exame 21/10 | confirmada | nenhuma |
| 15 | "Hoje ele acordou com outra ideia" | painel (Brent US$ 111,95, +2,88%) | confirmada (humor sobre dado do painel) | nenhuma |

### A história do dia

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 16 | Brent a US$ 111,95 | painel; InfoMoney ("chegando a ser cotado em US$112"); Money Times ("mais de US$ 112", +3,3% de madrugada) | confirmada | nenhuma |
| 17 | Ataques à Arábia Saudita atribuídos a houthis do Iêmen | InfoMoney ("novos ataques dos militantes houthis, do Iêmen, contra a Arábia Saudita") | confirmada | nenhuma |
| 18 | Relato da TV estatal do Irã sobre sete petroleiros em chamas em Ormuz | Valor (Ásia): "sete petroleiros pegaram fogo e foram danificados". Valor (Mundo): "pegaram fogo **ou** sofreram danos", por ataques iranianos ou minas navais | confirmada, com ressalva | "sete petroleiros que teriam pegado fogo ou sido danificados" |
| 19 | "Sem confirmação independente nas fontes consultadas" | Valor (Mundo): a AP "não conseguiu confirmar de forma independente"; o UKMTO "não confirmou" os episódios | confirmada | nenhuma |
| 20 | Ormuz = saída marítima do petróleo do Golfo | Valor (Mundo): "uma das principais rotas de transporte de petróleo e gás natural do mundo" | confirmada | nenhuma |
| 21 | Kospi caiu 3,52% | Money Times (3,52%, para 5.533,77) | confirmada | ver correção sobre termos (Kospi sem explicação) |
| 22 | Nikkei caiu 2,65% | Money Times | confirmada | idem |
| 23 | Tecnologia do Hang Seng -5%, o pior desde abril de 2025 | Money Times ("queda de 5% do seu componente de tecnologia, a maior desde abril de 2025") | confirmada | nenhuma |
| 24 | Os números da Ásia ficam sem link na própria frase; o link do Money Times aparece só na frase seguinte | Money Times | confirmada, com ressalva | pôr o link ao fim da frase dos números |
| 25 | "O Money Times aponta o temor com o retorno dos investimentos em IA, após a Tesla cortar o capex" | Money Times: "temores sobre o ritmo e o retorno dos agressivos investimentos em IA ganharam força após a Tesla reduzir sua meta de capex para 2026". O texto é da Estadão Conteúdo, republicado no Money Times | confirmada, com ressalva | opcional: "a Estadão Conteúdo, no Money Times, aponta" |
| 26 | Tesla cortou o capex de 2026 para cerca de US$ 20 bi, de mais de US$ 25 bi | CNBC (matéria de analistas): JPMorgan "~$20 bn from ~$25 bn+"; Barclays "$20bn vs prior guidance of $25bn+". A CNBC diz que Tesla justificou o corte por "capital efficiency" e que o gasto operacional (opex) subiu | confirmada, com ressalva (números vêm de notas de analistas, não do comunicado da Tesla) | "segundo analistas citados pela CNBC", ou trocar pela fonte primária (apresentação de resultados da Tesla) |
| 27 | Capex = gasto em fábricas, chips e data centers | explicação do redator; a fonte não define | confirmada, com ressalva | nenhuma |
| 28 | Às 9h04, Ibovespa futuro -0,68% | InfoMoney ("Por volta das 9h04 ... caía 0,68%, aos 208.060 pontos") | confirmada | nenhuma |
| 29 | Dólar futuro +0,57% | InfoMoney ("aos R$ 5,061") | confirmada | "dólar futuro" sem explicação (ver termos) |
| 30 | TL;DR e título: "a Ásia caiu **até 3,52%**" | Money Times: Kospi -3,52% é a maior queda entre os índices principais, mas o corpo da própria edição traz -5% na tecnologia de Hong Kong | não confirmada (contradição interna) | "os principais índices da Ásia caíram até 3,52%" |
| 31 | American Airlines cortou a previsão; quarta grande aérea dos EUA a fazer isso em outubro | CNBC ("fourth major U.S. carrier to cut its 2026 forecast this month") | confirmada | nenhuma |
| 32 | Gasto em combustível 67,5% maior no 3º tri, US$ 4,64 bi | CNBC ("up 67.5% ... to $4.64 billion") | confirmada | nenhuma |
| 33 | "~R$ 23 bi" | conversão do redator: 4,64 x R$ 5,05 (dólar do painel) = R$ 23,4 bi. Não está na fonte | confirmada (conta correta) | opcional: "(~R$ 23 bi pelo dólar de hoje)" |
| 34 | Passagens mais de 20% mais caras em um ano | CNBC ("driven up airfare more than 20% from last year"), no contexto dos EUA | confirmada, com ressalva | "nos EUA", para ninguém ler como preço no Brasil |
| 35 | Dólar em alta de 0,43% | painel (R$ 5,05, +0,43%, às 09:17) | confirmada | deixar claro que é o dólar à vista; um parágrafo acima já aparece o dólar futuro +0,57% |
| 36 | "Petróleo caro pesa primeiro em quem vive de combustível" | inferência do redator. CNBC: combustível é a maior despesa das aéreas depois de mão de obra | confirmada, com ressalva (leitura do redator, sem selo) | aceitável como explicação; se quiser reforçar: "como mostra a American Airlines" |
| 37 | "Aqui, o dólar em alta ... encarece viagem e importado" | inferência econômica sem fonte | confirmada, com ressalva | "tende a encarecer" |
| 38 | "quanto do petróleo chega à bomba depende da Petrobras e do câmbio" | **nenhuma fonte**. Também é incompleto: tributos, etanol na gasolina e margens de distribuição entram no preço na bomba | não confirmada | cortar, ou trocar por frase com fonte (ver correções) |

### Agenda

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 39 | 9h30, EUA: pedidos semanais de seguro-desemprego | Valor, Exame (9h30 de Brasília) | confirmada | nenhuma |
| 40 | 199 mil na semana anterior; expectativa de 200 mil | Valor (199 mil; "Estimam-se 200 mil"). O Exame traz só os 199 mil | confirmada | nenhuma |
| 41 | Termômetro do mercado de trabalho que o Fed acompanha ao decidir os juros | Exame ("um dos fatores acompanhados pelo Federal Reserve (Fed) nas decisões sobre os juros") | confirmada | "Fed" sem explicação (ver termos) |
| 42 | 11h: Receita divulga a arrecadação de setembro | Valor | confirmada | nenhuma |
| 43 | Agosto rendeu R$ 235,6 bi, melhor agosto da série (desde 1995) descontada a inflação | Valor (R$ 235,566 bi; "o melhor para o mês em toda a série histórica, com início em 1995", nos números atualizados pela inflação) | confirmada | nenhuma |
| 44 | Leilão de LTN e NTN-F às 11h (Valor) e às 11h30 (Exame) | Valor: 11h. Exame: 11h30. A edição já avisa da divergência | confirmada | opcional: conferir no edital do Tesouro Nacional e deixar um horário só |
| 45 | Prefixados: o juro é travado na compra | Exame ("remuneração definida no momento da compra") | confirmada | nenhuma |
| 46 | Bradesco divulga o balanço do 3º tri depois do fechamento | Exame ("previsto para após o fechamento do mercado"; "noite desta quinta-feira, 22") | confirmada | nenhuma |

### Radar

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 47 | França: juro de 10 anos a 5,113%, maior em 24 anos | CNBC ("hitting 5.113%"; "fresh 24-year high") | confirmada | nenhuma |
| 48 | Passou o dos EUA pela 1ª vez desde 2013 | CNBC ("surpassing the yield on the 10-year U.S. Treasury for the first time since 2013"); coerente com o painel (EUA 5,04%) | confirmada | nenhuma |
| 49 | Investidor duvida de que a França aprove um ajuste fiscal, em meio à turbulência política | CNBC ("Investors are increasingly skeptical that France will pass a program of fiscal consolidation") | confirmada | nenhuma |
| 50 | Braskem: credores pediram nos EUA um Chapter 11 involuntário contra a Braskem America Finance | Money Times (Braskem informou na quarta, 21/10) | confirmada | nenhuma |
| 51 | Deve cerca de US$ 589 mi em notas de 2041 | Money Times ("aproximadamente US$ 589 milhões") | confirmada | "notas" sem explicação (ver termos) |
| 52 | A empresa diz que o pedido só afeta essa subsidiária | Money Times ("envolve e afeta apenas a America Finance") | confirmada | nenhuma |
| 53 | Barclays vai cortar 5 mil empregos, cerca de 5% do quadro, em plano de eficiência ligado à IA | CNBC | confirmada | nenhuma |
| 54 | Bitcoin cai 3,15%, a US$ 81.778 | **painel** (09:17). O Money Times, linkado na mesma frase, traz US$ 81.740,51 e -1,84% em 24h, às 8h45 (CoinMarketCap) | confirmada, com ressalva (número do painel ao lado de link que mostra outro número) | marcar "(painel)" ou separar a frase |
| 55 | ETFs de bitcoin dos EUA captaram US$ 528 mi numa sessão; Money Times cita realização de lucros | Money Times ("captaram US$ 528 milhões em uma sessão"; "combinação de realização de lucros ...") | confirmada | "realização de lucros" sem explicação (ver termos) |

## Itens do rigor (pente-fino)

- **Opinião sem selo:** nenhuma frase de opinião explícita. As frases 36 e 37 são inferências do redator na seção "E no seu bolso?", que o manual manda escrever; ficam sem selo se forem apenas explicação.
- **Recomendação de investimento:** nenhuma. Não há "compre", "venda", preço-alvo nem frase que sugira posição. O rodapé está certo.
- **Pesquisa eleitoral e quem lidera:** nenhuma. Não há nomes de candidatos, institutos nem números de pesquisa. A eleição entra só como efeito no preço, com fonte. Observação: os dois links do InfoMoney e do Exame contêm pesquisas e quem lidera, mas o texto da edição não repete nada; o título atual da matéria do Exame de 21/10 cita "empate entre Flávio e Lula nas pesquisas".
- **Aspas inventadas e citações acima de 15 palavras:** o texto não tem aspas.
- **Número no link errado:** só o caso do bitcoin (54); o caso do Valor "NY sobe" (9) é sanável porque os números estão no painel.
- **Termos técnicos sem meia frase de explicação:** Kospi, Nikkei e Hang Seng (nem o país aparece); "dólar futuro"; "Fed"; "realização de lucros"; "notas de 2041". Estão explicados: Brent, capex, Ibovespa futuro, Ormuz, VIX, Chapter 11, ETFs, juro de 10 anos, prefixados.

## Correções obrigatórias

1. **Wall Street, causa que a fonte não dá.**
   - Atual: "fecharam longe das máximas do dia **por causa de** novos ataques no Oriente Médio"
   - Sugerido: "fecharam longe das máximas do dia, **em meio a** novos ataques no Oriente Médio"

2. **Título e TL;DR contradizem o corpo (3,52% x 5%).**
   - Atual (TL;DR): "e a Ásia caiu até **3,52%**, também por dúvida sobre o retorno do gasto em IA."
   - Sugerido: "e os principais índices da Ásia caíram até **3,52%**, também por dúvida sobre o retorno do gasto em IA."
   - Atual (título no front matter): "a Ásia cai até 3,52%". Sugerido: "os índices da Ásia caem até 3,52%".

3. **Bitcoin: número do painel ao lado de link que mostra outro número.**
   - Atual: "→ **Bitcoin**: cai 3,15%, a US$ 81.778, mesmo com os ETFs de bitcoin dos EUA ..."
   - Sugerido: "→ **Bitcoin**: cai 3,15%, a US$ 81.778 (painel), mesmo com os ETFs ..." O Money Times mostra US$ 81.740,51 e -1,84% às 8h45; o leitor não deve achar que o 3,15% é dele.

4. **"E no seu bolso?": afirmação sem fonte e incompleta.**
   - Atual: "Aqui, o dólar em alta de 0,43% encarece viagem e importado; quanto do petróleo chega à bomba depende da Petrobras e do câmbio."
   - Sugerido: "Aqui, o dólar à vista em alta de 0,43% tende a encarecer viagem e importado." Cortar a oração da bomba. Se quiser mantê-la, precisa de link (política de preços da Petrobras) e de menção a tributos e etanol.

5. **Termos sem explicação de meia frase (manual do Mercado, seção 2).**
   - Atual: "Na Ásia, o Kospi caiu 3,52%, o Nikkei, 2,65%, e a tecnologia do Hang Seng, 5%"
   - Sugerido: "Na Ásia, o Kospi (Seul) caiu 3,52%, o Nikkei (Tóquio), 2,65%, e a tecnologia do Hang Seng (Hong Kong), 5%"
   - Atual: "o dólar futuro subia 0,57%". Sugerido: "o dólar futuro (a aposta sobre o dólar de amanhã) subia 0,57%".
   - Atual: "que o Fed acompanha ao decidir os juros". Sugerido: "que o Fed, o banco central americano, acompanha ao decidir os juros".
   - Atual: "o Money Times cita realização de lucros". Sugerido: "o Money Times cita realização de lucros (quem vende para embolsar o ganho)".
   - Atual: "em notas de 2041". Sugerido: "em notas (títulos de dívida) de 2041".

6. **Tesla: números de capex são de analistas, não da empresa.**
   - Atual: "após a Tesla cortar o *capex* ... de 2026 para cerca de **US$ 20 bi**, de mais de US$ 25 bi ([CNBC](...))"
   - Sugerido: "... para cerca de **US$ 20 bi**, de mais de US$ 25 bi, segundo analistas citados pela CNBC" (ou trocar pelo link da apresentação de resultados da Tesla).

## Correções recomendadas (não bloqueiam o envio)

- "cautela **de sempre** às vésperas do segundo turno" -> "a cautela às vésperas do segundo turno" (a fonte não diz que é recorrente).
- Frase 18: "sete petroleiros em chamas" -> "sete petroleiros que teriam pegado fogo ou sido danificados" (o Valor diz "ou").
- Frase 34: "as passagens ficaram mais de 20% mais caras em um ano" -> "as passagens nos EUA ficaram ..."
- Frase 10: "com os primeiros balanços de tecnologia" -> "com o início da temporada de balanços, puxado pela tecnologia".
- Frase 24: pôr o link do Money Times na frase dos números da Ásia, não só na seguinte.
- Frase 25: o texto do Money Times é da Estadão Conteúdo; opcional creditar assim.
- Frase 35: o 0,43% é o dólar à vista; o futuro (+0,57%) aparece três linhas acima. Escrever "à vista" evita estranhamento.
- Assunto "a ia pisou no freio" e título "IA com o pé no freio": as fontes falam em **dúvida dos investidores** sobre o retorno do gasto em IA. A própria Tesla atribui o corte de capex a eficiência e aumentou o opex, e a Meta, no mesmo dia, criou ações sem voto para financiar a "corrida da IA" (Exame, InfoMoney). Sugestão: "a dúvida sobre a IA derrubou a Ásia".
- Horário do leilão (44): se o edital do Tesouro Nacional trouxer um horário só, usar esse.
- Tamanho da história do dia (277 palavras com título e TL;DR): se for contar tudo, passa de 250; cortar uma frase.
