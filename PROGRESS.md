# LOREFORGE PROGRESS (snapshot, max 40 lines, replaced fully each day)

## Status
- Current day: Day 7 done, Day 8 next
- Week: 2 (starts with frontend setup)
- Last session: Day 7 (pytest auth tests on test DB, email normalization, Week 1 doc)
- Mood/pace: on track, 8 auth tests green

## Completed (one line per finished week, compressed)
- Week 1: design system done (DESIGN.md); uv + Docker backend; register/login/refresh with rotation + reuse detection; 8 pytest tests on a separate test DB

## This week so far (max 7 lines)
- (Week 2 not started)

## Current state of the code
- Tooling set up: uv [x] / Docker [x] / Next.js [ ]
- Folders/files that exist: loreforge/ (git), docs/weekly/week-01.md, docker-compose.yml, .env.example, .gitignore, backend/ (pyproject.toml, uv.lock, alembic/, app/main.py, app/core/{config,security,deps}.py, app/db/, app/models/{user,refresh_token}.py, app/schemas/{user,auth}.py, app/routers/auth.py, tests/{conftest,test_auth}.py), PROJECT/PROGRESS/DESIGN/ROADMAP/STRUCTURE.md
- What works end to end: register, login (JWT + refresh), refresh rotation, reuse detection, /auth/me, emails trimmed + lowercased
- Editor note: run all commands from backend/; run tests with `uv run pytest -v` (pythonpath set in pyproject.toml)

## Open problems / bugs (max 5)
- Real art not sourced yet (user uploads + Met Open Access)
- Verify "loading/empty/error" and mobile in code once the frontend exists (Day 8+)
- Register: IntegrityError race not caught (revisit later)
- Refresh endpoint has no rate limit; token delivery (JSON vs httpOnly cookie) decided Day 13
- Test DB URL hardcoded in conftest (make configurable in CI, Day 51); httpx deprecation warning (ignore)

## Decisions made (max 8, most important only)
- Monorepo: backend/, frontend/, docs/; backend organised by layer
- Dark-first; ember = actions, brass = trim only; fonts Source Serif 4 + IBM Plex Sans
- Dev setup: API runs locally via uv, only Postgres and Redis in Docker
- Sync SQLAlchemy; UUID ids; schema changes only via Alembic, never edit applied migrations
- Argon2 for passwords; SHA-256 for refresh tokens
- Auth: HTTPBearer + JSON login, 15 min access JWT, 7 day DB-stored rotating refresh tokens
- Tests: separate loreforge_test DB, tables truncated after each test

## Next up
- Day 8: frontend setup: Next.js, Tailwind, shadcn customized from DESIGN.md tokens, fonts, Lucide, themed empty app shell

## Concepts I still feel shaky on
- Contrast ratios (4.5:1 = brightness gap; accents on shapes, not paragraphs)
- Hashing vs encryption; why slow hashes suit passwords but not random tokens
- Why commit before raising (HTTPException rolls back the session)
- Refresh reuse detection: what the thief and the real user each experience
- Test isolation: dependency_overrides and truncate-after-test