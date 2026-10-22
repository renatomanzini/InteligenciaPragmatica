# Verificação do caderno IA nº 1 (teste) — 22/10/2026

Dois checadores Sonnet em paralelo. Todas as correções obrigatórias foram aplicadas na edicao.md (ver a lista no fim de cada parte).

# Verificação, parte 1 (caderno IA, 22/10/2026, quinta)

Escopo: do bom dia e do "Nesta edição" até o fim de MODELOS NOVOS (Flint e Mercury 3), passando por O QUE MUDOU DE VERDADE.
Datas conferidas: 19/10 é segunda, 20/10 terça, 21/10 quarta, 22/10 quinta (calendário de 2026). Todos os 14 links desta parte abrem (HTTP 200). Nenhum link é AI Drops, Neat Prompts ou TechDrops.
Estrelas: `main.py github deepseek-ai/DeepInfer` deu **19.696** (primeira consulta) e **19.700** (consulta final). A edição diz 19.693: está só desatualizada, a contagem sobe. O federalregister.gov bloqueou o texto integral com CAPTCHA (não contornado); usei a API (JSON) e o HTML do GovInfo, que é a fonte citada.

## Tabela de afirmações

### Bom dia e "Nesta edição"

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| "Na terça, a DeepSeek publicou de graça o motor que roda o próprio serviço" | TechNode: lançado em 20/10; README: "powers DeepSeek's large-scale production services"; Latent Space: post da DeepSeek de 20/10 | confirmada | nenhuma |
| "No mesmo dia, o governo americano mandou tirar a DeepSeek dos computadores federais" | Federal Register 2026-21447, publicado 20/10: ordem vale para **agências civis** (federal civilian executive branch) | errada (alcance) | "computadores federais" é amplo demais. Trocar por "dos sistemas das agências civis federais" |
| "Código aberto e desconfiança andam juntos, e esta edição é sobre isso" | tese do redator | opinião sem selo | baixa gravidade; ou cortar a tese, ou marcar como **Opinião:** |
| Bullet: "um que escreve mil tokens por segundo" | Inception/The Decoder: 1.068 tokens/s é número do laboratório ("In Inception's internal benchmarks") | não confirmada como fato; falta atribuição | "...que, segundo a Inception, escreve mil tokens por segundo". Idem no título da história no front matter (só metadado) |
| Bullet: "um que roda em notebook (não no seu)" | Recursive: >125 tokens/s num MacBook Pro com M4 Pro; docs.recursive.com/edge/rec: exige 48 GB | confirmada | nenhuma |
| Bullet: "as três peças que ficaram em casa" | README do DeepInfer: KV cache, desagregação prefill/decode e balanceamento de carga "not included" | confirmada | nenhuma |

