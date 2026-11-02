# Verificação — 2026-11-02

Todas as correções obrigatórias das duas partes foram aplicadas na edicao.md (revisão do editor).

# Verificação, parte 1 (bom dia até IA na prática), edição 2026-11-02

Fontes abertas por curl/WebFetch em 02/11/2026. github.com devolve 403, então usei os arquivos raw (README do global-law e do brazil-law, manifest.json, MCP.md). O Planalto não abriu desta máquina (sem resposta), então os dois links de conferência dele não foram testados; o LexML abriu (200).

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Pardela-de-Manx, ave marinha do tamanho de um pombo | Ars Technica (Lewin: "about the same size as a pigeon") | confirmada | nenhuma |
| 2 | Usa o Sol como bússola; relógio interno desalinha ao voar a leste/oeste | Ars | confirmada | nenhuma |
| 3 | Erro de rumo até ~15 graus | Ars: "up to around 15 degrees" | confirmada | nenhuma |
| 4 | Estudo na Science, 20 anos de GPS | Ars: "new Science study"; GPS desde 2004, "Two decades later" | confirmada | nenhuma |
| 5 | "Até o passarinho precisa de uns dias para acertar o relógio" | Ars: o relógio é recalibrado a cada amanhecer e entardecer; "uns dias" não aparece | não confirmada | Cortar a frase ou trocar por algo que a fonte diga (o relógio se reajusta todo amanhecer e entardecer) |
| 6 | Haas (30/10): engenheiro da Databricks, committer do PostgreSQL | blog de Haas: "Sr. Staff Software Engineer @ Databricks, PostgreSQL Major Contributor and Committer", 30/10/2026 | confirmada | nenhuma |
| 7 | Versão 19 deve sair "most likely" em novembro | Haas: "most likely won't be released until November" | confirmada | nenhuma (citação curta, ok) |
| 8 | Na última década saíram entre meados de setembro e meados de outubro | Haas: "no earlier than the middle of September, and no later than the middle of October" | confirmada | nenhuma |
| 9 | Ramo da versão anterior, 08/04 a 25/09: 248 para 433, +74% | Haas: 248 commits (REL_17, 2025) e 433 (REL_18, 2026), "more than 74%" | confirmada | nenhuma. Opcional: Haas escreve "mais de 74%" |
| 10 | Ramo da versão nova: 724 para 1.169, +60% | Haas: 724 (REL_18, 2025) e 1169 (REL_19, 2026), "more than 60%". 1169/724 = +61,5% | confirmada | Opcional: "mais de 60%", como na fonte |
| 11 | Haas diz não saber como o projeto vai alcançar o acúmulo | Haas: "how are we ever going to catch up... Right now, I'm not sure" | confirmada | nenhuma |
| 12 | Muita gente reporta bugs achados com LLMs; IA rascunha correções nem sempre certas; humanos precisam revisar | Haas | confirmada | nenhuma |
| 13 | Calegari (01/11), convidado no blog do Tao | Tao: "This is a guest post by Frank Calegari", 1 Nov 2026 | confirmada | A atribuição está certa (convidado no blog do Tao, link com "texto de Calegari") |
| 14 | OpenAI liberou mais de 700 artigos em 6 de outubro | Calegari: "The release by OpenAI on October 6 of over 700 research papers" | confirmada | nenhuma |
| 15 | TL;DR: "a matemática recebeu mais de 700 artigos de uma vez" | Calegari ("release... of over 700 research papers") | confirmada | nenhuma |
| 16 | Propõe tratar todo trabalho como se tivesse ajuda de IA; mais entrevista presencial nas contratações | Calegari: "Evaluate all work as if it is AI-assisted"; "Interview postdocs and graduate students in person" | confirmada | nenhuma |
| 17 | Provas em Lean (como proposta de Calegari) | Calegari: "Is it Lean-verified?", "hopefully Lean-checked"; não é uma regra proposta de forma tão direta | confirmada, com ressalva | Suavizar: "e valorizar provas verificadas em Lean" |
| 18 | Citação: "Choosing worthwhile problems may end up mattering more than producing proofs" | Calegari, texto idêntico (11 palavras) | confirmada | nenhuma |
| 19 | Classificação dos grupos simples finitos "foi anunciada em 1972, declarada completa em 1983, e um caso só fechou umas duas décadas depois" | Calegari: em 1972 Gorenstein anunciou um programa rumo à classificação; a classificação foi anunciada em 1983, "somewhat prematurely", com o caso quasithin concluído "another two decades" depois (Aschbacher e Smith) | errada (parcial) e sem link/atribuição | Escrever: "o programa foi lançado em 1972, a classificação foi declarada completa em 1983 e o caso quasithin só fechou umas duas décadas depois (Calegari)" |
| 20 | Altman, num podcast, disse ter mais resultados guardados | Verge: podcast Cheeky Pint, "We do. Of course." | confirmada | nenhuma |
| 21 | Gasto na casa das centenas de milhões de dólares; ~US$ 10 milhões só no Navier-Stokes | Verge: "in the order of hundreds of millions", "around $10 million — 'maybe a little more'" | confirmada | Opcional: "cerca de US$ 10 milhões (talvez um pouco mais)" |
| 22 | Verge registra críticas de verificação insuficiente | Verge: "insufficient verification" | confirmada | nenhuma |
| 23 | Altman: "a humanidade merece o conhecimento" (otimistas) | Verge: "Humanity deserves fundamental knowledge" | confirmada | nenhuma |
| 24 | Kingsbury (Jepsen) achou 96 problemas no ParticleDB | Jepsen: "We present 96 issues in ParticleDB" | confirmada | nenhuma |
| 25 | ParticleDB se dizia "formally proven" sem ter a especificação que o provaria | Jepsen: home page "formally proven" com prova TLA+; "no TLA+ specification was available" | confirmada | nenhuma |
| 26 | Para Kingsbury, LLMs corroem a confiança em documentação e software | Jepsen/Willison: "the use of LLMs erodes trust in documentation, in software, and in the organizations which produce them" | confirmada | nenhuma |
| 27 | Otimista Haas: "código mais escrutinado fica mais seguro" | Haas diz que cada recurso será escrutinado por IA e que é "challenge and opportunity"; "mais seguro" não é dito | não confirmada (inferência) | Trocar por "vê desafio e oportunidade" |
| 28 | Pessimista Haas: "a revisão humana não escala" | Haas: correções da IA precisam de revisão humana e "humans have not gotten any smarter"; "não escala" é paráfrase | confirmada, com ressalva | Aceitável; mais fiel: "a revisão humana não acompanha" |
| 29 | "matemáticos ouvidos pelo Verge" como pessimistas | Verge: matemáticos criticam anúncio, atribuição e verificação | confirmada | nenhuma |
| 30 | "a IA agora é o estagiário que entrega 700 páginas na sexta às 18h" | A fonte fala de 700 artigos de pesquisa, não 700 páginas | errada (unidade) | "entrega 700 artigos" ou tornar a frase claramente figurada |
| 31 | "O valor migra de produzir para conferir e assinar" (em "Por que isso importa") | Sem fonte; é opinião de tendência, antes do selo `**Opinião:**` | opinião sem selo | Mover para depois do selo `**Opinião:**` ou abrir com "a aposta é" |
| 32 | `global-law`, da organização lexifina, reúne leis de vários países | README do global-law | confirmada | nenhuma |
| 33 | `brazil-law` declara o Planalto como fonte, um arquivo por artigo e um commit por alteração | README do brazil-law: "published by the Presidency of the Republic (Casa Civil) on planalto.gov.br"; "one file per article, one commit per amendment" | confirmada | nenhuma |
| 34 | Constituição 122 versões, Código Civil 64, CLT 220, LGPD 11 | README do brazil-law, tabela | confirmada | nenhuma |
| 35 | "registro até 28/10/2026" | manifest.json: Brazil `record_to` 2026-10-28 | confirmada | Cuidado: vale para o Brasil como corpus; a CLT, p. ex., vai só até 06/04/2026 (a frase pode induzir a erro) |
| 36 | Servidor roda na máquina, só lê o repositório, sem chamadas de rede | README do global-law: "runs on your machine over stdio, reads the repository and changes nothing. It makes no network calls." | confirmada | nenhuma |
| 37 | 18 ferramentas | README do global-law: "18 read-only tools" | confirmada | nenhuma |
| 38 | Comando `claude mcp add global-law -- python tools/mcp_server.py` | README do global-law (idêntico) | confirmada | nenhuma |
| 39 | "não é oficial" | README do brazil-law: "not legal advice and not an official publication" | confirmada | nenhuma |
| 40 | "o mantenedor não se identifica" | Os READMEs só mencionam "Lexifina" (marca/organização); não consegui ver o perfil no GitHub (403, API bloqueada) | não confirmada | Cortar ou escrever "não consegui identificar o mantenedor nos READMEs" |
| 41 | A 8.666 vai até 30/12/2023, a 9.099 até 23/11/2021, como "leis paradas no passado" | brazil-law: Lei 8.666 vai até a revogação pela 14.133 em 30/12/2023 (pasta fica vazia); 9.099 até 23/11/2021 | datas confirmadas; enquadramento impreciso | A 8.666 está revogada, não "parada". Trocar o exemplo ou escrever "a 8.666 termina na revogação (30/12/2023); a 9.099 para em 23/11/2021" |
| 42 | "os anexos e as tabelas ficam de fora" | brazil-law: depende da lei. O anexo da CLT está em `clt/anexo.md` e o do ITR em `anexo.md`; a Lei de Migração, a do ISS, a 4.320 e a 9.986 não trazem anexos | errada (generalização) | "alguns anexos e tabelas ficam de fora, conforme a lei" |
| 43 | A checagem de citações não reconhece citações do Brasil | manifest.json, Brazil: "corpus.json has no citation rule, so citations of this law are not recognised" | confirmada | nenhuma |
| 44 | Python 3.10+ e git para o MCP | README do global-law | confirmada | nenhuma |
| 45 | Clonar tudo com submódulos pode pesar num notebook de 8 GB (não testado) | Sem fonte; está marcado como não testado | não confirmada (declarada) | Aceitável como está, ou cortar |
| 46 | Brasil entra no global-law, "outros países" | manifest.json lista Brazil (`iso_path` br/national/acts) | confirmada | nenhuma |
| 47 | Links Planalto (`/ccivil_03/leis/`) e LexML | LexML: 200; Planalto não respondeu a esta máquina | não testado (Planalto) | Testar o link na checagem de links do `main.py` |
| 48 | "Sem instalar nada", ver histórico de artigo da LGPD ou do CDC no navegador | brazil-law inclui `lgpd/` e `codigo-de-defesa-do-consumidor/` (16 versões) | confirmada | nenhuma |

