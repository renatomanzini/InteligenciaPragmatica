# Verificação, parte 2 — caderno IA de 22/10/2026 (quinta)

Escopo: de "OPEN SOURCE" até o fim (Open source, Ferramentas e agentes, Regulação, IA na prática, Radar, pergunta e fecho). A edicao.md não foi editada.
Conferido em 22/10/2026, abrindo cada link citado (WebFetch ou curl com texto dos parágrafos). Estrelas pelo `main.py github`. Dias da semana conferidos: 19/10 segunda, 21/10 quarta, 22/10 quinta (todos certos).
Páginas lidas: nenhuma continha instrução dirigida a mim.

## Tabela

### Open source

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| Kitten-TTS 2 é um modelo de voz de 1,7 bilhão de parâmetros | README do GitHub e model card no Hugging Face ("1.7B-parameter") | confirmada | — |
| clona uma voz com 5 a 30 segundos de áudio | README ("Clone any speaker from 5-30 seconds of audio") | confirmada | — |
| fala 20 línguas (português incluído) | README, seção Features ("20 languages", Portuguese na lista) | não confirmada (fontes do próprio projeto se contradizem) | O README diz 20, mas `docs/voices-and-expression.md` diz que são **dez** (nove línguas do treino mais hindi, uma voz por língua) e o model card do Hugging Face fala em **16** línguas com voz própria. Português está nas três. Escrever "segundo o README, 20 línguas" ou "mais de dez línguas". A mesma doc avisa que as outras línguas são "menos robustas que o inglês" e que o normalizador de números e datas é afinado para inglês |
| pesa **506 MB** | README, tabela "Available Models" ("506 MiB") e Quick Start | errada (imprecisa) | 506 **MiB** (≈ 531 MB) é só a versão reduzida (`weights="emb4"`, que o README diz custar "um pouco de qualidade"). A versão padrão, sem perda, tem **947 MiB**. O backend para Mac (MLX, o caminho rápido em Apple silicon) **recusa** a reduzida e usa a "packed" (padrão). Trocar por "947 MiB (506 MiB na versão reduzida)". Mesmo ajuste no título do front matter ("pesa 506 MB") |
| licença Apache 2.0 | README, seção License; LICENSE.md e model card no Hugging Face | **errada** | A Apache 2.0 cobre só o **código** do repositório. O README diz: "The models are licensed separately" e que o Kitten-TTS 2 sai sob a **Stellon Labs Community License** (model card: `license: other`). Pela LICENSE.md: grátis para pesquisa e uso pessoal; uso comercial só se a pessoa/empresa faturar menos de US$ 1 milhão por ano **e** tiver captado menos de US$ 1 milhão no total, com registro na Stellon Labs e o crédito "Powered by KittenML"; acima disso, a licença cai e é preciso pedir outra. Manual, seção 4: licença própria tem restrições e vale uma linha. Corrigir também "voz aberta" no título do front matter |
| 16,3 mil estrelas em 22/10 | `main.py github KittenML/KittenTTS`: 16.332 estrelas | confirmada | — |
| "na prática, roda no seu Mac" | README, seção "Running on a Mac" (backend MLX, "several times realtime on Apple silicon") e docs/mlx.md | confirmada com ressalva | Não contradiz a regra de bolso (1,7B ≈ 1 GB, "roda bem"), mas a frase não diz que é estimativa e o README pede "about 6 GB of RAM" na CPU; não há teste em Mac de 8 GB. Sugestão: "roda em Mac com chip Apple pelo backend MLX (estimativa pela regra de bolso; o README pede uns 6 GB de memória, então feche o resto)" |
| "clonar a voz de alguém sem autorização continua sendo problema seu" | nenhuma (não está na fonte) | opinião/aviso jurídico sem selo | Marcar **Opinião:** ou marcar ⚖️ com base legal e fonte; ou cortar |
| (omissão) se precisa de programação | README: `pip install kittenml`, Python 3.9+; há demo no navegador e API gratuita | faltando | Manual, seção 4 (Open source): dizer se precisa de programação. Ex.: "precisa de um pouco de Python; há demo no navegador" |
| Granite Speech 5.0 (IBM): transcrição e tradução abertas, Apache 2.0, com português | Blog no Hugging Face e model card ("released under an Apache 2.0 license"; PT na lista; "translates to and from English in those languages") | confirmada | — |
| versão de 2 bilhões de parâmetros, em 2º lugar entre os modelos abertos do ranking Open ASR em inglês em 21/10 | Blog, gráfico 1 ("ranks #2 among top open-weight ASR models on average English WER (5.06%)... as of 21 October 2026") | confirmada (declarada pela IBM) | O dado está no post da própria IBM; não consegui abrir o ranking ao vivo (página dinâmica). Acrescentar "segundo a IBM". "ASR" e "Open ASR" não são explicados (ex.: "ranking Open ASR, de reconhecimento de fala") |
| uma de 470 milhões para rodar no aparelho | Blog ("470M-parameter encoder built for speed"; "on-device transcription"; Turbo CTC agora com português) | confirmada | — |
| "a de 2 bilhões funciona em Mac pelo mlx-audio" | Blog ("support in Transformers, vLLM, llama.cpp, and mlx-audio for Apple Silicon") | confirmada | A fonte diz "suporte", não teste em Mac de 8 GB; pela regra de bolso (2B ≈ 1,2 GB) cabe. "mlx-audio" aparece sem explicação: "(biblioteca de áudio para Macs com chip Apple)". Faltou dizer se precisa de programação (card: Python/transformers; o de 470M tem demo no navegador) |

