# PROJECT: Loreforge

## What I'm building
Loreforge is a multi-tenant AI game master for tabletop RPGs. Groups ("guilds") create campaigns, upload their rulebooks and world lore, and an AI game master runs sessions for the players. The AI answers rules questions with citations, keeps lore consistent, and takes actions through tools (roll dice, update character sheets, manage inventory, advance quests). Big moves (killing a character, granting a legendary item) need the Dungeon Master's approval.

Working name: Loreforge (easy to rename later). Suggested URLs: loreforge.vercel.app (frontend), GitHub repo: loreforge.

## Access hierarchy
- Guild Owner: manages the guild, members, billing-like settings, sees everything
- Dungeon Master (manager): runs campaigns, approves risky AI actions, manages lore
- Player (team member): sees only their own party/campaign and own characters

Every row of data belongs to a guild (multi-tenancy), so one guild never sees another's data.

## Stack
- Backend: FastAPI (Python), managed with uv (packaging, virtual env, lockfile; no pip or requirements.txt)
- Frontend: Next.js + Tailwind CSS + shadcn/ui (customized, never default)
- DB: Postgres + pgvector
- Cache/queue: Redis
- Local dev: Docker
- Deploy (free tiers): Vercel (frontend), Render/Railway (backend), Neon (Postgres), Upstash (Redis)
- LLM: free tier (Gemini/Groq) or Ollama locally
- No paid services (maybe a domain at the very end)

## Concepts to learn (rough order)
1. Auth: JWT access + refresh tokens with rotation
2. Roles: Guild Owner > Dungeon Master > Player (RBAC)
3. Multi-tenancy: data scoped per guild
4. Redis: rate limiting, caching, background job queue
5. Idempotency keys (a retry never rolls the dice or grants loot twice)
6. RAG: chunking, embeddings, pgvector, citations, basic evals (rules and lore Q&A)
7. Agents: tool-calling loop (dice, character sheets, inventory, quests), human-in-the-loop approval by the DM, guardrails, streaming replies
8. MCP: my own MCP server (dice, character sheets, world state) that the agent connects to
9. Admin dashboard: usage, token cost per campaign, session logs, audit log of every AI decision, agent traces
10. Production: logging, tests, CI/CD, deployment, load testing (includes uv basics: pyproject.toml, uv.lock, uv add/sync/run, and using uv in Docker and CI)
11. Frontend: design system, components, API integration, client auth, loading/error/empty states

## My situation
- Intermediate programmer, working alone
- 1 hour per day, 8 weeks (~56 sessions)
- Free Claude plan, so token efficiency matters
- Built a support-desk project before; I want this one to be fun

## Weekly shape (high level)
- Week 1: design decisions + project setup + auth
- Week 2: guilds, campaigns, roles/RBAC, characters (basic CRUD)
- Week 3-4: lore/rulebook upload, ingestion queue, RAG with citations
- Week 5-6: AI game master agent + tools, MCP server, DM approvals, rate limiting, idempotency
- Week 7: admin dashboard, usage, audit logs, evals
- Week 8: deployment, CI/CD, monitoring, load test, README + architecture diagram

(Detailed day-by-day plan lives in ROADMAP.md.)
