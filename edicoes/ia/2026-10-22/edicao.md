---
data: 2026-10-22
tipo: regular
numero: 1
assunto: "a deepseek abriu a cozinha, mas não toda"
previa: "+ como deixar um agente entrar na conta sem dar a senha"
tempo_leitura_min: 10
dia: forte
breakthrough: false
historias:
  - id: deepseek-deepinfer
    titulo: "DeepSeek abre o DeepInfer, o motor que serve o próprio modelo"
    tema: open_source
    urls:
      - "https://github.com/deepseek-ai/DeepInfer"
      - "https://technode.com/2026/10/21/deepseek-open-sources-inference-framework-with-support-for-nvidia-and-huawei-chips/"
    em_andamento: true
  - id: dhs-deepseek-ordem
    titulo: "DHS manda tirar a DeepSeek dos sistemas das agências civis dos EUA"
    tema: regulacao
    urls: ["https://www.govinfo.gov/app/details/FR-2026-10-20/2026-21447"]
    em_andamento: true
  - id: deepseek-rodada-15-bi
    titulo: "DeepSeek levantaria cerca de US$ 15 bi, segundo a Bloomberg"
    tema: negocios_ia
    urls: ["https://techcrunch.com/2026/10/22/deepseek-reportedly-raises-15b-days-after-us-restrictions/"]
    em_andamento: true
  - id: recursive-flint
    titulo: "Recursive lança o Flint, modelo aberto de 39,8 bi de parâmetros feito com ajuda de IA"
    tema: modelos
    urls: ["https://huggingface.co/RecursiveSI/flint"]
    em_andamento: false
  - id: inception-mercury-3
    titulo: "Inception lança o Mercury 3, modelo de difusão de mais de 1.000 tokens por segundo"
    tema: modelos
    urls: ["https://www.inceptionlabs.ai/blog/introducing-mercury-3"]
    em_andamento: false
  - id: kitten-tts-2
    titulo: "Kitten-TTS 2: modelo de voz que clona com 5 segundos de áudio, com licença de uso comercial restrito"
    tema: open_source
    urls: ["https://github.com/KittenML/KittenTTS"]
    em_andamento: false
  - id: granite-speech-5
    titulo: "IBM abre o Granite Speech 5.0, de transcrição com português"
    tema: open_source
    urls: ["https://huggingface.co/blog/ibm-granite/granite-speech-5"]
    em_andamento: false
  - id: openai-google-cloud
    titulo: "Google Cloud passa a oferecer modelos da OpenAI ao lado de Gemini e Claude"
    tema: ferramentas
    urls: ["https://the-decoder.com/google-cloud-now-offers-openai-models-alongside-gemini-and-claude-becoming-the-only-major-provider-with-all-three/"]
    em_andamento: false
  - id: lovable-certificacoes-app
    titulo: "Lovable explica que as certificações dela não cobrem o app do cliente"
    tema: ferramentas
    urls: ["https://lovable.dev/blog/lovable-compliance-and-your-app"]
    em_andamento: false
  - id: ai-act-norma-en-18286
    titulo: "Sai a primeira norma harmonizada do AI Act, a EN 18286"
    tema: regulacao
    urls: ["https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal"]
    em_andamento: true
  - id: china-mofcom-exportacao-ia
    titulo: "China propõe licença para exportar pesos de modelos de fronteira"
    tema: regulacao
    urls: ["https://www.chinatalk.media/p/mofcoms-new-ai-rules"]
    em_andamento: true
  - id: 1password-agentes
    titulo: "1Password for Agents deixa o agente fazer login sem ver a senha"
    tema: agentes
    urls: ["https://1password.com/press/2026/october/1password-for-agents-trust-layer-personal-ai-agents"]
    em_andamento: true
  - id: linux-foundation-pr-lixo-ia
    titulo: "Mantenedores estimam que 25% dos pull requests são lixo de IA"
    tema: open_source
    urls: ["https://www.linuxfoundation.org/press/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop"]
    em_andamento: false
  - id: citrini-antiveneno-claude
    titulo: "Claude desenha proteínas contra veneno de escorpião, longe de um remédio"
    tema: pesquisa
    urls: ["https://www.theverge.com/ai-artificial-intelligence/1016443/anthropic-claude-citrini-vibecoding-scorpion-antivenom"]
    em_andamento: false