### Ferramentas e agentes

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| Google Cloud passou a oferecer os modelos Astra, Sol e Luna, da OpenAI | The Decoder e blog do Google Cloud, 21/10 (GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna) | confirmada | — |
| em prévia fechada para clientes empresariais | The Decoder ("private preview for select enterprise customers, with sign-ups open now"); Google ("rolling out now in private preview to select enterprise customers... use this form") | confirmada | — |
| "virou a única grande nuvem com Gemini, Claude e OpenAI no mesmo lugar" | The Decoder repete; é afirmação do próprio Google ("only hyperscale cloud provider offering access to all three leading closed source LLMs") | confirmada como afirmação do Google, não como fato apurado | Escrever "segundo o Google" |
| "na prática, quem já paga o Google testa os três na mesma conta" | contradiz as duas fontes | **errada** | Não é qualquer cliente: é prévia fechada para clientes empresariais selecionados, com formulário de interesse; sem preço divulgado. Reescrever, ex.: "na prática, só clientes empresariais escolhidos pelo Google testam por enquanto; os demais podem pedir acesso por formulário". É anúncio de acesso restrito, não disponibilidade geral |
| LiteLLM 1.107.0 saiu no PyPI com ladrão de credenciais | SafeDep ("carries a credential stealer and a remote code execution backdoor") | confirmada | — |
| na quarta (21/10), das 11h39 às 13h23 em UTC | SafeDep: 11:39 a 11:40 upload das sete rodas; 13:23 "PyPI removes 1.107.0" (2026-10-21, quarta) | confirmada | — |
| a última versão limpa é a 1.106.2 | SafeDep ("Versions 1.106.2, 1.107.0rc1, and 1.107.0rc2 are clean") | confirmada | Pode dizer "última estável limpa" (as rc1/rc2 também estão limpas) |
| quem instalou a 1.107.0 deve tratar como vazadas as chaves e senhas daquela máquina | SafeDep lista o que o ladrão coleta (chaves SSH, nuvem, CI/CD, navegador, chaves de LLM); a página não lista passos e remete ao relatório do LiteLLM | confirmada (conclusão do redator, coerente) | Opcional: a fonte diz que as **imagens Docker** (`v1.107.0`, `latest`, `main-latest`, `main-stable`) também ficaram infectadas das 11h46 às 14h20 UTC; quem usa Docker precisa saber. Dar o passo direto: "troque as chaves e volte à 1.106.2" |
| Lovable: certificações (SOC 2, ISO 27001) cobrem a plataforma, não o app | Lovable, 21/10 ("doesn't constitute an audit of your business or app") | confirmada | A página cita também AIUC-1 e GDPR; "certificações" não é explicado (certificações de segurança) |
| coleta de dados, controle de acesso, aviso de privacidade e pedidos de exclusão são do dono do app | Lovable (seção "Your responsibilities") | confirmada | — |
| controlador é quem decide sobre os dados (art. 5º, VI, da LGPD) | planalto.gov.br, Lei 13.709, conferida: "VI - controlador: pessoa natural ou jurídica, de direito público ou privado, a quem competem as decisões referentes ao tratamento de dados pessoais" | confirmada | — |
| "quem vende o app ao cliente precisa combinar quem é o quê" | não está na fonte | interpretação do redator | Aceitável, mas é leitura jurídica: marcar **Opinião:** ou citar também o art. 5º, VII (operador) |