## Opinião sem selo e atribuição
- Os blocos "Os otimistas / Os pessimistas" e "Por que isso importa pra você" rotulam posições de terceiros; o item 27 atribui a Haas algo que ele não disse.
- O item 31 é opinião de tendência fora do selo.
- O selo `**Opinião:**` está presente no fim da matéria, e a frase ali ("a aposta é que...") está ok.
- Atribuição de "Mathematics has changed": certa. A edição fala em "No blog do matemático Terence Tao, o convidado Frank Calegari" e liga ao "texto de Calegari". Nada a corrigir.

## Correções obrigatórias
1. Item 19: separar 1972 (programa de Gorenstein) de 1983 (classificação declarada completa) e atribuir a Calegari.
2. Item 30: "700 páginas" para "700 artigos".
3. Item 27: não atribuir a Haas "código mais escrutinado fica mais seguro"; usar "desafio e oportunidade".
4. Item 5: cortar "uns dias para acertar o relógio" (a fonte diz que o relógio é recalibrado todo amanhecer e entardecer).
5. Item 40: cortar "o mantenedor não se identifica" ou reescrever como limite da checagem.
6. Item 42: "alguns anexos e tabelas" (a CLT tem `anexo.md`).
7. Item 41: a 8.666 está revogada, não "parada"; ajustar o exemplo.
8. Item 31: pôr a frase de tendência depois de `**Opinião:**` ou marcar como aposta.

