# Manual do caderno IA

O caderno IA é a newsletter de inteligência artificial da Inteligência Pragmática. Sai **segunda e quinta, de manhã**, e vai mais fundo que a geral: breakthroughs, modelos novos e o que mudou de verdade, open source, ferramentas e agentes, regulação e o IA na prática.

Vale tudo o que está no `manual/MANUAL_DE_REDACAO.md`: a voz (seção 2), o critério de breakthrough (seção 3), o arco do IA na prática (seção 6), as linhas rápidas (seção 7), o assunto e a prévia (seção 8), números com escala (seção 9), as cotas de estilo (seção 10), o ângulo Direito & tech (seção 11), radar e não repetição (seção 13), o rigor (seção 14) e o formato do arquivo (seção 15). Este arquivo diz só o que muda.

## 1. A missão em uma frase
Em **6 a 9 minutos de leitura**, duas vezes por semana, o leitor entende **o que mudou de verdade em IA desde a última edição, o que é hype e o que ele pode fazer com isso**. Profundidade antes de volume: é melhor explicar bem três coisas que listar quinze.

## 2. A divisão com a geral
A geral sai todo dia e fala muito de IA. O caderno **não é uma segunda geral de IA**: ela dá o fato do dia, e o caderno dá o mecanismo, o teste e a consequência.
- **Antes da pauta, leia o que a geral publicou** desde a última edição do caderno (`python3 main.py historico --dias 5`, e a seção "Nos outros cadernos" do histórico do caderno).
- **Assunto que a geral já deu só entra com valor novo:** o que mudou desde então, o mecanismo que a geral não explicou, um teste, o lado jurídico, o "roda no seu Mac?", o "como vira serviço". Nesse caso, diga: "a geral contou na terça (20/10); aqui, o que isso muda". Nunca reconte a mesma notícia no mesmo formato.
- **O caderno fica com o que a geral costuma deixar de fora:** a ficha técnica dos modelos, o open source, as ferramentas de nicho, a China em detalhe e o andamento da regulação.
- **O IA na prática do caderno usa outro caso** que não o da geral nos últimos 7 dias.
- Itens marcados `JÁ COBERTO` nos candidatos já saíram em alguma newsletter da família: só entram com novidade.

## 3. O tom
- A voz da geral (seção 2 do manual geral): informal, precisa, frases curtas, humor seco. Pode ser **um pouco mais técnica**, mas o leitor continua sendo um estudante de Direito que constrói coisas com IA, não um engenheiro.
- **Todo jargão é explicado na primeira vez**, em meia frase: token, parâmetro, pesos abertos, quantização, janela de contexto, MoE, RAG, *fine-tuning*, agente, MCP, *benchmark*, inferência.
- **Antídoto contra o hype.** O caderno existe para separar o que muda a vida de uma pessoa comum do que só muda o placar de um *benchmark*. Quando a manchete promete mais do que a fonte entrega, diga isso com todas as letras.

## 4. Regras próprias de IA
**Modelos novos.**
- Número de *benchmark* informado pelo próprio laboratório leva "segundo o laboratório". Avaliação independente (LMArena, Artificial Analysis, Epoch AI, SWE-bench oficial) leva o nome de quem avaliou e a data.
- Não compare números de *benchmarks* medidos de jeitos diferentes. Na dúvida, compare com o modelo anterior do mesmo laboratório, na mesma tabela.
- Diga sempre **onde e para quem está disponível**: aberto a todos, pago, só nos EUA, fila de espera, só por API. Anúncio sem produto disponível não é lançamento.
- **Preço** por milhão de tokens com uma régua do mundo real ("ler um contrato de 30 páginas custa uns R$ 0,10"), quando a conta for simples e com os números à vista.
- **Pesos abertos** só com a licença: MIT e Apache 2.0 deixam usar comercialmente; licença própria tem restrições, e isso vale uma linha.

**Roda no seu Mac?** O leitor tem um MacBook M2 com 8 GB de memória. Quando o modelo for aberto e a fonte der o tamanho, diga se roda:
- regra de bolso, sempre como **estimativa**: em 4 bits, cada bilhão de parâmetros ocupa uns 0,6 GB, e o Mac de 8 GB deixa uns 5 GB livres para o modelo;
- **roda bem** até uns 4B; **apertado** de 7B a 8B (só com o resto fechado); **não roda** acima de uns 9B;
- em modelo MoE (vários especialistas, só alguns ativos por vez), o que pesa na memória é o total de parâmetros, não os ativos;
- se a fonte diz o contrário (um teste real num Mac de 8 GB), vale a fonte.

**Open source.**
- Estrelas e data só com `python3 main.py github dono/repo`, e com a data da consulta ("**12,3 mil** estrelas em 22/10").
- Diga o que o projeto faz em uma frase de leigo, a licença e se precisa de programação para usar.
- Repositório com muitas estrelas em pouco tempo não é prova de qualidade: procure quem testou (Hacker News, Simon Willison, uma issue com resultado).

**Agentes e ferramentas.** Diga o que o agente faz **sozinho** e o que precisa de aprovação, quanto custa e o que pode dar errado (dados, permissões, erro silencioso).

