# Manual do caderno Economia

O caderno Economia é a newsletter de economia da Inteligência Pragmática. A rotina **pesquisa todo dia** de madrugada e guarda o que vale na curadoria. A edição sai **segunda, quarta e sexta**, e num outro dia só quando há notícia muito importante (seção 2). Quando sai, chega às 06:00, junto com as outras.

Vale tudo o que está no `manual/MANUAL_DE_REDACAO.md`: a voz (seção 2), números com escala e a cadeia `»` (seção 9), política (seção 12), radar e não repetição (seção 13), o rigor (seção 14) e as convenções de formato (seção 15). Este arquivo diz só o que muda.

## 1. A missão em uma frase
Em **4 a 6 minutos de leitura**, o leitor entende **uma** coisa importante da economia a fundo (o explicador) e fica sabendo:
- o que mudou desde a última edição no Brasil, nas empresas e nos preços, e no mundo;
- o que isso faz com o bolso dele.

**O que o caderno não é:**
- **Não é o Mercado.** Nada de "o Ibovespa subiu 0,8% ontem", cotação do dia ou agenda do pregão. Bolsa e dólar só entram como **consequência** de um fato econômico, nunca como a notícia em si.
- **Não é a geral.** O "Economia em 3 linhas" da geral já deu o fato. Aqui entram o porquê, o mecanismo e a escala. Um assunto que a geral ou o Mercado já deram só entra com valor novo: a fonte primária, o mecanismo, um número que eles não trouxeram, o efeito no bolso. Senão, fica de fora.

## 2. Quando a edição sai (e a curadoria de todo dia)
A regra é do leitor (22/10/2026): a pesquisa é diária, o envio não. Há dias fixos, para o caderno não ficar muito tempo sem sair, e o que não é muito importante espera guardado.

1. **Dia fixo: segunda, quarta e sexta.** A edição sai sempre, com o que ficou na curadoria desde a última edição mais o que chegou hoje. Semana fraca dá edição curta, mas sai.
2. **Fora do dia fixo, só a edição urgente.** Ela sai quando há uma notícia que o leitor perderia se só soubesse dela no próximo dia fixo:
   - decisão do Copom, ou ata que muda o rumo dos juros; decisão do Fed;
   - IPCA, PIB, desemprego ou contas públicas com surpresa: muito longe do esperado, recorde ou virada de tendência;
   - medida do governo ou lei aprovada que mexe logo com o bolso (imposto, IR, salário mínimo, crédito, combustível, conta de luz, FGTS, INSS);
   - choque lá fora com efeito aqui: tarifa, guerra comercial, petróleo disparando, crise bancária.

   A edição urgente traz só esse fato: o bom dia, o painel, o explicador e o bolso. O resto continua na curadoria para o próximo dia fixo. **Na dúvida, guarde.**
3. **Nos outros dias, a curadoria.** A rotina guarda em `dados/economia/curadoria.md` o que vale para a próxima edição e publica só esse arquivo, com o `guardar`.

**Como é a curadoria:**
- Uma seção `## AAAA-MM-DD` por dia, com de 0 a 8 linhas no formato `- [tema] Título factual — por que importa (url)`. O tema é um dos da seção 6.
- Entra o que valeria uma linha numa edição: fato com número e fonte, não boato. Prefira o link da fonte primária.
- Tire o que ficou velho ou foi superado (um dado que saiu de novo, uma previsão revista) e o que a geral ou o Mercado já deram sem deixar valor novo.
- No dia da edição, o que entrou sai da curadoria. O que sobrar continua lá.

No máximo uma edição por dia. A primeira linha do `pauta.md` diz o motivo: `Motivo: dia fixo` ou `Motivo: urgente (...)`.

## 3. O tom
- **Professor bom de conversa:** explica com clareza, usa exemplo do cotidiano e tem humor seco quando cabe. Nada de economês.
- **Todo termo técnico ganha meia frase de explicação** na primeira vez em que aparece: juro real, resultado primário, núcleo da inflação, expectativa desancorada, IPCA-15, PTAX, curva de juros, prêmio de risco, *carry trade*, arcabouço fiscal.
- **Política só entra quando mexe com a economia** (manual geral, seção 12). A eleição aparece só pelo efeito econômico ("o mercado cobra prêmio de risco antes do segundo turno"), sem pesquisa e sem candidato como protagonista. Para medida de governo, use Quem defende diz / Quem critica diz, com números.
- **Nunca recomende investimento nem produto financeiro.** Explicar o efeito é permitido; dizer o que fazer com o dinheiro, não.
  - Pode: "com a Selic a 13,75%, um CDB que paga 100% do CDI rende mais que a poupança" (é conta, com fonte).
  - Não pode: "troque a poupança pelo CDB" ou "é hora de travar o juro".
  - O rodapé de toda edição diz: "Não é recomendação de investimento."

## 4. Os números
- **O painel não é escrito por você.** Ele sai do `python main.py economia-painel DATA`, direto das APIs do Banco Central e do IBGE, e entra no lugar do marcador `<!-- painel -->`. Nunca copie, arredonde ou "corrija" os números do painel no texto.
- No texto, cite um número do painel **com a mesma grafia** dele, ou com link para a fonte do número.
- O 🆕 do painel marca o dado que saiu desde a última edição. É candidato natural a explicador ou a uma linha de BRASIL.
- **Escala sempre** (manual geral, seção 9). As réguas que mais servem aqui:
  - contra o esperado (Focus, consenso de analistas, com a fonte);
  - contra a meta (inflação) ou contra a regra (arcabouço fiscal);
  - contra a série ("o menor desde 2012", com a fonte);
  - em reais por pessoa ou por mês ("R$ 300 a mais por ano numa conta de luz de R$ 200").
