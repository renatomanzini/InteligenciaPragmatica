# Manual do caderno Marketing

O caderno Marketing é a newsletter de marketing digital da Inteligência Pragmática. A pesquisa é **diária**, mas o envio não: a edição sai em **dois dias fixos por semana** (os `dias_envio` do bloco `marketing` no `cadernos.yaml`), às 06:00. Fora deles, só sai **edição extra** com notícia muito importante (seção 2).

Vale tudo o que está no `manual/MANUAL_DE_REDACAO.md`: a voz (seção 2), a regra contra a novidade forçada (seção 3), a anatomia da matéria principal (seção 5), números com escala (seção 9), o ângulo Direito & tech (seção 11), radar e não repetição (seção 13), o rigor (seção 14) e as convenções de formato (seção 15). Este arquivo diz só o que muda.

## 1. A missão em uma frase
Em **5 a 7 minutos de leitura**, o leitor sabe:
- o que mudou de verdade nas plataformas (Meta, Google, TikTok, YouTube, LinkedIn) e na busca com IA desde a última edição;
- um caso que funcionou, de preferência brasileiro, e o que dá para copiar dele;
- **que serviço ele poderia vender com isso**, para quem e por quê.

O leitor estuda Direito, constrói sites e apps com IA e está começando a vender serviços. Ele não é do mercado publicitário. O caderno é para quem **vende** marketing a pequenos negócios e escritórios, não para diretor de grande anunciante.

## 2. Quando sai: curadoria diária, dias fixos e edição extra
O leitor pediu assim (22/10): a pesquisa é diária, o envio não. A rotina roda **todo dia** às 05:15 e faz uma de três coisas:
1. **Dia fixo:** a edição sai sempre, com o que estiver na curadoria e o que chegou hoje.
2. **Fora do dia fixo, com notícia muito importante:** sai uma **edição extra**, curta (seção 8).
3. **Fora do dia fixo, sem nada urgente:** a rotina só **guarda** na curadoria o que achou e para. Sem edição e sem e-mail.

**A curadoria** fica em `dados/marketing/curadoria.md`: uma seção `## AAAA-MM-DD` por dia e uma linha por achado, no formato `- [tema] Título — por que importa (url)`. O tema é um dos da seção 10.
- Guarde só o que tem chance de entrar: de 3 a 8 itens por dia. Dia fraco pode ter zero.
- Um item que ficou velho ou foi superado sai da curadoria. Se a história andou, troque a linha pela versão nova.
- No dia da edição, **reconfira** cada item guardado antes de usar: recurso em teste vira lançamento (ou some), e prazo muda.
- O que entrou na edição sai da curadoria.

**O que conta como muito importante** (o critério da edição extra). Pelo menos um destes:
- uma mudança de plataforma **com prazo antes do próximo dia fixo** que pede ação de quem anuncia ou gere conta: recurso ligado por padrão a partir de tal dia, termos de uso novos, fim de um recurso ou de um formato de anúncio, prazo de migração;
- uma **falha, golpe ou bloqueio que pede ação hoje**: contas de anúncio invadidas em massa, golpe com falso suporte da plataforma, queda que para as campanhas, cobrança indevida;
- uma **regra nova no Brasil que vale já** para quem anuncia: publicidade de influenciador, dados para anúncio (LGPD e ANPD), proibição de uma categoria de anúncio.

Lançamento em teste, relatório, pesquisa, rodada de investimento, prêmio e case **não** são urgentes: vão para a curadoria. **Na dúvida, guarda.** Edição extra toda semana vira ruído.

## 3. Não repetir a geral nem o radar
- A geral fala de marketing quase todo dia (Brasil adentro, Mundo afora e, às vezes, a matéria principal). Antes da pauta, leia o que ela publicou desde a última edição do caderno (`python3 main.py historico --dias 5` e a seção "Nos outros cadernos" do histórico do caderno).
- Assunto que a geral já deu só entra com **valor novo**: o que mudou desde [data], o efeito para quem anuncia, o case por trás, o "como vira serviço". Diga a data em que saiu na geral quando voltar a ele ("a geral contou na terça (20/10) que...").
- O radar é a MarketingDrops (que chega pelo remetente "M15"). Ela serve para achar pauta, nunca para citar nem copiar. Assunto que já saiu lá só entra com valor que ela não deu.
- Itens marcados `JÁ COBERTO` nos candidatos já saíram em alguma newsletter da família: só entram com novidade.