### O QUE MUDOU DE VERDADE

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| TL;DR: publicou na terça (20/10) o DeepInfer; licença que permite uso comercial; 19,7 mil estrelas; veio sem três peças | GitHub (README, Apache-2.0, 19,7k); TechNode (20/10) | confirmada | nenhuma |
| "abriu o DeepInfer, o motor de inferência que ela usa no próprio serviço, com licença Apache 2.0, que permite usar e vender em cima" | GitHub: "Apache-2.0 license"; "powers DeepSeek's large-scale production services" | confirmada | nenhuma |
| "Junto, saiu o deepseek-recipe, que traduz os pedidos para o formato da API dela" | TechNode: converte requisições de API e trata entrada/saída do modelo "in line with DeepSeek's own service"; model card no HF: converte Messages/Chat Completions/Responses em prompt do modelo e interpreta a saída | confirmada, imprecisa | recomendado: "que converte os pedidos de API no formato que o modelo lê e interpreta as respostas" |
| "O modelo que o motor roda agora, o DeepSeek-V4.1-Flash-1017, tem pesos abertos sob licença MIT e janela de contexto de 1 milhão de tokens" | Hugging Face: "License: mit", "context_window 1M tokens"; README: "Supported models: DeepSeek-V4.1-Flash" | confirmada | nenhuma |
| "O que ficava em casa era o jeito de servir barato" | Interconnects: "likely far more efficient than vLLM/SGLang". Latent Space (citado): a equipe do vLLM reproduziu a vazão de decodificação "within 6%" do DeepInfer no GB200 | confirmada em parte; omite contraponto | recomendado: "o jeito de servir mais barato, segundo a Interconnects" e citar o dado do vLLM (a Latent Space traz) |
| A Interconnects é "newsletter de Nathan Lambert sobre modelos abertos" e "põe o DeepInfer entre os maiores lançamentos abertos de IA dos últimos meses, mesmo sem ser um modelo" | Interconnects (autores: Nathan Lambert e Florian Brand, 20/10): "one of the bigger open-source AI artifacts in the last few months" | confirmada | nenhuma |
| "19.693 estrelas no GitHub na quinta (22/10), segundo a API do GitHub" | `main.py github`: 19.696 e depois 19.700 em 22/10 | confirmada (desatualizada) | recomendado: rodar de novo antes de enviar e pôr o valor atual |
| "no horário de pico, US$ 0,30 por milhão de tokens de entrada e US$ 1,20 por milhão de saída. Fora do pico, metade" | api-docs.deepseek.com (HTML bruto): `deepseek-flash`, pico: entrada **sem cache** $0,30, saída $1,20; fora do pico $0,15 e $0,60. Entrada **com cache**: $0,006 (pico). O `deepseek-v4-pro` custa $1,32 e $3,96 | confirmada, sem qualificadores | dizer "no modelo Flash" e "entrada sem cache" (com cache é muito mais barato). Sem isso o leitor não sabe a que preço se refere |
| "O GPT-6 Luna e o Claude Haiku 5.5 cobram US$ 0,50 por milhão de tokens de **entrada** em textos curtos, segundo o The Decoder" | The Decoder: "Mercury 3 would cost more **for output** than GPT-6 Luna and Claude Haiku 5.5, at least for shorter inputs, where both charge $0.50". OpenAI (developers.openai.com/api/docs/pricing): gpt-6-luna **$0,10 entrada / $0,50 saída**. Anthropic (platform.claude.com pricing): Haiku 5.5 **$0,10 entrada / $0,50 saída** (prompts até 100 mil tokens). OpenRouter idem | **errada** | US$ 0,50 é o preço de **saída**; entrada é **US$ 0,10**. Corrigir para "cobram US$ 0,10 por milhão de entrada e US$ 0,50 de saída, em textos curtos". Cuidado com a comparação: com o número certo, o Flash da DeepSeek (US$ 0,30 e 1,20 no pico) fica mais caro que esses dois modelos pequenos; deixar claro que são faixas diferentes de modelo |
| "A Latent Space estima uma margem acima de 80% sobre esse preço, a partir dos dados de produção que a DeepSeek divulgou. A conta é dela, com custos supostos" | Latent Space: ">80% inference margin" calculada sobre o preço **fora do pico** (US$ 0,15/0,60), com custo "all-in" suposto de US$ 5-8 por placa por hora | confirmada em parte (preço errado) | "esse preço" aponta para o preço de pico (US$ 0,30/1,20). Trocar por "sobre o preço fora do pico (US$ 0,15 e US$ 0,60)". O resto (conta da Latent Space, custos supostos) está certo |
| "Também na terça (20/10), o Departamento de Segurança Interna dos EUA publicou a ordem que tira das agências civis federais os produtos da DeepSeek, inclusive os de terceiros feitos com ela, e proíbe novas compras" | Federal Register 2026-21447 (GovInfo e API): aviso publicado em 20/10; exclui produtos da DeepSeek e afiliadas das **compras** das agências civis e **remove** os produtos e os "third-party products and services developed using DeepSeek implementations" | confirmada | recomendado: "publicou o aviso da ordem" (o texto assinado vai em anexo, só em imagem). A data de assinatura da ordem não aparece no texto |
| "Dois dias depois, a Bloomberg noticiou que a DeepSeek levanta cerca de US$ 15 bilhões, com a CATL e a Tencent entre os possíveis investidores" | TechCrunch (22/10): "about $15 billion... Bloomberg reported"; "Just two days after" a ordem; CATL e Tencent citadas | confirmada | nenhuma |
| "É o dobro da rodada de junho, de mais de US$ 7 bi" | TechCrunch: "more than $7 billion" em junho | confirmada em parte | recomendado: "cerca do dobro" (15 contra "mais de 7" não é exatamente o dobro) |
| "A empresa não comentou" | TechCrunch: "did not immediately respond to a TechCrunch request for comment" | confirmada em parte | recomendado: "não respondeu de imediato ao pedido de comentário" |
| Otimistas: "a Interconnects espera que os provedores adotem o motor rápido, o que empurraria para baixo o preço de servir os modelos da DeepSeek no mercado todo" | Interconnects: "Inference companies will be quick to adopt these tools, which will drive prices for DeepSeek's models down" | confirmada | nenhuma |
| Pessimistas: faltam cache, separação das etapas e divisão da carga; só roda em GPUs NVIDIA SM100 e no Ascend 950 | README: "Required for a complete inference service (not included in this release)" e "Supported hardware: NVIDIA SM100 GPUs, Huawei Ascend 950 NPUs"; Linux e CUDA 13 | confirmada | nenhuma |
| "Os números de produção são da própria DeepSeek, sem auditoria" | Latent Space: "first-party production claims, not independently audited" | confirmada | nenhuma |
| "Por que isso importa pra você: o motor não roda no seu Mac nem num servidor comum. O efeito chega de lado: mais empresas servindo o modelo da DeepSeek, mais barato e fora da China" | A primeira frase bate com o README (Linux, SM100/Ascend). A segunda é previsão: é a expectativa da Interconnects; a própria pauta diz que "o efeito no preço é uma aposta, não um fato" | previsão sem selo | pelo MANUAL_DE_REDACAO 14.6, previsão leva "a aposta é" e quem aposta. Ex.: "A aposta da Interconnects é que mais empresas passem a servir o modelo da DeepSeek, mais barato e fora da China" |
| ⚖️ "A política de privacidade da DeepSeek diz que ela guarda os dados pessoais na China" | cdn.deepseek.com política (atualizada em 10/02/2026): "we directly collect, process and store your Personal Data in People's Republic of China" | confirmada (para apps, sites e serviços dela) | ver a linha seguinte |
| ⚖️ "Mandar dado pessoal de cliente para a API dela é transferência internacional, que a LGPD só permite nos casos do art. 33" | LGPD art. 33 (planalto.gov.br): "A transferência internacional de dados pessoais somente é permitida nos seguintes casos" (confirmado). Mas a própria política da DeepSeek e os termos da Open Platform (item 5.5) dizem que **não cobrem** os dados dos usuários finais de apps feitos sobre a API, e que o desenvolvedor é o controlador. A política não diz onde ficam os dados enviados pela API | não confirmada (a premissa não cobre o caso) | reescrever sem afirmar o local de armazenamento da API. Ex.: "A política diz que os dados de quem usa o app, o site e a conta ficam na China. Ela própria avisa que não cobre os dados dos clientes de quem constrói um app sobre a API, e não diz onde eles ficam. Se esses dados forem para servidores na China, é transferência internacional, que a LGPD só permite nos casos do art. 33". O art. 33 e o link do Planalto estão corretos |
| "Todo modelo de IA tem duas contas. A de treinar, que se paga uma vez, e a de servir..." | sem fonte (explicação de fundo) | não confirmada | baixa gravidade; "se paga uma vez" simplifica (retreino existe). Sugestão: "A de treinar, que é um custo grande e concentrado" |

