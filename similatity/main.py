from fastapi import FastAPI
from similatity.routers import router

app = FastAPI(
    title="Sentence Similarity",
    version="0.0.1"
)

app.include_router(router, prefix="")