formatos: [o_que_mudou, modelos_novos, open_source, ferramentas, regulacao, ia_na_pratica, radar, pergunta]
---
bom dia. Na terça, a DeepSeek publicou de graça o motor que roda o próprio serviço. No mesmo dia, o governo americano mandou tirar a DeepSeek dos sistemas das agências civis federais. Código aberto e desconfiança andam juntos, e esta edição é sobre isso.

**Nesta edição:**
- A DeepSeek abriu o motor que serve o modelo dela. O que muda no preço da IA, e as três peças que ficaram em casa
- Dois modelos novos: um que roda em notebook (não no seu) e um que, segundo quem fez, escreve mil tokens por segundo
- Voz clonada que cabe no seu Mac (com licença de letra miúda) e transcrição aberta em português
- A Europa publica a primeira norma técnica da lei de IA dela, e a China quer licença para exportar modelo
- 🧠 Como deixar um agente entrar na sua conta sem entregar a senha

---

#### O QUE MUDOU DE VERDADE
## A DeepSeek abriu a cozinha. A receita veio sem três ingredientes
> **TL;DR:** a DeepSeek publicou na terça (20/10) o DeepInfer, o programa que serve o modelo dela em produção, com licença que permite uso comercial; ele já tem **19,7 mil** estrelas no GitHub, mas veio sem três peças de que um serviço completo precisa.

Todo modelo de IA tem duas contas. A de treinar, que se paga uma vez, e a de servir, que se paga a cada pergunta. Essa segunda é a **inferência**: o trabalho de rodar o modelo para gerar cada resposta.

