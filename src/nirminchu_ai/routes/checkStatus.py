from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/")
async def checkStatus():
    return {"status": 200, "response": "Your civil engineering brain is alive."}


