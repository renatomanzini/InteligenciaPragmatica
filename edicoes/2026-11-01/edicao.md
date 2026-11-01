---
data: 2026-11-01
tipo: domingo
numero: 14
assunto: "quem pode dizer 'não aprenda comigo'?"
previa: "+ jefferson, a vela e a placa do robots.txt"
tempo_leitura_min: 5
dia: morno
breakthrough: false
historias:
  - id: ensaio-quem-pode-recusar-treino
    titulo: "Ensaio: conhecimento comum, treino de IA e quem pode dizer 'não aprenda comigo'"
    tema: filosofia
    urls: ["https://press-pubs.uchicago.edu/founders/documents/a1_8_8s12.html", "https://www.seroundtable.com/google-ai-training-control-42430.html"]
    em_andamento: false
  - id: robots-txt-treino-ia
    titulo: "OpenAI e Anthropic também planejam aderir ao sinal comum contra treino no robots.txt, segundo o Search Engine Roundtable"
    tema: direito_tech
    urls: ["https://www.seroundtable.com/google-ai-training-control-42430.html"]
    em_andamento: true
  - id: anthropic-restricoes-uso
    titulo: "Usuários relatam que o Claude recusa clonar jogos e tarefas de 'treinar concorrente'; Anthropic não comenta"
    tema: ia
    urls: ["https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked"]
    em_andamento: true
  - id: selic-copom-2026
    titulo: "Copom decide a Selic em 04/11, com 13,75% e aposta de manutenção"
    tema: economia
    urls: ["https://neofeed.com.br/economia/itau-ve-fim-do-ciclo-de-cortes-da-selic-diante-de-cenario-mais-adverso/"]
    em_andamento: true
  - id: kimi-k3-1-pro
    titulo: "Pesos do Kimi K3.1 Pro prometidos até 4/11 ainda não saíram"
    tema: china
    urls: ["https://www.kimi.ai/blog/kimi-k3-1-pro"]
    em_andamento: true
formatos: [ensaio, filosofia, em_3_linhas, pergunta]
---
bom dia. Domingo é dia de ensaio: um tema da semana, pensado com calma. Ensaio é texto de opinião. Os fatos têm fonte, e o resto é argumento.

---

#### ENSAIO
## Quem pode dizer "não aprenda comigo"?

> **TL;DR:** na mesma semana, sites ganharam um jeito de dizer à IA "não treine comigo", e uma empresa de IA foi acusada por usuários de dizer o mesmo a eles; a pergunta é quem tem esse direito.

