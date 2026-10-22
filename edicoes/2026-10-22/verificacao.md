# Verificação — 2026-10-22

Duas checagens independentes (Sonnet). Todas as correções obrigatórias foram aplicadas na edicao.md: terça (não segunda) 20/10; Patch the Planet sem atribuir à OpenAI; HN 'parte da discussão'; SEJ precaução só nos sites de governo; selos de opinião; sigilo profissional cortado; Keeta multa diária; LiteLLM sem 'trocar chaves' e ~1h40 no PyPI; teto de US$ 219 bi atribuído ao PPC Land; Meta 'no máximo US$ 3,4 bi' e 'diz que vai recorrer'; Desenrola com Estadão e 'pode superar'; agenda de hoje ajustada; MEI 'permite perdoar' com corte e vigência; Enter multa por descumprimento; OpenAI no condicional e link de destino; Mercado Ads topo de funil; WEG atribuída à reportagem; Lenny sem duração de vídeo; Simon Willison citado no lado pessimista. M. Dias Branco cortada por tamanho.

# Verificação – Parte 1 (abertura até o fim do IA na prática)

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | Marsupiais dados como extintos havia 6 mil anos (gambá-pigmeu-de-dedos-longos, planador de cauda anelada), achados vivos na Papua Ocidental | BBC | confirmada | – |
| 2 | "O achado, de março" | BBC (matéria de 6/3/2026, estudo publicado na sexta) | confirmada (é a data da publicação do estudo) | Opcional: "publicado em março" |
| 3 | Guia de anciãos dos povos Tambrauw e Maybrat; planador sagrado | BBC | confirmada (clãs; "sagrado: nem caçam nem dizem o nome") | – |
| 4 | PHP em 69,3% dos sites com linguagem identificável | W3Techs pl-php | confirmada (69.3%) | – |
| 5 | "69%" no bloco Nesta edição | idem | confirmada (arredondado de 69,3) | – |
| 6 | PHP 8.5.12, 8.4.27, 8.3.36 e 8.2.35 soltos na quarta (21); duas falhas de RCE | php.net/archive/2026 | confirmada (21/10, "unauthenticated RCE") | – |
| 7 | WordPress em 39,6% de todos os sites | W3Techs cm-wordpress | confirmada | – |
| 8 | "o site do seu cliente provavelmente está nessa" | – | inferência sem selo | Suavizar ("pode estar") ou marcar como opinião |
| 9 | Correção marcada para hoje (22), antecipada para 21 | PHP Foundation | confirmada | – |
| 10 | Falhas vazaram **na segunda (20)** | PHP Foundation: "Tuesday, October 20th" (20/10/2026 é terça) | **errada** | Trocar "segunda (20)" por "terça (20)" |
| 11 | Vídeo de PoC publicado por engano | PHP Foundation (Calif publicou por engano) | confirmada | – |
| 12 | Calif reportou em 11 de agosto | PHP Foundation | confirmada | – |
| 13 | Calif atuou "no Patch the Planet, programa da OpenAI" | PHP Foundation diz só "Patch the Planet program" e que a PHP Foundation colocou o PHP nele; nada diz que é da OpenAI. Wiz também não explica | **não confirmada** | Cortar "programa da OpenAI" ou achar fonte que diga quem o opera |
| 14 | OpenAI reportou no mesmo dia e mandou mais caminhos de ataque em setembro | PHP Foundation (mesma causa, 11/8; novos vetores 18/9) | confirmada | – |
| 15 | Wiz reportou em 24 de agosto | PHP Foundation e Wiz (timeline) | confirmada | – |
| 16 | Wiz diz ter usado Gemini 4 Argon e GPT-5.6 Sol | Wiz | confirmada | – |
| 17 | Primeiros sinais numa auditoria de 2024 | PHP Foundation (auditoria Quarkslab 2024 achou os primeiros sinais do problema de OOM). Sem link na frase | confirmada (falta link) | Citar o link da PHP Foundation na frase |
| 18 | CVSS 9,2 de 10; o "10" estava errado | PHP Foundation e php.net ("CVSS v4.0 9.2"; "10.0" errado) | confirmada | Opcional: dizer "CVSS v4.0" |
| 19 | 15 falhas registradas desde 1º/7 | PHP Foundation: "15 CVEs since July 1st" | confirmada (são CVEs) | Opcional: "15 CVEs" |
| 20 | Mais de 100 relatórios inválidos ou repetidos | PHP Foundation ("invalid, duplicates, or not reproducible") | confirmada | – |
| 21 | "Quase uma falha por semana" | cálculo (15 em ~16 semanas) | confirmada (cálculo) | – |
| 22 | PHP 8.1 e anteriores sem correção oficial; remendos mínimos para 7.4, 8.0, 8.1 | php.net/archive/2026 | confirmada | – |
| 23 | Citação "There are no complete mitigations, updating is the only safe choice" | GitHub release php-8.2.35 (obtida via WebFetch; curl/API deram 403) | confirmada, texto exato | – |
| 24 | Equipe do PHP: sem exploit funcional conhecido ao divulgar | PHP Foundation ("did not identify any functional exploits at the time of release") | confirmada | – |
| 25 | Elias Taylor testou as provas públicas; "not easy to exploit"; as do GitHub não funcionam num PHP comum | eliastaylor.com/noexploit | confirmada | – |
| 26 | Wiz diz ter provado ataque sem login contra Drupal e WordPress | Wiz | confirmada | – |
| 27 | Sites holandeses, finlandeses e de universidades saíram do ar por precaução | SEJ (Dutch parliament/NCSC e Finnish gov: precaução; a matéria não dá motivo para as universidades) | parcialmente confirmada | Escrever "sites do governo holandês e finlandês e de universidades saíram do ar antes da divulgação; para os holandeses e finlandeses, por precaução" |
| 28 | Atualizar WordPress/plugins não atualiza o PHP | SEJ 593812 ("will not update PHP") | confirmada | – |
| 29 | Caminho Ferramentas > Saúde do Site > Info > Servidor | SEJ 593812 | confirmada | – |
| 30 | Google recomenda 503, por no máximo 1 a 2 dias | SEJ 593873 (cita doc do Google: "longer than 1-2 days" não recomendado) | confirmada | – |
| 31 | PS: "ontem a gente falou de usar IA para fechar portas que você não usa" | edição 21/10 (título "O código que você não usa é a porta que você esqueceu aberta") | confirmada | – |
| 32 | Abertura: "A mesma IA que escreve o seu site agora acha os furos dele" / "Hoje a resposta depende de uma atualização que nem é você quem faz" | – | opinião/generalização sem selo (IA que acha ≠ a que escreve o site) | Reformular como fato ou marcar `**Opinião:**` |
| 33 | Anthropic lançou o Claude Duet na quarta (21) | The Verge (21/10) e página do produto (sem data) | confirmada | – |
| 34 | Roda na nuvem, conectado aos apps, avisa ao terminar ou ao precisar de decisão | claude.com/product/claude-duet | confirmada | – |
| 35 | "Mais de 6.000" conectores: Gmail, Slack, Drive, Notion, Stripe, QuickBooks | página do produto ("more than 6,000 connectors and plugins") | confirmada | – |
| 36 | Tarefas: resumo matinal, rascunho de respostas, faturas em aberto, folha para revisão, contratos | página do produto | confirmada | – |
| 37 | Verge: pede aprovação antes de passos grandes (pagar, apagar); concorre com Muse (Meta) e Dots (OpenAI) | The Verge | confirmada | – |
| 38 | Prévia com fila, só EUA, Pro e Max; Team e Enterprise fora | página do produto e Verge | confirmada | – |
| 39 | "miscalibrate what's urgent" | página do produto e Verge | confirmada | – |
| 40 | Claire Vo achou o lançamento o mais caprichado que já viu | Lenny ("the most polished agent launch I've seen") | confirmada | Opcional: "o lançamento de agente mais caprichado" |
| 41 | Esqueceu de usar; pouco proativo; lento; sem app de computador | Lenny (proatividade, latência, falta de app desktop) | confirmada; "lento" é paráfrase de reclamação sobre latência | – |
| 42 | HN: "a discussão mais acesa é sobre entregar e-mail e finanças a uma só empresa" | HN item 50186037: tema existe, mas as trocas mais acaloradas são sobre se comentários eram escritos por IA ("AI psychosis"); outros temas: fila de espera, UX | **errada / exagerada** | "No Hacker News, parte da discussão questiona entregar e-mail e finanças a uma só empresa" |
| 43 | Cenários (advogado, corretor, restaurante) e "Como isso vira serviço" (cobrar pela configuração e pelo manual do que o robô não faz; "o mesmo serviço vale com os agentes que já existem por aqui") | – | opinião/aposta sem selo | Marcar `**Opinião:**` |
| 44 | Título "…Mas ainda é estagiário" e "Bonito não é útil" | – | opinião sem selo | Marcar como opinião ou neutralizar |
| 45 | Advogado: "o sim final continua sendo do advogado, inclusive pelo sigilo profissional" | – | afirmação sem fonte (norma profissional) | Cortar "inclusive pelo sigilo profissional" ou citar fonte (Estatuto da OAB/CED) |

