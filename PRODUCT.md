# Produto: Inteligência Pragmática

Resumo do produto como ele está no repositório. O detalhe de cada parte fica no documento citado. Plano e estado: `PLANO.md`.

## O que é
- Uma família de newsletters escritas por IA para **um leitor**: a geral é diária, e os cadernos têm dias próprios.
- **Geral**, todos os dias: IA, economia, negócios e marketing, com fontes linkadas em cada afirmação. No sábado sai a semana em revista, e no domingo, o ensaio. Na terça e na quinta, a edição leva a seção MARKETING DIGITAL.
- **Cadernos ativos** (`cadernos.yaml`):
  - Desde 29/10/2026, os dois só saem com **breakthrough**: uma edição extra longa e bem explicada. Fora isso, não mandam nada.
  - **Mercado**: nos dias úteis, às 18:37, um alarme confere os gatilhos de preço e de evento (`manual/MANUAL_MERCADO.md`, seção 6). A edição da manhã e o bloco ECONOMIA foram suspensos.
  - **Niterói**: todo dia, às 05:22, um radar lê os títulos e decide pelo critério da seção 10 do `manual/MANUAL_NITEROI.md`. A edição de segunda, quarta e sexta foi suspensa.
- **Cadernos encerrados em 22/10/2026:** IA, Economia e Marketing, com `envio: desligado`. As edições antigas continuam no site.
- Cada edição chega por **e-mail** e fica num **site estático** (`docs/`, GitHub Pages) que dá para instalar no celular.

## Para quem
- Um leitor só, o dono do projeto. Não há lista de assinantes nem cadastro.
- O leitor ajusta o produto sem programar. Ele edita `preferencias.md` (gostos e feedback), `fontes*.yaml` e `config.yaml`/`cadernos.yaml`. O passo a passo está no `README.md`.

## Fluxo crítico
Cada rotina do Claude Code na nuvem segue o seu `manual/ROTINA*.md`, nesta ordem:

1. **Coleta:** `main.py coletar` lê RSS, APIs e o radar, e grava os candidatos em `dados/candidatos/`.
2. **Triagem e pauta:** a rotina escolhe o que entra e justifica a escolha em `pauta.md`.
3. **Apuração:** cada fato é conferido na fonte, de preferência a primária. Na geral, quem confere são 2 a 4 agentes Sonnet; na extra do Mercado, o próprio editor; na extra do Niterói, o agente redator.
4. **Redação:** segue as regras de `manual/MANUAL_*.md`.
5. **Checagem:** dois agentes independentes conferem a edição (na extra do Niterói, um só) e registram tudo em `verificacao.md`. O `main.py links` testa os links. A checagem nunca é pulada.
6. **Montagem:** `main.py montar` gera o e-mail, a versão curta e o site, e `main.py registrar` atualiza `dados/historico.json`.
7. **Envio:** `main.py enviar` roda antes do `publicar`. Antes das 05:55, a edição fica "aguardando", e a rotina de envio (`main.py enviar-pendentes`, às 05:59) manda as do dia ainda não enviadas. De 05:55 em diante, e na extra do Mercado (18:37), o próprio `enviar` manda na hora.
8. **Publicação:** `main.py publicar` grava na `main` e aguenta várias rotinas ao mesmo tempo. Se desistir, guarda a edição no ramo `pendente/<caderno>-<data>`.

Os números dos painéis do Mercado e da Economia entram por código (`mercado-painel` e `economia-painel`), sem passar pela IA.

## Restrições
- **Custo:** só a assinatura do Claude. Não usa a API da Anthropic, e os créditos extras ficam desligados. Se o limite de uso estourar, a edição do dia não sai.
- **E-mail:** sai pelo Resend, com o remetente de teste. Ele só entrega ao dono da conta e não agenda envio. Por isso existe a rotina de envio das 06:00.
- **Nuvem:**
  - as rotinas rodam com o Mac desligado, sem conectores e sem acesso ao Gmail do leitor;
  - as rotinas precisam de rede liberada para ler as fontes;
  - o e-mail de destino e as chaves ficam em variáveis e segredos do ambiente da nuvem.
- **Repositório público:** o e-mail do leitor e as chaves nunca vão para arquivo versionado.
- **Prazo:** a edição precisa estar publicada antes das 06:00. Se faltar tempo, cortam-se seções, nunca a checagem.
- **Código:** Python 3.9 no Mac e 3.11+ na nuvem, com só três dependências (`ESPEC_CODIGO.md`).
- **Fontes:** as newsletters que o leitor assina servem de radar, para achar pauta e evitar repetição. O texto delas nunca é copiado.

## O que não é
- Não é um produto para várias pessoas: não tem assinantes, login, cobrança nem painel.
- Não é um aplicativo com servidor: não tem back-end, banco de dados nem GitHub Actions. O site é estático e gerado pela montagem.
- Não é escrito por API: quem pesquisa e escreve são as rotinas do Claude Code, pela assinatura.
- Não lê a caixa de entrada do leitor nem republica o texto de outras newsletters.
- Ainda não sai por Telegram nem por WhatsApp. Os dois estão planejados nas Fases 2 e 3 do `PLANO.md` e não estão implementados na `main`.

## Como saber se está funcionando
- O e-mail do dia chega às 06:00, e a edição aparece no site.
- Cada edição tem `verificacao.md`, com as afirmações conferidas, e `links.json`, com o teste dos links.
- No código, `.venv/bin/python testes/testar.py` termina em `TUDO CERTO`.
