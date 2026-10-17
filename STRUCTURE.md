# LOREFORGE STRUCTURE

Legend: **NOW** = create on Day 0. Otherwise the day it appears.

```
loreforge/                      NOW   repo root, one git repo for everything
├── PROJECT.md                  NOW   what we build and why (source of truth)
├── PROGRESS.md                 NOW   daily snapshot, replaced fully each day
├── DESIGN.md                   NOW   design decisions, filled Days 1-3
├── ROADMAP.md                  NOW   56-day plan
├── STRUCTURE.md                NOW   this file
├── README.md                   Day 55  public front page of the repo
├── .gitignore                  Day 4   keeps .venv, .env, node_modules out of git
├── .env.example                Day 4   documents required env vars (no secrets)
├── docker-compose.yml          Day 4   local Postgres+pgvector and Redis
├── .github/workflows/          Day 51  CI pipeline
│
├── backend/                    NOW   FastAPI app, managed by uv
│   ├── pyproject.toml          NOW   project metadata + dependency list (made by uv init)
│   ├── uv.lock                 NOW   exact pinned versions (appears on first uv add)
│   ├── .python-version         NOW   Python version uv uses
│   ├── Dockerfile              Day 52  builds the backend image (uses uv)
│   ├── alembic/                Day 5   database migrations (version control for the schema)
│   ├── app/                    Day 4   all application code
│   │   ├── main.py             Day 4   creates the FastAPI app, mounts routers
│   │   ├── core/               Day 4   config, security (hashing, JWT), shared dependencies
│   │   ├── db/                 Day 5   engine, session, base class
│   │   ├── models/             Day 5   SQLAlchemy tables
│   │   ├── schemas/            Day 5   Pydantic request/response shapes
│   │   ├── routers/            Day 5   HTTP endpoints, thin
│   │   ├── services/           Day 9   business logic the routers call
│   │   ├── rag/                Day 17  chunking, embeddings, retrieval, citations
│   │   ├── worker/             Day 16  background jobs (ingestion)
│   │   ├── agent/              Day 29  tool loop, tools, approvals, guardrails
│   │   └── mcp_server/         Day 36  our own MCP server (dice, sheets, world state)
│   ├── tests/                  Day 6   pytest tests
│   └── evals/                  Day 25  RAG and agent quality checks
│
├── frontend/                   Day 8   Next.js + Tailwind + shadcn/ui
│   └── src/
│       ├── app/                Day 8   pages and layouts (App Router)
│       ├── components/ui/      Day 8   shadcn components, customized from DESIGN.md
│       ├── components/         Day 13  our own components (cards, chat, tables)
│       ├── lib/                Day 13  API client, auth helpers
│       └── styles/             Day 8   design tokens (colors, spacing, radius)
│
└── docs/                       NOW   learning notes and architecture
    ├── weekly/                 NOW   one entry per week (what, how, tradeoffs, interview Qs)
    └── architecture.md         Day 55  diagram and system overview
```

## Day 0 commands

```bash
mkdir loreforge && cd loreforge
git init                          # start version control
mkdir -p docs/weekly              # learning notes folder
uv init backend --app             # creates backend/ with pyproject.toml, .python-version, main.py
cd backend
uv add "fastapi[standard]"        # adds FastAPI + dev server to pyproject.toml, creates .venv and uv.lock
uv run python -c "import fastapi; print(fastapi.__version__)"   # run inside the uv environment, sanity check
```

Save PROJECT.md, PROGRESS.md, DESIGN.md, ROADMAP.md and STRUCTURE.md in the repo root.

## Why this shape (tradeoff note)
- Chose: one repo with `backend/`, `frontend/`, `docs/` (a "monorepo"). Gave up: independent repos per service. Alternative: separate repos, more setup for no benefit when working alone.
- Chose: backend organised by layer (routers / services / models). Gave up: organising by feature. Alternative: feature folders, nicer at large scale, harder to explain at first.