Em março de 2014, o Stack Overflow recebeu **207.204** perguntas novas. Em julho de 2026, recebeu **1.442**, uma queda de **99%** ([PPC Land](https://ppc.land/stack-overflow-drops-to-1-442-questions-in-july-down-99-from-2014-peak/)). Cada resposta ali foi escrita por alguém que não cobrou por ela. Quantas viraram material de treino de IA?

Agora a semana. Em 30/10, Google e Bing anunciaram apoio a um sinal único no robots.txt (o arquivo em que um site diz aos robôs o que não pode ser lido) para recusar treino de IA, e OpenAI e Anthropic também planejam aderir, segundo o [Search Engine Roundtable](https://www.seroundtable.com/google-ai-training-control-42430.html). No dia 31, o [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked) relatou que usuários dizem que o Claude passou a recusar clonar jogos e algumas tarefas de engenharia reversa. No [Hacker News](https://news.ycombinator.com/item?id=50319358), uma discussão repercutiu o tweet de um usuário que diz ter sido marcado por "training a competitor". É relato de usuário, sem confirmação.

Todo mundo quer dizer "não aprenda comigo". Quem pode?

*Transparência: esta newsletter é escrita com modelos da Anthropic.*

### Ideia tem dono?
Em 1813, Thomas Jefferson escreveu a Isaac McPherson que quem acende a vela na minha "receives light without darkening me", ou seja, recebe luz sem me deixar no escuro. Para ele, as invenções não podem, por natureza, ser objeto de propriedade ([Founders' Constitution](https://press-pubs.uchicago.edu/founders/documents/a1_8_8s12.html)).

⚖️ A lei brasileira concorda no ponto central: o art. 8º, I, da Lei 9.610/98 diz que ideias, procedimentos normativos, sistemas e métodos, como tais, não são protegidos como direito autoral ([Planalto](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm)).

**Opinião:** então o que o robots.txt protege não é a ideia. É o acesso ao texto e o trabalho de quem o escreveu. E ele é placa na porta, não fechadura: é voluntário, o rascunho ainda é do IETF, o Google mira 2027 sem dia marcado, e o Bing passa a respeitar as preferências em 01/02/2027 ([Google](https://developers.google.com/search/blog/2026/10/ai-training-control); [Search Engine Roundtable](https://www.seroundtable.com/microsoft-bing-ai-controls-42429.html); [IETF](https://datatracker.ietf.org/doc/draft-ietf-aipref-vocab/)).

### Quem misturou o trabalho, leva?
Para John Locke, quem mistura seu trabalho a algo tirado do comum faz disso propriedade, "at least where there is enough, and as good, left in common for others" ([Segundo Tratado, cap. V, §27](https://www.gutenberg.org/files/7370/7370-h/7370-h.htm)). Em português: desde que sobre o bastante, e tão bom, para os outros.

**Opinião:** os laboratórios fizeram isso com a web. Depois puseram cerca.

Os termos comerciais da Anthropic, em vigor desde 17/06/2025, proíbem usar o serviço "to train competing AI models" ([termos](https://www.anthropic.com/legal/commercial-terms)). A regra não é nova; o que usuários relatam seria a aplicação dela, e a Tom's Hardware diz que não há posição oficial da empresa. Em janeiro de 2025, o Financial Times noticiou que a OpenAI tinha indícios de que a DeepSeek usou destilação (treinar um modelo com as respostas de outro), prática que os termos da OpenAI proíbem ([Euronews](https://www.euronews.com/2025/01/29/openai-says-chinese-companies-are-trying-to-use-us-models-to-train-ai)).

**Opinião:** a cerca em si não é o escândalo. O que pesa é a ressalva de Locke: o teste é se fica "o bastante, e tão bom" para quem vem depois. Stack Overflow e Reddit sugerem que a fonte está secando. Na teleconferência de 29/10, o CEO do Reddit, Steve Huffman, disse: "AI Mode does not drive traffic, not for us and not for anybody" (...). O Reddit vai testar um modo só para logados em mercados selecionados fora dos EUA ([AdExchanger](https://www.adexchanger.com/platforms/reddit-is-going-login-only-blame-google)).

### A tragédia do comum é inevitável?
Garrett Hardin chamou de "tragédia dos comuns" (*Science*, 1968) o destino de um pasto aberto a todos, e a expressão virou sinônimo de que todo bem comum acaba destruído ([Science](https://www.science.org/doi/10.1126/science.162.3859.1243)). Em 1998, o próprio Hardin escreveu sobre o "unmanaged commons", o comum não gerido, que seria arruinado pelo excesso de pasto ([Garrett Hardin Society](https://garretthardinsociety.org/articles/art_extension_tragedy_commons.html)). O problema, ali, é a falta de gestão, não o comum em si.

Elinor Ostrom ganhou o Nobel de Economia de 2009 "pela análise da governança econômica, especialmente dos bens comuns" ([Nobel Prize](https://www.nobelprize.org/prizes/economic-sciences/2009/summary/)).

**Opinião:** a lição que se tira de Ostrom, resumida, é que o comum precisa de regras, não de dono único. O sinal no robots.txt é uma regra desse tipo: combinada entre as partes, voluntária, sem fechadura. Só que o rascunho está incompleto, diz Nate Hake, que participa do grupo de trabalho ([PPC Land](https://ppc.land/google-and-bing-back-one-robots-txt-rule-to-opt-out-of-ai-training/)). E regra de Ostrom funciona quando quem usa o pasto também sente o pasto secar.

### A objeção honesta
Jefferson joga também do outro lado: conhecimento não se gasta. Ler e aprender não tira a luz de ninguém. Segundo a eWeek, em junho de 2025 o juiz William Alsup decidiu que treinar com livros é uso justo (*fair use*), mas que obter as cópias em sites piratas não é. A Anthropic propôs um acordo de **US$ 1,5 bi**, cerca de **US$ 3.000** por livro ([eWeek](https://www.eweek.com/news/anthropic-settlement-copyright-case/)).

E o número do Stack Overflow mostra a queda, não o motivo: ele sozinho não prova que a culpa é da IA. A cerca dos laboratórios tem argumento. A Anthropic diz, num post de 12/10, que se defende de ataques de destilação, que copiam a capacidade de um modelo ([Anthropic](https://www.anthropic.com/news/distillation-defenses)).

**Opinião:** o que a tese não prova é que treinar seja roubar. Prova só que alguém precisa continuar produzindo o que se aprende.

### De volta a 2014
A vela de Jefferson acende outras sem se apagar, mas alguém precisa continuar fazendo vela. As 207 mil perguntas de 2014 eram velas de estranhos.

**Pergunta de domingo:** o que você produz que outros, ou máquinas, aprendem de graça, e o que você recebe em troca para continuar produzindo?

**Para ler com calma:**
- Thomas Jefferson, carta a Isaac McPherson (13/08/1813).
- John Locke, *Segundo Tratado sobre o Governo*, cap. V.
- Garrett Hardin, "The Tragedy of the Commons" (*Science*, 1968).
- Elinor Ostrom, *Governing the Commons* (1990): a resposta a Hardin.

---

#### EM 3 LINHAS: O QUE OBSERVAR NA SEMANA
→ **Copom**: decide os juros na quarta (04/11), depois do fechamento do mercado, com a Selic em **13,75%**; o Itaú espera manutenção e vê o fim do ciclo de cortes ([Neofeed](https://neofeed.com.br/economia/itau-ve-fim-do-ciclo-de-cortes-da-selic-diante-de-cenario-mais-adverso/)).

→ **Bolsa**: depois de cair **18,12%** na semana passada, a pior desde março de 2020, o Ibovespa chega à semana a **167.922** pontos, e o dólar a **R$ 5,44** ([InvestNews](https://investnews.com.br/investimentos/ibovespa-afunda-18-e-tem-pior-semana-desde-2020-dolar-salta-9/)).

→ **Kimi**: a Moonshot promete os pesos abertos do Kimi K3.1 Pro até **04/11**; em 01/11, ainda não estavam no Hugging Face ([Kimi](https://www.kimi.ai/blog/kimi-k3-1-pro); [Hugging Face](https://huggingface.co/moonshotai)).