Recomendadas: item 17 (suavizar Lean), item 35 (deixar claro que 28/10 vale para o Brasil, a CLT vai só até 06/04/2026), item 10 ("mais de 60%").

# Verificação, parte 2 (Economia até a pergunta), edição de 02/11/2026

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Copom decide na quarta (04/11) | NeoFeed, InfoMoney | confirmada | |
| 2 | Selic em 13,75%; Itaú espera manutenção | NeoFeed (30/10) | confirmada | |
| 3 | InfoMoney traz 13,50% como projeção | InfoMoney | confirmada o número (tabela "13,5%") | |
| 4 | "sinal de mercado dividido" | InfoMoney | não confirmada: o texto do InfoMoney diz que "a previsão geral dos mercados é de que o ciclo de cortes se interrompa"; o 13,5% da tabela contradiz o próprio texto. É inferência do redator, sem selo | Cortar "sinal de mercado dividido" ou escrever "a tabela do InfoMoney traz 13,50%, mas o texto da mesma matéria fala em interrupção dos cortes". Na NeoFeed, B3 dá 66,5% de chance de manutenção |
| 5 | Petrobras QAV +7,2%, +R$ 0,45/litro, desde domingo 01/11 | Estadão | confirmada | |
| 6 | "depois de +11,8% em outubro" | Estadão | confirmada | |
| 7 | "pesa no custo das companhias aéreas" | Estadão | não confirmada como fato da matéria (inferência razoável, sem selo) | Pôr "**Opinião:**" ou cortar |
| 8 | Binance "desde 31/10, reabriu os saques" | Estadão (01/11) | não confirmada: a matéria não dá a data 31/10; diz só "após a retomada dos saques" | Tirar "desde 31/10" ou citar fonte com a data |
| 9 | Saída líquida de ~US$ 3,64 bi "no domingo", 2,1% dos ativos | Estadão | confirmada com ressalva: o número cobre só "do início da manhã ao começo da tarde" de domingo (1º), não o dia todo. 2,1% são "ativos totais sob gestão" | "saída líquida de ~US$ 3,64 bi entre a manhã e o começo da tarde de domingo (01/11)" |
| 10 | Falta contexto: saques estavam suspensos por ataque hacker | Estadão | omissão | Incluir "após suspensão por ataque hacker" |
| 11 | Opep+ manteve metas para dezembro em 01/11 | Folha/Reuters | confirmada (domingo 1º; sete membros, reunião online) | |
| 12 | Brent fechou perto de US$ 118 na sexta (30/10), maior desde abril | Folha/Reuters | confirmada | |
| 13 | BoE decide quinta (05/11) com taxa em 3,75% | BoE | confirmada ("Next due: 5 November 2026", Bank Rate 3.75%) | |
| 14 | "em setembro manteve por 6 a 3, com três votos por 4%" | BoE (página citada) | não confirmada: a página não traz placar nem votos (só "held at 3.75%", 17/09/2026) | Citar a ata/Monetary Policy Summary de setembro ou cortar o placar. Obs.: a agenda do InfoMoney projeta 4,0% para quinta, divergente do 3,75% |
| 15 | PMI RatingDog 52,0 em outubro vs 52,1 em setembro | Valor | confirmada | |
| 16 | PMI oficial caiu de 50,1 para 49,3; abaixo de 50 é contração | Valor | confirmada os números; "abaixo de 50 é contração" é definição geral, a matéria não diz | Aceitável; opcional |
| 17 | Meio de mandato nos EUA, terça (03/11) | InfoMoney (sem data exata no trecho lido; só "semana de 2 a 6") | confirmada (03/11/2026 é terça) mas o link ao lado é o Valor, que não trata disso | Mover o link ou citar o InfoMoney |
| 18 | Chilli Beans pediu recuperação extrajudicial na sexta (30/10), R$ 340 mi | NeoFeed | confirmada | |
| 19 | Raízen: "assembleias de credores de 30/10 aprovaram dividir em duas listadas" | InvestNews | errada no sujeito: a matéria diz que os **acionistas** aprovaram nas assembleias (credores têm maioria dos conselhos) | "as assembleias de acionistas de 30/10 aprovaram..." |
| 20 | Distribuição com marca Shell; açúcar, etanol e bioenergia | InvestNews | confirmada | |
| 21 | Conselho vota aumento de capital de até R$ 39,8 bi em 06/11 | InvestNews | confirmada (reunião "prevista para 6 de novembro") | Usar "prevista" |
| 22 | 99: diretor-geral Simeng Wang; maioria das operações de delivery com mais de um ano é rentável, sem números | Estadão | confirmada | |
| 23 | Itaú compra NeoSpace por R$ 2,925 bi, sujeito a Cade e BC | Bloomberg Línea | confirmada | |
| 24 | Jan/2025: US$ 15 mi por 15% | Bloomberg Línea | confirmada ("anunciado... em rodada divulgada em janeiro de 2025") | Dizer "anunciou", não "pagou" |
| 25 | Toast: FTC, "sete estados e dois governos locais da Califórnia" | PPC Land; FTC | errada/ambígua: PPC Land diz "eight states". A FTC lista 8 estados (CA, CO, FL, IL, IA, NE, OK, UT), sendo a Califórnia representada por LA County e San Francisco | "a FTC, oito estados e dois governos locais da Califórnia" (ou "FTC e oito estados") |
| 26 | Taxa escondida de US$ 0,99 em pedidos online e cancelamento difícil | PPC Land; FTC | confirmada com ressalva: pedidos acima de US$ 10, de set/2021 a jul/2023 | "taxa de US$ 0,99 em pedidos online acima de US$ 10 (2021 a 2023)" |
| 27 | Toast "discorda fortemente" | PPC Land | confirmada ("strongly disagrees") | |
| 28 | ⚖️ CDC também combate taxa escondida e cancelamento difícil | sem link | não confirmada, sem fonte; opinião jurídica sem selo | Indicar artigo do CDC com link ou pôr "**Opinião:**" |
| 29 | Apple: Taiwan 30% para 26%; iguala Japão e Brasil | PPC Land | confirmada. Detalhe: vigente desde 31/10, anunciada em 29/10; "diz que iguala" na verdade vem da autoridade taiwanesa (Central News Agency), não da Apple | "a autoridade de Taiwan diz que iguala Japão e Brasil" |
| 30 | Shopify: prévia por convite, devs nos EUA, comissão base de 0,3%, "not final" | SEJ (WebFetch) | confirmada. A comissão extra é limitada aos EUA; a base de 0,3% não está dita como só EUA | Ok; cuidado com "nos EUA" aplicado ao 0,3% |
| 31 | ChatGPT Ads: desde sexta (30/10) ajustes ligados por padrão; reescrevem título, traduzem, trocam URL sem aprovação; dá para desligar | SEJ (WebFetch) | confirmada | |
| 32 | "quem anuncia precisa conferir o que sai no ar" | SEJ | recomendação do redator, sem selo | Pôr "**Opinião:**" ou suavizar |
| 33 | DoorDash: agentes de fora trouxeram "several hundred orders"; 993 mi de pedidos no 3º tri | Fool; Ars Technica | confirmada | |
| 34 | Tony Xu, teleconferência de 29/10 (quinta) | Fool | confirmada | |
| 35 | Clarity: checkout em 25% das sessões de agentes vs 15% das humanas | Clarity | confirmada com arredondamento: 25,21% e 14,65% | Escrever "25,2%" e "14,7%" |
| 36 | "Mas é evento de página, não compra, e pode ter humano assumindo" | Clarity | parcialmente: a fonte diz que não é prova de que o agente concluiu tarefa; "humano assumindo" é inferência | Trocar por "não prova que o agente concluiu a compra" |
| 37 | Conector em beta (menos de um mês) | Ars Technica | confirmada | |
| 38 | Cadeia final "pedido simples vai direto ao app... quem vende 'venda por agente' vende promessa" | Ars Technica | opinião sem selo | Pôr "**Opinião:**" na conclusão |
| 39 | Nolan Lawson (28/10): mesmo app em 12 frameworks; US$ 2,67 a US$ 4,97 por execução | Nolan Lawson | confirmada (12 linhas na tabela; mediana de 5 execuções; valores de API, não gasto real) | |
| 40 | Lenny's: Hector Serrano, Wispr Flow, 1h27, ~50 criadores, 500 a 600 anúncios UGC/mês | Lenny's | confirmada (1:27:46; post de 01/11, pago) | |
| 41 | Karpathy HackerTube: 6.454 vídeos, ~2 horas, com o Claude | bearblog | confirmada (diz "~2 hours now", Opus 5.5, Claude Code) | Ressalva: autor aparece como post em primeira pessoa; confirmar que é Karpathy |
| 42 | Pergunta do dia | n/a | n/a | |

