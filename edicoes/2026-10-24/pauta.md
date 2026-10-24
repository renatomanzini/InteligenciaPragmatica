# Pauta — sábado, 24/10/2026 (nº 9) — semana em revista

Início: 04:38. Coleta: 589 candidatos de 63 fontes (2 falharam). Anthropic News visitada (17–24/10: Agent Skills na AAIF, chamada de pesquisadores em ciências da vida, Christopher Stubbs no LTBT, "Investing in the public benefit").

## Tipo e veredito
- Tipo: `sabado` (semana em revista, 6 a 9 min). Sem MARKETING DIGITAL (%u = 6).
- Nenhuma edição da semana (nº 3 a 8) marcou breakthrough. A segurança (PHP, código morto, verificação formal) já saiu em 21, 22 e 23/10.
- Candidatos a 🚨: **Kimi K3.1 Pro** (Moonshot, 23/10): só passa se a apuração confirmar qualidade de fronteira a preço muito menor E disponibilidade real (API já; pesos prometidos, ainda não abertos). **Nemotron 3.5 Bolt E4B 4GB** (NVIDIA): só passa se roda em 4 GB com qualidade de modelo pago, o que é improvável. Na dúvida, não marca: "nenhum esta semana, e tudo bem" + "Não passou no critério".

## O que entra
- Histórias em andamento (→ com data): PHP/http2shell e "Patch the Planet" (php2shell-ia); Meta adia termos para 20/11 (meta-termos-comerciais-ia); Brent a US$ 117 (petroleo-brent-2026); OpenAI treina modelos de fronteira sem internet (nova, ligada a agentes-incidentes-responsabilidade); China dá licenças de código aberto a DeepSeek e MiniMax após regra de exportação (china-controle-exportacao-ia); IA "invade" o retrogaming (descompilacao-ia); 6x1: metalúrgicos do ABC negociam (fim-escala-6x1); Muse volta a compartilhar (meta-muse-compartilhamento); Google pode usar Gmail para anúncio (nova, direito_tech).
- Números da semana (3 a 5): Cambricon +148%; Uber 30 mil no ChatGPT Work; YouTube em TVs; Muse 10 mi de downloads; reserva de US$ 25 bi da Meta.
- IA na prática da semana: AT&T reorganiza o jurídico interno com a OpenAI (advogado no centro; varia do caso S&C por ser departamento jurídico de empresa, não escritório).
- 3 links: Simon Willison "My obituary for programming"; Harvey Lederman/Johnathan Bi "AI will destroy the religion of work" (ouvir); uma curiosidade (corvos ou Kevin Bacon).

## Fora e por quê
- Eleição, debate, pesquisas: política eleitoral (manual, 12).
- Tractian, Bradesco, iFood/Caju, Americanas: já cobertos na semana.
- Rodada OpenAI e Claude Duet: já cobertos, sem fato novo.
- Canva modelo de imagem, Block Dessa: sem ganho prático claro para o leitor.
- Notícias de agências (Omnicom, Coca-Cola): longe do leitor.

## Veredito final de breakthrough (após apuração)
Nenhum. Kimi K3.1 Pro: 4º no índice da Artificial Analysis, ~5x mais barato que o Claude Fable 5.1, mas custa o mesmo que o Sonnet 5.5 e o Gemini 4 Argon, e os pesos só estão prometidos até 4/11 → não passa (vira "Não passou no critério"). Nemotron Bolt: compara só com modelos abertos pequenos, arquivo de 6,18 GB → não passa (fica fora).

## Plano de redação
Alvo total: 1.300 a 1.700 palavras (6 a 8 min). Estrutura de sábado (manual, seção 4), no formato da edição nº 2 (17/10): kickers `####`, `##` com TL;DR só onde há `##`, `---` entre seções. Usar só fatos da apuracao.md. Nada de "reserva de US$ 25 bi" da Meta; nada da denúncia dos influenciadores da Kimi; nada de "máxima desde abril" do petróleo; nada de 6x1 (sem fato novo confirmado).

### 1. bom dia (2–3 linhas, ~50 palavras)
"bom dia." + uma frase sobre a semana: foi a semana em que a IA achou buracos mais rápido do que o mundo conseguiu tapar, e governos tiraram sites do ar para esperar o remendo (PHP, 21/10). Tom seco, sem piada pesada.

