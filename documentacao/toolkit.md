# Vibe Coding Toolkit neste projeto

Este documento registra a adoção do [Vibe Coding Toolkit](https://github.com/soumatheusgomes/vibe-coding-toolkit) neste projeto. O caminho usado foi o prompt 12, de projeto existente, em versão enxuta. Ele faz o papel do `docs/setup.md` do toolkit e de parte do `docs/quality.md`. Aqui, `docs/` é o site público, por isso a pasta se chama `documentacao/`.

Data: 23/10/2026. Escopo: documentação e harness. O código Python, o site, as edições, os dados, os manuais e as configurações não foram alterados.

## (a) Revisão do toolkit

- Commit `790a895304e0c08b70a5b215c9d334f1c86b816c` (18/10/2026, "feat: default to Harness2-inspired setup workflow"), clonado numa pasta temporária fora do projeto.
- Arquivos lidos:
  - `docs/prompts/12-existing-project-setup.md`;
  - `README.md`;
  - `docs/00-overview.md`, `01-installation.md`, `02-playbook-onboarding.md` e `06-project-defaults.md`;
  - `docs/tools/README.md`;
  - `templates/README.md`, `AGENTS.md.template`, `CLAUDE.md.template`, `project-docs/manifest.json` e `task-handoff.md.template`;
  - de apoio: `docs/tools/23-harness2.md`, `docs/07-harness-evaluation.md` e os prompts 13 e 15.
- Nenhum script do toolkit rodou. Do toolkit, entraram a adaptação do template de `AGENTS.md` (versionada) e a linha `@AGENTS.md` do template de `CLAUDE.md` (local, fora do git). `PRODUCT.md` e este documento seguem os destinos do manifest.
- **Para repetir:**
  1. Clone uma revisão nova fora do projeto.
  2. Releia o prompt 12 e `docs/tools/README.md`.
  3. Compare a matriz abaixo, linha a linha.
  4. Atualize só o que mudou, sem duplicar seções e preservando o que o dono personalizou.

## (b) Matriz de cobertura

O que cada estado quer dizer:
- **instalado:** entrou no projeto nesta adoção;
- **reutilizado:** já existe na máquina ou no cliente (global), ou há um equivalente em uso;
- **não se aplica:** o projeto não tem a necessidade;
- **bloqueado:** depende de uma condição externa.

A matriz cobre todas as linhas das duas tabelas de `docs/tools/README.md`. O guia 17 e o guia 20 viraram duas linhas cada, porque cobrem duas capacidades.

| Componente | Precisa? | Estado atual | Ação | Motivo e validação |
|---|---|---|---|---|
| 01 Superpowers | Sim | Plugin global `superpowers@claude-plugins-official` | Reutilizado | Está na lista de plugins do Claude Code, e as skills aparecem na sessão. Não vai para o projeto. |
| 02 Subagentes | Sim | Nativo do Claude Code; as rotinas já delegam apuração, escrita e checagem pelo roteiro | Reutilizado | A política curta está no `AGENTS.md`: um escritor por arquivo e o diff conferido pelo coordenador. O que os roteiros já delegam ficou como estava. |
| 03 RTK | Sim (no Mac) | `rtk` 1.0.1 (Homebrew), com o hook oficial `rtk hook claude` na configuração global do Claude Code | Reutilizado | `rtk --version` respondeu. Não existe na nuvem, e as rotinas rodam sem ele. Nenhum hook novo. |
| 04 Ponytail | Sim | Plugin global `ponytail@ponytail`, em `full` | Reutilizado | Está na lista de plugins. |
| 05 Caveman | Sim (conversa) | Plugin global `caveman@caveman` | Reutilizado | Está na lista de plugins. Código, documentos e commits continuam em texto normal. |
| 06 ESLint/Biome | Não | Quase não há JS: só o `docs/sw.js` (fixo) e um `<script>` de uma linha, gerado pelo `montagem.py`, que registra o service worker. Não há JS que justifique lint | Não se aplica | O toolkit manda não pôr ESLint em projeto sem JS de verdade. O gate é o `testes/testar.py`. |
| 07 Graphify | Sob demanda | CLI `graphify` 0.9.95 (ferramenta do uv) e skill global; não há grafo no projeto | Reutilizado | O código é pequeno (o `main.py` e 11 módulos), então não gerei grafo. Se gerar, exclua `.venv/`, `edicoes/`, `dados/`, `docs/`, `ferramentas/_vendor/` e `chave_resend.txt`. |
| 08 Obsidian | Equivalente em uso | Uma nota externa no Mac, citada pelo `CLAUDE.md` local, guarda o estado, as decisões e as armadilhas | Reutilizado | Não precisa de MCP nem de cofre novo. A nota fica fora do repositório. |
| 09 Memória do Claude | Sim | Memória automática do Claude Code e `CLAUDE.md` local | Reutilizado | As camadas estão descritas na seção (d). A memória do produto (`dados/historico.json` e `preferencias.md`) é outra coisa e não mudou. |
| 10 Hooks | Não | Na configuração global, só o hook do RTK. Os plugins ativos (Superpowers, Caveman e Ponytail) trazem os próprios hooks. Nenhum hook é do projeto | Não se aplica | Nenhuma lacuna pede hook. A adoção proíbe hook de git e hook novo. |
| 11 agent-browser | Não | Não instalado | Não se aplica | Não há fluxo interativo. Para ver o e-mail e o site, basta o `--dry-run` ou o navegador embutido do cliente. |
| 12 Context7 | Sim (para conferir APIs de biblioteca) | Plugin global `context7@claude-plugins-official` instalado, mas o MCP pede autenticação | Bloqueado | Para destravar, o dono autoriza pelo `/mcp`; depois, testar uma consulta real. Até lá, vale a documentação oficial. |
| 13 Anthropic Skills | Não | Disponíveis no cliente (artefatos, PDF, criação de skill) | Não se aplica | O projeto não gera documentos nem artefatos. Ficam disponíveis no cliente se surgir a necessidade. |
| 14 Chrome DevTools MCP | Não | Não instalado | Não se aplica | O site é estático, gerado pela montagem e coberto pelo `testar.py`. Não há app JS para depurar. |
| 15 Codex | Opcional | Codex CLI 0.164.0 instalado globalmente | Reutilizado | O Codex lê o `AGENTS.md` da raiz. A descoberta não foi testada numa sessão do Codex. |
| 16 Vercel skills | Não | Não instaladas | Não se aplica | Não há React nem Next.js, e o site está no GitHub Pages. |
| 17 `next-dev-loop` | Não | Não instalado | Não se aplica | Não há Next.js. |
| 17 `next-bundle-optimizer` | Não | Não instalado | Não se aplica | Não há bundle JS. |
| 18 `supabase-postgres-best-practices` | Não | Não instalado | Não se aplica | Não há banco: os dados são arquivos JSON e Markdown. |
| 19 `gh-fix-ci` | Não | Não instalado | Não se aplica | O repositório não tem GitHub Actions. |
| 20 Revisão de segurança (prompt 13) | Sim | O projeto não tinha procedimento | Instalado (registrado, não executado) | A invocação está na seção (d). Os pontos sensíveis são o repositório público, as chaves, o e-mail do leitor, o `envio.py` e o `publicar.py`. |
| 20 `differential-review` | Às vezes | Não instalado; existe a skill nativa `security-review` do Claude Code | Reutilizado (equivalente) | Revisão de diff pela skill nativa ou por leitura manual do código. Não instalei skill nova. |
| 21 shadcn | Não | Não instalado | Não se aplica | Não há interface de app nem sistema de componentes. |
| 22 Sentry MCP | Não | Não instalado | Não se aplica | Não há serviço no Sentry. O diagnóstico usa os logs das rotinas (seção (d)). |
| 23 Harness2 | Sim (procedimento) | Adaptação nativa documentada; a CLI oficial não foi escolhida | Instalado (procedimento) | O smoke é o `testar.py`. Não houve falha de harness observada, então não houve comparação de candidato. Veja a seção (d). |

**Total:** 25 linhas. São 2 instaladas, 10 reutilizadas, 12 que não se aplicam e 1 bloqueada.

Extras de `docs/01-installation.md`:
- `aia-harness`: **não se aplica**, porque geraria agentes, hooks e `settings.json` que duplicam este harness;
- plugins oficiais do Claude: **reutilizados**, porque o marketplace oficial já está adicionado e é de lá que vêm o Superpowers e o Context7.

Templates fora do catálogo:
- `CLAUDE.md.template`: virou a linha `@AGENTS.md` no `CLAUDE.md` local;
- `task-handoff.md.template`: existe no toolkit, mas não foi copiado, porque não há trabalho de várias sessões em aberto;
- os templates de Next.js, ESLint, settings e hooks: não se aplicam;
- a fixture de avaliação de harness: não rodou (seção (f)).

## (c) Os 9 destinos do manifest

| Destino no toolkit | Documento aqui | Observação |
|---|---|---|
| `README.md` | `README.md` | Guia do dono: uso, nuvem, problemas comuns e cadernos. Ganhou uma linha que aponta para os documentos novos. |
| `PRODUCT.md` | `PRODUCT.md` | Novo. Só fatos do repositório. |
| `AGENTS.md` | `AGENTS.md` | Novo e curto: comandos, restrições, acordos e o mapa das fontes. |
| `CLAUDE.md` | `CLAUDE.md` local, **fora do git** (em `.git/info/exclude`) | Contém `@AGENTS.md` e a seção "Memória". Fica fora do git de propósito, para as rotinas da nuvem não carregarem a seção "Memória". Sem ele no clone, elas provavelmente carregam o `AGENTS.md` (veja abaixo). |
| `docs/architecture.md` | `ESPEC_CODIGO.md` | Também valem as docstrings de `ferramentas/` (por exemplo, `publicar.py`) e a seção 7 do `README.md`, sobre os cadernos. Há uma defasagem: veja a seção (f). |
| `docs/design.md` | `manual/MANUAL_*.md` | As regras editoriais são o "design" do produto. O visual do e-mail e do site está na parte de `montagem.py` do `ESPEC_CODIGO.md`. Não há UI de app, então os critérios visuais de app não se aplicam. |
| `docs/onboarding.md` | `README.md` (seções 3, 5 e 6) | Rodar no Mac, configuração da nuvem e problemas comuns. |
| `docs/quality.md` | `testes/testar.py` e a seção (d) | O que o teste prova e o que fica de fora. |
| `docs/setup.md` | este documento | Revisão, matriz, baseline e pendências. |

Além desses, `PLANO.md` guarda o plano e o estado, e `manual/ROTINA*.md` guardam os roteiros das rotinas.

**As rotinas e o `AGENTS.md`:**
- **Fato:** o Claude Code v2.1.277 ou mais novo lê o `AGENTS.md` sozinho quando não há `CLAUDE.md` nem `CLAUDE.local.md` na pasta de trabalho ou acima (https://code.claude.com/docs/en/memory.md#agents-md). A documentação das sessões na nuvem não cita o `AGENTS.md`: nem confirma nem nega.
- **Consequência provável:** o `CLAUDE.md` daqui é só local, então o clone das rotinas não tem `CLAUDE.md`. Por isso, é provável que as rotinas carreguem o `AGENTS.md` assim que ele entrar na `main`, e é esse o motivo de ele abrir com um aviso para as rotinas.
- **Para confirmar depois da integração:** rode `/context` numa sessão na nuvem ou leia o log de uma execução de rotina (pendência na seção (f)).

## (d) Harness

### Smoke: `.venv/bin/python testes/testar.py`

Para passar, o teste tem que terminar em `TUDO CERTO`, com saída 0. Leva uns 11 s. Ele roda numa pasta temporária e confere:
- a montagem (e-mail, versão curta, site e as convenções do Markdown);
- o histórico;
- o envio, com um Resend falso;
- o `enviar-pendentes`;
- a linha de comando;
- o `publicar` de três rotinas num git local: a geral primeiro e depois dois cadernos ao mesmo tempo;
- a coleta com filtros;
- o painel da Economia;
- a coerência de `cadernos.yaml` e `fontes*.yaml`;
- e, no fim, que nenhum arquivo foi criado ou apagado em `edicoes/` e `docs/` e que o `dados/historico.json` não mudou.

A verificação de links usa a internet. Sem rede, ela fica "inconclusiva" e o teste segue.

O teste **não** prova:
- a qualidade editorial;
- a coleta real na nuvem;
- o envio real pelo Resend;
- o push real;
- o comportamento das rotinas.

### Como validar uma mudança

1. Fora das janelas das rotinas, rode `git pull --ff-only` e trabalhe num ramo local.
2. Leia o documento responsável (o mapa está no `AGENTS.md`) e defina o critério de aceite.
3. Faça a mudança. Se mudou o comportamento do código, acrescente um caso em `testes/testar.py`.
4. Rode o `testar.py`, que tem que dar `TUDO CERTO`. Para ver o visual, use o `main.py --dry-run` e depois descarte o que ele gravou com `git restore -- edicoes docs dados && git clean -fd -- edicoes docs dados`.
5. No `git status`, confira que nada mudou em `edicoes/`, `dados/` e `docs/`. No diff, confira que não entrou e-mail, chave nem caminho pessoal.
6. Uma mudança em `manual/ROTINA*.md` só vale na próxima execução da rotina. Confira o log dessa primeira execução.
7. Uma mudança não trivial ganha revisão independente, só de leitura. Mudanças em envio, publicação ou segredos ganham também a revisão de segurança, descrita abaixo.

### Recuperação

- **O `publicar` desistiu:** a edição não entra no site.
  - Se ele desistir depois de tentar, ele tenta guardar a edição no ramo `pendente/<caderno>-<data>` do GitHub. A mensagem diz se conseguiu.
  - Se não conseguir, ou se o erro for outro (por exemplo, no `git add`/`commit` ou ao refazer histórico e site), a edição só existe no clone da rotina, que é descartado no fim.
  - Para listar: `git ls-remote --heads origin 'pendente/*'`.
  - Para inspecionar: `git fetch origin` e depois `git log origin/pendente/<caderno>-<data>`.
  - Não há procedimento escrito para levar o ramo de volta à `main` (seção (f)). Não use `push --force`.
- **Uma rotina falhou ou o resultado veio estranho:** leia o log da execução. Numa sessão do Claude Code, use a ferramenta de rotinas (`RemoteTrigger`, com `list_runs` e `get_run_log`). Fora dela, use claude.ai/code/routines. Verde só quer dizer que a rotina rodou.
- **O e-mail não chegou:** veja o status real no painel do Resend. A chave local só serve para enviar.
- **Uma fonte quebrou:** veja `dados/candidatos/AAAA-MM-DD-fontes.log` (geral) ou `dados/candidatos/<caderno>-AAAA-MM-DD-fontes.log` (cadernos).
- **Um erro passou pela checagem:** abra o `verificacao.md` da edição.

### Melhoria de harness (adaptação nativa do Harness2, prompt 15)

- **Modo:** adaptação nativa. Ela não roda o framework Harness2 nem reproduz os resultados dele.
- Nesta adoção, não houve falha de harness observada, então não houve comparação de candidato.
- **Procedimento,** para quando uma instrução ou um roteiro falhar de forma recorrente (por exemplo, um agente usar `git push` direto ou mexer em `docs/` fora da rotina):
  1. Registre a falha e o critério de aceite.
  2. Reproduza a falha com uma tarefa descartável, numa cópia do projeto sem remoto (`git remote remove origin`) ou com o `origin` apontando para um repositório bare local, como faz o `testes/testar.py`. Uma cópia feita com `cp -r` ou `git clone` mantém o `origin` no GitHub: repetir uma falha de `git push` direto faria um push de verdade no repositório público.
  3. Faça uma mudança mínima no documento responsável, que é o `AGENTS.md` ou um `manual/ROTINA*.md`.
  4. Rode o mesmo caso e o `testar.py`.
  5. Adote a mudança só se ela melhorou o resultado, e registre a lição aqui, com a data.
- **Limite:** uma comparação por falha.

### Revisão de segurança

- **Fonte:** `docs/prompts/13-security-review.md` do toolkit, na revisão acima. Rode em modo repositório ou em modo diff (`base` e `head` reais).
- **O relatório é privado e fica fora do repositório,** porque o repositório é público.
- **Alternativa nativa:** a skill `security-review` do Claude Code.
- Nunca foi executada.

### Memória em camadas

| Camada | Onde | Quem carrega |
|---|---|---|
| Produto | `dados/historico.json` e `preferencias.md` (versionados) | As rotinas, pelo roteiro |
| Instruções compartilhadas | `AGENTS.md` (versionado) | O Codex, direto; o Claude Code no Mac, pelo `@AGENTS.md` do `CLAUDE.md` local; provavelmente as rotinas, que não têm `CLAUDE.md` (seção (c)) |
| Estado e armadilhas de desenvolvimento | Uma nota externa no Mac, citada pelo `CLAUDE.md` local | As sessões do Claude Code no Mac |
| Memória automática | A memória do Claude Code, por usuário | As sessões do Claude Code no Mac |

A nota externa e a memória automática não vão para a nuvem. O `AGENTS.md` vai no clone das rotinas, e é provável que elas o carreguem (seção (c)); por isso ele abre com um aviso para as rotinas. **Gatilho para atualizar a nota externa:** mudança no `PLANO.md`, no `README.md` ou nos roteiros.

## (e) Baseline dos testes

| Quando | Árvore | Comando | Resultado |
|---|---|---|---|
| 23/10/2026, 22:06 (BRT), antes | `origin/main` em `1093782` | `.venv/bin/python testes/testar.py` (Python 3.9.6) | `TUDO CERTO`: 264 verificações ok, 0 falhas, saída 0, ~11 s |
| 23/10/2026, 22:12 (BRT), depois | ramo `toolkit-setup`, com `AGENTS.md`, `PRODUCT.md`, este documento e uma linha no `README.md` | o mesmo | `TUDO CERTO`: 264 verificações ok, 0 falhas, saída 0. Nenhuma regressão (a mudança é só de documentação) |

## (f) Pendências

1. **Context7:** o dono precisa fazer o login pelo `/mcp`. Depois, testar uma consulta real.
2. **Plano da assinatura (resolvido):** o certo é o plano Max, desde 22/10/2026, como dizem o `PLANO.md` e o `manual/ROTINA_MERCADO.md`. O "plano Pro" do pedido desta adoção veio de uma instrução desatualizada.
3. **O `ESPEC_CODIGO.md` está atrás do código:**
   - não cobre os cadernos, o `publicar`, o `enviar-pendentes`, o `mercado-painel`, o `mercado-alarme` nem o `economia-painel`;
   - ainda descreve o envio agendado (`scheduled_at`), mas hoje o `enviar` deixa a edição "aguardando" e o envio sai junto às 06:00;
   - atualizar na próxima mudança de código.
4. **O ramo `pendente/`:** falta um procedimento escrito para levar uma edição guardada de volta à `main`.
5. **Avaliação de harness** (prompt 14, com a fixture do toolkit): não rodou, porque exige o avaliador do toolkit (um script Node), e esta adoção vetou rodar scripts do toolkit.
6. **Sem verificação em sessão limpa:** a descoberta do `AGENTS.md` numa sessão nova do Claude Code ou do Codex.
7. **As rotinas e o `AGENTS.md`:** depois da integração na `main`, confirmar se as rotinas carregam o `AGENTS.md` (com `/context` numa sessão na nuvem ou no log de uma execução de rotina). Veja a seção (c).
8. **Roteiros encerrados:** `manual/ROTINA_IA.md`, `manual/ROTINA_ECONOMIA.md` e `manual/ROTINA_MARKETING.md` ainda mandam rodar `main.py guardar`, comando que foi removido. Só importa se um desses cadernos voltar.
9. **Decisões para rever, com o gatilho de cada uma:**
   - lint de Python (por exemplo, ruff): só se os erros de estilo ou de tipo começarem a escapar do `testar.py`;
   - grafo do graphify: se o código crescer bastante;
   - `gh-fix-ci`: se surgir GitHub Actions;
   - agent-browser e Chrome DevTools: se surgir uma interface interativa;
   - a matriz inteira: a cada revisão nova do toolkit.
