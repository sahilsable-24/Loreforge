import uuid
from datetime import datetime, timedelta, timezone

import httpx
import jwt

from app.core.config import settings

BASE = "http://127.0.0.1:8000"
client = httpx.Client(base_url=BASE)

email = f"test-{uuid.uuid4().hex[:8]}@example.com"  # fresh user every run
password = "CorrectHorse!42"
failures = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global failures
    print(f"{'PASS' if ok else 'FAIL'}  {name} {detail}")
    if not ok:
        failures += 1


def login(pw: str = password):
    return client.post("/auth/login", json={"email": email, "password": pw})


def me(token: str | None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return client.get("/auth/me", headers=headers)


# ---------- REGISTER ----------
r = client.post("/auth/register", json={"email": email, "password": password})
check("register new user -> 201", r.status_code == 201, str(r.status_code))
check("register never returns the hash", "hash" not in r.text.lower())

r = client.post("/auth/register", json={"email": email, "password": password})
check("register duplicate -> 409", r.status_code == 409, str(r.status_code))

# ---------- LOGIN (negative) ----------
wrong_pw = login("not-the-password")
unknown = client.post("/auth/login", json={"email": "nobody@example.com", "password": password})
check("login wrong password -> 401", wrong_pw.status_code == 401)
check("login unknown email -> 401", unknown.status_code == 401)
check("same error message for both (no email leak)", wrong_pw.json() == unknown.json())
r = client.post("/auth/login", json={"email": email})
check("login missing password -> 422", r.status_code == 422, str(r.status_code))

# ---------- LOGIN (positive) ----------
r = login()
check("login correct -> 200", r.status_code == 200, str(r.status_code))
tokens = r.json()
access, refresh1 = tokens["access_token"], tokens["refresh_token"]
check("login returns both tokens", bool(access) and bool(refresh1))

# ---------- PROTECTED ROUTE ----------
r = me(None)
# Newer FastAPI returns 401 for a missing header, older versions return 403
check("/me without token -> 401/403", r.status_code in (401, 403), str(r.status_code))
check("/me garbage token -> 401", me("abc.def.ghi").status_code == 401)

expired = jwt.encode(
    {"sub": str(uuid.uuid4()), "exp": datetime.now(timezone.utc) - timedelta(minutes=1)},
    settings.jwt_secret, algorithm="HS256",
)
check("/me expired token -> 401", me(expired).status_code == 401)

forged = jwt.encode(
    {"sub": str(uuid.uuid4()), "exp": datetime.now(timezone.utc) + timedelta(minutes=5)},
    "wrong-secret-wrong-secret-wrong-secret", algorithm="HS256",
)
check("/me token signed with wrong secret -> 401", me(forged).status_code == 401)

valid_but_ghost = jwt.encode(
    {"sub": str(uuid.uuid4()), "exp": datetime.now(timezone.utc) + timedelta(minutes=5)},
    settings.jwt_secret, algorithm="HS256",
)
check("/me valid token, user doesn't exist -> 401", me(valid_but_ghost).status_code == 401)

r = me(access)
check("/me valid token -> 200", r.status_code == 200, str(r.status_code))
check("/me returns the right user", r.json().get("email") == email)

# ---------- REFRESH ----------
r = client.post("/auth/refresh", json={"refresh_token": "garbage"})
check("refresh garbage token -> 401", r.status_code == 401)

r = client.post("/auth/refresh", json={"refresh_token": refresh1})
check("refresh valid -> 200", r.status_code == 200, str(r.status_code))
pair2 = r.json()
refresh2 = pair2["refresh_token"]
check("rotation gives a different refresh token", refresh2 != refresh1)
check("new access token works", me(pair2["access_token"]).status_code == 200)

r = client.post("/auth/refresh", json={"refresh_token": refresh1})
check("REUSE of old refresh token -> 401", r.status_code == 401, str(r.status_code))

r = client.post("/auth/refresh", json={"refresh_token": refresh2})
check("new token revoked by theft rule -> 401", r.status_code == 401, str(r.status_code))

# ---------- RECOVERY ----------
r = login()
check("user can log in again after revocation", r.status_code == 200)
r2 = client.post("/auth/refresh", json={"refresh_token": r.json()["refresh_token"]})
check("fresh login's refresh works", r2.status_code == 200)

print(f"\n{'ALL PASSED' if failures == 0 else f'{failures} FAILED'}")