## Correções obrigatórias
1. Trocar "vazaram na segunda (20)" por "terça (20)" (fonte diz Tuesday; 20/10/2026 é terça).
2. Remover "programa da OpenAI" do Patch the Planet (não confirmado em nenhuma fonte lida) ou apresentar fonte.
3. Corrigir a frase do Hacker News: a discussão mais acesa não é sobre privacidade, e sim sobre comentários supostamente gerados por IA. Reescrever como "parte da discussão".
4. Ajustar a frase da SEJ: o motivo "por precaução" vale para os sites holandeses e finlandeses, não para universidades (motivo não dado).
5. Colocar o selo `**Opinião:**` (ou transformar em fato com fonte) em: "provavelmente está nessa", a abertura ("a mesma IA que escreve o seu site…"), "Como isso vira serviço" com "o mesmo serviço vale com os agentes que já existem por aqui", e o título/rótulo "ainda é estagiário"/"Bonito não é útil".
6. Cortar ou fontear "inclusive pelo sigilo profissional" (item advogado).
7. Recomendado: link na frase da auditoria de 2024; dizer "15 CVEs" e "CVSS v4.0".

Observações: BBC, GitHub e The Verge bloquearam o WebFetch em parte; li BBC e Verge por curl e o release php-8.2.35 via WebFetch (a API do GitHub deu 403). O vídeo de "16 minutos" do Lenny está na Parte 2 e não foi confirmado pela página (marcadores vão até 15:05).

