---
data: 2026-10-22
tipo: dia_util
numero: 7
assunto: "o furo no php que a ia achou"
previa: "+ o agente novo da anthropic, que ainda não chegou aqui"
tempo_leitura_min: 8
dia: forte
breakthrough: false
historias:
  - id: php2shell-ia
    titulo: "IA ajuda a achar duas falhas críticas no núcleo do PHP; correção sai em 21/10"
    tema: ia
    urls:
      - "https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/"
      - "https://www.php.net/archive/2026.php"
    em_andamento: true
  - id: claude-duet
    titulo: "Anthropic lança o Claude Duet, agente para profissionais e pequenos negócios, só nos EUA"
    tema: ia
    urls: ["https://claude.com/product/claude-duet"]
    em_andamento: true
  - id: stf-iss-pis-cofins
    titulo: "STF tira o ISS da base do PIS/Cofins por 6 a 5"
    tema: economia
    urls: ["https://www.estadao.com.br/economia/por-6-a-5-stf-exclui-iss-da-base-do-piscofins-em-derrota-de-r-354-bi-para-a-uniao/"]
    em_andamento: true
  - id: desenrola-3
    titulo: "Desenrola 3 prevê leilão de até R$ 90 bi em dívidas"
    tema: economia
    urls: ["https://www.estadao.com.br/economia/desenrola-3-governo-espera-comprar-r-90-bi-em-dividas-antigas-em-novembro-diz-durigan/"]
    em_andamento: true
  - id: prospera-mei
    titulo: "Lei sancionada perdoa a parte previdenciária das dívidas de MEIs e sobe o teto"
    tema: economia
    urls: ["https://investnews.com.br/economia/prospera-mei-perdao-dividas/"]
    em_andamento: false
  - id: tesla-3t-2026
    titulo: "Lucro da Tesla cai 43% no 3º trimestre"
    tema: economia
    urls: ["https://arstechnica.com/cars/2026/10/tesla-profits-drop-43-in-q3/"]
    em_andamento: false
  - id: enter-oab-sp
    titulo: "Justiça adia restrições à Enter pedidas pela OAB-SP e manda preservar registros"
    tema: direito_tech
    urls: ["https://c-level.folha.uol.com.br/negocios/2026/10/justica-rejeita-suspensao-imediata-de-servicos-de-startup-juridica-de-ia-por-pedido-da-oab-sp.shtml"]
    em_andamento: true
  - id: keeta-anr
    titulo: "Associação de restaurantes processa a Keeta pela 'compra intermediada'"
    tema: negocios
    urls: ["https://neofeed.com.br/negocios/a-revolta-dos-restaurantes-associacao-vai-a-justica-contra-compra-intermediada-da-keeta/"]
    em_andamento: true
  - id: weg-america-norte
    titulo: "WEG cresce 31% na América do Norte com data centers"
    tema: negocios
    urls: ["https://investnews.com.br/negocios/weg-ganha-espaco-eua-data-center/"]
    em_andamento: false
  - id: agentes-bloqueados-sites
    titulo: "Walmart abre o site para agentes de IA, enquanto a Amazon bloqueia"
    tema: ia
    urls: ["https://www.theverge.com/ai-artificial-intelligence/1015715/walmart-ai-shopping-agents"]
    em_andamento: true
  - id: meta-nova-classe-acoes
    titulo: "Meta cria classe de ações sem voto para financiar IA"
    tema: negocios
    urls: ["https://www.theverge.com/tech/1015799/meta-shares-class-ai-q3-2026-earnings"]
    em_andamento: false
  - id: chatgpt-anuncios-reescritos
    titulo: "OpenAI vai reescrever anúncios do ChatGPT por padrão a partir de 29–30/10"
    tema: marketing
    urls: ["https://ppc.land/openai-to-rewrite-chatgpt-ads-by-default-as-advertisers-get-days-to-opt-out/"]
    em_andamento: false
  - id: meta-novo-mexico-multa
    titulo: "Meta condenada a pagar US$ 25 bi ao Novo México no caso Cambridge Analytica"
    tema: direito_tech
    urls: ["https://ppc.land/metas-ad-revenue-gains-26-on-the-day-a-new-mexico-judge-fines-it-25bn/"]
    em_andamento: true