## 4. O tom
- A voz da geral: frases curtas, humor seco, "você".
- **Prático antes de tudo.** A pergunta de cada item é: "o que isso muda para quem anuncia, cria conteúdo ou vende esse serviço?".
- **Jargão explicado na primeira vez**, numa oração curta: CPM (quanto custa mil exibições), CPC, CTR, ROAS (quanto volta de venda para cada real em anúncio), CAC, LTV, funil, topo e fundo de funil, *retargeting*, *lookalike*, Advantage+, Performance Max, AI Overviews, AI Mode, GEO (otimizar para aparecer na resposta das IAs), UGC (conteúdo feito pelo cliente ou por criador), *creator economy*.
- **Nada de guru.** Proibido: "escalar", "faturar seis dígitos", "hack", "segredo", "fórmula", "resultado garantido". Marketing digital tem muito vendedor de curso; o caderno é o antídoto.

## 5. Número de case é alegação de quem vende
- Case de agência, de plataforma ou de ferramenta é **comunicação de quem quer vender**. Conte o fato e atribua o número: "a marca diz que as vendas cresceram 40%", "segundo a agência...". Diga o período e a base quando a fonte disser, e diga quando ela **não** diz ("a empresa não informou a base de comparação").
- Estudo de plataforma (Meta, Google, TikTok) sobre a eficácia dos próprios anúncios é estudo de parte interessada: diga isso em meia frase. Vale o mesmo para pesquisa de empresa que vende o serviço pesquisado.
- Prêmio (Cannes Lions, Effie, Wave) não prova resultado. Pode entrar como contexto, nunca como prova.
- Número de seguidor, visualização ou "viralizou" sem fonte não entra.

## 6. Disponibilidade e datas
- Todo recurso novo de plataforma diz **onde e quando** vale: "já liberado para todos", "em teste nos EUA", "chega ao Brasil em novembro, segundo a Meta", "sem data para o Brasil". Recurso só em teste lá fora é escrito como teste, nunca como novidade disponível.
- Escreva a data explícita ("na terça (20/10)"), nunca "esta semana" ou "ontem" sozinhos. Isso vale em dobro para o que veio da curadoria, que pode ter dias.
- Mudança anunciada com data futura (regra que vale a partir de tal dia) leva a data e "a partir de".

## 7. A fonte primária das plataformas
- O que a plataforma lançou ou mudou se confirma na **fonte dela**: Meta Newsroom, Meta for Developers ou a Central de Ajuda da Meta para empresas, Google Ads & Commerce Blog ou a Ajuda do Google Ads, Google Search Central, YouTube Official Blog, TikTok Newsroom, LinkedIn News. A imprensa especializada (Social Media Today, Search Engine Roundtable, PPC Land) serve para achar e dar contexto.
- Quando o "lançamento" só aparece num print de usuário ou num teste visto por um jornalista, diga isso: "em teste, segundo o Search Engine Roundtable; o Google não anunciou".
- As páginas do facebook.com recusam robôs (o `links` dá "inconclusivo"): confira o texto pelo WebFetch, que segue o endereço web.facebook.com.

## 8. A estrutura da edição

### Dia fixo
1. **bom dia.** E de 2 a 3 linhas com o tema da edição. Começa com "bom dia." em minúsculas.
2. **Nesta edição:** de 3 a 5 bullets que já vendem cada parte.
3. **#### A HISTÓRIA PRINCIPAL**: a mudança mais importante para quem vende marketing, com a anatomia da seção 5 do manual geral (`## Título-gancho`, `> **TL;DR:**`, os números com escala, os dois lados e **"Por que isso importa pra você:"**). De 300 a 500 palavras.
4. **#### O QUE MUDOU NAS PLATAFORMAS**: de 2 a 5 linhas `→`, com a plataforma no rótulo e os dois-pontos fora do negrito (`→ **Meta**: ...`, `→ **Google**: ...`, `→ **TikTok**: ...`, `→ **YouTube**: ...`, `→ **LinkedIn**: ...`). Uma frase com o que mudou, onde vale (seção 6) e a fonte; termine com "na prática, ..." quando ajudar. Plataforma sem novidade relevante fica de fora.
5. **#### TRÁFEGO E BUSCA**: de 1 a 4 linhas `→` sobre tráfego pago, SEO e busca com IA (AI Overviews, AI Mode, ChatGPT, Perplexity): o que mudou no custo, no alcance ou no tráfego, com escala.
6. **#### CRIADORES E MARCAS**: de 1 a 4 linhas `→` sobre criadores, *branding* e funis: o que uma marca ou um criador fez e deu (ou não deu) certo, com fonte.
7. **#### O CASE**: pelo menos uma vez por semana, de preferência brasileiro, de 200 a 350 palavras, com `### Título` e nesta ordem:
   - o que a marca ou a pessoa fez (canal, formato, público);
   - o resultado, atribuído a quem diz (seção 5);
   - **O que dá para copiar:** de 2 a 4 linhas, adaptando para um negócio pequeno (clínica, escritório, restaurante, loja);
   - **⚠️ Freio de realidade:** o que o case não prova (verba, marca forte, sorte, falta de base de comparação).
   Sem um case bom, a seção sai, e ele fica para a edição seguinte.
