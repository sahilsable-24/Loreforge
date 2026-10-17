# LOREFORGE PROGRESS (snapshot, max 40 lines, replaced fully each day)

## Status
- Current day: Day 5 done, Day 6 next
- Week: 1
- Last session: Day 5 (SQLAlchemy, Alembic, users table, Argon2 hashing, POST /auth/register)
- Mood/pace: on track, register works end to end

## Completed (one line per finished week, compressed)
- (none yet)

## This week so far (max 7 lines)
- Day 0: ROADMAP.md and STRUCTURE.md saved; repo, docs/weekly and backend/ created with uv
- Day 1: DESIGN.md sections 0-1 filled (wordmark, 3 adjectives, 3 references)
- Day 2: DESIGN.md sections 2-4 filled; Claude design canvas made
- Day 3: contrast verified, tokens confirmed, 8 wireframes with states, DESIGN.md complete
- Day 4: .gitignore, .env.example, docker-compose (db + redis), /health, core/config.py
- Day 5: db/ (base, session, get_db), models/user.py, Alembic migration "create users", core/security.py (Argon2), schemas/user.py, routers/auth.py register (201 / 409)

## Current state of the code
- Tooling set up: uv [x] / Docker [x] / Next.js [ ]
- Folders/files that exist: loreforge/ (git), docs/weekly/, docker-compose.yml, .env.example, .gitignore, backend/ (pyproject.toml, uv.lock, alembic/, app/main.py, app/core/{config,security}.py, app/db/, app/models/user.py, app/schemas/user.py, app/routers/auth.py), PROJECT/PROGRESS/DESIGN/ROADMAP/STRUCTURE.md
- What works end to end: POST /auth/register saves a user with an Argon2 hash, duplicate email returns 409, response never includes the hash
- Editor note: Pyrefly search-path = ["."] set in pyproject.toml; run all commands from backend/

## Open problems / bugs (max 5)
- Real art not sourced yet (user uploads + Met Open Access)
- Verify "loading/empty/error" and mobile in code once the frontend exists (Day 8+)
- Register: email not lowercased, IntegrityError race not caught (revisit later)

## Decisions made (max 8, most important only)
- Monorepo: backend/, frontend/, docs/; backend organised by layer
- Design is DONE (Days 1-3); frontend code starts Day 8
- Dark-first, art-led; ember = actions, brass = trim only, status = icon + label
- Fonts: Source Serif 4 (headings, GM replies) + IBM Plex Sans (UI)
- Dev setup: API runs locally via uv, only Postgres and Redis in Docker
- Secrets: real .env never committed, .env.example documents variables
- Sync SQLAlchemy (not async); UUID ids; schema changes only via Alembic
- Argon2 via pwdlib (memory-hard); register returns no token, login is Day 6

## Next up
- Day 6: login, JWT access token, refresh token with rotation, one protected route

## Concepts I still feel shaky on
- Contrast ratios (4.5:1 = brightness gap; accents on shapes, not paragraphs)
- Why slow hashes beat fast ones; session lifecycle (get_db + close); why migrations beat create_all