# Apuração: edição nº 2 (17/10/2026)

C = confirmado, P = parcial, NC = não confirmado.

## (c) IA na prática: duas IAs jurídicas, dois destinos

### Sullivan & Cromwell e o Agreement Analyzer
- **A fonte (C):** estudo de caso da própria OpenAI, de 15/10 (é material de venda). https://openai.com/index/sullivan-cromwell/
- **Como funciona (C):** o advogado põe a minuta, os precedentes e o "playbook" do escritório. Agentes revisam por ângulos diferentes, e outros agentes contestam os achados. A saída separa o que resistiu, o que foi descartado e o que não foi verificado, e vem como memorando e alterações em controle de alterações. O advogado revisa, adapta ou rejeita.
- **Quem fez (C):** o sócio John Savva montou a prova de conceito com o Codex em ~1 semana, em março. Em julho, engenheiros da OpenAI refinaram. O modelo exato não foi divulgado. https://news.bloomberglaw.com/tech-and-telecom-law/sullivan-cromwells-openai-gambit-delivers-tech-talent-access
- **Sem números de desempenho:** não há horas economizadas nem número de usuários. Savva fala em análise "mais minuciosa no mesmo prazo".
- **Sigilo (P):** o desenvolvimento usou contratos hipotéticos, e o uso por ora é interno. O código é do escritório.

### Enter × OAB-SP (C)
- **A ação:** em 07/10, a OAB-SP ajuizou ação civil pública contra a Talisman AI Ltda. ("Enter") na 4ª Vara Cível Federal de SP, processo nº 5031169-20.2026.4.03.6100. A tese é que a plataforma pratica atos privativos da advocacia sem ser sociedade de advogados.
  - https://www.oabsp.org.br/jornaldaadvocacia/26-10-07-1742-oab-sp-aciona-justica-contra-empresa-de-ia-para-estabelecer-limites-a-automacao-e-proteger-atividades-privativas-da-advocacia
  - https://www.migalhas.com.br/quentes/466111/oab-sp-aciona-enter-na-justica-por-uso-de-ia-em-atividades-juridicas
  - https://lawletter.com.br/exclusiva/oab-sp-acao-civil-publica-enter-inteligencia-artificial
- **Pedidos:**
  - liminar contra publicidade de "substituto do advogado";
  - novos contratos só com advogado responsável identificado, sob multa de R$ 50 mil por contrato;
  - supervisão humana auditável;
  - R$ 1 milhão de dano moral coletivo.
- **Sem decisão até 17/10** nas fontes encontradas.
- **A Enter:** nega substituir advogado e diz que a revisão, a assinatura e o protocolo ficam com advogados. Fala em "informações equivocadas" e diz que mantém diálogo com o Conselho Federal. https://startups.com.br/negocios/legaltech/oab-sp-entra-com-acao-contra-a-enter-e-pede-r-1m-por-dano-moral/
- **Avaliação de mercado:** US$ 1,2 bi, segundo o Startups.
- **Conselho Federal:** em 17/08, o plenário aprovou medidas judiciais contra empresas de IA que pratiquem atos privativos da advocacia. https://www.oab.org.br/noticia/64465/oab-defende-advocacia-contra-empresas-de-ia-que-praticarem-atos-exclusivos-da-classe

## (d) Para ler no fim de semana (C)
- **MIT TR:** rins de porco vitrificados a −150 °C, um deles guardado por pouco mais de 1 ano, voltaram a funcionar (cerca de 2/3 da urina esperada).
  - Ressalvas: é preprint e os rins tinham lesão.
  - Hoje, um órgão humano dura de 24 a 36 h fora do corpo.
  - https://www.technologyreview.com/2026/10/15/1146091/pig-kidneys-that-were-frozen-for-a-year-have-been-brought-back-to-life/