Obs.: Selic "13,75%" aparece como taxa atual implícita na NeoFeed (manter em 13,75%). Dias da semana conferidos: 30/10 sexta, 01/11 domingo, 03/11 terça, 04/11 quarta, 05/11 quinta, 06/11 sexta (todos corretos).

## Correções obrigatórias
1. Raízen: trocar "assembleias de credores" por "assembleias de acionistas" (item 19).
2. Toast: "sete estados" para "oito estados" (item 25).
3. BoE: placar "6 a 3, três votos por 4%" não está na fonte; citar a ata ou cortar (item 14).
4. Binance: retirar "desde 31/10" (sem fonte) e ajustar "no domingo" para "da manhã ao começo da tarde de domingo" (itens 8 e 9).
5. Copom: cortar ou reformular "sinal de mercado dividido" (item 4).
6. Apple: atribuir a comparação com Japão e Brasil à autoridade taiwanesa (item 29).
7. Pôr selo `**Opinião:**` ou cortar: nota do CDC (28), "precisa conferir" do ChatGPT Ads (32), cadeia final do STATS (38), "pesa no custo das aéreas" (7).
8. Clarity: usar 25,2% e 14,7%, ou "cerca de" (35); trocar "pode ter humano assumindo" (36).
9. Toast: acrescentar que a taxa de US$ 0,99 valeu de 2021 a 2023, em pedidos acima de US$ 10 (26).
10. Meio de mandato nos EUA: o link ao lado é o Valor, que não cobre o fato (17).
