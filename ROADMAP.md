# LOREFORGE ROADMAP

8 weeks, 1 hour a day, 56 sessions. Every 7th day is a lighter review/catch-up day (tests, cleanup, weekly docs entry, finish whatever slipped).
Rules: design is finished (Days 1-3) before any UI code. Frontend code starts Day 8. Every screen gets loading, empty and error states.

## Weekly goals

| Week | Theme | Goal at end of week |
|------|-------|---------------------|
| 1 | Design + setup + auth | Design decided in DESIGN.md. Backend runs with Postgres and Redis in Docker. Users can register and log in (JWT access + rotating refresh tokens). |
| 2 | Guilds, roles, campaigns, characters | Multi-tenant data (every row has a guild). Owner / DM / Player permissions work. Campaigns and characters CRUD. Next.js app styled from DESIGN.md, login + guild hub screens working. |
| 3 | Lore ingestion | Upload a rulebook or lore file, a background worker extracts text, chunks it, embeds it, stores vectors in pgvector. Similarity search works. Lore library screen. |
| 4 | RAG with citations | Ask a rules/lore question, get an answer that cites its sources, scoped to the guild. A small eval set measures quality. Citations view in the UI. |
| 5 | AI game master agent | Tool-calling loop (dice, character sheets, inventory, quests), session history, streaming replies, session screen. |
| 6 | MCP, approvals, safety | Own MCP server the agent connects to. DM approval queue for risky actions. Idempotency keys. Redis rate limiting and guardrails. |
| 7 | Admin + evals | Token usage and cost per campaign, audit log of every AI decision, agent traces, agent evals. Character sheet, admin and settings screens. |
| 8 | Ship it | Logging, tests, CI with uv, deploy on free tiers, load test, mobile/empty/error polish, README + architecture diagram. |

## 56-day plan

| Day | Week | Focus | Output |
|-----|------|-------|--------|
| 1 | 1 | Design I: brand, 3 adjectives, 3 reference products | DESIGN.md sections 0-1 |
| 2 | 1 | Design II: color (light + dark), typography | DESIGN.md sections 2-3 |
| 3 | 1 | Design III: tokens + wireframes of all 8 screens | DESIGN.md sections 4-6 done |
| 4 | 1 | Setup: git, docker-compose (Postgres+pgvector, Redis), FastAPI skeleton, /health | `docker compose up` works, /health returns ok |
| 5 | 1 | Database: SQLAlchemy, Alembic, users table, password hashing, register | POST /auth/register works |
| 6 | 1 | Auth: login, JWT access token, refresh token with rotation | Login + refresh + protected route |
| 7 | 1 | Review: auth tests, cleanup, weekly docs entry | Week 1 doc, tests green |
| 8 | 2 | Frontend setup: Next.js, Tailwind, shadcn customized from tokens, fonts, Lucide | Themed empty app shell |
| 9 | 2 | Guilds + memberships tables, guild_id on every row | Create/list guilds |
| 10 | 2 | RBAC: Owner > DM > Player dependency checks | Role-protected endpoints |
| 11 | 2 | Campaigns + isolation tests (guild A never sees guild B) | Campaign CRUD + tenancy tests |
| 12 | 2 | Characters CRUD (players see only own) | Character endpoints |
| 13 | 2 | Frontend: login/register + guild hub screens with all states | Working login and hub |
| 14 | 2 | Review: tests, cleanup, weekly docs entry | Week 2 doc |
| 15 | 3 | RAG overview + lore/rulebook upload endpoint | Upload stores file + metadata |
| 16 | 3 | Redis job queue + background worker | Job runs outside the request |
| 17 | 3 | Text extraction + chunking | Document becomes chunks |
| 18 | 3 | Embeddings + storing vectors in pgvector | Chunks have vectors |
| 19 | 3 | Similarity search endpoint (guild-scoped) | Query returns top-k chunks |
| 20 | 3 | Frontend: lore library screen (upload, status, empty, error) | Upload from the UI |
| 21 | 3 | Review: ingestion tests, weekly docs entry | Week 3 doc |
| 22 | 4 | RAG answer: retrieve + prompt the LLM | Rules Q&A endpoint |
| 23 | 4 | Citations: map answer back to source chunks/pages | Answers with sources |
| 24 | 4 | Guardrail: "not in the rules" when retrieval is weak | No made-up rules |
| 25 | 4 | Eval set: ~20 rules/lore questions with expected sources | Eval script |
| 26 | 4 | Run evals, tune chunk size and top-k | Before/after scores |
| 27 | 4 | Frontend: Q&A view with citations | Citations visible in UI |
| 28 | 4 | Review: cleanup, weekly docs entry | Week 4 doc |
| 29 | 5 | Agent concept: tool-calling loop with one tool (roll dice) | Agent rolls dice |
| 30 | 5 | Character sheet tools (read, update HP/stats) | Agent edits sheets |
| 31 | 5 | Inventory + quest tools | Agent manages loot and quests |
| 32 | 5 | Sessions + message history + system prompt (lore via RAG) | Multi-turn session |
| 33 | 5 | Streaming replies (SSE) | Tokens stream to client |
| 34 | 5 | Frontend: session screen (chat, dice, party) | Playable session UI |
| 35 | 5 | Review: agent tests, weekly docs entry | Week 5 doc |
| 36 | 6 | Build own MCP server (dice, sheets, world state) | MCP server runs |
| 37 | 6 | Agent connects to the MCP server | Tools now come via MCP |
| 38 | 6 | Human-in-the-loop: risky action becomes "pending approval" | Agent pauses for DM |
| 39 | 6 | DM approval queue: API + screen | Approve/reject from UI |
| 40 | 6 | Idempotency keys (retry never rolls twice or grants loot twice) | Safe retries |
| 41 | 6 | Redis rate limiting + guardrails (max tool steps, input limits) | Limits enforced |
| 42 | 6 | Review: tests for approvals/idempotency, weekly docs entry | Week 6 doc |
| 43 | 7 | Usage tracking: tokens per call, cost per campaign | Usage table filled |
| 44 | 7 | Audit log of every AI decision + agent traces | Audit endpoint |
| 45 | 7 | Admin analytics API | Aggregated stats |
| 46 | 7 | Frontend: admin analytics + audit log screens | Admin screens |
| 47 | 7 | Frontend: character sheet + settings screens | Last two screens |
| 48 | 7 | Agent evals (right tool, right args, respects approvals) | Agent eval script |
| 49 | 7 | Review: cleanup, weekly docs entry | Week 7 doc |
| 50 | 8 | Structured logging, error handling, tests on critical paths | Logs + coverage of key flows |
| 51 | 8 | CI with GitHub Actions + uv | Green pipeline |
| 52 | 8 | Backend Dockerfile (uv) + deploy backend, Neon, Upstash | Live API |
| 53 | 8 | Deploy frontend on Vercel, env config, smoke test | Live app |
| 54 | 8 | Load test + fixes + mobile/empty/error polish pass | Load test report |
| 55 | 8 | README + architecture diagram + final docs | Portfolio-ready repo |
| 56 | 8 | Final review: mock interview questions, retrospective | Interview cheat sheet |
