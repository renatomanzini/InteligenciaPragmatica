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
