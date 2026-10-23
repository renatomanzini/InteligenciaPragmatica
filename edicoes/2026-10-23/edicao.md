---
data: 2026-10-23
tipo: dia_util
numero: 8
assunto: "a ia que tenta provar que o código não quebra"
previa: "+ a receita que já roda em 70 agentes"
tempo_leitura_min: 7
dia: morno
breakthrough: false
historias:
  - id: verificacao-formal-llm
    titulo: "Anthropic usa o Claude para provar formalmente 239 pontos de entrada de 123 bibliotecas abertas"
    tema: ia
    urls: ["https://www.anthropic.com/research/formal-verification"]
    em_andamento: true
  - id: agent-skills-aaif
    titulo: "Anthropic doa o padrão Agent Skills à Agentic AI Foundation"
    tema: ia
    urls: ["https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation"]
    em_andamento: false
  - id: bradesco-3t-2026
    titulo: "Lucro do Bradesco fica estável no 3º tri com inadimplência a 4,6%"
    tema: economia
    urls: ["https://www.bloomberglinea.com.br/negocios/lucro-do-bradesco-perde-folego-no-3-tri-com-alta-da-inadimplencia-e-das-provisoes/"]
    em_andamento: false
  - id: petroleo-brent-2026
    titulo: "Brent chega a cerca de US$ 114, perto da máxima de 4 anos"
    tema: economia
    urls: ["https://tradingeconomics.com/commodity/brent-crude-oil"]
    em_andamento: true
  - id: tractian-unicornio
    titulo: "Tractian capta US$ 130 mi e vira unicórnio"
    tema: negocios
    urls: ["https://www.bloomberglinea.com.br/startups/tractian-capta-us-130-milhoes-e-se-torna-o-mais-novo-unicornio-de-ia-brasileiro/"]
    em_andamento: false
  - id: openai-rodada-ipo
    titulo: "OpenAI negocia US$ 30 bi a US$ 1,25 tri, abaixo do valor reportado antes"
    tema: negocios
    urls: ["https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/"]
    em_andamento: true
  - id: meta-termos-comerciais-ia
    titulo: "Anunciantes tiram anúncios alterados pela IA da Meta antes dos termos de 30/10"
    tema: marketing
    urls: ["https://www.adweek.com/media/advertisers-pull-meta-ads-that-had-unwanted-ai-glow-ups/"]
    em_andamento: true
  - id: ai-overviews-buscas-comerciais
    titulo: "AI Overviews aparecem em 88% das buscas comerciais monitoradas pela Semrush"
    tema: marketing
    urls: ["https://www.semrush.com/blog/ai-overviews-commercial-modifiers-study/"]
    em_andamento: false
formatos: [explicador, materia_principal, ia_na_pratica, economia, rodadas, stats, links, pergunta]
---
bom dia. Ontem a gente contou como a IA ajudou a achar um furo de mais de uma década no PHP. Hoje a notícia é a IA tentando provar que o código **não** tem furo. Achar um erro é uma coisa; garantir que não existe nenhum é outra, bem mais cara.