### MODELOS NOVOS, Flint (Recursive)

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| Modelo aberto para programação, MoE, **39,8 bi** de parâmetros no total e uns **2,5 bi** ativos | Hugging Face: "39.8 billion total parameters and approximately 2.5 billion active per token" | confirmada | nenhuma |
| "A Recursive diz que um sistema interno de IA, a Eureka Machine, participou de quase todas as etapas" | The Decoder: "involved in nearly every step"; blog da Recursive: "nearly every part of Flint's model-building stack" | confirmada | nenhuma |
| "e que o modelo saiu em quatro meses" | The Decoder (citado): "built in four months". Blog da Recursive (primária): "**under** four months" | confirmada pela fonte citada; a primária é mais precisa | recomendado: "em menos de quatro meses" |
| "Segundo o laboratório, o Flint lidera os MoE abaixo de 50 bi em três testes de programação. Ninguém de fora verificou ainda" | The Decoder: "Recursive claims Flint leads... SWE-Bench Pro v2, Terminal-Bench 2.1 e SWE-Bench Verified among MoE models with fewer than 50 billion parameters. The results haven't been independently verified yet" | confirmada (tem "segundo o laboratório") | nenhuma |
| "De graça, com pesos abertos sob Apache 2.0" | HF: "License: apache-2.0"; The Decoder | confirmada | nenhuma |
| "Roda no llama.cpp, no Ollama e no LM Studio (mesma fonte)" | The Decoder: "llama.cpp, Ollama, LM Studio, vLLM, and SGLang" | confirmada | nenhuma |
| "Roda no seu Mac? Não. Em 4 bits, quase 40 bi de parâmetros pedem uns 24 GB (estimativa pela regra de bolso)" | Regra do MANUAL_IA seção 4: 39,8 x 0,6 = 23,9 GB; MoE conta o total; acima de ~9B "não roda" | confirmada (usa a regra como estimativa, sem contradizê-la) | nenhuma |
| "o teste de velocidade da Recursive foi num **MacBook Pro de 48 GB** (mesma fonte)" | The Decoder: "MacBook Pro with M4 Pro", sem memória. Blog da Recursive: "M4 Pro MacBook Pro", sem memória. A Recursive só diz que o `rec` (motor dela para Mac) **exige M4 Pro, M5 Pro ou M5 Max com pelo menos 48 GB** de memória unificada (docs.recursive.com/edge/rec) | **não confirmada** | o "48 GB" não está na fonte citada. Trocar por: "o teste de velocidade da Recursive foi num MacBook Pro com chip M4 Pro, e o motor dela para Mac (o rec) exige pelo menos 48 GB de memória ([Recursive](https://docs.recursive.com/edge/rec))". O veredito "Não" continua certo |
| Veredito (**Opinião:**) | selo presente | confirmada | nenhuma |
| Jargão: "parâmetros" (primeira vez no corpo) e "4 bits" | nenhuma explicação no corpo; o MANUAL_IA seção 3 lista "parâmetro" e "quantização" | falta explicação | ver correções obrigatórias |

