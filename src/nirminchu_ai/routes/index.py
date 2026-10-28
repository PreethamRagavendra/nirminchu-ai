from fastapi import APIRouter
from nirminchu_ai.routes.checkStatus import api_router as statusRouter
from nirminchu_ai.routes.generate import api_router as generateRouter

api_router = APIRouter()

api_router.include_router(statusRouter)
api_router.include_router(generateRouter)