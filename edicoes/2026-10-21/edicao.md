---
data: 2026-10-21
tipo: dia_util
numero: 6
assunto: "a anthropic faturou us$ 16,3 bi e perdeu us$ 80,7 bi"
previa: "+ o código que você não usa é a porta que você esqueceu aberta"
tempo_leitura_min: 8
dia: morno
breakthrough: false
historias:
  - id: anthropic-receita-ipo
    titulo: "Rascunho do prospecto da Anthropic: US$ 16,3 bi de receita e US$ 80,7 bi de prejuízo no 1º semestre"
    tema: ia
    urls:
      - "https://techcrunch.com/2026/10/20/anthropics-cloud-partnerships-are-getting-messy/"
      - "https://www.investing.com/news/stock-market-news/anthropic-revenue-hits-163-billion-as-preliminary-s1-outlines-ipo-risks--wsj-4960928"
    em_andamento: true
  - id: claude-superficie-ataque
    titulo: "Anthropic usa o Claude para cortar código desnecessário exposto a ataque em 25 projetos abertos"
    tema: ia
    urls: ["https://www.anthropic.com/research/attack-surface-reduction"]
    em_andamento: false
  - id: emudhra-certificados
    titulo: "Chaves de 8 certificados intermediários da eMudhra vazam, e navegadores bloqueiam"
    tema: ia
    urls: ["https://emudhra.we-have-a-problem.com/"]
    em_andamento: false
  - id: spacex-ia-receita
    titulo: "IA já é 52% da receita da SpaceX"
    tema: economia
    urls: ["https://techcrunch.com/2026/10/20/spacexs-ai-business-is-beating-expectations/"]
    em_andamento: false
  - id: ifood-caju
    titulo: "iFood Benefícios compra a Caju"
    tema: negocios
    urls: ["https://neofeed.com.br/startups/ifood-beneficios-compra-caju-por-mais-de-r-12-bilhao/"]
    em_andamento: false
  - id: anima-einstein
    titulo: "Ação da Ânima cai 9% após acordo com o Einstein"
    tema: negocios
    urls: ["https://investnews.com.br/negocios/r-600-milhoes-em-jogo-por-que-o-mercado-reagiu-mal-ao-acordo-da-anima-com-o-einstein/"]
    em_andamento: false
  - id: salesforce-braze
    titulo: "Salesforce compra a Braze por cerca de US$ 5,66 bi"
    tema: marketing
    urls: ["https://ppc.land/salesforce-agrees-to-buy-braze-for-5-66bn-in-cash/"]
    em_andamento: false
  - id: anthropic-projeto-lei-seguranca
    titulo: "Anthropic leva ao Congresso dos EUA rascunho de lei de segurança de IA"
    tema: direito_tech
    urls: ["https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed/"]
    em_andamento: true
  - id: meta-muse-compartilhamento
    titulo: "Meta pausa o compartilhamento de conversas do Muse"
    tema: ia
    urls: ["https://www.theverge.com/tech/1014627/meta-muse-ai-sharing-ai-chats"]
    em_andamento: false
formatos: [continuacao, materia_principal, ia_na_pratica, economia, rodadas, stats, links, pergunta]
---
bom dia. Hoje a pauta é sobre conta que não fecha à primeira vista. A empresa que faz a ferramenta que você mais usa perdeu cinco vezes o que faturou. E o código que mais te protege pode ser o que você apaga.

