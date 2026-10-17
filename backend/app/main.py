from fastapi import FastAPI

app = FastAPI(title="Loreforge")

@app.get("/health")
def health():
    return {"stauts": "ok"}