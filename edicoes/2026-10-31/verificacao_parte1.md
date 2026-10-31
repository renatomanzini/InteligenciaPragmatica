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
