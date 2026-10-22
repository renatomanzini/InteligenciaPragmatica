# Manual do caderno Mercado

O caderno Mercado é a newsletter de mercado financeiro e de economia da Inteligência Pragmática. Sai **de segunda a sexta, por volta das 07:00**, antes da abertura da bolsa. Nas **segundas, quartas e sextas**, a edição ganha o bloco **ECONOMIA** (seção 9), que era o caderno Economia até 22/10/2026. Quando acontece algo grande no pregão, sai também uma **edição extra** no fim do dia.

Vale tudo o que está no `manual/MANUAL_DE_REDACAO.md`: a voz, o rigor (seção 14), números com escala (seção 9), radar e não repetição (seção 13) e as convenções de formato (seção 15). Este arquivo diz só o que muda.

## 1. A missão em uma frase
Em **3 a 4 minutos de leitura** (**5 a 6** nos dias do bloco ECONOMIA), o leitor chega ao café sabendo:
- como a bolsa e o dólar fecharam;
- o que mexe no mercado hoje;
- o que isso faz com o bolso dele;
- nas segundas, quartas e sextas, uma coisa importante da economia entendida a fundo e o que mudou no Brasil, nas empresas e no mundo.

## 2. O tom
- **Leve, animado e bem-humorado**, no espírito dos comunicadores que explicam mercado com alegria (a referência do leitor é o Pablo Spyer, do "Vai, tourinho!").
- **Imite o jeito, nunca o bordão nem a persona.** Nada de "tourinho" e nada de "vai, tourinho". Também nada de anedota em 1ª pessoa.
- Dá para brincar com touro (alta) e urso (baixa), com "pregão de ressaca", com "o dólar acordou de mau humor". Use uma metáfora por seção, no máximo.
- **Clareza primeiro.** O leitor estuda Direito e não é do mercado. Todo termo técnico (DI, *yield*, *spread*, VIX, *guidance*) ganha uma explicação de meia frase na primeira vez em que aparece.
- **Nunca recomende investimento.** Nada de "compre", "venda", "vale a pena entrar", "preço-alvo" ou "carteira recomendada". Quando a notícia for uma recomendação de banco, conte que é a recomendação *do banco*, com a fonte. O rodapé de toda edição diz: "Não é recomendação de investimento."

## 3. Os números
- **Os painéis não são escritos por você.** O de cotações é gerado pelo `python main.py mercado-painel` direto das fontes de dados (B3, CNBC, AwesomeAPI, CNN, alternative.me) e entra no lugar do marcador `<!-- painel -->`. O painel oficial do bloco ECONOMIA vem do `python main.py economia-painel DATA --caderno mercado`, direto das APIs do Banco Central e do IBGE, e entra no lugar de `<!-- painel-economia -->`. Nunca copie, arredonde ou "corrija" os números de nenhum dos dois no texto.
- No texto, cite número de cotação **só se estiver no painel** (e com a mesma grafia) ou **com link** para a fonte do número.
- Variação sempre com sinal e base: "o Ibovespa caiu 0,86% ontem", nunca "o Ibovespa caiu bastante".
- Escala: diga se o movimento é grande ("a maior queda desde abril", com fonte) ou normal ("um dia comum").

## 4. Política e eleição
- Corrida eleitoral não entra (`preferencias.md`): nada de pesquisa de intenção de voto como notícia.
- Mas o **efeito da eleição no preço** entra: "a bolsa caiu com a cautela antes do segundo turno". Diga o movimento e a explicação do mercado, com fonte, **sem** dizer quem está na frente nem os números das pesquisas.
- No bloco ECONOMIA, política só entra quando mexe com a economia (a seção 12 do manual geral), e a eleição só pelo efeito econômico ("o mercado cobra prêmio de risco antes do segundo turno"), sem pesquisa e sem candidato como protagonista. Para medida de governo, use Quem defende diz / Quem critica diz, com números.

