# Manual do caderno IA

O caderno IA é a newsletter de inteligência artificial da Inteligência Pragmática. Vai mais fundo que a geral: breakthroughs, modelos novos e o que mudou de verdade, open source, ferramentas e agentes, regulação e o IA na prática. A pesquisa é diária; a edição sai nos **dias fixos** e, fora deles, só quando há notícia muito importante (seção 2).

Vale tudo o que está no `manual/MANUAL_DE_REDACAO.md`: a voz (seção 2), o critério de breakthrough (seção 3), o arco do IA na prática (seção 6), as linhas rápidas (seção 7), o assunto e a prévia (seção 8), números com escala (seção 9), as cotas de estilo (seção 10), o ângulo Direito & tech (seção 11), radar e não repetição (seção 13), o rigor (seção 14) e o formato do arquivo (seção 15). Este arquivo diz só o que muda.

## 1. A missão em uma frase
Em **6 a 9 minutos de leitura**, nos dias fixos, o leitor entende **o que mudou de verdade em IA desde a última edição, o que é hype e o que ele pode fazer com isso**. Profundidade antes de volume: é melhor explicar bem três coisas que listar quinze.

## 2. Quando sai: curadoria diária, dias fixos e edição extra
O leitor pediu assim (22/10): a pesquisa é diária, o envio não. A rotina roda **todo dia** às 05:15 e faz uma de três coisas:
1. **Dia fixo** (os `dias_envio` do bloco `ia` no `cadernos.yaml`): a edição sai sempre, com o que estiver na curadoria e o que chegou hoje.
2. **Fora do dia fixo, com notícia muito importante:** sai uma **edição extra**, curta (seção 6).
3. **Fora do dia fixo, sem nada urgente:** a rotina só **guarda** na curadoria o que achou e para. Sem edição e sem e-mail.

**A curadoria** fica em `dados/ia/curadoria.md`: uma seção `## AAAA-MM-DD` por dia e uma linha por achado, no formato `- [tema] Título — por que importa (url)`. O tema é um dos da seção 7.
- Guarde só o que tem chance de entrar: de 3 a 8 itens por dia. Dia fraco pode ter zero.
- Um item que ficou velho ou foi superado por novidade sai da curadoria. Se a história andou, troque a linha pela versão nova.
- No dia da edição, **reconfira** cada item guardado antes de usar: preço, disponibilidade e número mudam em poucos dias.
- O que entrou na edição sai da curadoria.

**O que conta como muito importante** (o critério da edição extra). Pelo menos um destes:
- um **breakthrough** que passa no critério da seção 3 do manual geral;
- uma **falha de segurança ou ataque que pede ação hoje** de quem usa a ferramenta (atualizar, trocar chave ou senha, desligar algo), numa ferramenta que o leitor ou os clientes dele podem usar;
- uma mudança **que vale já** e mexe no trabalho ou no bolso do leitor: preço, plano gratuito ou termos de uso de uma ferramenta popular, ou uma regra de IA no Brasil com prazo próximo.

Lançamento de modelo, rodada de investimento, previsão de executivo e polêmica **não** são urgentes: vão para a curadoria. **Na dúvida, guarda.** Edição extra toda semana vira ruído.

## 3. A divisão com a geral
A geral sai todo dia e fala muito de IA. O caderno **não é uma segunda geral de IA**: ela dá o fato do dia, e o caderno dá o mecanismo, o teste e a consequência.
- **Antes da pauta, leia o que a geral publicou** desde a última edição do caderno (`python3 main.py historico --dias 5`, e a seção "Nos outros cadernos" do histórico do caderno).
- **Assunto que a geral já deu só entra com valor novo:** o que mudou desde então, o mecanismo que a geral não explicou, um teste, o lado jurídico, o "roda no seu Mac?", o "como vira serviço". Nesse caso, diga: "a geral contou na terça (20/10); aqui, o que isso muda". Nunca reconte a mesma notícia no mesmo formato.
- **O caderno fica com o que a geral costuma deixar de fora:** a ficha técnica dos modelos, o open source, as ferramentas de nicho, a China em detalhe e o andamento da regulação.
- **O IA na prática do caderno usa outro caso** que não o da geral nos últimos 7 dias.
- Itens marcados `JÁ COBERTO` nos candidatos já saíram em alguma newsletter da família: só entram com novidade.

