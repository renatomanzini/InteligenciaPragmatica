---
data: 2026-10-17
tipo: sabado
numero: 2
assunto: "abriram a caixa-preta (e ela ficou barata)"
previa: "+ a OAB processa uma IA, e a Meta recua"
tempo_leitura_min: 7
dia: forte
breakthrough: true
historias:
  - id: descompilacao-ia
    titulo: "IA passa a descompilar jogos e programas em dias; decomp.dev desativa seu índice"
    tema: ia
    urls: ["https://popcar.bearblog.dev/ai-is-mass-decompiling-games-thats-both-awesome-and-scary/", "https://decomp.dev", "https://github.com/morluto/rea"]
    em_andamento: true
  - id: claude-haiku-5-5
    titulo: "Claude Haiku 5.5 fica ~75% mais barato na média que o Haiku 4.5"
    tema: ia
    urls: ["https://www.anthropic.com/news/claude-haiku-5-5"]
    em_andamento: false
  - id: gemini-4-argon
    titulo: "Google lança o Gemini 4 Argon, só em planos pagos"
    tema: ia
    urls: ["https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/"]
    em_andamento: false
  - id: meta-termos-comerciais-crawling
    titulo: "Meta tira 'treinar' da versão em inglês dos termos; robô segue autorizado para anúncios"
    tema: direito_tech
    urls: ["https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites"]
    em_andamento: true
  - id: agentes-bloqueados-sites
    titulo: "Sites e bancos começam a barrar agentes de IA"
    tema: ia
    urls: ["https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web"]
    em_andamento: true
  - id: fim-escala-6x1
    titulo: "EC 141: 42h a partir de 2 meses da publicação (16/12) e 40h um ano depois"
    tema: economia
    urls: ["https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc141.htm"]
    em_andamento: true
  - id: anthropic-receita-ipo
    titulo: "Anthropic diz a investidores que faturou US$ 16,8 bi no 3º trimestre"
    tema: negocios
    urls: ["https://www.dealstreetasia.com/?p=498196", "https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/"]
    em_andamento: true
  - id: xbow-chrome-exploit
    titulo: "XBOW monta exploit completo do Chrome com IA em 6 dias e leva US$ 250 mil"
    tema: ia
    urls: ["https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit"]
    em_andamento: false
  - id: openclaw-estrelas
    titulo: "OpenClaw estaciona perto de 392 mil estrelas"
    tema: ia
    urls: ["https://github.com/openclaw/openclaw"]
    em_andamento: false
  - id: enter-oab-sp
    titulo: "OAB-SP move ação civil pública contra a legaltech Enter"
    tema: direito_tech
    urls: ["https://www.oabsp.org.br/jornaldaadvocacia/26-10-07-1742-oab-sp-aciona-justica-contra-empresa-de-ia-para-estabelecer-limites-a-automacao-e-proteger-atividades-privativas-da-advocacia"]
    em_andamento: true
  - id: sullivan-cromwell-agreement-analyzer
    titulo: "Sullivan & Cromwell cria revisor de contratos com agentes que se contestam"
    tema: direito_tech
    urls: ["https://openai.com/index/sullivan-cromwell/"]
    em_andamento: false
formatos: [semana_em_revista, breakthroughs, historias_em_andamento, numeros, ia_na_pratica, links, pergunta]
---
bom dia. Foi a semana em que abrir jogos e programas fechados ficou coisa de dias. E duas notícias da semana passada seguem rendendo: usar IA ficou bem mais barato, e a OAB-SP foi à Justiça para dizer até onde a IA pode ir.

---

#### 🚨 OS BREAKTHROUGHS DA SEMANA

## 1. Abrir a caixa-preta virou trabalho de dias
> **TL;DR:** agentes de IA estão descompilando jogos e programas em dias. Antes, eram anos de trabalho de comunidade.

Descompilar é pegar um programa pronto, sem o código-fonte, e reconstruir como ele foi escrito. Quem fazia isso eram especialistas ou comunidades inteiras, ao longo de anos.