**Hoje eu aprendi:** segundo Charlie Precourt, ex-astronauta e membro do painel de segurança da NASA, a última estimativa é de cerca de **22 voos** da Starship para um pouso da Artemis IV na Lua, contra algo como uma dúzia pelo que a NASA deixou entender em 2023, porque a nave precisa ser reabastecida em órbita várias vezes; Musk diz que serão "6 a 8" ([Ars Technica](https://arstechnica.com/space/2026/10/latest-estimate-for-starship-launches-required-to-support-a-moon-landing-22/)).

**Nesta edição:**
- A IA que tenta provar que o código não quebra (e por que "provar" não é "testar")
- A "receita" que vale para 70 agentes de IA, e o serviço que dá para vender com ela
- Bradesco, Ibovespa e um petróleo acima de US$ 114
- Tractian vira unicórnio; a OpenAI baixa a pedida
- 88%: o resumo do Google já aparece em quase toda busca de compra

---

#### IA
## E se a IA provasse que o código não quebra?
> **TL;DR:** a Anthropic diz ter usado o Claude para **provar matematicamente** que **239** pontos de entrada de **123** bibliotecas abertas não falham com nenhuma entrada de menos de 64 MB, num trabalho de poucas semanas.

Em pesquisa publicada na quinta (22), a Frontier Red Team da Anthropic, com a empresa Theorem, diz que o Claude provou **239** pontos de entrada de **123** bibliotecas abertas, sem falha para entradas de menos de 64 MB, em algumas semanas ([Anthropic](https://www.anthropic.com/research/formal-verification)).

**O que é isso.** Teste é conferir alguns casos, como ouvir três testemunhas. Prova formal é demonstrar que vale para **todos**, como a escritura registrada. A conferência roda no Rocq, programa que confere provas matemáticas.

**Por que era cara.** O seL4, um núcleo de sistema verificado, levou **2** pessoas-ano para ser escrito e **20** para ser verificado, **10 vezes** mais (dado citado pela Anthropic). Aqui são cerca de **180 milhões** de linhas de prova, **600 mil** numa prova típica.

O fio com ontem: no PHP2Shell, falhas escondidas por mais de uma década foram achadas com IA da OpenAI e do Google (não da Anthropic), e a Amazon viu tentativa de ataque **4 dias** antes do aviso público ([Ars Technica](https://arstechnica.com/security/2026/10/hackers-got-a-four-day-head-start-on-epic-php2shell-vulnerability/)).

No caminho, "centenas" de bugs apareceram. A conta é em tokens, os pedaços de palavra que o modelo processa: provas podem gastar "centenas de milhões".

**Os otimistas:** Jason Gross, coautor do estudo (logo, parte interessada), diz no Hacker News que, na verificação de software, o gargalo "é só escala" ([HN](https://news.ycombinator.com/item?id=50202217)).

**Os pessimistas:** a própria Anthropic avisa que "formalmente verificado" não é "sem bug": o erro pode estar na especificação, a descrição do que o código deveria fazer. As provas principais valem para binários RISC-V estáticos e de uma thread só; houve um caso em x86, e a empresa diz que ampliar o escopo está ao alcance. No HN, a pergunta seca: "Formal verification against what?" (contra o quê?).

⚖️ **Opinião:** em contrato de software, "verificado formalmente" tende a virar argumento de qualidade e de responsabilidade, mas só prova o que a especificação disse.

**Por que isso importa pra você:** **Opinião:** quem vende sites e apps feitos com IA deve ouvir do cliente, cada vez mais, "como você sabe que funciona?". Por enquanto é pesquisa de ponta, não recurso do dia a dia; o passo prático é pedir testes à IA e conferir o que ela diz que testou.

🔗 [Anthropic: LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification)

---

#### 🧠 IA NA PRÁTICA
## A receita que o seu agente lê virou padrão de todo mundo
> **TL;DR:** a Anthropic doou o padrão Agent Skills à Agentic AI Foundation em 22/10; segundo ela, mais de **70** plataformas de agentes já o usam.

Pense no manual que o escritório dá ao estagiário novo: ele lê o capítulo certo quando o caso chega. Uma *skill* é isso para o agente: uma pasta com um arquivo SKILL.md (nome, quando usar, instruções) e, se quiser, scripts. O agente carrega só nome e descrição, cerca de **100** tokens, e abre o resto quando precisa ([especificação](https://agentskills.io/specification)).

O que mudou: em 22/10, a Anthropic doou o padrão à Agentic AI Foundation, braço da Linux Foundation que já guarda o MCP. Segundo ela, **mais de 70** plataformas, como ChatGPT, Cursor e GitHub Copilot, o usam, com **1 milhão** de skills publicadas e quase **280 milhões** de instalações; a receita feita para o Claude Code serve em outras ferramentas ([Anthropic](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)).

**O caso real.** Yusuke Kaji, gerente-geral de IA da Rakuten, diz que um processo de contabilidade que levava um dia passou a levar uma hora; é depoimento no material de lançamento da Anthropic ([Claude](https://claude.com/blog/skills)). E, segundo o Artificial Lawyer, o advogado Zack Shapiro, de um escritório pequeno nos EUA, montou skills para revisar contratos e padronizar citações ([Artificial Lawyer](https://www.artificiallawyer.com/2026/03/02/lawyer-uses-claude-skills-legal-world-loses-it/)).

🔗 [Anthropic: Agent Skills na Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)

⚠️ **Freio de realidade:** skill pode trazer script que o agente executa, e a Anthropic manda instalar só de fonte confiável ([Claude](https://claude.com/blog/skills)). A Snyk, que vende segurança, analisou **3.984** skills de marketplaces abertos: **534** (cerca de 13 em cada 100) tinham ao menos um problema crítico e **76** eram maliciosas ([Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub)). E o guia de segurança do padrão ainda é só proposta.

**Agora aplica no mundo real:**
- **Advogado:** skill de petição inicial no padrão da casa, com checklist de prazos e o modelo de procuração.
- **Dono de restaurante ou clínica:** skill para responder avaliações no tom do lugar.
- **Professor:** skill para corrigir redação com a rubrica da escola.

**Como isso vira serviço:** montar e manter a biblioteca de skills de um escritório pequeno: entrevistar quem faz o trabalho, escrever os procedimentos e testar com casos reais. **Opinião:** o cliente pagaria agora porque o mesmo pacote passa a rodar em várias ferramentas, e quem documenta o processo do cliente vende algo que sobrevive à troca de ferramenta.

---

#### ECONOMIA
**🇧🇷 Por aqui**

→ **Ibovespa**: caiu **1,15%** na quinta (22), a **204.120** pontos, o menor fechamento desde 2/10; o dólar subiu **0,22%**, a **R$ 5,04**, na reta final do 2º turno ([InvestNews](https://investnews.com.br/investimentos/reta-final-da-eleicao-ibovespa-cai-mais-de-1-pressionado-por-pesquisas-dolar-sobe/)).

→ **Bradesco**: lucro recorrente de **R$ 7,11 bi** no 3º tri, **+0,8%** sobre o 2º e **+14,6%** em um ano, mas a inadimplência acima de 90 dias subiu a **4,6%** (era **4,1%** um ano antes), segundo a Bloomberg Línea ([fonte](https://www.bloomberglinea.com.br/negocios/lucro-do-bradesco-perde-folego-no-3-tri-com-alta-da-inadimplencia-e-das-provisoes/)).

**🌎 Lá fora**

→ **França**: o PMI composto (termômetro de empresas; abaixo de 50 é encolhimento) caiu a **48,4** em outubro, de **51,1**, o menor em 4 meses ([Trading Economics](https://tradingeconomics.com/france/composite-pmi)).

→ **Petróleo**: o Brent chegou a cerca de **US$ 114** nesta sexta (23), perto da máxima de 4 anos (US$ 114,44, em maio), com ataques houthis à Arábia Saudita; está cerca de **75%** acima de um ano atrás ([Trading Economics](https://tradingeconomics.com/commodity/brent-crude-oil)).

---

#### 🇧🇷 BRASIL ADENTRO
→ **Tractian**: Série D de **US$ 130 mi**, com avaliação de **US$ 1,4 bi**, **94%** acima da rodada anterior; a empresa, de sensores para prever quebra de máquina, diz ter passado de **US$ 100 mi** de receita anualizada, contra US$ 40 mi em 2024 ([Bloomberg Línea](https://www.bloomberglinea.com.br/startups/tractian-capta-us-130-milhoes-e-se-torna-o-mais-novo-unicornio-de-ia-brasileiro/)).

→ **iFood**: a Superintendência-Geral do Cade recomendou arquivar a queixa da Aiqfome sobre exclusividade; o acordo de 2023 limita a exclusividade a **25%** do valor vendido na plataforma, e é recomendação, não decisão final ([Bloomberg Línea](https://www.bloomberglinea.com.br/tech/cade-recomenda-arquivar-queixa-da-aiqfome-contra-o-ifood-sobre-exclusividade-no-interior/)).

→ **Carrefour**: vendeu **22** imóveis ao fundo Pátria Renda Urbana e passa a pagar aluguel neles; o valor não foi divulgado e a venda depende do Cade ([InvestNews](https://investnews.com.br/negocios/carrefour-vende-imoveis-ao-patria-e-passara-a-pagar-aluguel-pelas-lojas/)).

#### 🌎 MUNDO AFORA
→ **OpenAI**: negocia até **US$ 30 bi** a **US$ 1,25 tri** antes do dinheiro entrar, segundo a CNBC; um mês antes, a Bloomberg falava em **US$ 1,4 tri** ([TechCrunch](https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/)).

→ **Barclays**: vai cortar cerca de **5.000** vagas (**5%** do quadro) até o fim de 2026 e liga os cortes à produtividade com IA, segundo a Reuters ([Business Standard](https://www.business-standard.com/amp/companies/news/barclays-to-cut-5-000-jobs-in-ai-led-cost-drive-as-q3-profit-rises-12-126102201741_1.html)).

→ **Meta**: a Bookshop.org desligou todos os recursos de IA da Meta e agências como a Exverus tiraram anúncios do ar para desfazer alterações, antes dos termos de 30/10 que deixam o anunciante "solely responsible" pelo que a IA cria; a agência AdCellerant diz que desliga a automação padrão em toda campanha ([Adweek](https://www.adweek.com/media/advertisers-pull-meta-ads-that-had-unwanted-ai-glow-ups/)).

---

#### 📊 STATS
## 88%
> **TL;DR:** o resumo de IA do Google apareceu em **88%** das buscas comerciais testadas pela Semrush, quase o dobro de 11 meses antes.

Os AI Overviews (o resumo de IA no topo do Google) apareceram em **88%** de 400 buscas comerciais nos EUA, no desktop, em agosto, contra **45,75%** em setembro de 2025 ([Semrush](https://www.semrush.com/blog/ai-overviews-commercial-modifiers-study/)). A Semrush vende ferramenta de SEO e mede só aparição, não clique.

Contraponto: em 100 sites, as visitas vindas do ChatGPT foram **0,62%** do volume do Google orgânico, segundo estudo citado pelo PPC Land (amostra pequena) ([PPC Land](https://ppc.land/google-ai-overviews-reach-88-of-commercial-searches-as-ai-clicks-stay-thin/)).

**Opinião:** a leitura é esta: resumo no topo de quase toda busca de compra » parte de quem busca resolve sem clicar (hipótese da própria Semrush, não medida) » ficar em 1º rende menos visita » o site do cliente precisa ser citado no resumo, não só ranquear.

---

**Para ler, ouvir ou assistir:**
- [Para ler] [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html), de Dijkstra: a linguagem formal protege de erro bobo; a "naturalidade" do idioma facilita dizer absurdo sem perceber.
- [Curiosidade] [Agentes de IA soltos numa ilha digital](https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/): 13 agentes, 30 horas e nenhuma tarefa renderam jogos e um memorial para um anel (paper do MIT, sem revisão).
- [Para assistir] [What can you actually put in a robots.txt?](https://www.youtube.com/watch?v=-jHONLQgE-s), do Google Search Central: o robots.txt controla o acesso do robô, não o que acontece com o conteúdo depois.

---

**Pergunta do dia:** se você tivesse que escrever hoje o manual do seu próprio trabalho para um agente seguir, quantas regras ainda não saberia explicar?
