import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.greeting import router as greeting_router

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="testservice1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(greeting_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
