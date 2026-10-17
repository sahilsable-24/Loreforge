# LOREFORGE PROGRESS (snapshot, max 40 lines, replaced fully each day)

## Status
- Current day: Day 3 done, Day 4 next
- Week: 1
- Last session: Day 3 (Design III: contrast check, tokens confirmed, 8 wireframes)
- Mood/pace: on track, was lost mid-day but finished; design phase complete

## Completed (one line per finished week, compressed)
- (none yet)

## This week so far (max 7 lines)
- Day 0: ROADMAP.md and STRUCTURE.md saved; repo, docs/weekly and backend/ created with uv
- Day 1: DESIGN.md sections 0-1 filled (wordmark, 3 adjectives, 3 references)
- Day 2: DESIGN.md sections 2-4 filled; Claude design canvas made (hub + lore library with draggable 3D book)
- Day 3: contrast verified (one fix: light success #3F6B3A), tokens confirmed + focus ring, 8 wireframes with states, DESIGN.md complete, final-look preview canvas (hub + session)

## Current state of the code
- Tooling set up: uv [x] / Docker [ ] / Next.js [ ]
- Folders/files that exist: loreforge/ (git), docs/weekly/, backend/ (pyproject.toml, uv.lock, .python-version, main.py), PROJECT/PROGRESS/DESIGN/ROADMAP/STRUCTURE.md
- What works end to end: uv environment with fastapi installed (no app running yet)

## Open problems / bugs (max 5)
- Real art not sourced yet (user uploads + Met Open Access)
- Verify "loading/empty/error" and mobile in code once the frontend exists (Day 8+)

## Decisions made (max 8, most important only)
- Monorepo: backend/, frontend/, docs/; backend organised by layer
- Design is DONE (Days 1-3); frontend code starts Day 8
- Dark-first, art-led (D&D Beyond), paper editorial bands (Stripe Press)
- Colors: ink/paper neutrals, ember = actions, brass = trim only, status = icon + label
- Fonts: Source Serif 4 (headings, GM replies, 600 max) + IBM Plex Sans (UI, tabular-nums)
- Tokens confirmed Day 3 (spacing, radius, borders, focus ring 2px ember)
- Motion: 3D draggable rulebook on lore library only; reduced motion respected
- Art: user uploads + public-domain paintings, no clip-art

## Next up
- Day 4: Setup - .gitignore, .env.example, docker-compose (Postgres+pgvector, Redis), FastAPI skeleton in backend/app/main.py, /health returns ok

## Concepts I still feel shaky on
- Contrast ratios (what 4.5:1 measures: brightness gap, 1 to 21; accents go on shapes, not paragraphs)