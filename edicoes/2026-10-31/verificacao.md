# Verificação — 2026-10-31

Correções obrigatórias das duas partes aplicadas na revisão (Opus). DoorDash 993 mi conferido no release da SEC por curl; OpenAI/Anthropic no sinal do robots.txt conferido no Search Engine Roundtable 42430; 'low-double-digit' do Reddit conferido no PPC Land.

# Verificação, parte 1 (abertura até o fim de "O que mudou nas histórias em andamento") — 2026-10-31

Método: páginas baixadas com curl (e WebFetch quando bloqueado) e lidas. Bloqueios: BleepingComputer (Cloudflare; lido via WebFetch), Search Engine Journal (403; lido via WebFetch), WSJ (paywall).

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Abertura: "a bolsa teve a maior queda desde 2020" | InvestNews | confirmada (pior semana desde mar/2020) | nenhuma |
| 2 | Abertura: "corretora de cripto perdeu US$ 6,3 bi em cerca de 20 minutos" | Wired | **errada (exagero)**: Wired/TRM dizem que "a maior parte" dos US$ 6,3 bi saiu em ~20 min | "perdeu US$ 6,3 bi, a maior parte em cerca de 20 minutos" |
| 3 | Abertura: "as big techs combinaram como pedir licença antes de treinar IA" | Google Search Central (30/10) | parcialmente confirmada: o post do Google só fala do plano do Google e de "outros provedores"; Bing, OpenAI e Anthropic não aparecem no texto citado (conferir na parte 2) | trocar por "o Google e outras empresas" ou citar fonte que nomeie as demais |
| 4 | Gemini 4 Carbon (28/10), só para grupo de defensores de cibersegurança, sem data para o público | blog Google | confirmada (data 28/10, "subset of cyber defenders", "soon") | nenhuma |
| 5 | Gemini 4 Carbon: US$ 2 / US$ 10 por milhão (introdutório), depois US$ 4 / US$ 20 | blog Google | confirmada | nenhuma |
| 6 | Genie 4 (27/10): modelo de mundo, interativo por teclado, prévia só para testadores | DeepMind | confirmada (27/10, research preview para trusted testers, controles de teclado) | nenhuma |
| 7 | GPT-6.1 Terra a US$ 1 / US$ 5, "cerca de metade do preço do Sol", segundo Willison | Willison 26/10 | confirmada ("almost half the price of GPT-5.6 Terra and GPT-6.1 Sol") | nenhuma |
| 8 | "está longe de uma queda de 10 vezes" | Willison | frase é juízo do jornal, sem selo; ok como contexto do critério, mas é avaliação | opcional: marcar como **Opinião:** ou reescrever como fato ("metade do preço, não um décimo") |
| 9 | Willison (28/10): em outubro a IA passou a fazer jogos divertidos; "Building games that play well is shockingly easy now." | Willison 28/10 | confirmada (citação literal, 12 palavras; data 28/10) | nenhuma |
| 10 | "e o difícil virou o design" | Willison 28/10 | confirmada em substância ("new challenge is coming up with concepts...") | nenhuma |
| 11 | "**Opinião:** um modelo de fronteira que você não pode usar..." | n/a | opinião com selo | ok |
| 12 | Extensão Claude Code: em 29/10, ~11 horas, v2.1.313, "Claude Code for VS Code", marketplace do Cursor | BankInfoSecurity; BleepingComputer | confirmada (quinta 29/10, 9:27 a 20:35 UTC) | nenhuma |
| 13 | Instalava chave SSH do atacante (acesso remoto) | BankInfoSecurity (Cursor: adiciona chave a authorized_keys, abre túnel reverso) | confirmada. Ressalva da fonte: sem privilégio de admin o túnel falha, mas chave e persistência são instaladas | opcional: dizer isso |
| 14 | Enviava usuário, e-mail do Git e **nomes** (não valores) de variáveis KEY/TOKEN/SECRET | BankInfoSecurity (McCarty) | confirmada (nomes de até 40 variáveis com KEY, TOKEN, SECRET, PASS, AWS, GCP; hostname, usuário local, e-mail Git global). A fonte diz que não ficou claro se os dados chegaram ao servidor, mas o Cursor diz que "sends host details" | opcional: "tentava enviar" |
| 15 | Cursor: no máximo 5.000 usuários, "um teto" | BankInfoSecurity ("at most 5,000 users") | confirmada | nenhuma |
| 16 | Anthropic diz que não fez nem publicou a versão | BankInfoSecurity (Anthropic: "not involved with building, publishing or hosting") | confirmada | nenhuma |
| 17 | 2.1.314 é limpa; atualizar não remove o que foi instalado | BankInfoSecurity (Beaumont) | confirmada | nenhuma |
| 18 | Procurar a chave "svc-telemetry" em authorized_keys; se achar, isolar e trocar segredos | BleepingComputer (via WebFetch) | confirmada (svc-telemetry, isolar, rodar segredos). BankInfoSecurity não traz o nome da chave nem a troca de segredos, só o BleepingComputer | nenhuma |
| 19 | Ibovespa −18,12% na semana, pior desde março de 2020; fechou sexta (30/10) a 167.922 pts | InvestNews | confirmada | nenhuma |
| 20 | Segunda (26/10): queda de 14%, com circuit breaker (pausa automática) | InvestNews | confirmada | nenhuma |
| 21 | "É a 4ª maior queda semanal do século; a maior foi 10/10/2008 (−20,01%)" | InfoMoney | confirmada com ressalva: a tabela mostra 2008 (−20,01%), 2020 (−18,88%), 2001 (−18,12%) e 2026 (−18,12%): **empate com 2001** a duas casas | "entre as quatro maiores do século (empatada com a de 2001)" ou manter "4ª" ciente do empate |
| 22 | Dólar fechou a R$ 5,44, alta de 9% na semana | InvestNews | confirmada | nenhuma |
| 23 | Fundos perderam R$ 157,5 bi do dia seguinte à eleição até 28/10, segundo a Economática | Folha C-Level | confirmada (até quarta-feira; 28/10) | nenhuma |
| 24 | Itaú: PIB 2027 de 1,2% para 0,5%; IPCA de 4,6% para 6,1%; teto da meta 4,5% | Folha | confirmada | nenhuma |
| 25 | "Na conta do banco: dólar mais caro e mais imposto sobre combustível » inflação 2027 acima do teto » Selic parada em 13,75% em todo 2027" | Folha | confirmada em substância (volta do PIS/Cofins, ICMS, dólar depreciado; Selic em 13,75% ao longo de 2027) | nenhuma |
| 26 | Binance: ~20 min, ao menos 36 h de preparação, segundo TRM Labs | Wired | confirmada ("majority... around 20 minutes"; "at least 36 hours") | nenhuma |
| 27 | TRM e Chainalysis apontam TraderTraitor; Elliptic considera provável Coreia do Norte; nem Binance nem governos atribuíram | Wired | confirmada, mas "apontam" é mais forte que a fonte ("may be behind", "initially linked"). Elliptic "não ligou ao grupo", só vê sobreposição (o texto diz "Coreia do Norte", correto) | opcional: "TRM e Chainalysis ligam o ataque ao TraderTraitor" |
| 28 | Congelados US$ 2,8 bi (44%), quase tudo stablecoins; US$ 3,3 bi em BTC, ETH e XRP não congeláveis | Wired (Elliptic) | confirmada (a Wired diz "mostly" Bitcoin/Ether/XRP) | opcional: "em sua maioria" |
| 29 | Binance diz que cobrirá todas as perdas; admite "pontos adicionais de violação" além do notebook | Wired | confirmada em substância; as aspas são tradução do original "additional points of breach" | tirar as aspas ou indicar que é tradução |
| 30 | "o que mudou desde 30/10 é o desenho do ataque" | Wired (30/10) | **inconsistente**: a fonte é do próprio dia 30/10, não há "mudança desde 30/10". Provável intenção: desde 29/10/o primeiro relato | trocar por "o que mudou desde a primeira notícia (29/10)" |
| 31 | Anthropic: S-1 de 26/10; FT diz que Blackstone espera "alto junk"; Anthropic e Blackstone não comentaram | Anthropic; TechCrunch | confirmada (S-1 anunciado 26/10; "double B", topo do grau especulativo; ambos declinaram comentar) | nenhuma |
| 32 | OpenAI: WSJ diz menos da metade da meta de US$ 30 bi, US$ 1,25 tri, abaixo de US$ 1,4 tri buscados | WSJ | não verificável (paywall/401). Sustentada por outros veículos que citam o WSJ (cerca de US$ 11 bi comprometidos, US$ 1,25 tri, antes US$ 1,4 tri), mas todos são secundários | manter, mas atribuir "segundo o WSJ" (já está) |
| 33 | "desde 23/10, quando falamos de US$ 30 bi a US$ 1,25 tri" | edição anterior | não conferida nesta fonte (autorreferência) | conferir a edição de 23/10 |
| 34 | Reddit: em outubro perdeu em média mais de 1 milhão de visitas/semana vindas da busca | PPC Land (carta aos acionistas) | confirmada | nenhuma |
| 35 | Usuários diários (130,3 mi) podem cair "dois dígitos baixos" no 4º trimestre | PPC Land | confirmada com ajuste: a carta diz base de "130 million", o 130,3 mi vem do título do PPC; condicional ("se o ritmo continuar"); aspas são tradução de "low-double-digit" | acrescentar "se o ritmo continuar"; tirar aspas ou marcar tradução |
| 36 | Huffman apontou AI Overviews e AI Mode como hipótese principal | Search Engine Journal (WebFetch) | confirmada ("biggest part of Reddit's working hypothesis is Google's AI Overviews and AI Mode"). Nota: o PPC Land diz que a **carta** não atribui a causa; a atribuição foi na teleconferência, como a edição escreve | nenhuma |
| 37 | Reddit vai testar login obrigatório fora dos EUA nos próximos meses | PPC Land | confirmada ("select markets outside the U.S. in the coming months") | nenhuma |
| 38 | Cyrus Shepard: ~0,9% de cliques em respostas de IA, estudo de um site só | Search Engine Roundtable | confirmada (~0.9% CTR, "small case study") | nenhuma |
| 39 | Raízen: em 30/10 credores aprovaram a recuperação extrajudicial; passivo R$ 65 bi; credores ~80%; Shell 13% a 15%; aporte R$ 3,5 bi | NeoFeed | confirmada | nenhuma |
| 40 | "A empresa se divide em Energia e Combustíveis a partir da 2ª quinzena de dezembro" | NeoFeed | confirmada em parte: a cisão se conclui na 2ª quinzena de dezembro; as duas empresas começam a operar em meados de janeiro de 2027 | "a cisão se conclui na 2ª quinzena de dezembro; as duas começam a operar em janeiro" |
| 41 | Kimi K3.1 Pro: pesos ainda não estavam no HF da Moonshot em 31/10 | Hugging Face | confirmada por ausência (a página não lista K3.1; só K3, K2.x) | nenhuma |
| 42 | Prazo prometido para os pesos é 4/11 | link HF citado | **não confirmada na fonte citada** (a página do HF não menciona prazo). O 4/11 vem da edição/pauta de 24/10 | citar a fonte do prazo (blog Kimi) ou escrever "prazo prometido na edição de 24/10" |
| 43 | Termos comerciais da Meta seguem para 20/11, "sem mudança" | PPC Land (23/10) | confirmada para 23/10 (30/10 para 20/11); "sem mudança" **não é sustentado** por fonte posterior a 23/10, o PPC ainda apontava página UK com data antiga | trocar por "adiados para 20/11 (anúncio de 23/10)", sem afirmar que nada mudou desde então |