## 5. A estrutura da edição da manhã (dias úteis)
1. **bom dia.** Uma ou duas frases com o humor do mercado (subiu, caiu, de lado) e o tema do dia. Pode ter graça. Nos dias do bloco ECONOMIA, pode citar também o tema do explicador.
2. **Painel** (`<!-- painel -->`, sozinho numa linha). O código preenche.
3. **#### O QUE MEXEU ONTEM**: 2 ou 3 linhas `→` explicando o porquê dos movimentos do painel, uma no Brasil e uma ou duas nos EUA. Cada uma com fonte.
4. **#### A HISTÓRIA DO DIA**: a notícia de mercado mais importante, com `## Título-gancho`, `> **TL;DR:**`, de 150 a 250 palavras e **"E no seu bolso?"** no fim (o efeito prático: juros do financiamento, preço da viagem, rendimento da poupança e do CDB, preço da gasolina...). Pode ser balanço de empresa, decisão de juros, IPO, fusão ou regra nova da CVM.
5. **#### ECONOMIA** (só segunda, quarta e sexta): o painel oficial, três blocos de linhas `→` e um explicador. A estrutura completa está na seção 9. Nos outros dias, esta parte não existe.
6. **#### AGENDA DE HOJE**: de 2 a 5 linhas `→` com o que sai hoje e importa: indicadores (IPCA, payroll, PIB), decisões de juros (Copom, Fed), balanços relevantes e vencimentos. Cada linha com horário de Brasília quando a fonte der e com link para a agenda. Se não houver nada relevante, escreva "Agenda fraca hoje." numa linha só.
7. **#### RADAR**: de 2 a 4 linhas `→` com o resto que importa (empresas, cripto, câmbio lá fora, commodities). Uma frase cada, com fonte.
8. **#### PARA ENTENDER** (opcional, no máximo 3 vezes por semana, e **nunca** nos dias do bloco ECONOMIA, porque o explicador já faz esse papel): um conceito em até 80 palavras, com um exemplo do dia ("o que é o VIX", "por que dólar alto encarece o pão").
9. **Rodapé:** "Não é recomendação de investimento."

Alvo: **de 450 a 750 palavras** fora os painéis. Nos dias do bloco ECONOMIA, **de 1.000 a 1.400 palavras**. Dia fraco é edição curta, sem encher linguiça.

## 6. A edição extra (o 🚨 do Mercado)
Sai **só** quando há um gatilho. O `python main.py mercado-alarme` confere os gatilhos de preço:
- Ibovespa, S&P 500 ou Dow Jones variando 3% ou mais no dia;
- Nasdaq variando 4% ou mais;
- dólar variando 2,5% ou mais;
- bitcoin variando 10% ou mais;
- Brent variando 8% ou mais;
- VIX em 35 ou mais;
- Medo & Ganância das ações em 10 ou menos, ou em 90 ou mais.

Também conta como gatilho um **evento**, mesmo sem número extremo, quando é grande o bastante para o leitor querer saber no mesmo dia:
- decisão de juros fora do esperado (Copom ou Fed);
- circuit breaker na B3;
- quebra, intervenção ou recuperação judicial de empresa grande;
- intervenção do Banco Central no câmbio;
- fusão ou aquisição acima de US$ 10 bilhões envolvendo empresa brasileira;
- mudança de regra que mexe com o investidor comum (IR sobre investimentos, poupança, FGC).

**Na dúvida, não sai.** A edição extra é rara; edição extra toda semana vira ruído. Desde que a Economia virou bloco, não existe mais edição urgente de economia: o que não passa por um destes gatilhos espera o próximo bloco ECONOMIA.

Formato da extra: assunto começando com "🚨", painel atualizado, `## Título`, `> **TL;DR:**`, de 200 a 400 palavras com:
- o que aconteceu;
- por que aconteceu;
- o que muda no bolso;
- o que observar amanhã.

O front matter leva `breakthrough: true`, `tipo: extra` e a justificativa em `motivo_extra`. A extra não leva o bloco ECONOMIA.

## 7. O front matter
Igual ao da geral (manual, seção 15), com estas diferenças:
- `tipo`: `dia_util` ou `extra`;
- `tema` das histórias: `bolsa_br | bolsa_eua | moedas | juros | cripto | empresas | macro`; no bloco ECONOMIA, também `inflacao | fiscal | cambio | emprego | crescimento | setores | precos | consumo | mundo`;
- `formatos`: `[painel, o_que_mexeu, historia_do_dia, agenda, radar, para_entender]`, só os usados; nos dias do bloco, acrescente `economia` e `explicador`.

