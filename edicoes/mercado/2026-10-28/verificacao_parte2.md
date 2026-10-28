# Verificação, parte 2 (explicador, agenda, radar) - edição 2026-10-28

Fontes abertas por curl. Painéis conferidos em `painel.md` e `painel_economia.md`. Selic conferida na série 432 do BC (API).

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| Antes da eleição, a maioria das apostas era de corte de 0,25 p.p. em 04/11 | Valor Investe (76% de corte até sexta, 23) | OK | - |
| Na terça (27) a probabilidade de corte caiu para 28% | Valor Investe | OK | - |
| Manter a 13,75% saltou de 17,5% para 62% | Valor Investe | OK | - |
| Pausa interrompe cortes de 0,25 p.p. a cada Copom desde março | Valor Investe; série 432 do BC (19/03 14,75; 30/04 14,50; 18/06 14,25; 06/08 14,00; 17/09 13,75) | OK | - |
| IPCA 4,58% em 12 meses, acima do teto de 4,5% | painel_economia.md | OK (mesma grafia) | - |
| Cadeia "dúvida fiscal » prêmio de risco » juros futuros e dólar sobem » inflação demora a cair » BC com menos espaço" | Valor Investe (Sueishi: dívida, dólar, juros futuros; dólar alto pressiona preços) | Parcial: a cadeia é inferência do redator, sem atribuição, e "juros futuros" não é explicado | Atribuir (ver correção 1) e explicar "juros futuros" |
| "Lá fora, juro americano alto e petróleo caro empurram na mesma direção" | Valor Investe (Rosário: inflação alta nos EUA dificulta queda dos juros americanos; petróleo pressionado) | Parcial: a fonte fala de inflação alta nos EUA, não de "juro alto", e é opinião de Rosário | Atribuir a Rosário (correção 2) |
| Sueishi (Manchester): custo de esperar uma reunião é baixo; cortar com expectativas piorando pode arranhar a credibilidade | Valor Investe | OK | - |
| Durigan: segunda foi "troca de posição" de quem apostava em outro candidato | g1 | OK | - |
| "...e não uma mudança de fundamento" atribuído a Durigan | g1 | NÃO CONFERE: o g1 não traz essa frase nem esse sentido; a fonte (Sueishi) diz que também há preocupação com a dívida | Cortar o trecho (correção 3) |
| Copom na quarta, 04/11 | painel_economia.md, oficiais.md; 04/11/2026 é quarta | OK | - |
| "O nome do ministro da Fazenda" e "projeto da meta fiscal" como o que observar | Valor Investe / g1 | OK | - |
| No bolso: "CDB e poupança seguem rendendo o que rendem hoje, e o crédito não barateia tão cedo" | Valor Investe diz que a interrupção "manterá os juros elevados por mais tempo, encarecendo o crédito" | Parcial: previsão sem atribuição, sem número e sem fonte, e o manual exige número e fonte em cada linha do No bolso | Reescrever (correção 4) |
| Focus de 23/10 previa Selic de 13,25% no fim do ano | painel_economia.md | OK (mesma grafia); "Focus" não é explicado | Explicar na 1ª vez (correção 4) |
| Explicador: tamanho (200 a 300 palavras) | contagem | ~316 palavras com o título | Deixar como está ou cortar 1 frase (a correção 2 já enxuga) |
| Fed decide hoje e deve manter 3,75% a 4,00% | InfoMoney (reunião de quarta, 28) | OK | - |
| Agenda: horário da decisão do Fed | pauta.md diz 15h; InfoMoney não traz horário | Sem horário na linha (manual pede horário quando a fonte der) | Opcional, ver correção 6 |
| Santander: balanço do 3º tri antes da abertura | InfoMoney | OK | - |
| Goldman projeta lucro recorrente de cerca de R$ 4 bi, perto de 14% acima de um ano antes | InfoMoney ("lucro líquido recorrente", "avanço anual próximo de 14%") | OK; "recorrente" não é explicado | Opcional, ver correção 7 |
| SK Hynix: lucro operacional mais de 7 vezes sobre um ano antes, US$ 63 bi no 3º tri | Valor (83,3 trilhões de wons, US$ 63 bi) | OK | - |
| B3: a partir de terça, 3/11, o pregão abre às 10h e fecha às 17h55, com o fim do horário de verão nos EUA | InvestNews (3/11 é terça; horário de verão dos EUA termina em 1/11; 2/11 é Finados) | OK | - |
| Bitcoin US$ 81.082; medo e ganância das criptos de 48 para 51, neutro | painel.md | OK (mesma grafia) | - |

