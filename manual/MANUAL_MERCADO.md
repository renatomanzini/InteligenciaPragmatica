# Manual do caderno Mercado

O caderno Mercado é a newsletter de mercado financeiro da Inteligência Pragmática. Sai **de segunda a sexta, por volta das 07:00**, antes da abertura da bolsa. Quando acontece algo grande no pregão, sai também uma **edição extra** no fim do dia.

Vale tudo o que está no `manual/MANUAL_DE_REDACAO.md`: a voz, o rigor (seção 14), números com escala (seção 9), radar e não repetição (seção 13) e as convenções de formato (seção 15). Este arquivo diz só o que muda.

## 1. A missão em uma frase
Em **3 a 4 minutos de leitura**, o leitor chega ao café sabendo:
- como a bolsa e o dólar fecharam;
- o que mexe no mercado hoje;
- o que isso faz com o bolso dele.

## 2. O tom
- **Leve, animado e bem-humorado**, no espírito dos comunicadores que explicam mercado com alegria (a referência do leitor é o Pablo Spyer, do "Vai, tourinho!").
- **Imite o jeito, nunca o bordão nem a persona.** Nada de "tourinho" e nada de "vai, tourinho". Também nada de anedota em 1ª pessoa.
- Dá para brincar com touro (alta) e urso (baixa), com "pregão de ressaca", com "o dólar acordou de mau humor". Use uma metáfora por seção, no máximo.
- **Clareza primeiro.** O leitor estuda Direito e não é do mercado. Todo termo técnico (DI, *yield*, *spread*, VIX, *guidance*) ganha uma explicação de meia frase na primeira vez em que aparece.
- **Nunca recomende investimento.** Nada de "compre", "venda", "vale a pena entrar", "preço-alvo" ou "carteira recomendada". Quando a notícia for uma recomendação de banco, conte que é a recomendação *do banco*, com a fonte. O rodapé de toda edição diz: "Não é recomendação de investimento."

## 3. Os números
- **O painel não é escrito por você.** Ele é gerado pelo `python main.py mercado-painel` direto das fontes de dados (B3, CNBC, AwesomeAPI, CNN, alternative.me) e entra no lugar do marcador `<!-- painel -->`. Nunca copie, arredonde ou "corrija" os números do painel no texto.
- No texto, cite número de cotação **só se estiver no painel** (e com a mesma grafia) ou **com link** para a fonte do número.
- Variação sempre com sinal e base: "o Ibovespa caiu 0,86% ontem", nunca "o Ibovespa caiu bastante".
- Escala: diga se o movimento é grande ("a maior queda desde abril", com fonte) ou normal ("um dia comum").

## 4. Política e eleição
- Corrida eleitoral não entra (`preferencias.md`): nada de pesquisa de intenção de voto como notícia.
- Mas o **efeito da eleição no preço** entra: "a bolsa caiu com a cautela antes do segundo turno". Diga o movimento e a explicação do mercado, com fonte, **sem** dizer quem está na frente nem os números das pesquisas.

## 5. A estrutura da edição da manhã (dias úteis)
1. **bom dia.** Uma ou duas frases com o humor do mercado (subiu, caiu, de lado) e o tema do dia. Pode ter graça.
2. **Painel** (`<!-- painel -->`, sozinho numa linha). O código preenche.
3. **#### O QUE MEXEU ONTEM**: 2 ou 3 linhas `→` explicando o porquê dos movimentos do painel, uma no Brasil e uma ou duas nos EUA. Cada uma com fonte.
4. **#### A HISTÓRIA DO DIA**: a notícia de mercado mais importante, com `## Título-gancho`, `> **TL;DR:**`, de 150 a 250 palavras e **"E no seu bolso?"** no fim (o efeito prático: juros do financiamento, preço da viagem, rendimento da poupança e do CDB, preço da gasolina...). Pode ser balanço de empresa, decisão de juros, IPO, fusão ou regra nova da CVM.
5. **#### AGENDA DE HOJE**: de 2 a 5 linhas `→` com o que sai hoje e importa: indicadores (IPCA, payroll, PIB), decisões de juros (Copom, Fed), balanços relevantes e vencimentos. Cada linha com horário de Brasília quando a fonte der e com link para a agenda. Se não houver nada relevante, escreva "Agenda fraca hoje." numa linha só.
6. **#### RADAR**: de 2 a 4 linhas `→` com o resto que importa (empresas, cripto, câmbio lá fora, commodities). Uma frase cada, com fonte.
7. **#### PARA ENTENDER** (opcional, no máximo 3 vezes por semana): um conceito em até 80 palavras, com um exemplo do dia ("o que é o VIX", "por que dólar alto encarece o pão").
8. **Rodapé:** "Não é recomendação de investimento."

Alvo: **de 450 a 750 palavras** fora o painel. Dia fraco é edição curta, sem encher linguiça.

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

**Na dúvida, não sai.** A edição extra é rara; edição extra toda semana vira ruído.

Formato da extra: assunto começando com "🚨", painel atualizado, `## Título`, `> **TL;DR:**`, de 200 a 400 palavras com:
- o que aconteceu;
- por que aconteceu;
- o que muda no bolso;
- o que observar amanhã.

O front matter leva `breakthrough: true`, `tipo: extra` e a justificativa em `motivo_extra`.

## 7. O front matter
Igual ao da geral (manual, seção 15), com estas diferenças:
- `tipo`: `dia_util` ou `extra`;
- `tema` das histórias: `bolsa_br | bolsa_eua | moedas | juros | cripto | empresas | macro`;
- `formatos`: `[painel, o_que_mexeu, historia_do_dia, agenda, radar, para_entender]`, só os usados.

## 8. Checklist
- [ ] O marcador `<!-- painel -->` está sozinho numa linha, logo depois do "bom dia".
- [ ] Nenhum número do painel foi reescrito à mão.
- [ ] Todo termo técnico ganhou explicação na primeira vez.
- [ ] Nenhuma frase soa como recomendação de compra ou venda.
- [ ] A eleição só aparece como efeito no preço, sem pesquisa.
- [ ] "E no seu bolso?" está na história do dia.
- [ ] Toda afirmação tem link.
- [ ] O rodapé diz "Não é recomendação de investimento."
