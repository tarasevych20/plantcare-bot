from fastapi import APIRouter, Request, Response
from aiogram import types
from .bot import dp, bot
from .config import get_settings
from .services.scheduler import tick_scheduler

router = APIRouter()
settings = get_settings()

@router.post(f"/webhook/{settings.WEBHOOK_SECRET_PATH}")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = types.Update(**data)
    await dp.feed_update(bot, update)
    return Response(status_code=200)

@router.get("/health")
async def health():
    return {"ok": True}

@router.post("/scheduler")
async def scheduler_endpoint():
    await tick_scheduler()
    return {"status": "tick"}
