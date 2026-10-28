from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/generate")
def generateChat():
    return "Your first response"