## Opinião sem selo
- Item 8 ("longe de uma queda de 10 vezes"): leve, é avaliação editorial. O resto das opiniões da parte tem selo ou é atribuído.
- Item 25: o encadeamento é do Itaú (atribuído "na conta do banco"); ok.
- Nenhuma recomendação de investimento encontrada.

## Aspas
- "Building games that play well is shockingly easy now." existe na fonte, literal.
- "dois dígitos baixos", "pontos adicionais de violação": traduções entre aspas; não são citação literal. Retirar aspas ou sinalizar tradução.
- "junk", "alto junk": ok (fonte usa "high junk").

## Correções obrigatórias
1. Abertura: "perdeu US$ 6,3 bi em cerca de 20 minutos" vira "perdeu US$ 6,3 bi, a maior parte em cerca de 20 minutos" (item 2).
2. Abertura: "as big techs combinaram..." só tem o Google na fonte citada; ajustar ou conferir Bing/OpenAI/Anthropic na parte 2 (item 3).
3. Binance: "o que mudou desde 30/10" é inconsistente com a fonte datada de 30/10 (item 30).
4. Kimi: o prazo de 4/11 não está na página citada (item 42); citar a origem.
5. Meta: remover "sem mudança" ou atribuir à data de 23/10 (item 43).
6. Ibovespa: informar o empate com 2001 ao dizer "4ª maior" (item 21).
7. Raízen: separar cisão (2ª quinzena de dezembro) de início das operações (janeiro) (item 40).
8. Reddit: acrescentar a condição ("se o ritmo de queda continuar") e tirar aspas de tradução (item 35); mesma regra para "pontos adicionais de violação" (item 29).

