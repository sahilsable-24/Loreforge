# Week 1: Design, setup and auth

## What it is
The foundation: a documented design system, a FastAPI backend with Postgres
and Redis in Docker, and a complete login system (register, login, JWT access
tokens, rotating refresh tokens) with automated tests.

## How I did it
- Days 1-3: DESIGN.md (brand, dark-first color, type, tokens, 8 wireframes).
- Day 4: uv backend, docker-compose (Postgres + pgvector, Redis), /health.
- Day 5: SQLAlchemy + Alembic, Argon2 password hashing, POST /auth/register.
- Day 6: /auth/login, 15 min access JWT, 7 day refresh tokens stored as
  SHA-256 hashes, rotation + reuse detection, get_current_user dependency.
- Day 7: pytest on a separate loreforge_test DB (tables truncated after each
  test), 8 auth tests, emails normalized by a Pydantic validator.

## Tradeoffs
- Argon2 for passwords (slow on purpose) vs SHA-256 for refresh tokens
  (random and high-entropy, so a fast hash is fine and lookups stay quick).
- Truncate-after-test vs rollback-per-test: chose simpler truncation because
  endpoints call commit() themselves.
- create_all for the test DB vs running migrations: faster setup, but
  migrations aren't tested yet.

## Interview questions
1. Why hash passwords with a slow algorithm but refresh tokens with a fast one?
2. How does refresh token rotation with reuse detection work, and what does
   the legitimate user experience when a token is stolen?
3. How do you keep tests from touching real data, and what are the tradeoffs
   of your approach?