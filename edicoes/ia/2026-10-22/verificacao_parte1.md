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