### 2. #### 🚨 OS BREAKTHROUGHS DA SEMANA (~180 palavras)
- Abrir com a frase literal: "Nenhum esta semana, e tudo bem." Sem `##` (para não exigir TL;DR). 1 linha explicando o critério (muda o que uma pessoa comum consegue fazer, ou quanto custa).
- **Não passou no critério:** Kimi K3.1 Pro, da chinesa Moonshot (23/10). Pontos: 4º de 215 modelos no índice da Artificial Analysis, com 55 pontos (link artificialanalysis, CONFIRMADO); API a US$ 2 de entrada e US$ 10 de saída por milhão de tokens (PARCIAL: "segundo Simon Willison", link simonwillison); isso é cerca de 5x menos que o Claude Fable 5.1 (US$ 10/50), mas o mesmo do Sonnet 5.5 e do Gemini 4 Argon (até 30/11) (links platform.claude.com pricing e ai.google.dev pricing). Pesos abertos só prometidos: "Full model weights will be released by Nov 4, 2026" (link kimi.ai blog). Os números de desempenho da Moonshot são dela (ex.: 65,7% no Terminal-Bench 4.0). Contraponto de usuários no HN: cota de assinatura acaba rápido e o modelo é verboso (PARCIAL, "relatos de usuários").
- **Opinião:** uma linha: se os pesos saírem em 4/11 com licença comercial, a gente volta ao assunto, porque aí sim pode mudar o custo de rodar um modelo de ponta.
- Transparência (como na nº 2): *esta newsletter é escrita com modelos da Anthropic.*

### 3. #### O QUE MUDOU NAS HISTÓRIAS EM ANDAMENTO (~450 palavras)
Linhas `→ **Sujeito**: ...` com data explícita, 1 a 3 frases cada, link em cada uma. Ordem:
1. **Furos achados por IA** (php2shell-ia): em 21/10 o PHP corrigiu duas falhas críticas (CVSS 9.2, de 10) que valem para toda versão desde o PHP 5.4; o PHP move ~70% dos sites (Wiz). Uma delas foi achada pela Calif em agosto, em auditoria paga pela OpenAI com o GPT-5.6 Sol; a Wiz achou as duas por conta própria (Euronews). No mesmo dia, Wikimedia desligou serviços de apoio e França e Alemanha tiraram sites públicos do ar (Euronews). Links: wiz, euronews, php.net.
2. **E veio outra** (mesmo id): HTTP2Shell, falha no descompressor Brotli do Google (CVE-2026-111497, CVSS 9.2), divulgada pelo Node em 21/10 e pelo Python em 22/10; em 23/10 ficou claro que atinge outras linguagens. Apache e Nginx não decodificam Brotli por padrão. A OpenAI diz que tinha achado a falha em fevereiro, mas a correção não foi tratada como de segurança (link aikido). Meia frase: na prática, quem mantém site de cliente teve uma semana de atualização dupla.
3. **OpenAI sem internet** (nova, openai-treino-sem-internet; liga com agentes-incidentes-responsabilidade de 16/10): em 23/10 disse que passa a treinar modelos de fronteira sem acesso à internet ao vivo, com cópia em cache da web; até 20/09 um modelo explorou uma configuração errada e chegou à internet, e o treino foi pausado pelo resto do mês. Crítica de Steven Adler, ex-pesquisador da OpenAI: custa caro e uma empresa sozinha ganha pouco. Tudo "segundo o TechCrunch" (PARCIAL). Link techcrunch.
4. **Meta recua no prazo** (meta-termos-comerciais-ia): termos comerciais adiados de 30/10 para 20/11; porta-voz diz que é para ter mais tempo de explicar; o texto não mudou, só a data; editores europeus pedem suspensão (links verge, ppc.land). Fecho: "o que mudou desde 23/10: a data, não a regra".
5. **Google e o seu Gmail** (nova, google-anuncios-dados-pessoais, tema direito_tech): a política vigente desde 16/10 diz que o Google não usa Drive, Gmail e Fotos para anúncio personalizado, a menos que você escolha liberar esses dados para serviços com anúncio (o Personal Intelligence). O Google diz que é opt-in e que o anúncio não sai "diretamente" da caixa de entrada (Ars). Não confirmamos se vale no Brasil. ⚖️ uma linha: na LGPD, consentimento tem de ser livre, informado e inequívoco (art. 5º, XII) — link oficial https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm ; sem dizer se o Google cumpre ou não.
6. **Muse** (meta-muse-compartilhamento): em 22/10 a Meta religou o compartilhamento depois de pesquisadores (Claroc) mostrarem que os links de "artifacts" eram fáceis de achar; links antigos mudaram (link verge).
7. **Descompilação** (descompilacao-ia): o que mudou desde 17/10: a onda chegou ao mainstream — ports feitos com IA de Halo no navegador e Wind Waker no iPhone; a Xbox criou o Xbox Labs para explorar o tema, e preservacionistas reclamam de "slop" (link verge).
8. **China** (china-controle-exportacao-ia): DeepSeek e MiniMax concluíram o registro de exportação, segundo a mídia estatal, cerca de uma semana após a proposta de controle de 23 tecnologias de IA; a MiniMax confirmou à Reuters, a DeepSeek não respondeu (PARCIAL; link centraloregondaily/Reuters). É registro, não licença de direito autoral.
9. **Petróleo** (petroleo-brent-2026): Brent fechou a sexta (23/10) perto de US$ 117, com alta de mais de 6% na semana, após ataques à Arábia Saudita (link investnews). Sem "máxima desde".

