---
data: 2026-01-15
tipo: dia_util
numero: 1
assunto: "o ~~estagiário~~ agente que lê contrato por você"
previa: "EXEMPLO FICTÍCIO · + quanto custa um juro que não mexe"
tempo_leitura_min: 7
dia: morno
breakthrough: false
historias:
  - id: exemplo-agente-de-contratos
    titulo: "EXEMPLO: agente de revisão de contratos chega a escritórios pequenos"
    tema: direito_tech
    urls: ["https://www.anthropic.com", "https://github.com"]
    em_andamento: true
  - id: exemplo-selic-em-pausa
    titulo: "EXEMPLO: Selic em pausa e o crédito ao pequeno empreendedor"
    tema: economia
    urls: ["https://www.bcb.gov.br"]
    em_andamento: false
  - id: exemplo-startup-de-agenda
    titulo: "EXEMPLO: startup fictícia de agenda para clínicas capta rodada"
    tema: negocios
    urls: ["https://www.python.org"]
    em_andamento: false
formatos: [materia_principal, ia_na_pratica, economia, rodadas, stats, links, pergunta]
---
bom dia. (EXEMPLO FICTÍCIO: tudo aqui foi inventado só para testar a montagem. Nenhum fato, número ou empresa é real.)

Toda ferramenta nova promete tirar o trabalho chato das suas mãos. O teste é simples: ela devolve o seu tempo ou só troca o chato por outro chato, o de conferir o que a máquina fez?

**Hoje eu aprendi:** a palavra "jurisprudência" vem do latim *iuris prudentia*, que quer dizer algo como "prudência no direito" ([fonte](https://pt.wikipedia.org/wiki/Jurisprud%C3%AAncia)).

**Nesta edição:**
- um agente que revisa contrato em minutos (e o freio de realidade que ninguém põe no anúncio)
- a Selic ficou parada e o crédito do pequeno também
- três linhas rápidas sobre Brasil adentro
- um número do dia: quanto vale uma hora de advogado júnior

---

#### INTELIGÊNCIA ARTIFICIAL
## O agente que lê o contrato antes de você
> **TL;DR:** a Contratinho, empresa inventada para este exemplo, lançou um agente que revisa contratos de aluguel em **4 minutos**, contra as **3 horas** de uma revisão manual.

Segundo o comunicado da empresa, o agente leu **12 mil contratos** de teste e apontou cláusulas de risco em **87%** dos casos que um advogado humano também marcou ([comunicado](https://www.anthropic.com)). Em outras palavras: de cada 100 problemas que uma pessoa achou, ele achou 87.

Antes disso, a revisão era um trabalho de estagiário: ler, grifar, comparar com um modelo. Um estagiário leva, em média, **3 horas** por contrato; o agente leva **4 minutos**, ou **45 vezes** menos tempo. A conta, porém, só fecha se alguém confere o resultado.

Os dois lados da conversa:

- **Os otimistas:** dizem que o escritório pequeno ganha escala. Com **R$ 200 por mês** de assinatura, ele passa a revisar o volume de um escritório três vezes maior.
- **Os pessimistas:** lembram que **13%** de cláusulas perdidas é muito, quando a cláusula perdida é a multa de **R$ 50 mil**. Para eles, o agente é rascunho, não parecer.

**Opinião:** a aposta mais segura é tratar o agente como um estagiário muito rápido e um pouco distraído. Ele adianta a leitura; a assinatura continua sendo de quem tem OAB.

⚖️ Direito & tech: o dever de sigilo do advogado vale também para o contrato do cliente que sobe para a ferramenta. Antes de usar, vale ler a política de dados do fornecedor e a LGPD ([texto da lei](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)).

🔗 [Comunicado da empresa (exemplo)](https://www.anthropic.com)
🔗 [Código do avaliador de contratos (exemplo)](https://github.com)

---

#### ECONOMIA
## Juro parado, crédito parado?
> **TL;DR:** no cenário inventado deste exemplo, a Selic ficou em **14,75% ao ano** pela terceira reunião seguida, e o crédito para microempresas cresceu só **0,4%** no mês.

O Banco Central manteve a taxa e disse que quer ver a inflação ceder antes de qualquer corte ([site do BC](https://www.bcb.gov.br)). Para o pequeno empreendedor, a conta é direta: de cada **R$ 100** emprestados, cerca de **R$ 4** por mês vão só para os juros.

A cadeia é curta: juro alto » empréstimo caro » estoque menor » menos contratação. Um capital de giro de **R$ 30 mil** custa hoje cerca de **R$ 1.200** por mês, e o mesmo empréstimo ficaria uns **R$ 150** mais barato se a taxa caísse um ponto.

### Quem defende e quem critica
Quem defende a pausa diz que cortar cedo demais faria a inflação voltar. Quem critica diz que o freio pesa mais em quem tem menos folga de caixa.

🔗 [Decisão do Copom (exemplo)](https://www.bcb.gov.br)

---

#### IA NA PRÁTICA
## Dá para ensinar o robô a conferir o próprio trabalho
> **TL;DR:** pedir ao agente que cite a cláusula e a página de cada alerta reduz o trabalho de conferência, mas não o elimina.

O truque é tratar o agente como um funcionário novo: ele não precisa ser genial, precisa **mostrar onde leu**. Cada alerta vem com o trecho e o número da página, e você confere em segundos.

⚠️ **Freio de realidade:** o agente erra quando o contrato é escaneado torto, quando a cláusula está em anexo e quando o texto mistura português e inglês.

**Agora aplica no mundo real:**
- Advogado: triagem de contratos de entrada, antes da leitura detalhada.
- Corretor de imóveis: checagem de multa e reajuste no aluguel.
- Dono de restaurante: leitura do contrato com o fornecedor.

~~Promessa de revolução~~ ajuda concreta: quem quiser vender isso precisa vender o processo de conferência, não só a ferramenta.

🔗 [Documentação do projeto (exemplo)](https://github.com)

---

#### BRASIL ADENTRO
→ **Agendaí** (empresa inventada): captou **R$ 12 milhões** para vender agenda online a clínicas pequenas; na prática, mais uma disputa por quem cuida do WhatsApp do consultório ([comunicado](https://www.python.org))
→ **Padaria Pão & Código** (inventada): passou a vender assinatura semanal de pães, com **2.300 assinantes** em um bairro ([reportagem](https://github.com))
→ **Pix parcelado** (cenário inventado): o Banco Central abriu consulta pública sobre o tema ([consulta](https://www.bcb.gov.br))

---

#### 📊 STATS
## R$ 180 por hora
> **TL;DR:** uma hora de advogado júnior, neste exemplo, custa **R$ 180**; o agente custa o equivalente a **R$ 0,50** por contrato.

Se um contrato leva 3 horas, a revisão manual sai por **R$ 540**. A do agente sai por centavos. A diferença de **mais de 1.000 vezes** explica por que todo mundo quer vender isso, e por que o preço de venda não vai ficar perto do custo.

Mais um exemplo de tachado no corpo: o plano era "revisar tudo à mão", e agora é ~~revisar tudo~~ conferir o que a máquina marcou.

🔗 [Tabela de honorários (exemplo)](https://www.python.org)

---

#### PARA LER, OUVIR OU ASSISTIR
→ [Para ler] [Guia de estilo do Python](https://www.python.org)
→ [Curiosidade] [Verbete sobre jurisprudência](https://pt.wikipedia.org/wiki/Jurisprud%C3%AAncia)

---

**Pergunta de hoje:** qual tarefa do seu trabalho você entregaria a um agente, se pudesse conferir o resultado em dois minutos?