**Regulação.**
- Brasil: o PL 2338/2023 (marco da IA), a ANPD, decisões do STF, do TSE e de tribunais. Europa: o AI Act. EUA: leis estaduais e federais. China: as regras da CAC e do MOFCOM.
- Cite lei, artigo e fase da tramitação só com certeza e com o link do texto oficial (planalto.gov.br, camara.leg.br, senado.leg.br, eur-lex.europa.eu). Tramitação muda: escreva "segundo a Câmara, em 21/10".
- Use ⚖️ e o formato **Quem defende diz:** / **Quem critica diz:** quando houver polêmica.

**China.** Prefira a fonte primária (o repositório no GitHub ou no Hugging Face, o comunicado da empresa, o texto da norma). Imprensa chinesa estatal ou próxima do governo leva "segundo a imprensa estatal".

**Segurança.** Falha ou ataque com IA entra com o que fazer (atualizar, trocar senha, desligar algo), nunca com o passo a passo do ataque.

## 5. A estrutura da edição (segunda e quinta)
1. **bom dia.** Uma ou duas frases com o tema da edição. Pode ter graça.
2. **Nesta edição:** de 3 a 5 bullets que já vendem cada parte.
3. **#### O QUE MUDOU DE VERDADE**: a história mais importante do período, com a anatomia da seção 5 do manual geral (`## Título-gancho`, `> **TL;DR:**`, lead, contexto, números com escala, os dois lados, **Por que isso importa pra você**, 🔗). De **400 a 700 palavras**. Se passou no critério de breakthrough, leva 🚨 e a justificativa em uma linha. Em período morno, vira **raio-x** (um modelo ou ferramenta destrinchado), **explicador** ("o que é X e por que importa") ou **continuação** ("o que mudou desde [data]").
4. **#### MODELOS NOVOS**: de 1 a 3 modelos lançados no período, cada um com `### Nome do modelo (laboratório)` e uma ficha curta:
   - **O que é:** uma frase;
   - **O que mudou de verdade:** contra o modelo anterior, com número e fonte;
   - **Onde usar e quanto custa:** disponibilidade e preço;
   - **Roda no seu Mac?** (só modelo aberto): sim, apertado ou não, com o porquê;
   - **Veredito:** uma linha, com o selo **Opinião:** se for julgamento.
   Período sem lançamento relevante: a seção sai.
5. **#### OPEN SOURCE**: de 2 a 4 linhas `→` (repositório ou modelo aberto, o que faz, estrelas conferidas, licença). Uma delas pode virar um parágrafo, se for o achado da semana.
6. **#### FERRAMENTAS E AGENTES**: de 2 a 4 linhas `→` com o que mudou, para quem e quanto custa.
7. **#### ⚖️ REGULAÇÃO**: de 1 a 3 itens (linhas `→` ou um parágrafo curto), sempre com a fonte oficial quando houver. Período sem nada: a seção sai.
8. **#### 🧠 IA NA PRÁTICA**: o arco da seção 6 do manual geral, de **300 a 500 palavras**. O ⚠️ freio de realidade é obrigatório, o advogado aparece sempre que fizer sentido, e o **Como isso vira serviço** também. O **Para testar hoje** é bem-vindo aqui, desde que caiba num Mac de 8 GB ou numa conta gratuita.
9. **#### RADAR**: de 3 a 6 linhas `→` com o resto que importa: China, pesquisa, IA no Brasil, negócios de IA (rodada só se mudar o mercado, não rodada pequena).
10. **Pergunta de fechamento:** uma linha que faz o leitor pensar no próprio trabalho.
11. **Fecho** de uma linha: "Até quinta." (na segunda) ou "Até segunda." (na quinta).

Alvo: **de 1.300 a 2.000 palavras**. Período fraco é edição curta: só o bom dia, O QUE MUDOU DE VERDADE, IA NA PRÁTICA, a pergunta e o fecho já são uma edição. Seção nenhuma é preenchida para completar.

## 6. O front matter
Igual ao da geral (manual, seção 15), com estas diferenças:
- `tipo`: `segunda` ou `quinta`;
- `tema` das histórias: `modelos | open_source | ferramentas | agentes | pesquisa | regulacao | china | brasil | negocios_ia | seguranca`;
- `formatos`: `[o_que_mudou, modelos_novos, open_source, ferramentas, regulacao, ia_na_pratica, radar, pergunta]`, só os usados, mais `raio_x`, `explicador` ou `continuacao` quando for o caso;
- `breakthrough`: `true` só se a principal passou no critério.

## 7. Checklist
- [ ] Nada repete a geral dos últimos dias sem valor novo, e o que volta diz "a geral contou em [data]".
- [ ] Todo *benchmark* do laboratório diz "segundo o laboratório"; as avaliações independentes têm nome e data.
- [ ] Todo modelo novo diz onde está disponível e quanto custa; todo modelo aberto diz a licença.
- [ ] O "roda no seu Mac?" usa a regra de bolso como estimativa, ou um teste real com fonte.
- [ ] Toda contagem de estrelas foi conferida com `main.py github`, com a data.
- [ ] Lei, artigo e tramitação só com certeza e com o link oficial.
- [ ] O 🚨 só aparece se passou no critério, com a justificativa em uma linha.
- [ ] O ⚠️ freio de realidade e o "como vira serviço" estão no IA na prática.
- [ ] Todo jargão foi explicado na primeira vez.
- [ ] O radar (AI Drops, Neat Prompts, TechDrops) não aparece como fonte.
- [ ] O fecho aponta para a próxima edição certa.