Na quarta (14), o desenvolvedor indie Popcar listou o que mudou. Com IA, saíram versões novas de **The Binding of Isaac** (a versão original, em Flash, agora em 1440p), **Colin McRae Rally 2.0** e **Final Fantasy Tactics Advance**, entre outros. O do Isaac levou alguns dias, segundo ele. Ele mesmo admite que o código não sai tão limpo quanto o feito à mão. O título do texto já diz tudo: "awesome and scary" (incrível e assustador) ([Popcar](https://popcar.bearblog.dev/ai-is-mass-decompiling-games-thats-both-awesome-and-scary/); [Simon Willison](https://simonwillison.net/2026/Oct/14/ai-is-mass-decompiling-games/)).

No dia seguinte veio o sinal mais forte. O **decomp.dev**, índice e placar dos projetos dessa comunidade, anunciou que está encerrando: o índice e a entrada de projetos novos foram desativados, e o que existe fica no ar como arquivo. Segundo o site, o lado comunitário do trabalho foi quebrado por quem usa IA para tomar e portar projetos alheios ([decomp.dev](https://decomp.dev); [404 Media](https://404media.co/video-game-reverse-engineering-community-shuts-down-because-ai-has-made-it-too-easy)).

Um exemplo de ferramenta do tipo é o **REA**, que liga o agente de IA a programas de inspeção como o Ghidra e roda na máquina do usuário. Tem **mais de 308 mil estrelas** no GitHub, mas não é novidade da semana: o repositório existe desde **abril** ([GitHub](https://github.com/morluto/rea)).

🚨 **Por que é breakthrough:** o tempo para entender por dentro um programa que não é seu despencou de anos de especialista para dias de agente.

⚖️ **E é legal?** O Popcar afirma que descompilar é "completamente legal". No Brasil, não é tão simples:
- a Lei do Software (Lei 9.609/98) não fala em descompilação nem em engenharia reversa;
- ela põe o software sob o regime do direito autoral (art. 2º);
- as exceções do art. 6º não citam a descompilação, e a mais próxima, a "integração" do inciso IV, vale só para uso exclusivo de quem a fez;
- violar o direito do autor de programa é crime (art. 12).

A lei, portanto, não resolve a questão ([Planalto](https://www.planalto.gov.br/ccivil_03/leis/l9609.htm)). **Opinião:** na prática, a resposta tende a depender da licença do software e da finalidade. O próprio REA avisa que é para software que você possui ou está autorizado a examinar ([REA](https://github.com/morluto/rea)).

## 2. A IA pequena ficou 4 vezes mais barata
> **TL;DR:** o Claude Haiku 5.5 custa, na média, cerca de 75% menos que o Haiku 4.5 e acerta bem mais em tarefas de computador.

Saiu em 7/10, antes desta newsletter existir, por isso entra aqui. A preço de tabela, são **US$ 0,10** por milhão de tokens de entrada (em prompts de até 100 mil tokens), contra **US$ 1,00** no modelo anterior, um corte de 90% ([preços](https://platform.claude.com/docs/en/about-claude/pricing)). Mas o modelo novo conta o mesmo texto em cerca de 30% mais tokens ([guia](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide)), e prompts longos custam mais. Por isso a própria Anthropic fala em ~**75%** de economia média ([Anthropic](https://www.anthropic.com/news/claude-haiku-5-5)).

Em escala: resumir **1.000 contratos** (5 mil tokens de entrada e 500 de saída cada) sai por **US$ 7,50** no modelo antigo e cerca de **US$ 1** no novo, já contando os 30% de tokens a mais (conta nossa, com os preços oficiais). Num teste de uso de computador (OSWorld 2.1), ele foi de **15,7%** para **72,4%** de acerto. Os números são da Anthropic.

🚨 **Por que é breakthrough:** automatizar tarefa simples e repetitiva, como triar, resumir ou classificar, ficou barato o bastante para caber no orçamento de um escritório pequeno.

*Transparência: esta newsletter é escrita com modelos da Anthropic.*

**Não passou no critério:** o **Gemini 4 Argon**, do Google (13/10). Ele só está nos planos pagos, a partir de **R$ 96,99/mês**. Na API, custa US$ 2 de entrada e US$ 10 de saída por milhão de tokens até 30/11 e depois dobra, para US$ 4 e US$ 20. O Gemini 3.1 Pro custa US$ 2 e US$ 12 ([Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/); [planos](https://gemini.google/subscriptions/); [preços](https://ai.google.dev/gemini-api/docs/pricing)).

---

#### O QUE MUDOU DESDE ONTEM

→ **Meta**: depois da reação, tirou da versão em inglês dos novos termos a frase que, segundo especialistas, poderia permitir usar o conteúdo dos sites para "treinar" produtos. O robô continua autorizado nos sites de clientes comerciais, agora para "desenvolver, melhorar, pesquisar e manter" produtos de anúncio e negócio. Até a noite de sábado, a versão em português ainda trazia o texto antigo. A Meta diz que "não é sobre raspar sites de notícia" ([The Verge](https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites); [termos](https://www.facebook.com/legal/commercial_terms_preview)).

→ **Agentes barrados**: a Delta impede agentes de comprar passagens, o JPMorgan e a Schwab bloqueiam agentes nas contas, e o Yelp só libera quem paga pela licença de dados ([The Verge](https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web)). Ontem falamos de agente invadindo sistema. Hoje o movimento é o contrário: os sites trancando a porta.

→ **6x1, com correção**: ontem escrevemos que a jornada de 42h valeria "em 60 dias". A emenda diz **2 meses após a publicação** (16/10), e esse prazo termina em **16/12/2026** (conta nossa; há quem conte a partir de 17/12). As 40h vêm um ano depois ([EC 141](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc141.htm)). Na Câmara, Hugo Motta mandou aplicar a escala nova a ~1.700 terceirizados a partir da próxima semana ([Câmara](https://www.camara.leg.br/noticias/1311899-motta-determina-adocao-imediata-da-nova-escala-de-trabalho-na-camara-dos-deputados)).

---

#### 📊 OS NÚMEROS DA SEMANA

→ **US$ 16,8 bilhões**: a receita da Anthropic no 3º trimestre, cerca de **45%** acima do anterior, segundo um investidor que estava na apresentação da empresa ([Reuters](https://www.dealstreetasia.com/?p=498196); [Simon Willison](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/)). A empresa não divulgou os números. Segundo a Bloomberg, a oferta do IPO pode começar na semana de 9/11 ([The Next Web](https://thenextweb.com/news/anthropic-q3-revenue-16-8bn-ipo)).

→ **US$ 40 mil**: foi o gasto em IA da empresa de segurança XBOW para montar, em **6 dias**, um ataque completo ao Chrome. Era a segunda tentativa: a primeira levou 2 meses e foi descartada. Segundo a XBOW, o Google concedeu **US$ 250 mil** de recompensa, e a falha já foi corrigida ([XBOW](https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit)). A empresa estima que, sem IA, seriam 4 pessoas por 6 a 9 meses ([relato técnico](https://xbow.com/labs/research/zero-to-calc-in-six-days-inside-xbow-chrome-full-chain)).

→ **392 mil**: são as estrelas do OpenClaw, o agente pessoal de código aberto. Parece explosão, mas eram 388 mil no fim de agosto ([GitHub](https://github.com/openclaw/openclaw); [GitHub Blog](https://github.blog/open-source/maintainers/openclaw-went-viral-meet-the-maintainers-building-and-securing-it/)). **Opinião:** o hype também estaciona.

---

#### 🧠 IA NA PRÁTICA DA SEMANA
## Duas IAs jurídicas, dois destinos
A diferença entre ferramenta e substituto do advogado parece filosofia. Desde o dia 7, ela virou processo.

**Nos EUA**, o escritório Sullivan & Cromwell criou com a OpenAI o **Agreement Analyzer**, apresentado em 17/09. O advogado põe a minuta, os precedentes e o "playbook" do escritório. Pela descrição do sócio John Savva, agentes revisam por ângulos diferentes, e outros agentes **contestam** os achados. A saída é um memorando com alterações em controle de alterações, que o advogado revisa, adapta ou rejeita ([OpenAI](https://openai.com/index/sullivan-cromwell/); [Bloomberg Law](https://news.bloomberglaw.com/tech-and-telecom-law/sullivan-cromwells-openai-gambit-delivers-tech-talent-access)).

**Em São Paulo**, a OAB-SP entrou em 07/10 com uma ação civil pública contra a legaltech **Enter** (processo nº 5031169-20.2026.4.03.6100). A tese é que a plataforma pratica atos privativos da advocacia sem ser sociedade de advogados. Os pedidos:
- em caráter de urgência, que novos contratos tenham advogado responsável identificado, sob multa de **R$ 50 mil** por contrato;
- supervisão humana auditável;
- **R$ 1 milhão** de dano moral coletivo.

A Enter nega que substitua advogados e diz que a revisão, a assinatura e o protocolo ficam com eles. Não encontramos decisão até 17/10 ([OAB-SP](https://www.oabsp.org.br/jornaldaadvocacia/26-10-07-1742-oab-sp-aciona-justica-contra-empresa-de-ia-para-estabelecer-limites-a-automacao-e-proteger-atividades-privativas-da-advocacia); [Lawletter](https://lawletter.com.br/exclusiva/oab-sp-acao-civil-publica-enter-inteligencia-artificial); [Startups](https://startups.com.br/negocios/legaltech/oab-sp-entra-com-acao-contra-a-enter-e-pede-r-1m-por-dano-moral/)).

⚖️ A ideia de "ato privativo" vem do Estatuto da Advocacia: são privativas da advocacia a postulação ao Judiciário e a consultoria, a assessoria e a direção jurídicas (Lei 8.906/94, art. 1º) ([Planalto](https://www.planalto.gov.br/ccivil_03/leis/l8906.htm)).

⚠️ **O freio:**
- O caso americano é um estudo de caso publicado pela própria OpenAI e não traz **nenhum** número de desempenho.
- O brasileiro ainda não tem decisão.
- A fronteira entre ferramenta e substituto não foi julgada.

**Agora aplica no mundo real:**
- **Advogado:** a ideia de "agente que contesta o outro" funciona até sem software próprio. Peça a revisão a uma IA e, depois, peça a outra que ataque essa revisão.
- **Estudante de Direito:** use a IA como parte contrária. Peça que ela derrube a sua peça antes do professor.
- **Quem cria legaltech:** **Opinião:** os pedidos da OAB-SP funcionam como um checklist de produto: advogado responsável identificado, registro de revisão e nada de vender como "substituto".

**Como isso vira serviço:** montar, para escritórios pequenos, o "playbook" de cláusulas e um fluxo de revisão com IA em que o advogado assina e fica registrado. **Opinião:** depois da ação da OAB-SP, a parte de conformidade, com a trilha de quem revisou o quê, vale tanto quanto a IA.

---

**Para ler no fim de semana:**
- [Para ler] [O texto do Popcar](https://popcar.bearblog.dev/ai-is-mass-decompiling-games-thats-both-awesome-and-scary/) sobre a descompilação de jogos, em inglês, com os dois lados.
- [Curiosidade] [Um rim de porco "congelado" por mais de um ano voltou a funcionar](https://www.technologyreview.com/2026/10/15/1146091/pig-kidneys-that-were-frozen-for-a-year-have-been-brought-back-to-life/) (MIT Technology Review), produzindo cerca de 2/3 da urina esperada e com sinais de lesão. Ainda é preprint, e para comparar: hoje um órgão humano dura de 24 a 36 horas fora do corpo.
- [Para ler] [Import AI 476](https://importai.substack.com/p/import-ai-476-creativity-and-rsi), de Jack Clark: os novos modelos abertos americano (Beam) e europeu (Mistral Large 4) ainda ficam atrás do chinês GLM-5.3 em código. Clark é cofundador da Anthropic ([Anthropic](https://www.anthropic.com/company)).

---

**Pergunta da semana:** se uma IA fizesse a primeira versão de todas as suas peças, o que exatamente continuaria sendo trabalho seu?