# Verificação — Parte 2 (ECONOMIA até Pergunta) — edição 2026-10-22

Método: cada link aberto (WebFetch ou curl). Folha (Desenrola) e Estadão aparecem só parcialmente (paywall/resumo). Conteúdo da web tratado como dado.

| # | Afirmação | Fonte | Status | Correção sugerida |
|---|---|---|---|---|
| 1 | STF decidiu por 6 a 5 excluir ISS da base do PIS/Cofins | Estadão | confirmada | — |
| 2 | Voto de desempate de Fux | Estadão | confirmada | Julgamento estava 5 a 5 e faltava o voto de Fux. |
| 3 | União estima R$ 35,4 bi em 5 anos | Estadão | confirmada | Fonte: estimativa da LDO 2026, "até R$ 35,4 bi", considera 5 anos. Pode citar "até". |
| 4 | Valor real depende da modulação, ainda não decidida | Estadão | confirmada | — |
| 5 | Desenrola 3: leilão de até R$ 90 bi em dívidas antigas | Folha | confirmada | — |
| 6 | Leilão "entre o fim de novembro e o começo de dezembro" | Folha | não confirmada | A página da Folha só diz "em novembro" (título de matéria relacionada) e "pode comprar até R$ 90 bi". Trocar por "em novembro" ou achar fonte da janela. |
| 7 | "mais que os R$ 81,6 bi somados dos dois primeiros programas" | Folha | parcialmente confirmada | A Folha diz "pode superar" (não "mais que") e não traz a soma. Traz R$ 53,2 bi (Desenrola 1) e R$ 28,37 bi (Desenrola 2.0) = 81,57. É conta nossa: escrever "pode superar os cerca de R$ 81,6 bi (R$ 53,2 bi + R$ 28,4 bi) dos dois primeiros". |
| 8 | MEI: lei sancionada "ontem" (21/10) | InvestNews | confirmada | — |
| 9 | Perdoa a parte do INSS do DAS não pago de cerca de 3,6 mi de MEIs | InvestNews | parcialmente confirmada | A fonte diz que 3,6 mi "poderão ter dívidas perdoadas" e que o perdão é de 100% da parcela previdenciária elegível, com corte de dívidas até 13/10/2026 e vigência em 1/1/2027. Trocar "perdoa" por "permite perdoar" e dizer "até 13/10/2026". |
| 10 | R$ 12,57 bi em débitos | InvestNews | confirmada | Fonte: "débitos federais que poderão ser cancelados". Valor potencial. |
| 11 | Teto de R$ 81 mil para R$ 110 mil em 2027 | InvestNews | confirmada | (Fonte ainda cita R$ 140 mil em 2028.) |
| 12 | ISS municipal continua devido | InvestNews | confirmada | — |
| 13 | Hoje (22) saem arrecadação federal de setembro e balanço do Bradesco | InfoMoney | parcialmente confirmada | Bradesco confirmado. Arrecadação: a página só diz que dois técnicos da Receita comentam a arrecadação de setembro; não diz que o dado sai hoje. Datas do texto são inconsistentes ("quarta (22)"/"quinta (22)"; 22/10/2026 é quinta). Confirmar na Receita ou escrever "Receita comenta a arrecadação de setembro". |
| 14 | Tesla: lucro de US$ 787 mi no 3T, queda de 43% | Ars Technica | confirmada | — |
| 15 | Margem operacional 2,6% (era 5,8%) | Ars Technica | confirmada | — |
| 16 | Investimento "mais que dobrado", a US$ 4,7 bi | Ars Technica | confirmada | Fonte: capex +110% para US$ 4,7 bi. |
| 17 | Meta elevou o piso do investimento 2026 para US$ 135-145 bi | The Verge | confirmada | Antes: US$ 130-145 bi. |
| 18 | Nova classe de ações sem voto, negociada a partir de 2027, para IA, aquisições e salários | The Verge | confirmada | — |
| 19 | Enter: juíza Raquel Fernandez Perrini, 4ª Vara Cível Federal, restrições só após provas | Folha | confirmada | Decisão de quarta (21). |
| 20 | Preservar contratos, versões dos modelos e registros de uso desde janeiro de 2024 | Folha | confirmada | — |
| 21 | "sob multa de R$ 50 mil" | Folha | parcialmente confirmada | A fonte diz "multa por ato de descumprimento de R$ 50 mil". Escrever "multa de R$ 50 mil por descumprimento". |
| 22 | "na prática, a briga vai ser decidida pelo que a máquina guardou" | — | opinião sem selo | A Folha diz o contrário do "decidida": a juíza afirma que a medida não é juízo sobre a legalidade do modelo. Cortar ou virar `**Opinião:**`. |
| 23 | Keeta: ANR entrou com ação civil pública contra a "compra intermediada" | NeoFeed | confirmada | Ação protocolada no TJ-SP. |
| 24 | "pede multa de R$ 10 mil por restaurante listado sem autorização" | NeoFeed | errada (omissão) | É "multa **diária** de R$ 10 mil por restaurante listado de forma indevida". Corrigir. |
| 25 | Keeta diz que é um piloto local | NeoFeed | confirmada | — |
| 26 | Mercado Ads lançou o Engage+, IA que automatiza campanhas de vídeo e display | Meio & Mensagem | parcialmente confirmada | A fonte limita a campanhas de topo de funil (awareness). Acrescentar "de topo de funil". |
| 27 | Sinais de mais de 131 mi de compradores do Mercado Livre | Meio & Mensagem | confirmada | — |
| 28 | M. Dias Branco: R$ 208,4 mi por 80% da Grespan, pães congelados | InvestNews | confirmada | — |
| 29 | Grespan faturou R$ 138,7 mi em 2025; primeira compra em 4 anos | InvestNews | confirmada | — |
| 30 | WEG: América do Norte +31% em dólares, US$ 723 mi no 3T | InvestNews | confirmada | — |
| 31 | "puxada por data centers" | InvestNews | parcialmente confirmada | É leitura da reportagem; a WEG não divulga a fatia de data centers. Escrever "que a reportagem atribui em grande parte a data centers". |
| 32 | Exterior já é 62,5% da receita | InvestNews | confirmada | Fonte chama de recorde. |
| 33 | Walmart: a partir de novembro, agentes de IA compram via "Agent Gateway"; aprovação de toda compra por padrão | The Verge | confirmada | Fonte: "next month"; o Gateway já está em beta. |
| 34 | Amazon segue bloqueando agentes, como o da Perplexity e o Muse | The Verge | confirmada | — |
| 35 | OpenAI: a partir de 29-30/10 reescreve títulos, descrições e links dos anúncios self-serve do ChatGPT, sem aprovação de cada versão, opt-out no Ads Manager | PPC Land | parcialmente confirmada | Datas divergem na própria fonte (e-mail: 30/10; página de ajuda: 29/10), o que justifica "29-30". Fonte usa "may" (pode reescrever) e fala em "otimizar a URL de destino", não "reescrever links". Ajustar: "poderá reescrever ... e ajustar o link de destino". Opt-out vale "antes de 30/10". |
| 36 | LiteLLM 1.107.0 publicada no PyPI na quarta (21), com ladrão de credenciais | SafeDep | confirmada | — |
| 37 | Ficou no ar por menos de 2 horas | SafeDep | confirmada com ressalva | No PyPI, cerca de 1h44. As imagens Docker ficaram cerca de 2h34. Escrever "no PyPI". |
| 38 | Voltar à 1.106.2 | SafeDep | confirmada | 1.106.2 é listada como limpa. |
| 39 | "e trocar todas as chaves" | SafeDep | não confirmada | A SafeDep não recomenda isso. Reformular: "quem instalou deve checar os indicadores de comprometimento e, se achar, trocar as credenciais expostas (a fonte descreve roubo de SSH, nuvem, CI/CD e chaves de LLM)". Marcar como recomendação nossa, ou cortar. |
| 40 | STATS: juiz Francis J. Mathew mandou a Meta pagar US$ 25 bi na quarta (21), caso Cambridge Analytica | PPC Land | confirmada | — |
| 41 | Júri decidiu em setembro que enganou consumidores em 43.899.720 violações | PPC Land | confirmada | O número exato só está no PPC Land. A AP/ABC7 diz "over 43 million". |
| 42 | Cerca de 39% do faturamento do 3T (US$ 64,6 bi) | PPC Land | confirmada | 25/64,6 = 38,7%. Cálculo nosso, explícito. |
| 43 | Ao câmbio de R$ 5, uns R$ 125 bi | — | confirmada (cálculo) | Conversão aritmética correta. Declarada como premissa. |
| 44 | "A US$ 5.000 por violação, o teto passaria de US$ 219 bi" | PPC Land (não a AP/ABC7) | número atribuído ao link errado | US$ 5.000 e US$ 219,5 bi estão no PPC Land. A AP/ABC7 não traz nenhum dos dois. A citação AP/ABC7 no fim do parágrafo induz a erro. Citar PPC Land para esta frase. |
| 45 | "Mesmo assim, saiu barato pela régua da lei" | — | opinião sem selo | Julgamento. Mover para o bloco `**Opinião:**` ou reescrever neutro ("ficou abaixo do teto de US$ 219 bi"). |
| 46 | Estado pediu US$ 35-40 bi | AP/ABC7 | confirmada | — |
| 47 | Meta propôs cerca de US$ 3,4 bi | AP/ABC7 | parcialmente confirmada | A AP diz que a Meta defendeu pagar "no more than $3.4 billion" (teto). Escrever "defendeu pagar no máximo US$ 3,4 bi". |
| 48 | Meta vai recorrer | AP/ABC7 | parcialmente confirmada | A AP diz que a Meta planeja recorrer do veredito do júri. Escrever "diz que vai recorrer". |
| 49 | "uns US$ 570 por violação" | — | confirmada (cálculo) | 25 bi / 43.899.720 = US$ 569,4. Rotulado como "conta da gente". |
| 50 | Bloco `**Opinião:**` (cadeia multa por violação e lição da LGPD) | — | ok | Tem selo. |
| 51 | Para ler: Simon Willison, "o resumo mais claro do vazamento e do que atualizar" | Simon Willison | confirmada (página existe) | "o mais claro" é juízo subjetivo sem selo; trocar por "resumo do vazamento e do que atualizar". A página fala em exploits em circulação, o que deve ser conciliado com a Parte 1 ("não havia exploit funcional conhecido"). |
| 52 | Para ler: Lenny's, teste de Claire Vo, "com vídeo de 16 minutos" | Lenny's Newsletter | parcialmente confirmada | Autora e conteúdo ok. Duração não consta na página (capítulos vão até 15:05). Cortar "16 minutos" ou dizer "cerca de 15 minutos". |
| 53 | Para ler: OpenEvidence, usada por quase dois terços dos médicos dos EUA, US$ 15 bi, anúncios, Ars/FT | Ars Technica | confirmada | "Nearly two-thirds of US doctors", avaliação US$ 15 bi, texto de Rafe Rosner-Uddin (FT). "vive de anúncios" é forte; a fonte diz "ads-powered". |
| 54 | "Um modelo de negócio para olhar com lupa" | — | opinião sem selo | Reescrever neutro ou trocar por `**Opinião:**`. |
| 55 | Pergunta do dia | — | sem fatos | Ok. |