8. **#### COMO ISSO VIRA SERVIÇO**: o coração do caderno, em toda edição. Uma ideia de serviço que nasce do que saiu, com `### Título` e de 120 a 220 palavras:
   - **o que vender**, numa linha;
   - **para quem** (um nicho concreto: dentistas, escritórios de advocacia, restaurantes, imobiliárias...);
   - **por que o cliente pagaria agora** (a mudança que cria a dor);
   - **como entregar**, com as ferramentas;
   - **⚠️ o limite** (o que pode dar errado, regra de plataforma, LGPD, CONAR, conselho profissional).
   Nunca invente preço de mercado nem faturamento. Se citar valor, ele tem fonte.
9. **#### PARA ENTENDER** (opcional): um conceito em até 100 palavras, com um exemplo da edição ("o que é ROAS", "por que o CPM sobe no fim do ano").
10. **Pergunta de fechamento**, uma linha, e o fecho "Até [o próximo dia fixo]." (por exemplo, "Até sexta.").

Só a história principal usa `## Título` e TL;DR (o montador cobra o TL;DR de todo `##`).

Alvo: **de 1.000 a 1.600 palavras**. Período fraco é edição curta: as partes 5, 6, 7 e 9 podem sair, sem encher linguiça. A história principal e o "como isso vira serviço" ficam sempre.

### A edição extra (fora dos dias fixos)
Só com o critério da seção 2. Assunto começando com "🚨", e depois:
1. **bom dia.** Uma frase dizendo por que esta edição saiu fora do dia.
2. `## Título` e `> **TL;DR:**`, de **200 a 400 palavras**: o que mudou, quem é afetado, **o que fazer agora** (o passo concreto, com link e prazo) e o que observar nos próximos dias.
3. Fecho: "A edição normal sai [o próximo dia fixo]."

O resto da curadoria continua guardado para o dia fixo.

## 9. Direito & tech no marketing
Marketing digital esbarra no Direito o tempo todo. Quando couber, diga em 1 a 3 linhas com ⚖️:
- publicidade de influenciador e identificação de anúncio (Código de Defesa do Consumidor e o Guia de Publicidade por Influenciadores Digitais do CONAR);
- dados para anúncio, *pixel*, consentimento e *cookies* (LGPD);
- direito autoral e de imagem em criativo feito com IA;
- regras das plataformas e dos conselhos de classe para anunciar (a publicidade da advocacia segue o Provimento 205/2021 da OAB).
Mesma régua do manual geral: cite a norma com link oficial quando tiver certeza; se não tiver, descreva o problema sem citar dispositivo.

## 10. O front matter
Igual ao da geral (manual, seção 15), com estas diferenças:
- `tipo`: `regular` (dia fixo) ou `extra`; na extra, acrescente `motivo_extra` com o critério da seção 2 que ela cumpre;
- `tema` das histórias: `plataformas | trafego_pago | busca | criadores | branding | funis | cases | direito_tech | mercado`;
- `formatos`: `[historia_principal, plataformas, trafego_busca, criadores_marcas, case, vira_servico, para_entender, pergunta]`, só os usados;
- `breakthrough`: pelo critério da seção 3 do manual geral, que no marketing é raro.

## 11. Checklist
- [ ] Todo recurso novo diz onde vale (Brasil, EUA, teste) e a data está explícita.
- [ ] O lançamento foi confirmado na fonte da plataforma, ou está escrito como teste ou como "segundo [veículo]".
- [ ] O que veio da curadoria foi reconferido hoje.
- [ ] Todo número de case está atribuído a quem diz, e prêmio não virou prova.
- [ ] Todo jargão ganhou explicação na primeira vez.
- [ ] Nenhuma promessa de guru, nenhum preço ou faturamento inventado.
- [ ] O case (se houver) tem "O que dá para copiar" e "⚠️ Freio de realidade".
- [ ] O "Como isso vira serviço" diz o que, para quem, por que agora, como entregar e o limite.
- [ ] Nada repetido da geral (desde a última edição) ou do radar sem valor novo.
- [ ] Toda afirmação tem link.
- [ ] O fecho aponta para o próximo dia fixo certo.