Na terça (20/10), a DeepSeek abriu o DeepInfer, o motor de inferência que ela usa no próprio serviço, com licença Apache 2.0, que permite usar e vender em cima ([GitHub](https://github.com/deepseek-ai/DeepInfer)). Junto, saiu o deepseek-recipe, que traduz os pedidos para o formato da API dela (a porta pela qual outros programas usam o modelo) ([TechNode](https://technode.com/2026/10/21/deepseek-open-sources-inference-framework-with-support-for-nvidia-and-huawei-chips/)).

**Contexto.** A DeepSeek já abria os **pesos**, que são o modelo em si. O modelo que o motor roda agora, o DeepSeek-V4.1-Flash-1017, tem pesos abertos sob licença MIT e janela de contexto (quanto texto ele lê de uma vez) de **1 milhão** de tokens, os pedaços de palavra que o modelo lê e cobra ([Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)). O que ficava em casa era o jeito de servir barato.

**Os números.**
- **19.703** estrelas no GitHub na quinta (22/10), segundo a API do GitHub ([GitHub](https://github.com/deepseek-ai/DeepInfer)).
- No modelo Flash, a DeepSeek cobra, no horário de pico, **US$ 0,30** por milhão de tokens de entrada (sem cache) e **US$ 1,20** por milhão de saída. Fora do pico, metade. Na entrada, é menos de um quarto do preço do modelo Pro dela (**US$ 1,32**); na saída, menos de um terço (**US$ 3,96**) ([DeepSeek](https://api-docs.deepseek.com/quick_start/pricing)).
- A Latent Space estima uma margem acima de **80%** na inferência, a partir dos dados de produção que a DeepSeek divulgou e de um custo suposto de US$ 5 a 8 por placa por hora. A conta é dela, não da DeepSeek ([Latent Space](https://www.latent.space/p/ainews-deepseek-deepinfer-open-source)).

**O resto da semana.** Também na terça (20/10), o Departamento de Segurança Interna dos EUA publicou a ordem que tira das agências civis federais os produtos da DeepSeek, inclusive os de terceiros feitos com ela, e proíbe novas compras ([Federal Register, no GovInfo](https://www.govinfo.gov/app/details/FR-2026-10-20/2026-21447)). Dois dias depois, a Bloomberg noticiou que a DeepSeek estaria levantando cerca de **US$ 15 bilhões**, com a CATL e a Tencent entre os possíveis investidores. Seria o dobro da rodada de junho, de mais de **US$ 7 bi**. A empresa não comentou ([TechCrunch](https://techcrunch.com/2026/10/22/deepseek-reportedly-raises-15b-days-after-us-restrictions/)).

**Os otimistas:** a Interconnects, newsletter de Nathan Lambert sobre modelos abertos, põe o DeepInfer entre os maiores lançamentos abertos dos últimos meses e espera que os provedores adotem o motor rápido, o que empurraria para baixo o preço de servir os modelos da DeepSeek no mercado todo ([Interconnects](https://www.interconnects.ai/p/latest-open-artifacts-25-deepseek)).

**Os pessimistas:** o próprio repositório avisa que faltam três peças para um serviço completo: o cache (a memória do que o modelo já leu), a separação entre as etapas de ler e de escrever e a divisão da carga entre as máquinas. E ele só roda nas placas de processamento (GPUs) de data center mais novas da NVIDIA, da família SM100, e no chip Ascend 950, da Huawei ([GitHub](https://github.com/deepseek-ai/DeepInfer)). Os números de produção são da própria DeepSeek, sem auditoria ([Latent Space](https://www.latent.space/p/ainews-deepseek-deepinfer-open-source)).

**Por que isso importa pra você:** o motor não roda no seu Mac nem num servidor comum. Se algo chegar a você, chega de lado: a aposta da Interconnects é que mais provedores sirvam os modelos da DeepSeek, mais barato ([Interconnects](https://www.interconnects.ai/p/latest-open-artifacts-25-deepseek)).

⚖️ E isso importa para cliente. Mandar dado pessoal de cliente para um serviço que guarda dados fora do Brasil é transferência internacional, que a LGPD só permite nos casos do art. 33 ([Lei 13.709](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)). A política de privacidade da DeepSeek diz que os dados de quem usa o app, o site e a conta ficam na China ([DeepSeek](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html)). Antes de pôr dado de cliente na API dela, leia os termos da API. Rodar o mesmo modelo aberto num provedor daqui é outra conversa.

🔗 [DeepSeek no GitHub: DeepInfer](https://github.com/deepseek-ai/DeepInfer)

---

#### MODELOS NOVOS

### Flint (Recursive)
- **O que é:** um modelo aberto para programação, do tipo MoE (vários "especialistas", e só alguns trabalham em cada palavra), com **39,8 bilhões** de parâmetros (os "botões" ajustados no treino, que medem o tamanho do modelo) no total e uns **2,5 bilhões** ativos ([Hugging Face](https://huggingface.co/RecursiveSI/flint)).
- **O que mudou de verdade:** o método. A Recursive diz que um sistema interno de IA, a Eureka Machine, participou de quase todas as etapas, e que o modelo saiu em quatro meses. Segundo o laboratório, o Flint lidera os MoE abaixo de 50 bilhões de parâmetros em três testes de programação. Ninguém de fora verificou ainda ([The Decoder](https://the-decoder.com/recursive-shows-first-result-of-its-ai-driven-research-process-with-flint/)).
- **Onde usar e quanto custa:** de graça, com pesos abertos sob Apache 2.0. Roda no llama.cpp, no Ollama e no LM Studio (mesma fonte).
- **Roda no seu Mac?** Não. Comprimido para 4 bits (cada parâmetro guardado em menos espaço, com pouca perda), um modelo de quase 40 bilhões de parâmetros pede uns 24 GB de memória, pela regra de bolso. E o motor da própria Recursive para Mac pede pelo menos 48 GB ([Recursive](https://docs.recursive.com/edge/rec)).
- **Veredito:** **Opinião:** a IA que melhora a IA é promessa até alguém de fora repetir os números. O modelo aberto, esse já está aí.

### Mercury 3 (Inception)
- **O que é:** um modelo de **difusão**. Em vez de escrever uma palavra por vez, ele rascunha a resposta inteira e vai refinando, várias palavras de uma vez ([The Decoder](https://the-decoder.com/inceptions-mercury-3-diffusion-model-claims-to-beat-gpt-6-luna-and-claude-haiku-5-5-at-a-fraction-of-the-wait/)).
- **O que mudou de verdade:** a velocidade. Segundo o laboratório, são **1.068** tokens por segundo, contra uns **240** do Claude Haiku 5.5 e **130** do GPT-6 Luna na comparação dele: de 4 a 8 vezes mais rápido. Na tabela da própria Inception, ele vence 8 de 12 testes. Ainda não há teste independente (mesma fonte).
- **Onde usar e quanto custa:** saiu na segunda (19/10), pela API da Inception, OpenRouter, Baseten e Vercel. A tabela é de **US$ 0,20** por milhão de tokens de entrada e **US$ 0,70** de saída; com o desconto de lançamento, sem data para acabar, sai pela metade (**US$ 0,10** e **US$ 0,35**). Lê até 1 milhão de tokens ([Inception](https://www.inceptionlabs.ai/blog/introducing-mercury-3)).
- **Veredito:** **Opinião:** para atendimento e tarefa curta, velocidade é produto. Para trabalho que pede raciocínio longo, espere os testes de fora.

---

#### OPEN SOURCE
→ **Kitten-TTS 2**: modelo de voz de **1,7 bilhão** de parâmetros que clona uma voz com 5 a 30 segundos de áudio e fala português, entre outras línguas; o código tem licença Apache 2.0 e **16,3 mil** estrelas em 22/10 ([GitHub](https://github.com/KittenML/KittenTTS)), mas o modelo tem licença própria: uso comercial grátis só para quem fatura e captou menos de US$ 1 milhão, com registro e o crédito "Powered by KittenML" ([Hugging Face](https://huggingface.co/KittenML/kitten-tts-2/blob/main/LICENSE.md)); na prática, cabe no seu Mac pela regra de bolso.

→ **Granite Speech 5.0 (IBM)**: transcrição e tradução abertas (Apache 2.0) com português, numa versão de **2 bilhões** de parâmetros que estava em 2º lugar entre os modelos abertos do ranking Open ASR (de reconhecimento de fala) em inglês em 21/10, e numa de **470 milhões** para rodar no aparelho ([Hugging Face](https://huggingface.co/blog/ibm-granite/granite-speech-5)); na prática, a de 2 bilhões funciona em Mac com chip Apple (mesma fonte).

---

#### FERRAMENTAS E AGENTES
→ **Google Cloud**: passou a oferecer os modelos Astra, Sol e Luna, da OpenAI, em prévia fechada para clientes empresariais selecionados, e diz ser a única grande nuvem com Gemini, Claude e OpenAI no mesmo lugar ([The Decoder](https://the-decoder.com/google-cloud-now-offers-openai-models-alongside-gemini-and-claude-becoming-the-only-major-provider-with-all-three/)); na prática, por enquanto é coisa de empresa grande.

→ **Lovable** ⚖️: o construtor de apps por IA explicou que as certificações dele (SOC 2 e ISO 27001, selos de segurança da informação) cobrem a plataforma, não o app feito nela; coleta de dados, controle de acesso, aviso de privacidade e pedidos de exclusão são do dono do app ([Lovable](https://lovable.dev/blog/lovable-compliance-and-your-app)); no Brasil, quem decide sobre os dados é o controlador (art. 5º, VI, da LGPD), ou seja, quem vende o app ao cliente precisa combinar quem é o quê ([Lei 13.709](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)).

---

#### ⚖️ REGULAÇÃO
→ **Europa**: a Comissão anunciou na segunda (19/10) que saiu no Diário Oficial da UE a primeira norma técnica harmonizada do AI Act, a lei europeia de IA: a EN 18286:2026, sobre sistema de gestão da qualidade; quem segue a norma tem presunção de cumprir os requisitos do art. 17 que ela cobre, que valem para os fornecedores de sistemas de alto risco ([Comissão Europeia](https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal)); na prática, é o primeiro manual técnico de como cumprir a lei.

→ **China**: os ministérios do Comércio (MOFCOM) e de Ciência e Tecnologia propuseram, em 16/10, exigir licença para exportar pesos e código de modelos de fronteira, os que têm a partir de 10²⁶ operações de cálculo no treino ou 2 trilhões de parâmetros, ou que estão entre os melhores do mundo ([MOFCOM](https://www.mofcom.gov.cn/zfxxgk/gkml/art/2026/art_ccd0391072a94c809ae7e820abe2536b.html)); segundo a análise do ChinaTalk, abrir o código ganharia licença automática, e a consulta pública vai até 15/11 ([ChinaTalk](https://www.chinatalk.media/p/mofcoms-new-ai-rules)).

---

#### 🧠 IA NA PRÁTICA
## O agente entra. A senha fica com você
Pense no manobrista: você entrega a chave do carro, não a de casa. Até agora, para um agente de IA (um assistente que executa tarefas sozinho) entrar no seu e-mail ou no painel da loja, o jeito era dar a senha a ele, ou seja, a chave de casa.

Na quinta (22/10), o gerenciador de senhas 1Password lançou o 1Password for Agents. Quando o agente chega a uma tela de login, ele se identifica com uma chave digital própria. Você recebe no seu aparelho um aviso com a conta que ele quer e o motivo, e aprova ou recusa. Se aprovar, o 1Password preenche o login direto no formulário, e o agente nunca recebe a senha ([1Password](https://1password.com/press/2026/october/1password-for-agents-trust-layer-personal-ai-agents)). É parecido com a verificação em duas etapas, compara o The Verge ([The Verge](https://www.theverge.com/ai-artificial-intelligence/1016399/1password-ai-agent-password-sign-in)).

Entre os parceiros estão o Muse (Meta), o Claude Duet (Anthropic), o ChatGPT Work e o Dots (OpenAI) e o Grok Bot (mesma fonte). A geral contou hoje do Claude Duet; o 1Password quer ser a peça que deixa agentes assim mexerem nas suas contas sem pedir a senha.

🔗 [1Password: 1Password for Agents](https://1password.com/press/2026/october/1password-for-agents-trust-layer-personal-ai-agents)

⚠️ **Agora o freio:**
- **Ainda está chegando.** Na página das integrações, o Muse e o Grok Bot ainda estão sendo liberados "nos próximos dias", e há lista de espera ([1Password](https://1password.com/personal-ai-agent-integrations)). No comunicado, a Anthropic diz que o 1Password vai completar o login no Claude Duet "em breve" ([1Password](https://1password.com/press/2026/october/1password-for-agents-trust-layer-personal-ai-agents)).
- **Planos pessoais.** O recurso vem nos planos Individual e Família. A página não fala dos planos de empresa ([1Password](https://1password.com/personal-ai-agent-integrations)).
- **O agente não vê a senha, mas pode ver a conta.** Segundo a própria 1Password, depois do login o agente pode ver informações e agir dentro da conta, conforme o agente e o site ([1Password](https://1password.com/personal-ai-agent-integrations)). A senha fica protegida; o conteúdo, não necessariamente.
- **Opinião:** o risco novo é aprovar no automático. Se o celular apita vinte vezes por dia, ninguém lê o motivo.

**Agora aplica no mundo real:**
- **Advogado:** o agente entra no sistema de gestão do escritório para montar a agenda de prazos da semana, com aprovação a cada login. Acesso por certificado digital, como o de muitos sistemas de tribunal, não é senha de formulário e fica fora disso.
- **Dono de e-commerce:** o agente entra no painel da loja e no banco para conferir vendas e repasses, e o dono aprova cada acesso pelo celular.
- **Corretor de imóveis:** o agente atualiza os anúncios nos portais, sem a senha circular por mensagem.

**Como isso vira serviço:** implantar agente com acesso seguro em pequeno escritório. É mapear as contas que o agente pode usar, organizar o cofre de senhas, escrever a regra do que precisa de aprovação e revisar os acessos uma vez por mês. **Opinião:** o cliente paga porque hoje a alternativa é mandar a senha por WhatsApp; é um serviço pequeno e recorrente, bom para começar, não para viver só dele.

---

#### RADAR
→ **Linux Foundation**: segundo pesquisa da fundação com mantenedores e colaboradores de projetos abertos, **25%** dos pull requests (as propostas de mudança no código) que chegam são lixo gerado por IA, e **31%** nos projetos grandes, mesmo com a IA cortando em **52%** o tempo de escrever código, na estimativa dos entrevistados ([Linux Foundation](https://www.linuxfoundation.org/press/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop)).

→ **Claude e o antiveneno**: a Citrini Research usou um Claude ainda não lançado para desenhar proteínas contra veneno de escorpião; **17** das **211** passaram no teste de laboratório e se ligaram a 4 das 5 toxinas, e os especialistas ouvidos pelo The Verge dizem que isso ainda está longe de um remédio ([The Verge](https://www.theverge.com/ai-artificial-intelligence/1016443/anthropic-claude-citrini-vibecoding-scorpion-antivenom)).

---

Se um agente pudesse entrar amanhã em todas as suas contas de trabalho, qual você deixaria de fora, e por quê?

Até sexta.