Não verificável: WSJ (paywall), item 32; sustentado indiretamente por veículos que citam o WSJ.

# Verificação, parte 2 (Números da semana até a pergunta) - edição 2026-10-31

Método: WebFetch e curl simples nas fontes citadas. SEC bloqueou o acesso automatizado (não contornei). `main.py github` falhou (HTTP 403, repositório não habilitado na sessão); estrelas conferidas pela página do GitHub via WebFetch e a data pelo `git log` de um clone raso.

| Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|
| Desemprego 5,2% no trimestre até setembro, IBGE, divulgado 30/10 | Estadão (30/10/2026) | confirmada | - |
| Menor taxa para o trimestre desde 2012 | Estadão: "a menor taxa para o período desde 2012, início da série" | confirmada | - |
| Contra 5,6% um ano antes | Estadão: 5,6% no 3º tri de 2025 | confirmada | - |
| "FGV e Inter já veem perda de fôlego" | Estadão: FGV IBRE projeta alta do desemprego em 2027; Inter diz que o mercado está "muito próximo do pico" | confirmada (com nuance) | Ideal: "FGV prevê alta do desemprego em 2027; Inter vê o mercado perto do pico". |
| DoorDash: "algumas centenas" de pedidos de agentes de IA de terceiros, Tony Xu, no total, sem período | TechCrunch: "maybe several hundred orders in total from some of these third-party agents" (teleconferência do 3º tri) | confirmada | Opcional: "talvez algumas centenas". |
| 993 milhões de pedidos no 3º trimestre | Link SEC (press release). A SEC bloqueou o acesso automatizado; o TechCrunch não traz esse número | NÃO CONFIRMADA | Abrir o release no navegador e conferir "Total Orders" do 3T26 e o escala (milhões). Se não conferir, cortar o número ou apontar só a fonte que o traz. |
| Microsoft: ~11% da receita vem de acordos com a OpenAI, US$ 10 bi de US$ 92,3 bi, trimestre até 30/09 | Startups: "quase 11%", US$ 10 bi, US$ 92,3 bi, trimestre encerrado em 30/9 | confirmada | Conta 10/92,3 = 10,8%, coerente. |
| "Não se sabe quanto é repasse e quanto é Azure" | Startups: a Microsoft não detalhou | confirmada | - |
| Kalshi vale US$ 40 bi | Folha/C-Level: rodada avalia em US$ 40 bi (Tarek Mansour, 29/10) | confirmada | - |
| Alta de 82% desde maio (US$ 22 bi) | Folha: rodada de maio a US$ 22 bi; o "82%" não está na fonte, é conta (40/22 = +81,8%) | confirmada (número calculado) | Dizer "alta de cerca de 82%, pela nossa conta" ou "de US$ 22 bi em maio". |
| Quase o dobro da Polymarket (US$ 21 bi) | Folha: "quase o dobro"; Polymarket US$ 21 bi era a rodada de agosto "sendo finalizada" | confirmada (com nuance) | Acrescentar "na rodada de agosto". |
| Fujifilm quer 5 vezes a capacidade de fitas LTO "até o ano fiscal de 2028" | Ars Technica: 5x sobre o nível do ano fiscal de 2025; projeto roda dos anos fiscais 2026 a 2028 | confirmada (com ressalva) | "5x em relação ao ano fiscal de 2025, com o projeto indo até o ano fiscal de 2028". |
| Cerca de ¥10 bi (~US$ 63 mi) | Ars: "roughly 10 billion yen (about $63 million)" | confirmada | - |
| IA generativa aumentou a demanda por arquivar dados | Ars: Fujifilm atribui a alta à IA generativa | confirmada | Deixar claro que é a atribuição da Fujifilm. |
| "na prática, a fita, barata e fora da rede, voltou a ter emprego" | Ars não diz "barata" nem "fora da rede" (diz que o mundo corporativo nunca abandonou a fita) | NÃO CONFIRMADA / opinião sem selo | Cortar, ou reescrever como fato da fonte ("a fita nunca saiu das empresas") ou pôr `**Opinião:**`. "Voltou" também contraria a fonte. |
| IA na prática: em 30/10 o Google (John Mueller) anunciou controle novo baseado no AIPREF do IETF | Post do Google, sexta 30/10/2026, assinado por John Mueller, cita o AIPREF do IETF | confirmada | - |
| Meta é 2027 e é rascunho, não padrão | Google: "We aim to support this new control along with other AI providers in 2027"; "This draft proposal" | confirmada | - |
| Linha `user-agent: __usage_ai-training` com Disallow, "segundo SER e PPC"; o post do Google não a escreve | PPC Land traz o token `__usage_ai-training`. O post do Google fala em "policy token" e não a escreve. O SER (pelo que consegui ler) não menciona a linha | parcialmente confirmada | Atribuir a linha só ao PPC Land. A ressalva de que o Google não a escreve está correta. |
| Se o site recusar treino pelo token e não mencionar Google-Extended, o Google trata como se estivesse bloqueado | Google: "Google plans to interpret that as if the publisher had disallowed Google-Extended" | confirmada | Trocar "trata" por "pretende tratar" (é plano para 2027). |
| Bing separou treino de "grounding" (usar a página para montar resposta com citação) | SER e PPC: AI Training, AI Grounding e Limited Grounding | confirmada | - |
| Dá para recusar treino e seguir citado no Copilot; ranking normal do Bing não muda | SER: exemplo de editor que bloqueia treino e permite citação no Copilot; "traditional Bing rankings are unaffected" | confirmada | - |
| Bing passa a valer em 01/02/2027 | SER/PPC: 1/2/2027 "Microsoft starts honoring the new preferences as it crawls" | confirmada | - |
| Bing: controles temporários em 15/12 e migração das regras antigas até 01/03/2027 | SER/PPC: 15/12/2026 (para quem usa NoArchive/NoCache); 1/3/2027 prazo para quem usa as diretivas antigas | confirmada | Ressalva: 15/12 vale só para sites com NoArchive/NoCache. Falta citar 30/09/2027 (fim das preferências temporárias), opcional. |
| "OpenAI e Anthropic também aderem, segundo as mesmas fontes" | SER: OpenAI e Anthropic "on board". PPC: OpenAI publicou compromisso; Anthropic "reportedly", citando o SER. O post do Google não os menciona | confirmada (fraca para Anthropic) | Trocar por "segundo o Search Engine Roundtable" e, para a Anthropic, "segundo relato". Cuidado também com o título da história no front matter ("Google, Bing, OpenAI e Anthropic apoiam"). |
| Freio: Nate Hake, "editor que participou do grupo", diz que o trabalho está incompleto, segundo o PPC Land | PPC: Hake, "publisher" do grupo, alertou no X que o trabalho está inacabado (paráfrase, sem citação) | confirmada (cargo impreciso) | Trocar "editor" por "publisher/dono de site de mídia". Sem aspas, ok. |
| "E não se sabe o efeito sobre as AI Overviews na busca do Google" | Nenhuma fonte afirma isso; o post do Google não trata das AI Overviews | NÃO CONFIRMADA | Reescrever: "o post do Google não diz se o sinal vale para as AI Overviews" (verdadeiro como ausência) ou cortar. |
| "O robots.txt vale por educação, não por fechadura / é um pedido, não uma tranca" | Contexto geral, sem fonte específica | não confirmada (explicação genérica) | Aceitável como explicação; evitar tom de fato novo. |
| UE: Diretiva 2019/790, art. 4(3), só libera mineração de texto e dados se o titular não reservou o direito | legislation.gov.uk (art. 4): "has not been expressly reserved by their rightholders in an appropriate manner, such as machine-readable means in the case of content made publicly available online" (texto da UE, sem alteração) | confirmada | - |
| Aspas "por meios legíveis por máquina" | O texto oficial em inglês é "such as machine-readable means"; a versão portuguesa oficial (EUR-Lex PT) não conferi e não é essa frase literal | ASPAS NÃO VERIFICADAS | Tirar as aspas (parafrasear) ou copiar a redação exata da versão PT do EUR-Lex. Usar "reservado expressamente, de forma adequada, p. ex. por meios de leitura automática". |
| "Um sinal padronizado dá forma a essa reserva" | Inferência; o post do Google cita o Código de Práticas da UE (GPAI), não o art. 4(3) | opinião/inferência sem selo | Pôr `**Opinião:**` ou escrever "o Google cita o Código de Práticas de IA de uso geral da UE, que reconhece o robots.txt". |
| Oportunidades (advogado, e-commerce, jornalista) e o serviço "política de IA do site" | Sugestões editoriais | n/a | A frase "**Opinião:** é serviço pequeno..." tem selo. "Por que agora" usa as datas do Bing (confirmadas). |
| Link SigNoz (28/02/2026): "quando a IA resolve 95% dos incidentes, o humano piora nos 5% que importam" | SigNoz, 28/02/2026, "AI Isn't Replacing SREs. It's Deskilling Them.": o 95%/5% é pergunta hipotética, sem dado | PARCIAL (enganoso) | Escrever "e se a IA resolver 95% dos incidentes: o humano piora nos 5% que importam?" e deixar claro que a divisão é hipotética. |
| Verge (Lauren Feiner, 30/10): Wikimedia, em amicus brief, diz que treinar IA deve ser fair use, mas regurgitar artigos não | Verge, 30/10/2026, Lauren Feiner: amicus brief (sexta), sem apoiar nenhum lado no caso NYT x OpenAI | confirmada | "Pode ter paywall" não conferi (a página abriu por curl). |
| nesformer: Drew Breunig pôs a CPU do NES nos pesos do Qwen3.5-4B, Super Mario roda "very slowly" | Simon Willison (30/10): "emulator for a NES 6502 CPU into the weights of Qwen3.5-4B ... (very slowly)" | confirmada | - |
| Repositório criado em 30/10 | Clone raso: 1 commit, 30/10/2026 08:59 -0700. A API de criação não ficou acessível | confirmada (por indício) | - |
| 194 estrelas em 31/10 | Página do GitHub (WebFetch): 194 estrelas. `main.py github` falhou (403), então não foi pelo comando do manual | confirmada (por página) | Rodar `python main.py github dbreunig/nesformer` na máquina com token antes de enviar, para registrar a contagem. |
| Pergunta da semana | Sem afirmação factual | n/a | - |

