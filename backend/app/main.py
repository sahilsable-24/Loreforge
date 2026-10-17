from fastapi import FastAPI
from app.routers.auth import router as auth_router

app = FastAPI(title="Loreforge")

@app.get("/health")
def health():
    return {"stauts": "ok"}

app.include_router(auth_router)