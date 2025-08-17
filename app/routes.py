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
    try:
        # aiogram 3.x + pydantic v2: валідуємо так
        update = types.Update.model_validate(data)
    except Exception as e:
        print(f"[WARN] update parse failed: {e} | data={data}")
        return Response(status_code=200)
    await dp.feed_update(bot, update)
    return Response(status_code=200)
