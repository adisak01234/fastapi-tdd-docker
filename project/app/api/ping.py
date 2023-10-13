from fastapi import APIRouter, Depends

from app.config import get_setting, Settings

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_setting)):
    return {
        "ping": "pong!",
        'environment': settings.environment,
        'testing': settings.testing
    }