- **Real ou nominal:** diga se o número já desconta a inflação ("já descontada a inflação" ou "sem descontar a inflação").
- **Por cento ou ponto percentual:** a Selic que vai de 13,75% para 13,25% caiu **0,5 ponto percentual**, e não 0,5%.
- **Diga a comparação:** "sobre o trimestre anterior", "sobre um ano antes", "em 12 meses".
- **Projeção não é fato.** "A projeção do Itaú é de PIB de 1,8%" leva a fonte e o nome de quem projeta.
- **Links do IBGE:** o site do IBGE (agência de notícias, SIDRA e páginas de pesquisa) dá 403 a robôs, mas abre normalmente para o leitor. Use o link do release na agência de notícias (o `oficiais.md` traz os links). O checador confere o número no `oficiais.md` ou direto nas APIs (`servicodados.ibge.gov.br`, `apisidra.ibge.gov.br`).

## 5. A estrutura da edição
1. **bom dia.** Uma ou duas frases com o tema da edição. Pode ter graça.
2. **Painel** (`<!-- painel -->`, sozinho numa linha). O código preenche.
3. **#### O EXPLICADOR**: `## Título-gancho`, `> **TL;DR:**` e de 400 a 600 palavras.
   - O tema é o assunto mais importante desde a última edição, ou o conceito que o leitor precisa para entender o momento ("por que a inflação de serviços não cede", "o que é o arcabouço fiscal e por que ele aperta agora").
   - O lead traz o fato, o número em negrito e o link da fonte primária.
   - Depois vem o **mecanismo**: como a coisa funciona, de preferência com a cadeia `»` da edição ("petróleo caro » diesel caro » frete caro » comida cara").
   - Os números, cada um com escala.
   - Os dois lados: **Os otimistas:** / **Os pessimistas:**, ou **Quem defende diz:** / **Quem critica diz:**.
   - Fecha com **O que observar:** o próximo dado ou a próxima decisão, com a data.
4. **#### BRASIL**: de 2 a 4 linhas `→`, cada uma com um rótulo em negrito: `→ **Juros**: ...`, `→ **Inflação**: ...`, `→ **Contas públicas**: ...`, `→ **Câmbio**: ...`, `→ **Emprego**: ...`, `→ **Atividade**: ...`.
5. **#### EMPRESAS E PREÇOS**: de 2 a 4 linhas `→`. Balanço que diz algo sobre a economia, setor que acelera ou trava, preço que mexe com o consumidor (comida, combustível, aluguel, energia, passagem, remédio).
6. **#### MUNDO**: de 2 a 4 linhas `→` (EUA, China, Europa, emergentes). Quando o fato bate aqui, diga como: "...; na prática, ...".
7. **#### O QUE MUDA NO BOLSO**: de 2 a 4 linhas `→`, obrigatória. O efeito concreto do que a edição contou: financiamento, cartão e crédito, poupança e renda fixa (explicar, nunca recomendar), aluguel (IGP-M), salário e salário mínimo, imposto, conta de luz, preço na prateleira. Cada linha com número e fonte. Nada de conselho genérico ("planeje seu orçamento").
8. **#### NA AGENDA** (opcional): de 2 a 4 linhas `→` com o que sai nos próximos 7 dias e importa (o `oficiais.md` traz o calendário do IBGE e a próxima decisão do Copom). Cada linha com o dia, o horário de Brasília e o link.
9. **Fecho:** "Até a próxima." numa linha, e o rodapé "Não é recomendação de investimento."

Alvo: **de 900 a 1.400 palavras**, fora o painel. A **edição urgente** é curta (de 500 a 800 palavras): bom dia, painel, o explicador do fato e o bolso.

## 6. O front matter
Igual ao da geral (manual, seção 15), com estas diferenças:
- `tipo`: `edicao` (dia fixo) ou `urgente` (fora do dia fixo, por notícia muito importante);
- `tema` das histórias: `juros | inflacao | fiscal | cambio | emprego | crescimento | empresas | setores | precos | consumo | mundo`;
- `formatos`: `[painel, explicador, brasil, empresas_precos, mundo, no_bolso, agenda]`, só os usados;
- `breakthrough`: sempre `false`.

O explicador é a primeira história, com um `id` estável. Quando o tema voltar (a Selic, o arcabouço, a guerra tarifária), use o mesmo `id` e diga "o que mudou desde [data]".

## 7. Checklist
- [ ] A primeira linha do `pauta.md` diz o motivo (dia fixo ou urgente), e o que entrou saiu da curadoria.
- [ ] O marcador `<!-- painel -->` está sozinho numa linha, logo depois do "bom dia".
- [ ] Nenhum número do painel foi reescrito à mão.
- [ ] Nada repete a geral ou o Mercado sem valor novo; nada de cotação do dia como notícia.
- [ ] Todo termo técnico ganhou explicação na primeira vez.
- [ ] Todo número tem escala e diz a comparação (real ou nominal, % ou p.p., contra o quê).
- [ ] O explicador tem o mecanismo, os dois lados e "O que observar".
- [ ] "O que muda no bolso" tem de 2 a 4 linhas concretas, com número e fonte.
- [ ] Nenhuma frase soa como recomendação de investimento.
- [ ] A eleição só aparece como efeito econômico, sem pesquisa.
- [ ] Toda afirmação tem link.
- [ ] O rodapé diz "Não é recomendação de investimento."