### MODELOS NOVOS, Mercury 3 (Inception)

| Afirmação | Fonte | Status | Correção |
|---|---|---|---|
| Modelo de difusão: "rascunha a resposta inteira e vai refinando, várias palavras de uma vez" | The Decoder: "refines a rough draft of the whole answer step by step... generating many words at once" | confirmada | nenhuma |
| "Segundo o laboratório, **1.068** tokens por segundo, contra uns **240** do Claude Haiku 5.5 e **130** do GPT-6 Luna na comparação dele: de 4 a 8 vezes mais rápido" | The Decoder: "According to Inception, 1,068 tokens per second... Haiku 5.5 about 240 and GPT-6 Luna about 130"; "four to eight times faster" (1068/240 = 4,5; 1068/130 = 8,2); blog da Inception: "1,068 tokens per second on NVIDIA GPUs" | confirmada | nenhuma |
| "Na tabela da própria Inception, ele vence 8 de 12 testes. Ainda não há teste independente" | The Decoder: "wins eight of 12 tests" (os três em configuração média), "No independent tests exist yet" | confirmada | nenhuma |
| "saiu na segunda (19/10), pela API da Inception, OpenRouter, Baseten e Vercel" | Blog da Inception, 19/10/2026: "available today on the Inception API Platform and through OpenRouter, Baseten, and Vercel" | confirmada | nenhuma |
| "Custa **US$ 0,20** por milhão de tokens de entrada e **US$ 0,70** de saída, com 50% de desconto no lançamento, e lê até 1 milhão de tokens" | Inception: preço de tabela $0,20 / $0,70; **no lançamento, 50% off: $0,10 e $0,35** (OpenRouter lista $0,10 / $0,35); contexto 1M. The Decoder: a Inception não disse quando o desconto acaba | confirmada, mas ambígua | do jeito que está, dá para entender que US$ 0,20 e 0,70 já são o preço com desconto. Reescrever: "Preço de tabela: US$ 0,20 de entrada e US$ 0,70 de saída; no lançamento, com 50% de desconto, sai por US$ 0,10 e US$ 0,35, sem data para acabar" |
| Veredito (**Opinião:**) | selo presente | confirmada | nenhuma |

## Checagens de regra do MANUAL_IA

