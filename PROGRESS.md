# LOREFORGE PROGRESS (snapshot, max 40 lines, replaced fully each day)

## Status
- Current day: Day 6 done, Day 7 next (review day)
- Week: 1
- Last session: Day 6 (login, JWT access token, rotating refresh tokens, /auth/me, smoke test)
- Mood/pace: on track, auth works end to end, all smoke tests pass

## Completed (one line per finished week, compressed)
- (none yet)

## This week so far (max 7 lines)
- Days 0-1: repo + uv backend + roadmap/structure; DESIGN.md sections 0-1 (brand, adjectives, references)
- Day 2: DESIGN.md sections 2-4 (color, type, tokens); Claude design canvas made
- Day 3: contrast verified, tokens confirmed, 8 wireframes with states, DESIGN.md complete
- Day 4: .gitignore, .env.example, docker-compose (db + redis), /health, core/config.py
- Day 5: db/, models/user.py, Alembic, Argon2 (core/security.py), POST /auth/register (201 / 409)
- Day 6: pyjwt, refresh_tokens model + migration, /auth/login, /auth/refresh (rotation + reuse detection), core/deps.py get_current_user, GET /auth/me, tests/smoke_auth.py (all pass)

## Current state of the code
- Tooling set up: uv [x] / Docker [x] / Next.js [ ]
- Folders/files that exist: loreforge/ (git), docs/weekly/, docker-compose.yml, .env.example, .gitignore, backend/ (pyproject.toml, uv.lock, alembic/, app/main.py, app/core/{config,security,deps}.py, app/db/, app/models/{user,refresh_token}.py, app/schemas/{user,auth}.py, app/routers/auth.py, tests/smoke_auth.py), PROJECT/PROGRESS/DESIGN/ROADMAP/STRUCTURE.md
- What works end to end: register, login (JWT + refresh), refresh with rotation, reuse detection revokes all user tokens, /auth/me protected by HTTPBearer
- Editor note: Pyrefly search-path = ["."] set in pyproject.toml; run all commands from backend/; run smoke test with `uv run python -m tests.smoke_auth`

## Open problems / bugs (max 5)
- Real art not sourced yet (user uploads + Met Open Access)
- Verify "loading/empty/error" and mobile in code once the frontend exists (Day 8+)
- Register: email not lowercased, IntegrityError race not caught (revisit later)
- Smoke script is not pytest yet and leaves test users in dev DB (Day 7)
- Refresh endpoint has no rate limit; token delivery (JSON vs httpOnly cookie) decided Day 13

## Decisions made (max 8, most important only)
- Monorepo: backend/, frontend/, docs/; backend organised by layer
- Design is DONE (Days 1-3); frontend code starts Day 8
- Dark-first; ember = actions, brass = trim only; fonts Source Serif 4 + IBM Plex Sans
- Dev setup: API runs locally via uv, only Postgres and Redis in Docker
- Sync SQLAlchemy; UUID ids; schema changes only via Alembic, never edit applied migrations
- Argon2 for passwords; SHA-256 for refresh tokens (random, fast lookup)
- Auth: HTTPBearer + JSON login, 15 min access JWT, 7 day DB-stored refresh tokens with rotation
- Secrets: real .env never committed, .env.example documents variables

## Next up
- Day 7: review day: pytest auth tests (clean test DB), cleanup, Week 1 docs entry

## Concepts I still feel shaky on
- Contrast ratios (4.5:1 = brightness gap; accents on shapes, not paragraphs)
- Hashing vs encryption; why slow hashes suit passwords but not random tokens
- Why commit before raising (HTTPException rolls back the session)
- Refresh reuse detection: what the thief and the real user each experience