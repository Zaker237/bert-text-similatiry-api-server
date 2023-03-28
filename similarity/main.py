from fastapi import FastAPI
from similarity.routers import router

app = FastAPI(
    title="Sentence Similarity",
    version="0.0.1"
)

app.include_router(router, prefix="/api")