## Correções obrigatórias

1. **Keeta**: a multa de R$ 10 mil é **diária** por restaurante. Corrigir.
2. **LiteLLM**: remover ou reformular "trocar todas as chaves" (a SafeDep não diz isso). Especificar "no PyPI" para "menos de 2 horas" (Docker ficou ~2h34).
3. **Stats, número no link errado**: US$ 5.000 por violação e teto de US$ 219 bi estão no PPC Land, não na AP/ABC7. Corrigir a atribuição.
4. **Opiniões sem selo**: "na prática, a briga vai ser decidida pelo que a máquina guardou" (Enter, e contradiz a fonte), "saiu barato pela régua da lei" (Stats) e "um modelo de negócio para olhar com lupa" (Para ler). Cortar, neutralizar ou usar `**Opinião:**`.
5. **Desenrola 3**: tirar "entre o fim de novembro e o começo de dezembro" (a fonte só dá "em novembro") e trocar "mais que os R$ 81,6 bi" por "pode superar os cerca de R$ 81,6 bi", explicando que a soma é nossa (R$ 53,2 bi + R$ 28,4 bi).
6. **Hoje**: a arrecadação federal não está confirmada como divulgação de hoje (a página só diz que a Receita comenta o dado de setembro, e as datas do texto se contradizem). Ajustar ou checar na Receita.
7. **MEI**: trocar "perdoa" por "permite perdoar" e incluir o corte (dívidas até 13/10/2026) e a vigência de 1/1/2027.
8. **Enter**: multa de R$ 50 mil é "por ato de descumprimento".
9. **Meta (Stats)**: "propôs US$ 3,4 bi" deve ser "defendeu pagar no máximo US$ 3,4 bi"; "vai recorrer" deve ser "diz que vai recorrer".
10. **Para ler**: cortar "vídeo de 16 minutos" (não confirmado) e "o resumo mais claro" (subjetivo).
11. **OpenAI**: usar o condicional ("poderá reescrever"), trocar "links" por "link de destino" e lembrar que o opt-out vale até 30/10.
12. **Mercado Ads**: acrescentar "de topo de funil" (a automação se limita a esse tipo de campanha).
13. **WEG**: atribuir "puxada por data centers" à reportagem.

Pontos de atenção (sem erro): a página do Simon Willison diz que já há exploits em circulação e a Parte 1 diz "não havia exploit funcional conhecido" quando divulgou. Convém conferir a consistência entre as duas.