O explicador é uma história com `id` estável, no `historias` do front matter. Quando o tema voltar (a Selic, o arcabouço, a guerra tarifária), use o mesmo `id` e diga "o que mudou desde [data]".

## 8. Checklist
- [ ] O marcador `<!-- painel -->` está sozinho numa linha, logo depois do "bom dia".
- [ ] Nenhum número do painel foi reescrito à mão.
- [ ] Todo termo técnico ganhou explicação na primeira vez.
- [ ] Nenhuma frase soa como recomendação de compra ou venda.
- [ ] A eleição só aparece como efeito no preço, sem pesquisa.
- [ ] "E no seu bolso?" está na história do dia.
- [ ] Toda afirmação tem link.
- [ ] O rodapé diz "Não é recomendação de investimento."

Nos dias do bloco ECONOMIA, confira também (seção 9):
- [ ] O `<!-- painel-economia -->` está sozinho numa linha, logo depois de `#### ECONOMIA`, e nenhum número dele foi reescrito à mão.
- [ ] Nada do bloco repete o Mercado (cotação do dia como notícia) nem a geral sem valor novo.
- [ ] Todo número do bloco tem escala e diz a comparação (real ou nominal, % ou p.p., contra o quê).
- [ ] O explicador tem o mecanismo, os dois lados, "O que observar" e "No bolso", com número e fonte.
- [ ] Não há "PARA ENTENDER" na edição.

## 9. O bloco ECONOMIA (segunda, quarta e sexta)
O leitor decidiu em 22/10/2026 que a economia deixaria de ser um caderno e viraria um bloco do Mercado. O caderno Economia (`manual/MANUAL_ECONOMIA.md`) está encerrado; esta seção guarda o essencial dele.

**Quando:** só nas segundas, quartas e sextas, os mesmos dias fixos que o caderno tinha. Nos outros dias, nada de economia fora do que o Mercado já cobre. Não há mais edição urgente de economia (veja a seção 6).

**O que o bloco é.** Em cerca de 2 minutos a mais de leitura, o leitor entende **uma** coisa importante da economia a fundo (o explicador) e fica sabendo:
- o que mudou desde o último bloco no Brasil (macro), nas empresas e nos preços (micro) e no mundo;
- o que isso faz com o bolso dele.

**O que o bloco não é:**
- **Não é o resto do Mercado.** Nada de "o Ibovespa subiu 0,8% ontem", cotação do dia ou agenda do pregão: isso é do painel, do "O QUE MEXEU ONTEM" e da "AGENDA DE HOJE". Bolsa e dólar só entram no bloco como **consequência** de um fato econômico.
- **Não é a geral.** O "Economia em 3 linhas" da geral já deu o fato. Aqui entram o porquê, o mecanismo e a escala. Um assunto que a geral já deu, ou que o Mercado deu hoje, só entra com valor novo: a fonte primária, o mecanismo, um número que eles não trouxeram, o efeito no bolso. Senão, fica de fora.