## Outras checagens
- Opinião sem selo: o explicador usa "Quem defende a pausa diz / Quem minimiza o susto diz", com nome e fonte. As únicas inferências soltas são a cadeia do mecanismo e a linha do No bolso (correções 1, 2 e 4).
- Recomendação de investimento: nenhuma. A frase sobre CDB e poupança descreve efeito, não diz o que fazer.
- Pesquisa eleitoral: não há. A eleição aparece só como efeito no preço.
- Real ou nominal, p.p. ou %: o corte de "0,25 ponto percentual" está correto.
- Repetição: o tema (aposta na Selic) não está na geral de hoje nem na história do dia. O Mercado só cita o explicador no "bom dia". Sem problema.
- Dias da semana: 27/10 terça, 28/10 quarta, 04/11 quarta, 03/11 terça, 23/10 sexta. Todos corretos.
- Agenda: a edição traz 2 linhas (mínimo do manual). O `oficiais.md` e o `pauta.md` não trazem outro indicador para hoje.

## Correções obrigatórias

1. Atribuir a cadeia do mecanismo e explicar "juros futuros".
   Trocar: `O mecanismo é a dúvida fiscal virando preço: medo com a dívida pública » investidor cobra mais para emprestar ao governo (o prêmio de risco) » juros futuros e dólar sobem » importado fica mais caro » inflação demora a cair » o BC tem menos espaço para cortar.`
   Por: `O mecanismo, como o Valor Investe descreve a visão dos analistas, é a dúvida fiscal virando preço: medo com a dívida pública » investidor cobra mais para emprestar ao governo (o prêmio de risco) » juros futuros (as taxas que o mercado cobra hoje para contratos de juros mais adiante) e dólar sobem » importado fica mais caro » inflação demora a cair » o BC tem menos espaço para cortar.`

2. Atribuir a frase sobre o cenário externo.
   Trocar: `Lá fora, juro americano alto e petróleo caro empurram na mesma direção ([Valor Investe](https://valorinveste.globo.com/mercados/moedas-e-juros/noticia/2026/10/27/mercado-muda-apostas-para-selic-apos-reeleicao-de-lula-e-agora-preve-pausa-nos-cortes.ghtml)).`
   Por: `Lá fora, para Rodrigo Rosário, da VLG Investimentos, a inflação ainda alta nos EUA dificulta a queda dos juros americanos e o petróleo pressionado pelo conflito no Oriente Médio ameaça alimentar a inflação ([Valor Investe](https://valorinveste.globo.com/mercados/moedas-e-juros/noticia/2026/10/27/mercado-muda-apostas-para-selic-apos-reeleicao-de-lula-e-agora-preve-pausa-nos-cortes.ghtml)).`

3. Tirar do Durigan o que ele não disse.
   Trocar: `o ministro Durigan afirma que a segunda-feira foi uma "troca de posição" de quem apostava em outro candidato, e não uma mudança de fundamento`
   Por: `o ministro Durigan afirma que a segunda-feira foi uma "troca de posição" de quem apostava em outro candidato, e que o mercado já voltava a ter "racionalidade" na terça`

4. Reescrever o No bolso, com atribuição, número e fonte, e explicar o Focus.
   Trocar: `**No bolso:** se a Selic parar em 13,75%, o CDB e a poupança seguem rendendo o que rendem hoje, e o crédito não barateia tão cedo. O Focus de 23/10, feito antes da eleição, previa Selic de 13,25% no fim do ano (painel acima): é essa queda que agora fica em dúvida.`
   Por: `**No bolso:** se a Selic parar em 13,75%, o juro do crédito (cartão, financiamento) deixa de ter a perspectiva de queda: o Valor Investe aponta que a interrupção dos cortes mantém os juros elevados por mais tempo e encarece o crédito ([Valor Investe](https://valorinveste.globo.com/mercados/moedas-e-juros/noticia/2026/10/27/mercado-muda-apostas-para-selic-apos-reeleicao-de-lula-e-agora-preve-pausa-nos-cortes.ghtml)). O Focus (a pesquisa semanal do BC com a previsão de bancos e consultorias) de 23/10, feito antes da eleição, previa Selic de 13,25% no fim do ano (painel acima): é essa queda de 0,5 ponto percentual que agora fica em dúvida.`

5. (Facultativa, tamanho) Com as trocas acima o explicador fica um pouco acima de 300 palavras. Se quiser enxugar, cortar de `Se a pausa vier, ela interrompe...` a frase `Se a pausa vier, ela interrompe uma sequência de cortes de 0,25 ponto a cada reunião do Copom desde março.` e deixar só `Se a pausa vier, será o fim de uma sequência de cortes de 0,25 ponto desde março.`

6. (Facultativa) Horário do Fed. A edição não tem fonte aberta para o horário (o pauta.md diz 15h, sem link). Se o redator confirmar em fonte aberta, trocar `decisão de juros dos EUA hoje;` por `decisão de juros dos EUA hoje, às 15h (Brasília);`. Sem confirmação, manter como está.

7. (Facultativa) Trocar `projeta lucro recorrente de cerca de` por `projeta lucro recorrente (sem itens que não se repetem) de cerca de`.
