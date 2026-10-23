# Pauta — 2026-10-23 (sexta) · nº 8 · dia_util · MARKETING = não

Início: 04:38. Coleta: 420 candidatos de 63 fontes (2 falharam). Fontes sem RSS (Anthropic) visitadas pela apuração.

**Dia: morno.** Nada passa no critério de breakthrough (seção 3). O dia é dominado pela véspera do 2º turno (fora da pauta, seção 12).

## Entrou
- **Principal (explicador, IA):** pesquisa da Anthropic (22/10) diz que LLMs tornam a verificação formal de software viável em escala muito maior. Fio com a edição de ontem (PHP2Shell: a IA achou furos; agora a IA ajuda a provar que não há furo). Formato explicador: o que é verificação formal e por que importa. Breakthrough: não (pesquisa, não muda o que uma pessoa comum consegue fazer hoje).
- **IA na prática:** Anthropic doa o padrão Agent Skills à Agentic AI Foundation (Linux Foundation). Skills como "manual do estagiário"; o leitor usa Claude Code. Serviço: montar skills para escritórios.
- **Economia:** Ibovespa -1% e dólar a R$ 5,04 (reta final da eleição, só o efeito no mercado); Bradesco lucro R$ 7,11 bi com inadimplência subindo; lá fora: PMI fraco da França e euro; petróleo na semana; Banco do Japão.
- **Brasil adentro:** Tractian unicórnio (US$ 130 mi); Cade x Aiqfome/iFood; Enter x OAB-SP (continuação, só se houver fato novo desde 22/10); Carrefour vende imóveis ao Pátria; Hitachi Energy.
- **Mundo afora:** OpenAI rodada de US$ 30 bi a US$ 1,25 tri; Barclays corta 5% das vagas; Uber põe 30 mil no ChatGPT Work; Canva lança modelo de imagem; anunciantes tiram anúncios da Meta com "embelezamento" de IA.
- **STATS:** AI Overviews em 88% das buscas comerciais (Semrush, via PPC Land).
- **Hoje eu aprendi:** Starship precisaria de 22 lançamentos para um pouso na Lua.
- **Links:** Dijkstra 1978 "a tolice da programação em linguagem natural"; agentes de IA largados numa ilha virtual inventam jogos (MIT); vídeo do Google sobre o limite do robots.txt para IA.

## Ficou de fora
- Eleição, pesquisas, debate (seção 12). DeepSeek US$ 15 bi e licenças de exportação (já no caderno IA de 22/10). 1Password for Agents (caderno IA). Meta multa US$ 25 bi (já coberto 22/10). Microsoft "IA melhor que médicos" (claim de parte interessada; fica pra quando houver paper). OpenAI Decisions API (pouco valor para o leitor). Termos da Meta de 30/10 como notícia (já coberto em 18/10 e no marketing de 22/10; só entra o fato novo dos anunciantes tirando anúncios).

**Ajuste depois da apuração:** Enter x OAB-SP sai (mesmo fato de 22/10). Barclays entra com ressalva (PARCIAL). Ano do texto de Dijkstra não confirmado: não citar ano.

## Plano de redação
Edição curta e funda, dia morno. Alvo total: 1.250–1.450 palavras. Fio da edição: **a IA escreve muito, rápido; a pergunta agora é quem garante que está certo** (ontem: a IA achou o furo no PHP; hoje: a IA tenta provar que não há furo; skills = instruções escritas que viram padrão; Dijkstra avisando há quase 50 anos que linguagem natural é traiçoeira). Nada de anedota pessoal. Nada de política eleitoral (só o efeito no mercado, sem pesquisa).

### 1. bom dia (2–3 linhas, ~45 palavras)
Começa com "bom dia." Reflexão: ontem a IA achou um furo de mais de uma década no PHP; hoje a notícia é a IA tentando provar que o código **não** tem furo. Achar erro é uma coisa; garantir que não há erro é outra. Sem link.

### 2. Hoje eu aprendi (1–2 frases, ~45 palavras)
Na reunião do painel de segurança da NASA, em 22/10, o ex-astronauta Charlie Precourt disse que a última estimativa é de **cerca de 22 voos** da Starship para o pouso da Artemis IV (em 2023 a NASA falava em cerca de uma dúzia); Musk respondeu que serão "6 a 8". Link: https://arstechnica.com/space/2026/10/latest-estimate-for-starship-launches-required-to-support-a-moon-landing-22/ (CONFIRMADO). Explique em meia frase: a nave precisa ser reabastecida em órbita várias vezes.