Sem aspas inventadas encontradas, fora a do art. 4(3). A citação de Willison "very slowly" é do post dele, curta.

## Correções obrigatórias

1. **993 milhões de pedidos (DoorDash)**: não confirmado (TechCrunch não traz, SEC bloqueou). Conferir no release da SEC ou cortar o número.
2. **Fujifilm**: cortar ou selar como opinião "a fita, barata e fora da rede, voltou a ter emprego"; corrigir "até o ano fiscal de 2028" para "5x em relação ao ano fiscal de 2025, projeto até o ano fiscal de 2028".
3. **Art. 4(3)**: remover as aspas de "por meios legíveis por máquina" (ou usar a redação exata da versão PT) e selar com `**Opinião:**` a frase "Um sinal padronizado dá forma a essa reserva".
4. **"Não se sabe o efeito sobre as AI Overviews"**: reescrever como "o post do Google não diz" ou cortar.
5. **SigNoz**: marcar que o 95%/5% é hipotético, não dado.
6. **Google-Extended**: trocar "trata" por "pretende tratar".
7. **Linha `user-agent: __usage_ai-training`**: atribuir só ao PPC Land (o SER não a traz, pelo que li).
8. **OpenAI e Anthropic**: atribuir ao Search Engine Roundtable (e a Anthropic como "segundo relato"); o Google não os cita. Rever o título da história robots-txt-treino-ia no front matter.
9. **Estrelas do nesformer**: rodar `main.py github` com token antes do envio (hoje só a página do GitHub mostra 194).

Menores (opcionais): Nate Hake é "publisher", não "editor"; "82%" é conta nossa; Polymarket US$ 21 bi é da rodada de agosto; Bing 15/12 vale só para quem usa NoArchive/NoCache.