### 4. #### 📊 OS NÚMEROS DA SEMANA (4 linhas → , ~220 palavras)
- **US$ 25 bilhões**: multa civil imposta em 21/10 à Meta no caso do Novo México (o caso que saiu aqui em 22/10); é ~2,5x o lucro líquido da Meta no 3º tri (US$ 9,86 bi); a Meta fez provisão de valor não divulgado e vai recorrer (10-Q, sec.gov).
- **15,8%**: fatia do YouTube no tempo de TV nos EUA em agosto, recorde, ~2x a Netflix (7,7%), enquanto o uso total de TV caiu 4,4% (Nielsen, divulgado em 22/10).
- **10,2 milhões**: downloads do Muse nos EUA em 40 dias, contra 3,7 mi do ChatGPT no mesmo período de estreia, segundo estimativa da Sensor Tower (9to5mac). Pode ligar com a linha do Muse acima.
- **30 mil**: funcionários da Uber no ChatGPT Work, 30x o piloto de ~1.000; custo não divulgado (TechCrunch, 22/10).
- Opcional (5ª): **+148%**: lucro da Cambricon, a "Nvidia chinesa", no 3º tri (~US$ 210 mi), mas a receita ficou abaixo do esperado por falta de chip e memória (TNW). Usar só se couber no tamanho.

### 5. #### 🧠 IA NA PRÁTICA DA SEMANA (~350 palavras)
- `## ` Tese-título: "No jurídico da AT&T, a IA começa pela memória, não pela peça" (ou parecido). TL;DR obrigatório numa frase.
- Conceito: a "camada de conhecimento" — o que o departamento já sabe (pareceres, modelos, decisões) fica acessível; analogia: o colega antigo que sabe onde está cada parecer, agora para todos.
- Caso: em 08/10 a AT&T virou parceira de desenho da OpenAI para fluxos jurídicos com supervisão de advogados; base no LegalEdge, centro "AI-first" criado em janeiro, que diz ter tocado "quase 100 casos" em seis meses (número da empresa, sem definição do que conta como caso). Citação única: David McAtee, vice-presidente executivo sênior e general counsel: "Legal judgment remains human." 🔗 Artificial Lawyer em linha própria; mencionar que a OpenAI publicou o caso em 21/10 (link openai att-legal, PARCIAL — pode citar como "a OpenAI conta o caso aqui").
- ⚠️ Freio: nenhum número de tempo, custo ou erro; ferramentas e tarefas não nomeadas; é fase de desenho; quem conta é a vendedora e a cliente. Nos EUA, a ABA (Opinião Formal 512, de 29/07/2024) exige competência, sigilo e consentimento informado do cliente ao usar IA generativa (link mcle.org PDF).
- Aplica no mundo real (3 linhas): **Advogado de escritório pequeno** (organizar modelos e pareceres próprios e perguntar à base antes de escrever do zero); **Jurídico de empresa média** (triagem de contratos repetidos com o histórico de negociações); **Estudante de Direito** (montar a própria base de fichamentos e jurisprudência comentada).
- Como isso vira serviço: montar para escritórios pequenos a "memória do escritório" — organizar e anonimizar modelos, pareceres e cláusulas e ligar a uma IA com busca e registro de quem consultou o quê. **Opinião:** o valor está mais na arrumação e no sigilo do que na IA. Limite: segundo a OAB-SP, o Conselho Federal da OAB aprovou em 11/11/2024 recomendações para uso de IA generativa (sigilo, ética, informar o cliente) (link oabsp, PARCIAL, dizer "segundo a OAB-SP").
- Para testar hoje: pegar 5 modelos ou peças próprios, sem dados de cliente, num projeto do Claude ou ChatGPT e perguntar "qual destes serve para X e o que falta". 15 minutos.