- **a16z, "Agents Denied":** grandes varejistas bloqueiam agentes compradores. As respostas 403 a bots dobraram desde o verão (dados da Cloudflare). Só ~25% dos consumidores aceitariam a IA comprando por eles. https://www.a16z.news/p/this-week-in-charts-agents-denied
- **Import AI 476 (Jack Clark, cofundador da Anthropic):** os modelos ocidentais abertos (Beam, Mistral Large 4) ficam atrás dos chineses. https://importai.substack.com/p/import-ai-476-creativity-and-rsi

## (a) Breakthroughs da semana

### Claude Haiku 5.5 (C)
- **Lançamento:** 7/10/2026. É anterior à 1ª edição; entra como "ficou da semana passada". https://www.anthropic.com/news/claude-haiku-5-5
- **Preço por milhão de tokens:** US$ 0,10 de entrada e 0,50 de saída (prompt de até 100 mil tokens), contra US$ 1,00 e 5,00 do Haiku 4.5. https://platform.claude.com/docs/en/about-claude/pricing
- **Média real:** cerca de 75% mais barato, segundo a própria Anthropic: "On average, it now costs around 75% less to run". A diferença vem do tokenizador novo, que gera ~30% mais tokens. Guia de migração: https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide
- **Benchmarks (autorrelatados):**
  - OSWorld 2.1 (uso de computador): 72,4% no Haiku 5.5, contra 15,7% no Haiku 4.5;
  - Humanity's Last Exam: 45,9% contra 10,2%.
  - A Anthropic diz que ele serve melhor a tarefas estreitas (resumo, subagentes).
- **Conta:** 1.000 contratos de 5 mil tokens de entrada e 500 de saída custam US$ 7,50 no Haiku 4.5. No Haiku 5.5 custam US$ 0,75 a preço de tabela, ou ~US$ 0,98 contando o tokenizador (−87%).

### Gemini 4 Argon (C), não é breakthrough
- **Lançamento:** 13/10. No app, só para os planos AI Pro (R$ 96,99/mês) e Ultra (a partir de R$ 779,90). O plano grátis não tem.
- **API:** só no nível pago. US$ 2 de entrada e 10 de saída até 30/11, depois US$ 4 e 20. O 3.1 Pro custa US$ 2 e 12.
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/
  - https://gemini.google/subscriptions/
  - https://ai.google.dev/gemini-api/docs/pricing
- **Benchmarks:** 1º no Vals Index (autodeclarado).

### A onda de descompilação por IA (C)
- **O texto do Popcar (14/10):** a IA decompila jogos "em dias, ou menos", quando antes a comunidade levava anos.
  - Exemplos: IsaacRecomp (Binding of Isaac a 1440p e 165 FPS), Colin McRae Rally 2.0, Final Fantasy Tactics Advance, Animal Well portado para PC.
  - O lado bom: preservação de jogos. O lado ruim: "qualquer software" pode ser decompilado e copiado. Ele afirma que "é completamente legal", mas isso é OPINIÃO dele.
  - https://popcar.bearblog.dev/ai-is-mass-decompiling-games-thats-both-awesome-and-scary/
  - https://simonwillison.net/2026/Oct/14/ai-is-mass-decompiling-games/
- **decomp.dev:** a comunidade de descompilação de jogos anunciou o fim em 15/10, porque a IA "quebrou" o aspecto comunitário.
  - https://decomp.dev
  - https://404media.co/video-game-reverse-engineering-community-shuts-down-because-ai-has-made-it-too-easy
- **REA:** 308.662 estrelas e 78 mil forks, criado em 14/04/2026, licença MIT.
  - É um MCP que liga o agente a Ghidra, IDA e Hopper. A análise roda localmente.
  - O aviso do projeto: só para análise lícita e de software que você possui ou está autorizado a examinar.
  - https://github.com/morluto/rea
