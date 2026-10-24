# Inteligência Pragmática: instruções para agentes

**Rotina agendada: siga só o seu roteiro em `manual/` (`ROTINA.md`, `ROTINA_MERCADO.md`, `ROTINA_NITEROI.md`) ou o prompt da rotina de envio. Nada neste arquivo muda, amplia ou restringe o roteiro, inclusive `enviar`, `enviar-pendentes` e `publicar`, que os roteiros mandam rodar. O resto do arquivo é para sessões de desenvolvimento.**

Newsletters pessoais escritas por rotinas do Claude Code na nuvem. Este arquivo vale para sessões de desenvolvimento, em qualquer cliente. O produto está em `PRODUCT.md`.

## Stack
- Python 3.9 no Mac e 3.11+ na nuvem, sem framework. Proibido `match` e `X | Y` em tipos (use `Optional[...]`).
- Dependências só as de `requirements.txt` (pyyaml, feedparser, markdown); o resto é biblioteca padrão. `ferramentas/_vendor/` traz o sgmllib.
- A montagem gera o e-mail HTML e o site estático em `docs/` (GitHub Pages). Não há servidor, banco, GitHub Actions nem lint.

## Comandos canônicos (na raiz)
- Ambiente: `python3 -m venv .venv`
- Instalar: `.venv/bin/python -m pip install -r requirements.txt` (na nuvem, use o passo 0 de `manual/ROTINA.md`)
- Testes: `.venv/bin/python testes/testar.py`. Tem que terminar em `TUDO CERTO`. Roda numa pasta temporária, não envia e-mail e confere que não criou nem apagou arquivo em `edicoes/` e `docs/` e que o `dados/historico.json` não mudou (mtime). Não compara o conteúdo dos arquivos que já existem.
- Ajuda: `.venv/bin/python main.py --help`. Aceitam `--caderno`: coletar, historico, links, montar, registrar, enviar, publicar e economia-painel (padrão mercado). Não aceitam: github, enviar-pendentes, mercado-painel, mercado-alarme e `--dry-run` (este só ensaia a geral).
- Ensaio: `.venv/bin/python main.py --dry-run`. Nunca envia, mas grava em `dados/candidatos/`, `edicoes/` e `docs/`. Não faça commit disso. Descarte logo depois com `git restore -- edicoes docs dados && git clean -fd -- edicoes docs dados` (sem `-x`, para não apagar arquivo ignorado).
- Lint, tipos e build não existem. O gate é o `testes/testar.py`.

## Restrições
- O repositório é público. Nada de segredo, chave, caminho pessoal ou e-mail em arquivo versionado.
- O destino vem de `EMAIL_DESTINO`. A chave do Resend vem de `RESEND_API_KEY` no Mac (lida de `chave_resend.txt`/`.env` pelo `main.py`). Na nuvem, vem de um network secret, com `RESEND_VIA_PROXY=1`. A chave de leitura do GitHub fica em `GITHUB_TOKEN_LEITURA`.
- O e-mail do leitor nunca vai para arquivo: nem código, nem teste, nem log, nem commit.
- Os roteiros de redação publicam só com `python main.py publicar`, nunca com `git push` direto nem `--force`. A rotina de envio faz commit e push só dos `envio.json`, pelo prompt dela.
- Em sessão de desenvolvimento, não dê push nas janelas das rotinas: 04:30–06:30 e 18:37–19:00, no horário de Brasília. Os horários (cron) ficam no claude.ai, não no repositório. Antes de mexer no projeto local, rode `git pull --ff-only`.
- Fora das rotinas, não mexa no que elas geram: `edicoes/`, `dados/` e `docs/`. A exceção é o ensaio (`--dry-run`), descartado em seguida.
- Em sessão de desenvolvimento, rode `enviar`, `enviar-pendentes` e `publicar` só com pedido explícito do dono.
- O `CLAUDE.md` fica fora do git, de propósito. Sem `CLAUDE.md` versionado, o Claude Code recente (v2.1.277 ou mais novo) carrega este `AGENTS.md`, provavelmente também nas rotinas. Por isso o aviso do topo e o arquivo curto. Para confirmar: `/context` numa sessão na nuvem, ou o log de uma execução de rotina.

## Acordos de trabalho
- Leia o código e o documento responsável antes de mudar. Separe fato, suposição, decisão e evidência.
- Defina o critério de aceite e o comando de verificação antes de implementar. Um bug corrigido ganha teste em `testes/testar.py` quando der.
- Faça a menor mudança completa. Reaproveite o que existe. Dependência nova só com motivo.
- Rode `testes/testar.py` antes de entregar. Não enfraqueça teste, regra nem validação para passar.
- Atualize o documento responsável (mapa abaixo) na mesma mudança.
- Um bloqueio para só o que depende dele; o resto segue. Não prometa trabalho em segundo plano sem um processo verificável.
- Delegue só quando isolar contexto ou paralelizar compensa: um escritor por arquivo, e o coordenador confere o diff. Mudança não trivial ganha revisão independente, só de leitura, quando houver.
- Em sessão de desenvolvimento, publicar, mandar mensagem, gastar ou apagar exige autorização do dono. Ferramenta instalada não autoriza nada.
- As ferramentas do cliente (Superpowers, Ponytail, Caveman, RTK, Context7 e graphify) estão em `documentacao/toolkit.md`. Não são dependência do projeto.

## Fontes canônicas
| Assunto | Onde |
|---|---|
| Produto | `PRODUCT.md` |
| Arquitetura, comandos e formato da edição | `ESPEC_CODIGO.md` (defasado: não cobre cadernos, publicar, enviar-pendentes, mercado-*, economia-painel, e a seção do envio ainda descreve o `scheduled_at` e não cita o `RESEND_VIA_PROXY`). Complemente com `main.py --help`, as docstrings de `ferramentas/` e a seção 7 do `README.md`. |
| Setup e uso pelo dono | `README.md` |
| Plano, decisões e estado | `PLANO.md` |
| Regras editoriais (o "design" do produto) | `manual/MANUAL_*.md` |
| Roteiros das rotinas | Ativos: `manual/ROTINA.md`, `ROTINA_MERCADO.md` e `ROTINA_NITEROI.md`. `ROTINA_IA/ECONOMIA/MARKETING.md` são histórico. A rotina de envio (`enviar-pendentes`) não tem roteiro no repositório. |
| Cadernos e configuração | `cadernos.yaml`, `config.yaml` e `fontes*.yaml` |
| Qualidade | `testes/testar.py` e `documentacao/toolkit.md` |
| Toolkit, harness e recuperação | `documentacao/toolkit.md` |