### A estrutura do bloco
Vem logo depois de "A HISTÓRIA DO DIA" e antes da "AGENDA DE HOJE":
1. **`#### ECONOMIA`** e, na linha de baixo, o marcador **`<!-- painel-economia -->`**, sozinho numa linha. O código preenche com os números oficiais do Banco Central e do IBGE (Selic, IPCA, PIB, desemprego, dívida, resultado primário e as apostas do Focus). O 🆕 marca o dado que saiu desde o último bloco: é candidato natural a explicador ou a uma linha de Brasil. O dólar fica de fora, porque o painel de cotações já traz o dele.
2. **`### Brasil`** (macro): de 2 a 4 linhas `→`, cada uma com rótulo em negrito: `→ **Juros**: ...`, `→ **Inflação**: ...`, `→ **Contas públicas**: ...`, `→ **Câmbio**: ...`, `→ **Emprego**: ...`, `→ **Atividade**: ...`.
3. **`### Empresas, setores e preços`** (micro): de 2 a 4 linhas `→`. Balanço que diz algo sobre a economia, setor que acelera ou trava, preço que mexe com o consumidor (comida, combustível, aluguel, energia, passagem, remédio).
4. **`### Mundo`** (cenário global): de 2 a 3 linhas `→` (EUA, China, Europa, emergentes). Quando o fato bate aqui, diga como: "...; na prática, ...".
5. **`### O explicador: Título-gancho`**: de 200 a 300 palavras, sem `##` nem TL;DR.
   - O tema é o assunto mais importante desde o último bloco, ou o conceito que o leitor precisa para entender o momento ("por que a inflação de serviços não cede", "o que é o arcabouço fiscal e por que ele aperta agora").
   - O lead traz o fato, o número em negrito e o link da fonte primária.
   - Depois vem o **mecanismo**: como a coisa funciona, de preferência com a cadeia `»` ("petróleo caro » diesel caro » frete caro » comida cara").
   - Os números, cada um com escala, e os dois lados: **Os otimistas:** / **Os pessimistas:**, ou **Quem defende diz:** / **Quem critica diz:**.
   - Fecha com **O que observar:** (o próximo dado ou a próxima decisão, com a data) e **No bolso:** (de 1 a 2 linhas com o efeito concreto: financiamento, cartão e crédito, poupança e renda fixa explicados e nunca recomendados, aluguel, salário, imposto, conta de luz, preço na prateleira; cada linha com número e fonte; nada de conselho genérico).

Alvo do bloco: **de 450 a 700 palavras**, fora o painel. Semana fraca dá bloco curto (sem a linha de empresas, por exemplo), mas o explicador e o "No bolso" ficam sempre.

### Os números do bloco
- Cite um número do painel oficial **com a mesma grafia** dele, ou com link para a fonte do número.
- **Escala sempre** (manual geral, seção 9). As réguas que mais servem aqui:
  - contra o esperado (Focus, consenso de analistas, com a fonte);
  - contra a meta (inflação) ou contra a regra (arcabouço fiscal);
  - contra a série ("o menor desde 2012", com a fonte);
  - em reais por pessoa ou por mês ("R$ 300 a mais por ano numa conta de luz de R$ 200").
- **Real ou nominal:** diga se o número já desconta a inflação ("já descontada a inflação" ou "sem descontar a inflação").
- **Por cento ou ponto percentual:** a Selic que vai de 13,75% para 13,25% caiu **0,5 ponto percentual**, e não 0,5%.
- **Diga a comparação:** "sobre o trimestre anterior", "sobre um ano antes", "em 12 meses".
- **Projeção não é fato.** "A projeção do Itaú é de PIB de 1,8%" leva a fonte e o nome de quem projeta.
- **Todo termo técnico ganha meia frase de explicação** na primeira vez: juro real, resultado primário, núcleo da inflação, expectativa desancorada, IPCA-15, PTAX, curva de juros, prêmio de risco, *carry trade*, arcabouço fiscal.

### As fontes do bloco
- Prefira a fonte primária: nota do BC, ata e comunicado do Copom, release do IBGE (no `oficiais.md`), Tesouro, Fazenda, Fed, BCE, FMI. Abra de 8 a 14 páginas no máximo.
- **IBGE:** o site do IBGE (agência de notícias, SIDRA e páginas de pesquisa) dá 403 a robôs, mas abre normalmente para o leitor. Use o link do release na agência de notícias (o `oficiais.md` traz os links). O checador confere o número no `oficiais.md` ou direto nas APIs (`servicodados.ibge.gov.br`, `apisidra.ibge.gov.br`).
- FT, Bloomberg e WSJ têm paywall: use para achar pauta e só cite com outra fonte aberta que confirme.
- Não tire número novo de base de dados para o texto: o painel já traz os oficiais. Fora dele, use os números que a fonte traz.
- O `oficiais.md` (em `edicoes/mercado/DATA/`) traz os dados do painel que saíram desde o último bloco, os releases do IBGE do período e a agenda dos próximos 8 dias, com a próxima decisão do Copom. Serve para achar pauta e alimentar a "AGENDA DE HOJE" com os indicadores da semana.
