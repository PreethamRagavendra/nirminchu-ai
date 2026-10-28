from fastapi import FastAPI
import uvicorn
from nirminchu_ai.routes.index import api_router

app = FastAPI(
    title="nirminchu-ai-system",
    version="0.1.0",
    description="Your Civil Engineering brain.",
)

app.include_router(api_router)


def start():
    """Launch Nirminchu AI Backend Server"""
    uvicorn.run("nirminchu_ai.main:app", host="127.0.0.1", port=8000, reload=True)