### 3. Nesta edição (4–5 bullets, ~70 palavras)
- a IA que tenta provar que o código não quebra (principal);
- a "receita" que vale para 70 agentes (IA na prática);
- Bradesco, Ibovespa e o petróleo perto de US$ 114;
- Tractian vira unicórnio; OpenAI baixa a pedida;
- 88%: o resumo do Google já está em quase toda busca de compra (STATS).
Uma piada seca no máximo.

### 4. Matéria principal — EXPLICADOR (380–480 palavras)
`#### IA` / `## Título-gancho`. Sugestão: "## E se a IA provasse que o código não quebra?" (ou similar; pergunta ou tese).
TL;DR: a Anthropic diz ter usado o Claude para **provar matematicamente** que **239** pontos de entrada de **123** bibliotecas abertas não falham com nenhuma entrada até 64 MB, num trabalho de poucas semanas.
Pontos, nesta ordem:
1. **Lead** com o fato e os números em negrito, link https://www.anthropic.com/research/formal-verification (CONFIRMADO). Publicado em 22/10, pela Frontier Red Team da Anthropic com a empresa Theorem.
2. **O que é verificação formal**, em linguagem leiga: teste é conferir alguns casos; prova formal é demonstrar, como num teorema, que vale para **todos** os casos. Analogia sugerida: teste é provar 50 pratos do restaurante; prova formal é demonstrar que a receita não tem como sair crua — ou analogia jurídica (testar é ouvir algumas testemunhas; provar é ter a escritura registrada). Escolha uma, curta. Explique o Rocq (antigo Coq) numa oração: programa que confere provas matemáticas.
3. **Por que era cara (escala):** o seL4, núcleo de sistema verificado, levou **2 pessoas-ano** para ser escrito e **20** para ser verificado — **10 vezes** mais (dado citado pelo post da Anthropic). Agora: ~**180 milhões** de linhas de prova, prova típica de ~600 mil linhas. Fio: ontem, PHP2Shell — falhas achadas com IA da OpenAI e do Google depois de mais de uma década escondidas; a Amazon viu tentativa de exploração 4 dias antes do aviso público (https://arstechnica.com/security/2026/10/hackers-got-a-four-day-head-start-on-epic-php2shell-vulnerability/, CONFIRMADO). Deixe claro que a IA do PHP2Shell NÃO foi da Anthropic.
4. **Achados no caminho:** "centenas" de bugs nas tentativas de prova; um leitor de PDF rendeu numa semana tantos bugs de segurança quanto costumam ser reportados num ano (afirmação da Anthropic, diga isso). Custo: provas podem consumir "centenas de milhões de tokens" (token = pedaço de palavra que o modelo processa e que entra na conta).
5. **Os otimistas / Os pessimistas** (um par, obrigatório):
   - Otimistas: Jason Gross, coautor do estudo, diz no Hacker News que em software o gargalo "is just scale" (é parte interessada: diga que é coautor). Link HN: https://news.ycombinator.com/item?id=50202217
   - Pessimistas: a própria Anthropic avisa que "formalmente verificado" não é "sem bug": o erro pode estar na especificação (a descrição do que o código deveria fazer); só vale para binários RISC-V estáticos e de uma thread, enquanto a maioria roda x86/ARM; risco de a IA "trapacear" reescrevendo o código para nunca falhar (patches foram auditados). No HN, a pergunta seca: "Formal verification against what?" (verificação contra o quê?). Os 99,95% do interpretador de Python são teste, não prova — se citar, diga isso; pode cortar.
6. ⚖️ uma linha opcional (sem citar lei): em contrato de software, "verificado formalmente" vira argumento de qualidade e de responsabilidade — mas só prova o que a especificação disse. Sem artigo de lei.
7. **Por que isso importa pra você** (2–3 linhas): para quem vende sites e apps feitos com IA, a pergunta do cliente vai mudar de "funciona?" para "como você sabe?". Hoje isso é pesquisa de ponta, não ferramenta de prateleira; o passo prático é pedir à IA testes e conferir o que ela diz que testou.
`🔗 [Anthropic: LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification)`
Tom: humor seco no máximo uma vez (ex.: Armin Ronacher brincou que, com tanto software ruim escrito em 30 anos, "o universo está nos punindo" — PARCIAL, tom de piada; opcional, com link https://simonwillison.net/2026/Oct/22/armin-ronacher/). Não é breakthrough: sem 🚨.

### 5. 🧠 IA NA PRÁTICA (300–420 palavras)
`#### 🧠 IA NA PRÁTICA` / `## Tese numa linha`, ex.: "## A receita que o seu agente lê virou padrão de todo mundo".
1. **O fato:** em 22/10, a Anthropic doou o padrão Agent Skills à Agentic AI Foundation, braço da Linux Foundation que já guarda o MCP; segundo a Anthropic, **mais de 70** plataformas de agentes, incluindo ChatGPT, Cursor, GitHub Copilot e VS Code, já usam o padrão; **1 milhão** de skills publicadas e quase **280 milhões** de instalações. Link https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation (CONFIRMADO). A fundação recebeu no mesmo dia projetos da OpenAI, da Hugging Face e da Alibaba (https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox).
2. **O conceito com analogia:** skill é uma pasta com um arquivo SKILL.md (nome + descrição de quando usar + instruções) e, se quiser, scripts e modelos. Analogia: o manual de procedimentos que o escritório dá ao estagiário novo — ele não decora tudo; lê o capítulo certo quando o caso chega. O agente carrega só nome e descrição (~100 tokens) e abre o resto quando precisa (https://agentskills.io/specification, CONFIRMADO). O que muda com a doação: a receita escrita para o Claude Code serve em outras ferramentas, sem depender de uma empresa só ("open, community-driven, and vendor-neutral", diz a Anthropic).
3. **O caso real** (🔗 em linha própria): a Rakuten diz que um processo de contabilidade gerencial que levava um dia caiu para cerca de uma hora com skills — depoimento no material de lançamento da Anthropic, diga isso (https://claude.com/blog/skills). E o advogado Zack Shapiro, de um pequeno escritório nos EUA, descreveu um escritório "nativo em Claude" com skills próprias para revisar contratos, editar .docx com alterações rastreadas e padronizar citações (https://www.artificiallawyer.com/2026/03/02/lawyer-uses-claude-skills-legal-world-loses-it/, PARCIAL — escreva "segundo o Artificial Lawyer").
4. **⚠️ Freio de realidade:** skill pode trazer script que o agente executa: a Anthropic manda instalar só de fonte confiável. A Snyk analisou **3.984** skills de dois marketplaces e achou **534** (13,4%, uma em cada sete e pouco) com ao menos um problema crítico e **76** maliciosas (https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub; Snyk vende segurança: meia frase). O guia de segurança do padrão ainda é só proposta.
5. **Agora aplica no mundo real** (3 linhas): advogado/escritório (skill de petição inicial no padrão da casa, com checklist de prazos e o modelo de procuração); dono de restaurante ou clínica (skill de responder avaliações e mensagens no tom da casa); professor (skill de corrigir redação com a rubrica da escola).
6. **Como isso vira serviço:** montar e manter a biblioteca de skills de um escritório pequeno: entrevistar quem faz o trabalho, escrever os procedimentos, testar com casos reais, revisar a cada mudança. Por que pagariam agora: o mesmo pacote passa a rodar em várias ferramentas. `**Opinião:**` quem documenta o processo do cliente vende algo que sobrevive à troca de ferramenta. Sem preço, sem promessa.
7. **Para testar hoje** (15 min): no Claude Code, crie uma pasta com um SKILL.md descrevendo como você quer que ele revise um texto seu (nome, descrição de quando usar, 5 regras) e peça uma revisão. Nada de instalar skill de terceiros sem ler.

### 6. ECONOMIA (≈150 palavras)
`#### ECONOMIA` / **🇧🇷 Por aqui** / **🌎 Lá fora**, linhas `→`:
- → **Ibovespa**: caiu **1,15%** na quinta (22), a **204.120** pontos, o menor fechamento desde 2/10; o dólar subiu **0,22%**, a **R$ 5,04**, na reta final do 2º turno (InvestNews, https://investnews.com.br/investimentos/reta-final-da-eleicao-ibovespa-cai-mais-de-1-pressionado-por-pesquisas-dolar-sobe/). Sem números de pesquisa.
- → **Bradesco**: lucro recorrente de **R$ 7,11 bi** no 3º tri, **+0,8%** sobre o 2º (praticamente parado) e **+14,6%** em um ano; a inadimplência acima de 90 dias subiu a **4,6%** (era **4,1%** um ano antes) e o ROE caiu a **15,6%** (Bloomberg Línea, https://www.bloomberglinea.com.br/negocios/lucro-do-bradesco-perde-folego-no-3-tri-com-alta-da-inadimplencia-e-das-provisoes/); na prática, crédito mais caro de carregar.
- → **França**: o PMI composto (termômetro de empresas; abaixo de 50 é encolhimento) caiu a **48,4** em outubro, de **51,1**, o menor em 4 meses (https://tradingeconomics.com/france/composite-pmi); o euro ronda **US$ 1,12** (https://tradingeconomics.com/euro-area/currency) — não atribuir a queda só ao PMI.
- → **Petróleo**: o Brent passou de **US$ 114** nesta sexta (23), perto da máxima de 4 anos (US$ 114,44, em maio), com ataques houthis à Arábia Saudita; **+74%** em um ano (https://tradingeconomics.com/commodity/brent-crude-oil). Sem "alta semanal".
- → **Japão**: o banco central deve manter os juros em **1,25%** na reunião de 29 e 30/10, segundo o Nikkei (Valor, https://valor.globo.com/financas/noticia/2026/10/23/banco-do-japo-manter-taxa-de-juros-em-125-pontos-percentuais-na-reunio-da-prxima-semana.ghtml).

### 7. Brasil adentro / Mundo afora (3–5 linhas cada)
`#### 🇧🇷 BRASIL ADENTRO`
- → **Tractian**: Série D de **US$ 130 mi** (~R$ 650 mi) liderada pela Sapphire, avaliação de **US$ 1,4 bi**, 94% acima da rodada anterior; faz sensores e IA para prever quebra de máquina; receita anualizada passou de **US$ 100 mi** (era US$ 40 mi em 2024), segundo a empresa (https://www.bloomberglinea.com.br/startups/tractian-capta-us-130-milhoes-e-se-torna-o-mais-novo-unicornio-de-ia-brasileiro/).
- → **iFood**: a Superintendência-Geral do Cade recomendou arquivar a queixa da Aiqfome sobre exclusividade no interior; o acordo de 2023 já limita a exclusividade a **25%** do volume vendido; é recomendação, não decisão final (https://www.bloomberglinea.com.br/tech/cade-recomenda-arquivar-queixa-da-aiqfome-contra-o-ifood-sobre-exclusividade-no-interior/).
- → **Carrefour**: vendeu **22** imóveis ao fundo Pátria Renda Urbana e passa a pagar aluguel neles; valor não divulgado; depende do Cade (https://investnews.com.br/negocios/carrefour-vende-imoveis-ao-patria-e-passara-a-pagar-aluguel-pelas-lojas/).
- → **Hitachi Energy**: novo aporte de **US$ 77 mi** numa fábrica de componentes de transformadores em Pindamonhangaba (SP), que leva o plano no Brasil a **US$ 350 mi**; pronta no fim de 2028; na prática, data center e rede elétrica puxando indústria (https://c-level.folha.uol.com.br/negocios/2026/10/hitachi-energy-anuncia-nova-unidade-no-brasil-e-eleva-plano-de-investimentos-a-us-350-milhoes.shtml).
`#### 🌎 MUNDO AFORA`
- → **OpenAI**: negocia até **US$ 30 bi** a **US$ 1,25 tri** antes do dinheiro entrar, segundo a CNBC; a Bloomberg falava em **US$ 1,4 tri** — US$ 150 bi a menos (TechCrunch, https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/).
- → **Uber**: vai pôr os **30 mil** funcionários no ChatGPT Work, o agente corporativo da OpenAI, depois de um piloto com 1.000 (https://techcrunch.com/2026/10/22/uber-puts-all-30000-employees-on-chatgpt-work/).
- → **Barclays**: vai cortar cerca de **5.000** vagas (**5%** do quadro) até o fim de 2026 e liga os cortes à produtividade com IA; o lucro antes de impostos subiu **12%** no 3º tri (Business Standard, https://www.business-standard.com/amp/companies/news/barclays-to-cut-5-000-jobs-in-ai-led-cost-drive-as-q3-profit-rises-12-126102201741_1.html). Sem humor.
- → **Meta**: anunciantes como a Bookshop.org e a agência Exverus tiraram ou corrigiram anúncios que a IA da Meta alterou, antes dos termos de 30/10 que deixam o anunciante "solely responsible" até pelo que a Meta liga sozinha (Adweek, https://www.adweek.com/media/advertisers-pull-meta-ads-that-had-unwanted-ai-glow-ups/); na prática, revise as opções do Advantage+ campanha por campanha.
- → **Canva**: lançou o Canva Craft, seu primeiro modelo de imagem, para todos os usuários (TechCrunch, https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model/).

### 8. 📊 STATS (110–150 palavras)
`#### 📊 STATS` / `## 88%` / TL;DR obrigatório (todo `##` leva TL;DR).
- AI Overviews (o resumo de IA no topo do Google) apareceram em **88%** de 400 buscas comerciais nos EUA (desktop) em agosto, contra **45,75%** em set/2025 — **quase o dobro** em 11 meses; ponderado por volume, **97%** (Semrush, https://www.semrush.com/blog/ai-overviews-commercial-modifiers-study/; ppc.land). Semrush vende ferramenta de SEO (parte interessada) e mede só aparição, não clique.
- Contraponto de clique: num estudo com 100 sites, as visitas vindas do ChatGPT foram **0,62%** do volume do Google orgânico — menos de R$ 1 de cada R$ 100 de tráfego (https://ppc.land/google-ai-overviews-reach-88-of-commercial-searches-as-ai-clicks-stay-thin/, PARCIAL, amostra pequena).
- Cadeia `»` (marque como leitura): resumo no topo de quase toda busca de compra » parte de quem busca resolve sem clicar (hipótese da própria Semrush, não medida) » ficar em 1º rende menos visita » o site do cliente precisa ser citado no resumo, não só ranquear.

### 9. Para ler, ouvir ou assistir (3 links)
- [Para ler] Dijkstra, "On the foolishness of 'natural language programming'" (EWD667) — sem ano; uma frase: o cientista argumentou que linguagem formal protege de erro bobo e que a "naturalidade" do idioma facilita dizer absurdo sem perceber; liga com o fio da edição. https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html
- [Curiosidade] 13 agentes de IA soltos por 30 horas numa ilha digital, sem tarefa, inventaram jogos e um memorial para um anel jogado no mar (paper ainda sem revisão). https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/
- [Para assistir] Google Search Central: "What can you actually put in a robots.txt?" — o robots.txt controla o acesso do robô, não o que acontece com o conteúdo depois. https://www.youtube.com/watch?v=-jHONLQgE-s

### 10. Pergunta de fechamento (1 linha)
Ex.: "Se você tivesse que escrever hoje o manual do seu próprio trabalho para um agente seguir, quantas regras você ainda não sabe explicar?"

### Assunto, prévia e front matter
- **assunto:** "a ia que tenta provar que o código não quebra" (9 palavras, minúsculas)
- **prévia:** "+ a receita que já roda em 70 agentes"
```yaml
data: 2026-10-23
tipo: dia_util
numero: 8
assunto: "a ia que tenta provar que o código não quebra"
previa: "+ a receita que já roda em 70 agentes"
tempo_leitura_min: (palavras ÷ 220)
dia: morno
breakthrough: false   # pesquisa: não muda hoje o que uma pessoa comum consegue fazer
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
    titulo: "Brent passa de US$ 114, perto da máxima de 4 anos"
    tema: economia
    urls: ["https://tradingeconomics.com/commodity/brent-crude-oil"]
    em_andamento: true
  - id: tractian-unicornio
    titulo: "Tractian capta US$ 130 mi e vira unicórnio"
    tema: negocios
    urls: ["https://www.bloomberglinea.com.br/startups/tractian-capta-us-130-milhoes-e-se-torna-o-mais-novo-unicornio-de-ia-brasileiro/"]
    em_andamento: false
  - id: openai-rodada-ipo
    titulo: "OpenAI negocia US$ 30 bi a US$ 1,25 tri, abaixo da meta anterior"
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
```