## 4. O tom
- A voz da geral (seção 2 do manual geral): informal, precisa, frases curtas, humor seco. Pode ser **um pouco mais técnica**, mas o leitor continua sendo um estudante de Direito que constrói coisas com IA, não um engenheiro.
- **Todo jargão é explicado na primeira vez**, em meia frase: token, parâmetro, pesos abertos, quantização, janela de contexto, MoE, RAG, *fine-tuning*, agente, MCP, *benchmark*, inferência.
- **Antídoto contra o hype.** O caderno existe para separar o que muda a vida de uma pessoa comum do que só muda o placar de um *benchmark*. Quando a manchete promete mais do que a fonte entrega, diga isso com todas as letras.

## 5. Regras próprias de IA
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
- Estrelas e data só com `python3 main.py github dono/repo`, e com a data da consulta ("**12,3 mil** estrelas em 22/10"). Na nuvem, a API do GitHub costuma dar 403: se a consulta falhar, não cite o número de estrelas.
- Diga o que o projeto faz em uma frase de leigo, a licença e se precisa de programação para usar.
- Repositório com muitas estrelas em pouco tempo não é prova de qualidade: procure quem testou (Hacker News, Simon Willison, uma issue com resultado).

**Agentes e ferramentas.** Diga o que o agente faz **sozinho** e o que precisa de aprovação, quanto custa e o que pode dar errado (dados, permissões, erro silencioso).

**Regulação.**
- Brasil: o PL 2338/2023 (marco da IA), a ANPD, decisões do STF, do TSE e de tribunais. Europa: o AI Act. EUA: leis estaduais e federais. China: as regras da CAC e do MOFCOM.
- Cite lei, artigo e fase da tramitação só com certeza e com o link do texto oficial (planalto.gov.br, camara.leg.br, senado.leg.br, eur-lex.europa.eu). Tramitação muda: escreva "segundo a Câmara, em 21/10".
- Use ⚖️ e o formato **Quem defende diz:** / **Quem critica diz:** quando houver polêmica.

**China.** Prefira a fonte primária (o repositório no GitHub ou no Hugging Face, o comunicado da empresa, o texto da norma). Imprensa chinesa estatal ou próxima do governo leva "segundo a imprensa estatal".

**Segurança.** Falha ou ataque com IA entra com o que fazer (atualizar, trocar senha, desligar algo), nunca com o passo a passo do ataque.

## 6. A estrutura da edição

### A edição dos dias fixos
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
11. **Fecho** de uma linha que aponta para o próximo dia fixo: "Até quarta." (na segunda), "Até sexta." (na quarta) ou "Até segunda." (na sexta).

Alvo: **de 1.300 a 2.000 palavras**. Período fraco é edição curta: só o bom dia, O QUE MUDOU DE VERDADE, IA NA PRÁTICA, a pergunta e o fecho já são uma edição. Seção nenhuma é preenchida para completar.

### A edição extra (fora dos dias fixos)
Só com o critério da seção 2. Assunto começando com "🚨", e depois:
1. **bom dia.** Uma frase dizendo por que esta edição saiu fora do dia.
2. `## Título` e `> **TL;DR:**`, de **200 a 400 palavras**: o que aconteceu, por que importa, **o que fazer agora** (o passo concreto, com link) e o que observar nos próximos dias.
3. Fecho: "A edição normal sai [dia fixo]."

O resto da curadoria continua guardado para o dia fixo.

## 7. O front matter
Igual ao da geral (manual, seção 15), com estas diferenças:
- `tipo`: `regular` (dia fixo) ou `extra`; na extra, acrescente `motivo_extra` com o critério da seção 2 que ela cumpre;
- `tema` das histórias: `modelos | open_source | ferramentas | agentes | pesquisa | regulacao | china | brasil | negocios_ia | seguranca`;
- `formatos`: `[o_que_mudou, modelos_novos, open_source, ferramentas, regulacao, ia_na_pratica, radar, pergunta]`, só os usados, mais `raio_x`, `explicador` ou `continuacao` quando for o caso;
- `breakthrough`: `true` só se a principal passou no critério.

## 8. Checklist
- [ ] Edição fora do dia fixo só com o critério da seção 2, e o que entrou saiu da curadoria.
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
