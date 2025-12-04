from fastapi import FastAPI

app = FastAPI(title="testservice1")

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