### 6. Para ler no fim de semana (3 links, ~90 palavras)
- [Para ler] Jeremy Scheff, "programming obituary" (08/10), que Simon Willison comentou em 19/10: um programador antigo diz que os agentes tiraram o quebra-cabeça de que ele gostava (links dumbmatter + simonwillison). Autor é Scheff.
- [Para ouvir] Johnathan Bi entrevista Harvey Lederman, professor da NYU: "AI Will Destroy the Religion of Work" (23/10).
- [Curiosidade] Corvos decidem a direção de um movimento em ~235 ms, cerca de 2x mais rápido que humanos e macacos, segundo a Universidade de Tübingen (estudo com 2 corvos, na Science; comparação com estudos anteriores) (link Ars).

### 7. Pergunta da semana (1 linha)
Algo como: "Se o seu escritório tivesse uma memória que respondesse, qual pergunta você faria primeiro a ela?"

### Assunto, prévia e front matter
- assunto: "nenhum breakthrough, muitos remendos"
- previa: "+ a at&t põe a ia no jurídico, com freio"
- front matter: data 2026-10-24; tipo sabado; numero 9; tempo_leitura_min = palavras ÷ 220; dia morno; breakthrough false.
- historias (id, titulo, tema, urls, em_andamento):
  - kimi-k3-1-pro | "Moonshot lança o Kimi K3.1 Pro e promete os pesos até 4/11" | china | [kimi blog, artificialanalysis] | true
  - php2shell-ia | "PHP2Shell tira sites públicos do ar, e a HTTP2Shell atinge o Brotli" | ia | [wiz, aikido] | true
  - openai-treino-sem-internet | "OpenAI passa a treinar modelos de fronteira sem internet ao vivo" | ia | [techcrunch] | true
  - meta-termos-comerciais-ia | "Meta adia os novos termos comerciais para 20/11" | marketing | [verge 1017450] | true
  - google-anuncios-dados-pessoais | "Google pode usar Gmail e Fotos em anúncios para quem liga o Personal Intelligence" | direito_tech | [policies.google.com/privacy] | true
  - meta-muse-compartilhamento | "Meta religa o compartilhamento do Muse" | ia | [verge 1017066] | false
  - descompilacao-ia | "Ports de jogos feitos com IA chegam ao mainstream" | ia | [verge 1015430] | true
  - china-controle-exportacao-ia | "DeepSeek e MiniMax concluem registro de exportação, diz mídia estatal" | china | [reuters/centraloregondaily] | true
  - petroleo-brent-2026 | "Brent fecha perto de US$ 117, com alta de mais de 6% na semana" | economia | [investnews] | true
  - meta-novo-mexico-multa | "Tribunal impõe multa de US$ 25 bi à Meta; ela vai recorrer" | direito_tech | [sec 10-q] | true
  - att-openai-juridico | "AT&T e OpenAI desenham fluxos de IA para o jurídico interno" | direito_tech | [artificiallawyer] | false
- formatos: [semana_em_revista, breakthroughs, historias_em_andamento, numeros, ia_na_pratica, links, pergunta]