formatos: [materia_principal, ia_na_pratica, economia, rodadas, stats, links, pergunta]
---
bom dia. A IA que ajuda a escrever código agora também ajuda a achar furos nele. A corrida é entre quem conserta e quem invade. E, no site em hospedagem, quem faz a atualização é o host, não você.

**Hoje eu aprendi:** dois marsupiais que a ciência dava como extintos havia 6 mil anos, um gambá-pigmeu-de-dedos-longos e um planador de cauda anelada, foram achados vivos nas florestas da Papua Ocidental. O achado, de março, teve guia de anciãos dos povos Tambrauw e Maybrat, para quem o planador é sagrado ([BBC](https://www.bbc.com/news/articles/cp814l80pw2o)).

**Nesta edição:**
- Duas falhas no coração do PHP, a linguagem por trás de **69%** dos sites, achadas com ajuda de IA. O que fazer hoje
- O Claude Duet quer ser o seu assistente de escritório. Por enquanto, só nos EUA e com fila de espera
- STF tira o ISS da base do PIS/Cofins, e o governo prepara o maior Desenrola
- A Enter ganha tempo contra a OAB-SP, e a juíza manda guardar os registros da IA
- US$ 25 bi: a conta que o Novo México mandou para a Meta

---

#### IA
## A IA achou o furo. Agora a corrida é para fechar
> **TL;DR:** o PHP corrigiu ontem (21) **2** falhas críticas que deixam um invasor rodar código no servidor; IA ajudou a achá-las, e não há proteção completa sem atualizar.

O PHP, linguagem que roda no servidor de **69,3%** dos sites cuja linguagem dá para identificar, segundo a W3Techs ([W3Techs](https://w3techs.com/technologies/details/pl-php)), soltou na quarta (21) as versões **8.5.12, 8.4.27, 8.3.36 e 8.2.35**. Elas fecham duas falhas de execução remota de código, o tipo de brecha em que um estranho manda o seu servidor fazer o que ele quiser ([PHP](https://www.php.net/archive/2026.php)).

O WordPress, que roda em PHP, está em **39,6%** de todos os sites ([W3Techs](https://w3techs.com/technologies/details/cm-wordpress)). Ou seja: site de cliente em WordPress entra na conta.

**Contexto.** A correção estava marcada para hoje (22). Foi antecipada porque as falhas vazaram na terça (20), e um vídeo de prova de conceito chegou a ser publicado por engano ([PHP Foundation](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)).

Quem achou mostra a virada. A Calif reportou o problema em **11 de agosto**, dentro do programa Patch the Planet. A OpenAI reportou no mesmo dia e mandou mais caminhos de ataque em setembro. A Wiz, de segurança, reportou em **24 de agosto** (mesma fonte) e diz ter usado o Gemini 4 Argon e o GPT-5.6 Sol na busca ([Wiz](https://wiz.io/blog/php2shell-php-rce)). Os primeiros sinais já tinham aparecido numa auditoria de 2024 ([PHP Foundation](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)).

**Os números.**
- **9,2** de 10 na escala de gravidade CVSS v4.0. O "10" que circulou estava errado ([PHP Foundation](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)).
- **15** falhas registradas (CVEs) no PHP desde 1º de julho e mais de **100** relatórios inválidos ou repetidos no mesmo período. É quase uma falha por semana, com muito ruído no meio (mesma fonte).
- O PHP 8.1 e anteriores não têm correção oficial. Há só remendos mínimos para 7.4, 8.0 e 8.1 ([PHP](https://www.php.net/archive/2026.php)).

Lê de novo: "There are no complete mitigations, updating is the only safe choice", diz a nota da versão. Não há remendo completo, só atualizar ([GitHub](https://github.com/php/php-src/releases/tag/php-8.2.35)).

**Os otimistas:** a equipe do PHP diz que não havia exploit funcional conhecido quando divulgou ([PHP Foundation](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)). O desenvolvedor Elias Taylor testou as provas públicas e diz que a falha é real, mas "not easy to exploit". As que estão no GitHub não funcionam num PHP comum ([Elias Taylor](https://eliastaylor.com/noexploit/)).

**Os pessimistas:** a Wiz diz que provou ataque sem login contra Drupal e WordPress ([Wiz](https://wiz.io/blog/php2shell-php-rce)). Segundo a Search Engine Journal, sites dos governos holandês e finlandês saíram do ar por precaução, e sites de universidades também ficaram fora ([SEJ](https://www.searchenginejournal.com/critical-php-core-security-flaws-affect-websites-including-wordpress/593812/)). E Simon Willison relata que provas de conceito circularam depois do vazamento ([Simon Willison](https://simonwillison.net/2026/Oct/21/php-security-release/)).

**Por que isso importa pra você:** atualizar o WordPress ou os plugins **não** atualiza o PHP, que fica com a hospedagem (mesma fonte). Abra Ferramentas > Saúde do Site > Info > Servidor, veja a versão e mande uma mensagem ao host perguntando se a correção está instalada. Se precisar tirar o site do ar, o Google recomenda devolver o código 503, que avisa que a parada é temporária, e por no máximo 1 a 2 dias ([SEJ](https://www.searchenginejournal.com/google-reminds-sites-to-serve-503s-during-server-downtime/593873/)).

🔗 [PHP Foundation: Today's PHP security release](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)

---

#### 🧠 IA NA PRÁTICA
## O Claude quer ser o seu secretário. Por enquanto, de longe
Pense num secretário que lê a sua caixa de entrada antes de você acordar. Ele separa o que é urgente, rascunha as respostas e te chama só quando precisa de um "sim". Você não dá ordem a cada passo; você aprova.

Isso é um agente proativo: em vez de esperar a pergunta, ele trabalha sozinho e te procura.

A Anthropic lançou na quarta (21) o Claude Duet, nessa linha. Ele roda na nuvem, conectado aos seus apps, e avisa quando termina ou quando precisa de uma decisão ([Claude](https://claude.com/product/claude-duet)). São mais de **6.000** conectores, como Gmail, Slack, Google Drive, Notion, Stripe e QuickBooks. A lista de tarefas inclui resumo matinal, rascunho de respostas, achar faturas em aberto, preparar a folha de pagamento para revisão e preparar contratos (mesma fonte). Segundo o Verge, ele pede aprovação antes de passos grandes, como pagar ou apagar algo, e concorre com o Muse, da Meta, e o Dots, da OpenAI ([The Verge](https://www.theverge.com/ai-artificial-intelligence/1015843/anthropic-claude-duet-ai-agent)).

🔗 [Claude Duet](https://claude.com/product/claude-duet)

⚠️ **Agora o freio:**
- **Não chegou aqui.** É uma prévia com fila de espera, só nos EUA e para os planos Pro e Max. Team e Enterprise ainda não entram (mesma fonte). Não há informação sobre português.
- **Ele erra a urgência.** A própria página avisa que ele pode ler errado uma conversa ou "miscalibrate what's urgent" (mesma fonte).
- **Caprichado, mas esquecido.** Claire Vo testou para a newsletter do Lenny e achou o lançamento o mais caprichado que já viu. Mesmo assim, esqueceu de usar: ele é pouco proativo, lento e não tem app de computador ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/claude-duet-is-beautiful-i-still)).
- **E os seus dados?** No Hacker News, parte da discussão questiona entregar e-mail e finanças a uma só empresa ([Hacker News](https://news.ycombinator.com/item?id=50186037)).

**Agora aplica no mundo real:**
- **Advogado:** triagem do e-mail do escritório e rascunho de resposta ao cliente. O "sim" final continua sendo do advogado.
- **Corretor de imóveis:** resumo matinal de quem pediu visita e quem sumiu, com o follow-up já escrito.
- **Dono de restaurante:** achar boleto de fornecedor vencendo e preparar a lista de pagamento da semana para revisar.

**Como isso vira serviço:** configurar o agente para um pequeno negócio. É escolher os conectores, escrever as regras do que ele pode fazer sozinho e do que precisa de aprovação, e testar com o dono por uma semana. **Opinião:** o cliente paga pela configuração e pelo manual de "o que o robô não faz", não pelo robô. Enquanto o Duet não chega aqui, a mesma lógica vale para outros agentes disponíveis.

---

#### ECONOMIA
**🇧🇷 Por aqui**

→ **STF**: por 6 a 5, com o voto de desempate de Fux, o tribunal tirou o ISS da base do PIS/Cofins; a União estima **R$ 35,4 bi** em 5 anos de devolução, mas o valor real depende da modulação, que ainda não foi decidida ([Estadão](https://www.estadao.com.br/economia/por-6-a-5-stf-exclui-iss-da-base-do-piscofins-em-derrota-de-r-354-bi-para-a-uniao/)).

→ **Desenrola 3**: o ministro Dario Durigan prevê um leilão de **até R$ 90 bi** em dívidas antigas em novembro, podendo ir ao começo de dezembro ([Estadão](https://www.estadao.com.br/economia/desenrola-3-governo-espera-comprar-r-90-bi-em-dividas-antigas-em-novembro-diz-durigan/)); se sair inteiro, pode superar os dois primeiros programas somados ([Folha](https://www1.folha.uol.com.br/mercado/2026/10/com-estimativa-de-r-90-bi-desenrola-3-pode-superar-soma-dos-dois-primeiros-programas.shtml)).

→ **MEI**: a lei sancionada ontem permite perdoar, a partir de 1º/1/2027, a parte do INSS do DAS não pago até 13/10 por cerca de **3,6 mi** de MEIs (**R$ 12,57 bi** em débitos), e sobe o teto de faturamento de **R$ 81 mil** para **R$ 110 mil** em 2027; o ISS municipal continua devido ([InvestNews](https://investnews.com.br/economia/prospera-mei-perdao-dividas/)).

→ **Hoje**: o Bradesco divulga o balanço do 3º trimestre, e técnicos da Receita comentam a arrecadação federal ([InfoMoney](https://www.infomoney.com.br/mercados/datafolha-arrecadacao-balanco-bradesco-agenda-22102026/)).

**🌎 Lá fora**

→ **Tesla**: lucro de **US$ 787 mi** no 3º trimestre, **43%** menor que um ano antes, com margem operacional de **2,6%** (era **5,8%**) e investimento mais que dobrado, a **US$ 4,7 bi** ([Ars Technica](https://arstechnica.com/cars/2026/10/tesla-profits-drop-43-in-q3/)).

→ **Meta**: elevou o piso do investimento de 2026 para **US$ 135 bi a US$ 145 bi** e vai criar uma classe de ações sem direito a voto, negociada a partir de 2027, para pagar IA, aquisições e salários ([The Verge](https://www.theverge.com/tech/1015799/meta-shares-class-ai-q3-2026-earnings)).

---

#### 🇧🇷 BRASIL ADENTRO
→ ⚖️ **Enter**: a juíza Raquel Fernandez Perrini, da 4ª Vara Cível Federal de SP, deixou para depois da produção de provas as restrições pedidas pela OAB-SP, mas mandou preservar contratos, versões dos modelos de IA e registros de uso desde janeiro de 2024, sob multa de **R$ 50 mil** por descumprimento; não é decisão sobre a legalidade do serviço ([Folha](https://c-level.folha.uol.com.br/negocios/2026/10/justica-rejeita-suspensao-imediata-de-servicos-de-startup-juridica-de-ia-por-pedido-da-oab-sp.shtml)).

→ **Keeta**: a Associação Nacional de Restaurantes entrou com ação civil pública contra a "compra intermediada" do app e pede multa diária de **R$ 10 mil** por restaurante listado sem autorização; a Keeta diz que é um piloto local ([NeoFeed](https://neofeed.com.br/negocios/a-revolta-dos-restaurantes-associacao-vai-a-justica-contra-compra-intermediada-da-keeta/)).

→ **WEG**: a receita na América do Norte cresceu **31%** em dólares no 3º trimestre, a **US$ 723 mi**, com data centers como motor, segundo a reportagem; o exterior já é **62,5%** da receita ([InvestNews](https://investnews.com.br/negocios/weg-ganha-espaco-eua-data-center/)).

#### 🌎 MUNDO AFORA
→ **Walmart**: a partir de novembro, vai deixar agentes de IA comprarem no site por um "Agent Gateway", com aprovação de toda compra por padrão; a Amazon segue bloqueando agentes, como o da Perplexity e o Muse ([The Verge](https://www.theverge.com/ai-artificial-intelligence/1015715/walmart-ai-shopping-agents)).

→ **OpenAI**: a partir de 29–30 de outubro, a empresa poderá reescrever títulos, descrições e o link de destino dos anúncios self-serve do ChatGPT sem aprovação de cada versão; quem não quiser precisa desligar no Ads Manager ([PPC Land](https://ppc.land/openai-to-rewrite-chatgpt-ads-by-default-as-advertisers-get-days-to-opt-out/)).

---

#### 📊 STATS
## US$ 25 bi
É a multa civil que um juiz do Novo México, Francis J. Mathew, mandou a Meta pagar ao estado na quarta (21), no caso ligado ao Cambridge Analytica. Um júri já tinha decidido em setembro que a empresa enganou consumidores em **43.899.720** violações ([PPC Land](https://ppc.land/metas-ad-revenue-gains-26-on-the-day-a-new-mexico-judge-fines-it-25bn/)).

Dá cerca de **39%** do que a Meta faturou no 3º trimestre inteiro (**US$ 64,6 bi**, mesma fonte). Ao câmbio de R$ 5, uns **R$ 125 bi**.

A régua da lei era maior. A **US$ 5.000** por violação, o teto passaria de **US$ 219 bi** (mesma fonte). O estado pediu de **US$ 35 bi a US$ 40 bi**, a Meta defendeu pagar no máximo **US$ 3,4 bi** e diz que vai recorrer ([AP/ABC7](https://abc7ny.com/story/judge-orders-meta-pay-25-billion-violating-new-mexico-law-cambridge-analytica-data-breach/19965355/)). Pela conta da gente, a multa ficou em uns **US$ 570** por violação.

**Opinião:** a cadeia é esta: multa por violação » cada usuário enganado vira uma linha na conta » escala de bilhões de usuários vira escala de bilhões de dólares. Para quem monta produto com dados pessoais no Brasil, a lição é a mesma da LGPD: o risco se multiplica pelo tamanho da base.

---

**Para ler:**
- [Para ler] [Today's PHP security release](https://simonwillison.net/2026/Oct/21/php-security-release/), de Simon Willison: o cronograma do vazamento, as provas que circularam e o que atualizar.
- [Para ler] [Claude Duet is beautiful. I still forgot to use it](https://www.lennysnewsletter.com/p/claude-duet-is-beautiful-i-still) (Lenny's Newsletter): o teste de Claire Vo com o agente.
- [Para ler] [The $15 billion ad-powered AI startup your doctor may already be using](https://arstechnica.com/ai/2026/10/the-15-billion-ad-powered-ai-startup-your-doctor-may-already-be-using/) (Ars Technica/FT): a OpenEvidence, usada por quase dois terços dos médicos dos EUA, vive de anúncios, mesmo com dúvidas sobre precisão.

---

**Pergunta do dia:** se um cliente seu ligasse hoje perguntando "meu site está seguro?", você saberia responder em quanto tempo?