### Regulação

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| A Comissão anunciou na segunda (19/10) que a primeira norma harmonizada do AI Act, a EN 18286:2026, saiu no Diário Oficial da UE | Comissão Europeia (publicação de 19 de outubro de 2026; "published the reference to the first harmonised standard... in the Official Journal"; Decisão de Execução (UE) 2026/2274) | confirmada | Detalhe: o que saiu no Diário Oficial foi a **referência** da norma (feita por CEN/CENELEC). "AI Act" nunca é explicado no texto (nem na lista "Nesta edição"): "a lei europeia de IA" |
| sobre sistema de gestão da qualidade | idem ("Quality management system for EU AI Act regulatory purposes") | confirmada | — |
| quem segue a norma tem presunção de cumprir o art. 17 do AI Act, que vale para sistemas de alto risco | idem; art. 17 do AI Act conferido no texto oficial: "Quality management system... Providers of high-risk AI systems shall put a quality management system in place" | confirmada com nuance | A Comissão diz presunção "with the Article 17 requirements **covered by the standard**". Escrever "os requisitos do art. 17 que a norma cobre". O link citado é a página da Comissão (cita o art. 17); como o manual pede o texto oficial para artigo, vale acrescentar o EUR-Lex (https://eur-lex.europa.eu/eli/reg/2024/1689/oj). "Norma harmonizada" e "presunção" merecem meia frase |
| "na prática, vira o checklist que o auditor vai cobrar" | não está na fonte (a norma é caminho de conformidade; a fonte não fala em auditor) | não confirmada / opinião sem selo | Marcar **Opinião:** ou trocar por fato: "na prática, é um caminho pronto para provar que o sistema de qualidade cumpre o art. 17" |
| MOFCOM e o Ministério de Ciência e Tecnologia propuseram, em 16/10, exigir licença para exportar pesos e código de modelos de fronteira | ChinaTalk e fonte primária (Anúncio nº 48/2026 do MOFCOM e MOST, de 16/10, e entrevista do porta-voz) | confirmada | Manual: para China, preferir a fonte primária. Acrescentar o link do MOFCOM: https://www.mofcom.gov.cn/zfxxgk/gkml/art/2026/art_ccd0391072a94c809ae7e820abe2536b.html . Além da proposta, o anúncio já pôs em vigor, de imediato, um **registro prévio** provisório para exportar essas tecnologias; vale uma frase |
| os que "passam de" 10²⁶ operações no treino, "de" 2 trilhões de parâmetros ou que estão entre os melhores do mundo | ChinaTalk: "≥10^26 FLOPs, ≥2T parameters, or 'global leading capability'" (nota do projeto: top 10 mundial em avaliações públicas) | confirmada com ajuste | O corte é "a partir de" (≥), não "passam de" (>). "Entre os melhores do mundo" = entre os 10 melhores em avaliações públicas, segundo a nota |
| abrir o código ganharia licença automática | ChinaTalk e perguntas e respostas do MOFCOM ("基本实现即报即出", "basicamente" imediata); tecnologia já pública fica fora | confirmada | — |
| a consulta pública vai até 15/11 | MOFCOM (16/10 a 15/11/2026) | confirmada | — |
| Nvidia US$ 2,2 mi, Anthropic US$ 2,1 mi, OpenAI US$ 1,5 mi | The Verge | confirmada | — |
| trimestre recorde de lobby entre julho e setembro | The Verge ("each had their highest-spending lobbying quarter between July and September") | confirmada | — |
| até este ano, a OpenAI nunca tinha gastado US$ 1 mi num trimestre | The Verge ("didn't even spend $1 million on lobbying in a single quarter until this year") | confirmada | — |

### IA na prática

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| Na quinta (22/10), o 1Password lançou o 1Password for Agents | Comunicado da 1Password, quinta 22/10, 9h EDT ("today announced") | confirmada | Lançamento anunciado com liberação gradual (ver itens abaixo). "1Password" nunca é apresentado como gerenciador de senhas antes do "Para testar hoje": "o 1Password, gerenciador de senhas," |
| o agente se identifica com uma chave digital própria; você aprova ou recusa no seu aparelho; o 1Password preenche direto e o agente nunca recebe a senha | Comunicado ("a unique digital key... approval happens on the person's own device... fills it directly into the sign-in form") | confirmada | — |
| você recebe um aviso com a conta que ele quer e o motivo | The Verge ("sends you a notification about which account credentials it needs, and why") | confirmada | — |
| o The Verge compara o processo com a verificação em duas etapas | The Verge ("similar process to two-factor authentication") | confirmada | — |
| "Entre os parceiros estão o Muse (Meta), o Claude Duet (Anthropic), o ChatGPT Work e o Dots (OpenAI) e o Grok Bot (mesma fonte)" | O Verge lista os nomes; as empresas (Meta, Anthropic, OpenAI) e o dono do Grok Bot (SpaceXSI) vêm do comunicado | confirmada | "mesma fonte" é o The Verge, que não dá as empresas; citar o comunicado da 1Password. Dots é produto da OpenAI (lançado em 29/09), certo. O comunicado também cita a Town |
| "A geral contou hoje do Claude Duet" | `edicoes/2026-10-22/edicao.md` (geral): Claude Duet, lançado na quarta (21), só nos EUA e com fila | confirmada | — |
| "esta é a peça que faltava para ele mexer nas suas contas sem pedir a senha" | Comunicado, fala da Anthropic: "Claude Duet asks before it signs in anywhere, and soon 1Password will complete the sign-in" | errada (contradiz o freio da própria edição) | Para o Claude Duet a integração ainda é futura ("em breve"), e o Duet em si é só EUA com fila. Trocar por "será a peça que faltava, quando chegar" |
| Muse e Grok Bot aparecem como "chegando nos próximos dias", e há lista de espera | Página de integrações ("Rolling out over the coming days across all platforms"; "Join the waitlist to be notified when your agent is ready") | confirmada, mas aspas inexistentes | A página não diz "chegando nos próximos dias". Tirar as aspas ou escrever: liberados aos poucos "nos próximos dias". Claude, ChatGPT Work e Dots aparecem sem status na página |
| a Anthropic diz que o 1Password vai completar o login no Claude Duet "em breve" | Comunicado, fala de Ami Vora, diretora de produto da Anthropic ("soon") | confirmada | Tradução entre aspas aceitável |
| "Só nos planos pessoais. O recurso vem nos planos Individual e Família. A página não fala dos planos de empresa" | Página de integrações ("included in all Individual and Family plans"; "being introduced for 1Password Individual and Families accounts") | parcialmente confirmada | O corpo está certo; o título "Só" afirma exclusividade que a fonte não afirma (e o comunicado cita uso de empresa na Town). Trocar o título por "Por enquanto, planos pessoais" |
| "O agente não vê a senha, mas vê a conta. Depois do login, ele continua a tarefa com tudo o que a conta mostra" ([The Verge]) | The Verge só diz que o agente continua a tarefa sem ver a senha. A ideia vem da FAQ da página de integrações: "An agent may be able to see information or take actions within the signed-in account... depends on the agent and the website" | errada (número/afirmação atribuída ao link errado e forte demais) | Citar a página de integrações da 1Password e suavizar: "pode ver informações e agir na conta; depende do agente e do site" |
| **Opinião:** o risco novo é aprovar no automático | opinião com selo | ok | — |
| Advogado / dono de e-commerce / corretor presentes | — | ok (advogado presente) | O dono de e-commerce "entra no banco": risco alto (dinheiro) sem aviso. Tirar o banco ou acrescentar cautela. "Acesso por certificado digital... fica fora disso" é inferência do redator, sem fonte (plausível) |
| "O cliente paga porque hoje a alternativa é mandar a senha por WhatsApp" | nenhuma | opinião/afirmação sem fonte e sem selo | Passar para dentro do selo **Opinião:** ou cortar |
| "Até agora... o jeito era dar a senha a ele" | Comunicado diz que entregar a senha "é um atalho comum" | generalização | Trocar por "o atalho comum era dar a senha" |
| ⚠️ freio de realidade, "Como isso vira serviço", "Para testar hoje" | — | presentes | "Agente" nunca é definido na primeira vez (manual, seção 3): "agente (a IA que faz tarefas por você, como entrar em contas)". Tamanho da seção: cerca de **511 palavras**, acima do teto de 500 (manual, seção 5) |

### Radar, pergunta e fecho

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| só 13% de 2.002 CIOs e líderes de tecnologia relatam retorno grande ou transformador | The Decoder ("13 percent of respondents report major or transformative returns... survey of 2,002 CIOs and other technology leaders") | confirmada | "CIOs" sem explicação (diretores de tecnologia) |
| 51% esperam que a IA aumente o custo total da área | The Decoder ("51 percent expect AI to raise total operating costs for their tech stack") | imprecisa | Escrever "o custo operacional total da sua estrutura de tecnologia" |
| mantenedores estimam que 25% dos pull requests são lixo de IA, e 31% nos projetos grandes | Linux Foundation, 20/10 ("25% of incoming PRs are estimated to be low-quality 'AI slop'... 31% among large projects") | confirmada com ajuste | A fonte não diz **quem** estima (voz passiva). Escrever "a pesquisa da Linux Foundation estima" ou "segundo a pesquisa" |
| "mesmo com a IA cortando em 52% o tempo de escrever código" | Linux Foundation ("Respondents estimate average time reductions... code authoring (52%)") | confirmada com ajuste | É estimativa dos próprios entrevistados, escrita como fato. "segundo os entrevistados, a IA corta em 52%..." (o resumo do mesmo texto fala em "até 50%") |
| Citrini usou um Claude ainda não lançado para desenhar proteínas contra veneno de escorpião | The Verge ("an unreleased version of Claude") | confirmada | — |
| 17 das 211 passaram no teste de laboratório e se ligaram a 4 das 5 toxinas | The Verge ("Seventeen of the proteins passed muster, collectively binding to four of the five scorpion toxins"; 211 designs) | confirmada | — |
| especialistas ouvidos pelo The Verge dizem que ainda está longe de um remédio | The Verge ("far from a medicine and hyped") | confirmada | — |
| Pergunta de fechamento e fecho "Até segunda." | Manual, seção 5 (quinta fecha com "Até segunda.") | ok | — |
| AI Drops, Neat Prompts ou TechDrops como fonte | busca em `edicao.md` | nenhum | — |
| Seções com Opinião e ⚖️ | — | Opinião com selo em Flint, Mercury e 1Password (parte 1 fora do escopo) | Ver os itens "sem selo" acima |

## Correções obrigatórias

1. **Kitten-TTS 2, licença:** não é Apache 2.0. Essa é a licença do código. O modelo está sob a Stellon Labs Community License (grátis para pesquisa e uso pessoal; uso comercial só abaixo de US$ 1 milhão de faturamento anual e de captação total, com registro e crédito "Powered by KittenML"). Tirar também "voz aberta" do título do front matter.
2. **Kitten-TTS 2, tamanho:** 506 MiB é só a versão reduzida; a padrão tem 947 MiB, e é a que o backend para Mac (MLX) usa. Corrigir no corpo e no título do front matter.
3. **Kitten-TTS 2, línguas:** "20 línguas" é do README, mas a documentação do mesmo repositório diz dez e o model card diz 16; atribuir ao README ou usar "mais de dez".
4. **Google Cloud:** "quem já paga o Google testa os três na mesma conta" está errado. É prévia fechada para clientes empresariais selecionados, com formulário de interesse. "Única grande nuvem" é afirmação do Google: escrever "segundo o Google".
5. **Europa:** "vira o checklist que o auditor vai cobrar" é opinião sem selo e sem fonte; marcar **Opinião:** ou trocar por fato. Presunção vale para os requisitos do art. 17 "que a norma cobre". Acrescentar "AI Act" explicado ("a lei europeia de IA").
6. **China:** "passam de" deve ser "a partir de" (≥). Acrescentar o link primário do MOFCOM (o manual pede fonte primária para a China).
7. **1Password, abertura:** "esta é a peça que faltava" contradiz o freio (a Anthropic diz "em breve"; o Duet é só EUA com fila). Reescrever no futuro.
8. **1Password, aspas e planos:** tirar as aspas de "chegando nos próximos dias" (a página diz "Rolling out over the coming days"); trocar o título "Só nos planos pessoais" por "Por enquanto, planos pessoais".
9. **1Password, "vê a conta":** a afirmação não está no The Verge. Vem da FAQ da página de integrações da 1Password e diz "pode ver informações e agir na conta; depende do agente e do site". Trocar o link e suavizar.
10. **Opinião sem selo:** (a) "clonar a voz de alguém sem autorização continua sendo problema seu" (Kitten); (b) "O cliente paga porque hoje a alternativa é mandar a senha por WhatsApp" (Como isso vira serviço). Pôr o selo **Opinião:** ou cortar.
11. **Radar:** Linux Foundation, a fonte não diz que são os mantenedores que estimam os 25%, e os 52% são estimativa dos entrevistados (escrever "segundo os entrevistados"). Gartner, 51% esperam aumento do "custo operacional total da estrutura de tecnologia", não do "custo total da área".
12. **Jargão sem explicação na primeira vez:** "AI Act", "agente", "1Password" (gerenciador de senhas), "mlx-audio", "ASR/Open ASR". "Parâmetros" também nunca é definido (primeira aparição está na parte 1, no Flint).

## Recomendadas (não obrigatórias)

- Open source: dizer se precisa de programação em Kitten-TTS e Granite (manual, seção 4).
- Kitten-TTS "roda no seu Mac": marcar como estimativa e citar a pegadinha do README (~6 GB de RAM na CPU; MLX só em chip Apple).
- Granite: "segundo a IBM" no 2º lugar do ranking.
- LiteLLM: mencionar as imagens Docker infectadas (11h46 às 14h20 UTC) e o passo direto (trocar as chaves, voltar à 1.106.2).
- IA na prática: cortar uns 15 a 20 palavras para ficar abaixo de 500; tirar "e no banco" do exemplo do e-commerce; citar o comunicado, e não o The Verge, na lista de parceiros.
- China: acrescentar que o registro prévio provisório já está em vigor.
- Lovable: o "quem vende o app precisa combinar quem é o quê" é leitura jurídica; marcar **Opinião:** ou citar o art. 5º, VII.