**Hoje eu aprendi:** 16 anos depois do vazamento da Deepwater Horizon, a vida nas águas profundas do Golfo do México ainda não voltou. Peixes, crustáceos e lulas de profundidade caíram de **60% a 85%** em três anos e meio, e a queda dura mais de uma década. Os autores dizem que o vazamento é a explicação mais simples, mas não provam a causa ([Yale E360](https://e360.yale.edu/digest/deepwater-horizon-deep-sea-recovery); [PNAS](https://www.pnas.org/doi/full/10.1073/pnas.2616554123)).

**Nesta edição:**
- O prospecto da Anthropic vazou: receita 15 vezes maior e um prejuízo que é quase todo contábil
- Menos código, menos porta: a Anthropic pôs o Claude para achar o que fica exposto sem necessidade, e ele apontou 493 problemas
- iFood compra a Caju, e o mercado não gostou do preço que a Ânima vai pagar ao Einstein
- A SpaceX já fatura mais com IA do que com foguete

---

#### IA
## O que mudou desde 19/10: a Anthropic abriu (sem querer) o livro-caixa
> **TL;DR:** um rascunho do prospecto de IPO visto pelo WSJ mostra **US$ 16,3 bi** de receita no 1º semestre de 2026 e **US$ 80,7 bi** de prejuízo, quase tudo ajuste contábil.

O Wall Street Journal viu um rascunho do S-1 da Anthropic, o documento que uma empresa entrega à SEC antes de vender ações na bolsa. A receita do 1º semestre foi de **US$ 16,3 bi**, contra **US$ 1,1 bi** um ano antes ([Investing.com](https://www.investing.com/news/stock-market-news/anthropic-revenue-hits-163-billion-as-preliminary-s1-outlines-ipo-risks--wsj-4960928)). Dá **15 vezes** mais.

O documento ainda não é público. Na base da SEC não há S-1 da Anthropic ([SEC](https://www.sec.gov/cgi-bin/browse-edgar?company=anthropic&type=S-1)). Tudo o que vem a seguir é o que a imprensa leu no rascunho.

**Contexto.** No dia 17, a gente contou que a Anthropic teria dito a investidores ter faturado **US$ 16,8 bi** só no 3º trimestre. No dia 19, contou que ela prometeu 5% das ações a um fundo de benefício público. Agora aparecem os custos.

**Os números.**
- **Prejuízo de US$ 80,7 bi** no semestre. Cerca de **US$ 72 bi** são ajustes contábeis ligados a dívidas conversíveis e outros instrumentos financeiros, sem saída de caixa ([Investing.com](https://www.investing.com/news/stock-market-news/anthropic-revenue-hits-163-billion-as-preliminary-s1-outlines-ipo-risks--wsj-4960928)). Sem eles, pela conta da gente, sobram uns **US$ 9 bi** de perda.
- **Computação:** quase **US$ 9 bi** em seis meses, mais que os **US$ 7,3 bi** de 2025 inteiro (mesma fonte).
- **Nuvem:** compromissos de cerca de **US$ 450 bi** em dez anos com Google (**US$ 111 bi**), AWS (**US$ 110 bi**) e Microsoft (**US$ 31 bi**) (mesma fonte).
- **Concentração:** dois clientes respondem por cerca de **20%** da receita ([TechCrunch](https://techcrunch.com/2026/10/20/anthropics-cloud-partnerships-are-getting-messy/)).

A Anthropic também tem dificuldade para garantir capacidade de computação com os provedores de nuvem. Por isso aluga data centers e recorre a operadores com "limited operating history", pouco histórico, que ela mesma vê como risco. Outro risco declarado: ser responsabilizada por danos da IA acima do que o seguro cobre (mesma fonte).

**Os otimistas:** a receita cresceu 15 vezes, e a maior parte do prejuízo não é dinheiro saindo. Se o 3º trimestre de US$ 16,8 bi se confirmar, um trimestre fatura mais do que o semestre inteiro.

**Os pessimistas:** os US$ 450 bi de compromisso, espalhados por dez anos, equivalem a cerca de **14 vezes** um ano de receita no ritmo do semestre (US$ 32,6 bi), conta da gente. E a empresa depende de rivais para ter máquina.

**Por que isso importa pra você:** o Claude Code roda nessa conta, e o próprio prospecto lista falta de capacidade e dependência de terceiros como risco. **Opinião:** quem vende serviço em cima de uma única ferramenta herda o risco do fornecedor (preço, limite de uso, fila no horário de pico). Vale ter um plano B testado, nem que seja um prompt que funcione em outro modelo.

🔗 [TechCrunch: Anthropic's cloud partnerships are getting messy](https://techcrunch.com/2026/10/20/anthropics-cloud-partnerships-are-getting-messy/)

---

#### 🧠 IA NA PRÁTICA
## O código que você não usa é a porta que você esqueceu aberta
Pense num apartamento com sete portas. Você usa duas. As outras cinco ficam fechadas com trinco velho, e o ladrão não precisa achar a fechadura fraca se você simplesmente emparedar as portas que não usa.

Isso é reduzir a superfície de ataque: em vez de caçar cada falha, cortar o código que fica exposto sem necessidade. Assim a falha que ninguém achou ainda nem tem por onde entrar.

A Anthropic testou a ideia com o Claude em **25** projetos de código aberto, com mais de **5 milhões** de linhas. O modelo inventariou mais de **17.000** opções de configuração, das quais **3.842** mexem com segurança, e apontou **493** problemas ([Anthropic](https://www.anthropic.com/research/attack-surface-reduction)).

Exemplos do post, assinado por Chris Rohlf, do Frontier Red Team, o time que testa riscos dos modelos:
- **162** combinações de configuração perigosas eram aceitas sem erro, aviso ou documentação. Em **94**, um controle de segurança era desligado sem ninguém saber.
- No OpenSSH 10.4, cerca de **4.500** linhas de código experimental podiam ser alcançadas por quem nem tinha feito login, cerca de **16%** de todo o código que roda antes da autenticação. A versão 10.6 terminou de corrigir.

🔗 [Anthropic: Using Claude to reduce the attack surface of code](https://www.anthropic.com/research/attack-surface-reduction)

⚠️ **Agora o freio:**
- **É pesquisa inicial**, como o próprio post define. Parte dos achados não era explorável sozinha, e o post não diz quantos dos 493 foram corrigidos.
- **Não tem receita de bolo.** O método usa testes automáticos para conferir que nada quebrou. Sem testes, apagar código "que ninguém usa" pode derrubar o seu site.
- **Às vezes a porta é de outro.** Esta semana se descobriu que as chaves privadas de **8** certificados intermediários da eMudhra, uma autoridade certificadora, foram geradas de um jeito que permitia recuperá-las. Com elas, daria para se passar por qualquer site. Firefox e Chrome bloquearam desde o dia 17, a Apple no dia 19 e a Microsoft no dia 20 ([eMudhra incident](https://emudhra.we-have-a-problem.com/)); o caso foi resumido por [Simon Willison](https://simonwillison.net/2026/Oct/20/emudhra-certificates/). Nenhum corte de código seu resolveria isso: aí é atualizar navegador e sistema.

**Agora aplica no mundo real:**
- **Advogado:** num contrato de desenvolvimento de site, dá para prever quem atualiza as dependências e quem desliga o que não se usa. Fica claro de quem era a tarefa se algo vazar.
- **Dono de e-commerce:** plugin instalado e esquecido na loja é porta aberta. Tirar o que não vende é segurança, não faxina.
- **Clínica médica:** sistema com módulo de teleconsulta que ninguém usa ainda é um caminho até o prontuário.

**Como isso vira serviço:** uma revisão de "o que dá para desligar" em sites de pequenos negócios feitos em WordPress ou em código gerado por IA. Entrega: lista do que foi removido, teste de que nada quebrou e relatório para o cliente. **Opinião:** o cliente paga porque um vazamento custa mais caro que a revisão.

**Para testar hoje:** num projeto seu com Git, peça ao Claude Code: "liste dependências, rotas e arquivos que parecem não ser usados, e explique o risco de cada um. Não apague nada". Leia a lista antes de mexer.

---

#### ECONOMIA
**🇧🇷 Por aqui**

→ **Ontem (20)**: o Ibovespa subiu **1,57%**, a **208,3 mil** pontos, e devolveu com sobra a queda de **0,17%** da véspera; o dólar caiu **0,58%**, a **R$ 5,019** ([InfoMoney](https://www.infomoney.com.br/mercados/ibovespa-hoje-bolsa-de-valores-ao-vivo-20102026/)).

→ **Panda bonds**: o governo prepara a primeira emissão de títulos em yuan na China, começando com **5 bi de yuans**, num total buscado de cerca de **10 bi** (**US$ 1,5 bi**), para depois do 2º turno, segundo fonte ouvida pela Bloomberg ([InvestNews](https://investnews.com.br/economia/brasil-prepara-primeira-emissao-de-panda-bonds-para-depois-da-eleicao-presidencial/)).

→ **Hoje**: a WEG divulga o balanço do 3º trimestre antes da abertura, e sai a 2ª prévia do IGP-M de outubro às 8h ([InfoMoney](https://www.infomoney.com.br/mercados/pesquisa-quaest-balancos-weg-meta-tesla-21102026/)).

**🌎 Lá fora**

→ **SpaceX**: lucro líquido de **US$ 4,4 bi** no 3º trimestre, com receita de **US$ 14,6 bi**; a receita foi engordada por cerca de **US$ 1 bi** ligado à alta do Bitcoin e a partes relacionadas ([TechCrunch](https://techcrunch.com/2026/10/20/spacexs-ai-business-is-beating-expectations/)).

→ **Hoje**: Meta e Tesla divulgam os balanços do 3º trimestre ([InfoMoney](https://www.infomoney.com.br/mercados/pesquisa-quaest-balancos-weg-meta-tesla-21102026/)).

---

#### 🇧🇷 BRASIL ADENTRO
→ **iFood**: o iFood Benefícios vai comprar a Caju, somando **1,7 mi** e **1,3 mi** de usuários; o valor não foi divulgado, e o NeoFeed fala em mais de **R$ 1,2 bi**; depende do Cade e do BC ([NeoFeed](https://neofeed.com.br/startups/ifood-beneficios-compra-caju-por-mais-de-r-12-bilhao/)).

→ **Ânima**: a ação caiu **9%** ontem depois do acordo para usar a marca Einstein em **15** cursos de medicina por **20 anos**, com **R$ 150 mi** de entrada e custo total estimado pelo BTG acima de **R$ 600 mi** ([InvestNews](https://investnews.com.br/negocios/r-600-milhoes-em-jogo-por-que-o-mercado-reagiu-mal-ao-acordo-da-anima-com-o-einstein/)).

→ **Patria**: o fundo imobiliário HGRU11 acertou a compra de **22** imóveis de lojas do Atacadão para alugá-las de volta ao varejista, por cerca de **R$ 1 bi** segundo fontes de mercado; o Patria não comenta ([NeoFeed](https://neofeed.com.br/negocios/exclusivo-patria-acerta-compra-de-22-lojas-do-atacadao-por-cerca-de-r-1-bilhao/)).

#### 🌎 MUNDO AFORA
→ **Salesforce**: vai comprar a Braze, plataforma de mensagens de marketing, por **US$ 47,50** por ação em dinheiro, um valor de empresa de cerca de **US$ 5,66 bi**; o fechamento é esperado no ano fiscal de 2028 da Salesforce, que começa em fevereiro de 2027 ([PPC Land](https://ppc.land/salesforce-agrees-to-buy-braze-for-5-66bn-in-cash/)).

→ **Yelp**: vai cobrar **US$ 30** por mês, a partir de novembro, por um agente que responde e qualifica pedidos de orçamento; o atendente de telefone por IA foi lançado a **US$ 99** ([PPC Land](https://ppc.land/yelp-charges-30-a-month-for-ai-agent-that-answers-and-qualifies-leads-2/)).

→ **Meta**: pausou o compartilhamento de conversas do Muse depois que pesquisadores da Claroc acharam mais de **6.800** links públicos, alguns com dados de empresas e um pedido de empréstimo ([The Verge](https://www.theverge.com/tech/1014627/meta-muse-ai-sharing-ai-chats)).

→ ⚖️ **Anthropic**: mostra a congressistas dos EUA um rascunho de lei, revelado pelo Politico, em que o Departamento de Comércio precisa pedir a um juiz federal de Washington para suspender um modelo com risco iminente a mais de **50** pessoas ou de mais de **US$ 1 bi** em danos materiais; as agências não podem barrar sozinhas ([TechCrunch](https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed/)).

---

#### 📊 STATS
## 52%
É quanto a IA já responde do que a SpaceX ganha, segundo o TechCrunch. Em receita do 3º trimestre, são **US$ 7,5 bi** de **US$ 14,6 bi**, pouco mais da metade. O segmento, rebatizado de "Super Intelligence", junta o Grok, o Cursor (ferramenta de programação comprada há pouco) e o aluguel de computação, com **1,7 GW** de capacidade ([TechCrunch](https://techcrunch.com/2026/10/20/spacexs-ai-business-is-beating-expectations/)).

A empresa dos foguetes já fatura mais com IA do que com todo o resto junto.

Só que a IA deu **US$ 431 mi** de lucro (seria mais sem **US$ 1,2 bi** de remuneração em ações ligada à compra do Cursor), e a SpaceX gastou **US$ 19,6 bi** em investimento no trimestre, mais do que faturou. Para o 4º trimestre, a previsão de investimento é de **US$ 35 bi a US$ 40 bi** (mesma fonte).

**Opinião:** a cadeia é esta: receita de IA cresce » mais data center » mais investimento que receita » a conta só fecha se a demanda continuar subindo. É a mesma aposta da matéria principal, vista de outro lado do balcão.

---

**Para ler:**
- [Para ler] [What Shall I Teach My Son?](https://stevekrouse.com/ends), de Steve Krouse: um programador prestes a ser pai pergunta para que serve a escola quando a habilidade dele perde valor. Inspirado em *The End of Education*, de Neil Postman.
- [Curiosidade] [Battle Drones](https://simonwillison.net/2026/Oct/20/battledrones/), de Simon Willison: um jogo de estratégia estilo Command & Conquer feito quase todo por agentes, em **321** commits, com multiplayer por som entre aparelhos próximos.
- [Para ler] [We can do impossible things](https://www.technologyreview.com/2026/10/21/1146053/editor-letter-we-can-do-impossible-things/) (MIT Technology Review): abre a edição sobre ideias que parecem impossíveis, de sangue sintético a conversar com animais.

---

**Pergunta do dia:** se a ferramenta em que você mais confia subisse de preço amanhã, quantos dias o seu trabalho aguentaria?
