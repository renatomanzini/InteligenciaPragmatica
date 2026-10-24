# Inteligência Pragmática: instruções para agentes

Newsletters pessoais escritas por rotinas do Claude Code na nuvem. Este arquivo vale para sessões de desenvolvimento, em qualquer cliente. As rotinas seguem `manual/ROTINA*.md`. O produto está em `PRODUCT.md`.

## Stack
- Python 3.9 no Mac e 3.11+ na nuvem, sem framework. Proibido `match` e `X | Y` em tipos (use `Optional[...]`).
- Dependências só as de `requirements.txt` (pyyaml, feedparser, markdown); o resto é biblioteca padrão. `ferramentas/_vendor/` traz o sgmllib.
- A montagem gera o e-mail HTML e o site estático em `docs/` (GitHub Pages). Não há servidor, banco, GitHub Actions nem lint.

## Comandos canônicos (na raiz)
- Ambiente: `python3 -m venv .venv`
- Instalar: `.venv/bin/python -m pip install -r requirements.txt` (na nuvem, use o passo 0 de `manual/ROTINA.md`)
- Testes: `.venv/bin/python testes/testar.py`. Tem que terminar em `TUDO CERTO`. Roda numa pasta temporária, não envia e-mail e confere que não mexeu em `edicoes/`, `docs/` e `dados/historico.json`.
- Ajuda: `.venv/bin/python main.py --help`. Todo comando aceita `--caderno`.
- Ensaio: `.venv/bin/python main.py --dry-run`. Nunca envia, mas grava em `dados/candidatos/`, `edicoes/` e `docs/`. Não faça commit disso: descarte depois.
- Lint, tipos e build não existem. O gate é o `testes/testar.py`.

## Restrições
- O repositório é público. Nada de segredo, chave, caminho pessoal ou e-mail em arquivo versionado. A chave e o destino vêm de variáveis de ambiente (`RESEND_API_KEY`, `EMAIL_DESTINO`).
- O e-mail do leitor nunca vai para arquivo: nem código, nem teste, nem log, nem commit.
- Nas rotinas, publique só com `python main.py publicar`. Nunca use `git push` direto nem `--force`.
- Não dê push nas janelas das rotinas: 04:30–06:30 e 18:37–19:00, no horário de Brasília. Antes de mexer no projeto local, rode `git pull --ff-only`.
- Fora das rotinas, não mexa no que elas geram: `edicoes/`, `dados/` e `docs/`.
- Em sessão de desenvolvimento, rode `enviar`, `enviar-pendentes` e `publicar` só com pedido explícito do dono.
- O `CLAUDE.md` fica fora do git, de propósito: as rotinas não devem carregar instruções extras a cada execução.

## Acordos de trabalho
- Leia o código e o documento responsável antes de mudar. Separe fato, suposição, decisão e evidência.
- Defina o critério de aceite e o comando de verificação antes de implementar. Um bug corrigido ganha teste em `testes/testar.py` quando der.
- Faça a menor mudança completa. Reaproveite o que existe. Dependência nova só com motivo.
- Rode `testes/testar.py` antes de entregar. Não enfraqueça teste, regra nem validação para passar.
- Atualize o documento responsável (mapa abaixo) na mesma mudança.
- Um bloqueio para só o que depende dele; o resto segue. Não prometa trabalho em segundo plano sem um processo verificável.
- Delegue só quando isolar contexto ou paralelizar compensa: um escritor por arquivo, e o coordenador confere o diff. Mudança não trivial ganha revisão independente, só de leitura, quando houver.
- Publicar, mandar mensagem, gastar ou apagar exige autorização do dono. Ferramenta instalada não autoriza nada.
- As ferramentas do cliente (Superpowers, Ponytail, Caveman, RTK, Context7 e graphify) estão em `documentacao/toolkit.md`. Não são dependência do projeto.

## Fontes canônicas
| Assunto | Onde |
|---|---|
| Produto | `PRODUCT.md` |
| Arquitetura, comandos e formato da edição | `ESPEC_CODIGO.md` |
| Setup e uso pelo dono | `README.md` |
| Plano, decisões e estado | `PLANO.md` |
| Regras editoriais (o "design" do produto) | `manual/MANUAL_*.md` |
| Roteiros das rotinas | `manual/ROTINA*.md` |
| Cadernos e configuração | `cadernos.yaml`, `config.yaml` e `fontes*.yaml` |
| Qualidade | `testes/testar.py` e `documentacao/toolkit.md` |
| Toolkit, harness e recuperação | `documentacao/toolkit.md` |