- **Direito brasileiro:**
  - a Lei 9.609/98 (Lei do Software) **não fala em descompilação nem em engenharia reversa**;
  - o art. 6º só lista o que não ofende o titular: cópia de salvaguarda, citação didática, semelhança funcional e "integração" para uso exclusivo de quem a promoveu (inciso IV);
  - o art. 2º põe o software sob o regime de direitos autorais;
  - o art. 12 tipifica a violação como crime (detenção de 6 meses a 2 anos ou multa);
  - a licitude da descompilação depende de interpretação e da licença. A doutrina é escassa.
  - https://www.planalto.gov.br/ccivil_03/leis/l9609.htm

## (b) Histórias em andamento e números

### Meta recua (C)
- **A mudança (Verge, 17/10, 12h04 em Brasília):** saiu a frase "Meta may use any content... to... train..." dos termos comerciais. O robô continua autorizado, agora "para fornecer, desenvolver, melhorar, pesquisar e manter produtos de publicidade e de negócios". "Train" saiu; "desenvolver, melhorar, pesquisar" ficaram.
- **A Meta:** "This is not about scraping news sites", e o robots.txt continua valendo.
  - https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites
  - https://www.facebook.com/legal/commercial_terms_preview

### Sites fecham portas a agentes (C, sem números agregados)
- Delta barra agentes na compra de passagens. JPMorgan e Schwab bloqueiam agentes nas contas.
- O Yelp só libera agentes que pagam pela licença de dados.
- A Amazon diz que o acesso do Muse viola as políticas dela.
- https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web

### XBOW e o Chrome (C, autorrelatado; o Google não confirmou publicamente)
- **O que foi:** um exploit de cadeia completa no Chrome (JavaScript que escapa do sandbox no Windows), com três falhas: V8, WebP e Crashpad.
- **Como:** feito com o GPT-5.6 Sol (modelo público) e 4 humanos, em 6 dias (de 02 a 07/08), com ~US$ 40 mil de API. O Google pagou US$ 250 mil de recompensa.
- **Comparação:** pela XBOW, sem LLM seriam 4 pessoas por 6 a 9 meses.
- **Status:** a falha já foi corrigida.
- https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit

### Anthropic (C para o número, P para a taxa)
- **Receita:** US$ 16,8 bi no 3º tri, contra US$ 11,6 bi no 2º, ou +45% (Reuters, com investidores presentes no investor day de 14/10). O título do FT diz "nearly 50%".
- **O que a empresa diz:** não publicou nem comentou.
- **IPO:** o S-1 confidencial foi enviado em 01/06 (nota da Anthropic). Segundo a Bloomberg via TNW, o marketing pode começar por volta de 9/11, com ações antes de 26/11. Os planos são "fluidos".
  - https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/
  - https://www.dealstreetasia.com/?p=498196
  - https://thenextweb.com/news/anthropic-q3-revenue-16-8bn-ipo
  - https://www.anthropic.com/news/confidential-draft-s1-sec

### 6x1: prazos (C) e ERRATA da edição nº 1
- **O texto da EC 141 (DOU de 16/10, edição extra):** 42h "2 (dois) meses após a publicação" (art. 6º, I), e 40h um ano depois (art. 6º, II). As datas, por inferência, são 16/12/2026 e 16/12/2027.
- **A errata:** a edição nº 1 disse "em 60 dias", como o Senado resumiu, mas o texto da emenda diz 2 meses.
- **A Câmara:** Motta adota a nova escala já, para ~1.700 terceirizados.
  - https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc141.htm
  - https://www.camara.leg.br/noticias/1311899-motta-determina-adocao-imediata-da-nova-escala-de-trabalho-na-camara-dos-deputados

### OpenClaw (C)
- **Agora:** 392.291 estrelas (API, 17/10).
- **Em agosto:** 388 mil em 26/08, pelo GitHub Blog. Em 07/10, 391.558, por fonte de terceiros. O crescimento praticamente estacionou.
- **Os "145 mil":** sem fonte. NÃO USAR.
- https://github.blog/open-source/maintainers/openclaw-went-viral-meet-the-maintainers-building-and-securing-it/