- Benchmark do laboratório com "segundo o laboratório": ok no corpo (Flint, Mercury). Falha só no bullet de "Nesta edição" (linha acima).
- Comparação entre benchmarks medidos de jeitos diferentes: não há. A comparação de preço entre DeepSeek e Luna/Haiku mistura faixas de modelo (ver correção).
- Anúncio sem produto disponível tratado como lançamento: não há. DeepInfer tem código aberto, mas a edição diz o que falta; Flint e Mercury 3 estão disponíveis.
- "Roda no seu Mac?": Flint segue a regra de bolso (seção 4); só o "48 GB" está sem fonte.
- Lei: só o art. 33 da LGPD, confirmado, com link do planalto.gov.br. Nada de tramitação nesta parte. (O art. 5º, VI, da LGPD, citado no item do Lovable, fora do meu escopo, também confere: "controlador".)
- Opinião: os dois vereditos têm o selo. Falta selo ou "a aposta é" em "Por que isso importa pra você" e, de leve, no bom dia.
- Aspas inexistentes: não há aspas nesta parte.
- Número atribuído ao link errado: o US$ 0,50 (Luna/Haiku) e o "48 GB" (Flint). Os demais batem com o link citado.
- AI Drops, Neat Prompts ou TechDrops como fonte: nenhum.

## Correções obrigatórias

1. **Preço de Luna e Haiku (O QUE MUDOU, "Os números").** US$ 0,50 é preço de **saída**; a entrada é **US$ 0,10** (OpenAI, Anthropic, OpenRouter, e o The Decoder fala de "output"). Reescrever a frase e a comparação com a DeepSeek.
2. **Preço da DeepSeek.** Dizer "modelo Flash" e "entrada sem cache" (com cache custa US$ 0,006 no pico; o Pro custa US$ 1,32 e 3,96).
3. **Margem de 80% (Latent Space).** Foi calculada sobre o preço fora do pico (US$ 0,15 e 0,60), não sobre o de pico que a frase anterior cita. Trocar "sobre esse preço".
4. **LGPD e API (⚖️).** A política da DeepSeek diz que ela guarda na China os dados de quem usa o app, o site e a conta, e avisa que não cobre os dados dos clientes finais de apps feitos sobre a API. A frase "Mandar dado pessoal de cliente para a API dela é transferência internacional" não tem premissa confirmada. Reescrever como no quadro acima. O art. 33 e o link estão certos.
5. **Flint, "MacBook Pro de 48 GB (mesma fonte)".** O 48 GB não está no The Decoder nem no blog. Usar: teste num MacBook Pro com M4 Pro; o `rec` exige pelo menos 48 GB (https://docs.recursive.com/edge/rec). Veredito "Não" mantido.
6. **Mercury 3, preço.** Separar preço de tabela (US$ 0,20 e 0,70) do preço de lançamento com 50% de desconto (US$ 0,10 e 0,35).
7. **Bom dia.** "dos computadores federais" para "dos sistemas das agências civis federais" (a ordem não vale para Defesa e militares).
8. **Previsão sem selo.** Em "Por que isso importa pra você", a frase "mais empresas servindo o modelo da DeepSeek, mais barato e fora da China" vira "a aposta da Interconnects é que...".
9. **Jargão não explicado na primeira vez** (checklist do MANUAL_IA): **tokens** (aparece já no "Nesta edição" e no Contexto), **parâmetros** (Flint) e **4 bits** (quantização). Explicar em meia frase. Recomendo também "API", "GPU" e "SM100" (ex.: "chips de IA de data center da NVIDIA").
10. **"Nesta edição".** "um que escreve mil tokens por segundo" precisa de "segundo a Inception".

## Recomendadas (não bloqueiam)

- Flint: "em menos de quatro meses" (fonte primária).
- Atualizar as estrelas para o valor do dia do envio (19.700 em 22/10, depois da última consulta).
- "deepseek-recipe": "converte os pedidos de API no formato que o modelo lê".
- "O que ficava em casa era o jeito de servir barato": atribuir à Interconnects e citar o dado do vLLM (decodificação "within 6%" no GB200, na própria Latent Space).
- "É o dobro" para "cerca do dobro"; "A empresa não comentou" para "não respondeu de imediato".
- "publicou a ordem" para "publicou o aviso da ordem".
- "Código aberto e desconfiança andam juntos": marcar como **Opinião:** ou cortar.
- MIT: a edição só explica a Apache 2.0; vale meia frase dizendo que a MIT também permite uso comercial.
- Fora do meu escopo, mas à vista: o corpo todo tem ~2.280 palavras e `tempo_leitura_min: 10`, acima do alvo do MANUAL_IA (1.300 a 2.000 palavras; 6 a 9 minutos), e o IA na prática passa de 500 palavras.

---

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
