# Plano vivo: Inteligência Pragmática

Newsletter pessoal diária sobre IA, economia, negócios e marketing, escrita por IA para um leitor só. Ela chega às 06:00 de Brasília, junto com os cadernos do dia.

## Decisões fechadas (16/10/2026)
- **Quem escreve:** uma rotina do Claude Code na nuvem da Anthropic, paga pela assinatura do Claude (sem API). Ela roda com o Mac desligado.
- **Modelos:** o Opus coordena e escreve, e agentes Sonnet apuram e checam.
- **Estilo:** a clareza e os números do the news, o humor e as seções fixas das Drops e o arco "aplica no mundo real" da Ressonância. Imitar o jeito, nunca o texto. As regras estão em `manual/MANUAL_DE_REDACAO.md`.
- **Fim de semana:** no sábado sai a semana em revista e os breakthroughs da semana. No domingo sai o ensaio, o único dia com filosofia.
- **Fontes:** `fontes.yaml`, sem os dados do BCB e do IBGE. As newsletters que o leitor assina entram como **radar**, pela versão pública: servem para achar pauta e não repetir, nunca para copiar.
- **E-mail:** pelo Resend, com o remetente de teste, que só entrega ao dono da conta. A rotina **não** tem acesso ao Gmail.
- **Memória:**
  - `dados/historico.json` guarda as edições, as histórias em andamento e os formatos usados;
  - `preferencias.md` guarda os gostos e o feedback.
- **Arquivo:** o site estático `docs/` no GitHub Pages, instalável no celular.

## Como uma edição nasce
O passo a passo completo está em `manual/ROTINA.md`.
1. `coletar`: RSS, Hacker News, GitHub, Hugging Face, Reddit e radar.
2. Triagem pelo Opus: decide o dia forte ou morno e se há breakthrough.
3. Apuração por agentes Sonnet em paralelo, na fonte primária.
4. Redação pelo Opus.
5. Checagem por um agente novo, mais o teste dos links.
6. `montar`: o e-mail em HTML, a versão curta e o site.
7. `registrar` no histórico.
8. `enviar`, que manda o e-mail na hora. O remetente de teste do Resend não agenda: o envio agendado falhou em 20/10.
9. `python main.py publicar`, que publica na main e aguenta várias rotinas publicando ao mesmo tempo.

## Fases
- [x] **Plano** aprovado pelo leitor em 16/10/2026.
- [x] **Fase 1a, MVP local:** código, manual e 3 edições de teste. O leitor aprovou o estilo em 18/10/2026.
- [x] **Fase 1b, nuvem** (concluída em 19/10/2026):
  - o leitor criou as contas no GitHub e no Resend;
  - o repositório é público e o site está no GitHub Pages;
  - a rotina roda sem conectores;
  - a edição nº 4 saiu pelo "Run now" em 12 minutos, e o leitor confirmou que o e-mail chegou;
  - o agendamento foi ligado: todo dia às 05:07 de Brasília, com o e-mail agendado para as 06:30;
  - em 20/10/2026, o envio agendado falhou ("Domain is not verified"). Desde então, o e-mail sai na hora e a rotina começa às **06:07** (cron `7 9 * * *` em UTC), com chegada por volta das 06:20;
  - em 22/10/2026, o leitor pediu que todas as newsletters chegassem juntas às 06:00. As rotinas de redação agora rodam de madrugada e deixam a edição pronta, e a rotina de envio (`enviar-pendentes`, às 05:59) manda todas.
- [ ] **Fase 2, Telegram:** um bot com a versão curta e o link. É também por ele que entra o feedback "mais disso / menos disso".
- [ ] **Fase 3 (opcional), WhatsApp:** pela Cloud API oficial da Meta. Antes de implementar, levantar o custo por mensagem e os requisitos (conta Meta Business, número dedicado, template aprovado). Nada de biblioteca não oficial.
- [ ] **Cadernos** (pedido em 22/10/2026): newsletters especializadas ao lado da geral. Começaram no Sonnet para caber no plano Pro. Desde 22/10 (plano Max), todas as rotinas usam Opus com dois checadores e escrevem em paralelo às 05:15, e o envio de todas sai junto às 06:00.
  - [ ] **Mercado:** sai nos dias úteis, de manhã, com o painel de cotações gerado por código. Tem edição extra quando o pregão dispara um gatilho.
    - Pronto: código, manual e roteiro.
    - Falta: a edição de teste aprovada e as rotinas (manhã e alarme).
  - [ ] **Niterói e região:** Niterói 3 vezes por semana; Vassouras e Búzios num bloco semanal. Antes, é preciso levantar as fontes locais.
  - [ ] **IA:** pesquisa diária com curadoria, edição nos dias fixos (segunda e quinta) e extra só com notícia muito importante; mais fundo que a geral (modelos, open source, ferramentas, regulação e IA na prática).
    - Pronto: fontes testadas no Mac, manual, roteiro e a edição nº 1 (teste) de 22/10.
    - Falta: a aprovação do leitor, a rotina na nuvem e ligar o envio.
  - [ ] **Economia** (2 vezes por semana) e **Marketing digital** (semanal).

## Custos
- Nenhum além da assinatura do Claude. A rotina gasta do limite de uso, e o consumo será medido nos testes.
- Resend, GitHub e GitHub Pages: grátis.
- Os créditos extras ficam desligados, para nunca haver cobrança a mais. Se o limite estourar, a edição do dia não sai.
