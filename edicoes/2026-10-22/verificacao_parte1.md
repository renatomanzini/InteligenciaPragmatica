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
