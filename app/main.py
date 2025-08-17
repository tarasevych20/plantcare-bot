from fastapi import FastAPI
from .routes import router
from .handlers import start as start_handlers
from .bot import bot
from .config import get_settings

app = FastAPI()
app.include_router(router)

# Під'єднуємо aiogram-роутери
from .bot import dp
dp.include_router(start_handlers.router)

@app.on_event("startup")
async def on_startup():
    # Виставляємо вебхук
    s = get_settings()
    webhook_url = f"{s.PUBLIC_BASE_URL}/webhook/{s.WEBHOOK_SECRET_PATH}"
    await bot.set_webhook(url=webhook_url)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
