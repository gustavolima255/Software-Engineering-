# Software-Engineering-
Software Engineering
Sistema web de gerenciamento de tarefas com fluxo **Kanban**, desenvolvido pela
**TechFlow Solutions** (empresa fictícia) para uma startup de logística.

> Trabalho de Engenharia de Software — *Construindo um Projeto Ágil no GitHub: da Gestão ao Controle de Qualidade*.

## Objetivo
Permitir acompanhar o fluxo de trabalho em tempo real, **priorizar tarefas críticas** e
monitorar o desempenho da equipe.

## Escopo
**Inicial (v0.1)**
- CRUD de tarefas: criar, listar, consultar, atualizar e excluir.
- Cada tarefa tem título, descrição e status (A Fazer → Em Progresso → Concluído).
- Interface web em formato de quadro Kanban com três colunas.
- Testes automatizados + integração contínua (GitHub Actions).

**Após a mudança de escopo (v0.2)** — ver [Gestão de mudanças](#gestão-de-mudanças)
- Prioridade da tarefa (`baixa`, `media`, `alta`), filtro por prioridade e destaque visual de tarefas críticas.

**Fora do escopo (backlog):** persistência em banco de dados e autenticação de usuários.

## Metodologia
Abordagem **híbrida Kanban + Scrum leve**:
- **Kanban** no GitHub Projects com as colunas *To Do* (A Fazer), *In Progress* (Em Progresso) e *Done* (Concluído) — veja [docs/kanban.md](docs/kanban.md).
- **Scrum leve**: iterações curtas (sprints) com planejamento, revisão com o cliente e retrospectiva.
- **Limite de WIP**: no máximo 2 cards em *In Progress* ao mesmo tempo.
- **Commits semânticos** (`feat`, `fix`, `test`, `docs`, `ci`, `chore`) e integração contínua a cada push.

## Estrutura do repositório
```
techflow-tasks/
├── .github/workflows/ci.yml   # pipeline: flake8 + pytest
├── src/techflow/              # código-fonte (models, repository, app, templates)
├── tests/                     # testes automatizados (pytest)
├── docs/                      # kanban, UML, mudança de escopo, roteiro do vídeo
├── scripts/criar_kanban.sh    # cria o quadro e os cards via GitHub CLI
├── run.py                     # inicia o sistema
└── requirements.txt
```

## Como executar
Pré-requisito: Python 3.11+.
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py            # abre em http://127.0.0.1:5000
```

### API REST
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/tasks?status=&priority=` | Lista tarefas (filtros opcionais) |
| POST | `/api/tasks` | Cria tarefa `{title, description, status, priority}` |
| GET | `/api/tasks/<id>` | Consulta uma tarefa |
| PUT | `/api/tasks/<id>` | Atualiza campos da tarefa |
| DELETE | `/api/tasks/<id>` | Exclui a tarefa |

## Testes e qualidade
```bash
pytest -v          # 28 testes automatizados
flake8 src tests   # análise de estilo e erros
```
O workflow [`ci.yml`](.github/workflows/ci.yml) executa `flake8` e `pytest` em Python 3.11 e 3.12
a cada push e pull request na branch `main`.

## Gestão de mudanças
**MC-001 — Prioridade das tarefas (simulação de mudança de escopo).**
Na revisão da Sprint 1 o cliente pediu para *priorizar as tarefas críticas das entregas*.

- **Justificativa:** atende ao objetivo central do projeto, tem baixo risco (um campo e um filtro) e os testes
  automatizados protegem o que já funciona.
- **O que mudou:** campo `priority`, filtro `?priority=alta` na API, destaque visual e checkbox "Só críticas" na interface.
- **Kanban:** novo card nº 11 *"[MUDANÇA DE ESCOPO] Prioridade das tarefas + filtro de críticas"*, movido de To Do → In Progress → Done.
- **Commits:** `docs(scope)`, `feat(priority)`, `test(priority)`, `feat(ui)`.
- **Detalhes:** [docs/mudanca-de-escopo.md](docs/mudanca-de-escopo.md).

Principais desafios ao mudar o escopo no meio do projeto: preservar o que já funciona (resolvido com testes de
regressão no CI), manter documentação e quadro coerentes (README, UML e Kanban atualizados) e não estourar o prazo (WIP limitado).
