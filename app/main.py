from fastapi import FastAPI
from .routes import router
from .handlers import start as start_handlers
from .bot import bot, dp
from .config import get_settings

app = FastAPI()
app.include_router(router)

# aiogram routers
dp.include_router(start_handlers.router)

@app.get("/")
async def root():
    return {"ok": True}

@app.on_event("startup")
async def on_startup():
    s = get_settings()
    print("[STARTUP] app is starting…")
    if s.PUBLIC_BASE_URL and s.WEBHOOK_SECRET_PATH and s.TELEGRAM_BOT_TOKEN:
        webhook_url = f"{s.PUBLIC_BASE_URL.rstrip('/')}/webhook/{s.WEBHOOK_SECRET_PATH}"
        try:
            await bot.set_webhook(url=webhook_url, drop_pending_updates=True)
            print(f"[STARTUP] webhook set: {webhook_url}")
        except Exception as e:
            print(f"[WARN] set_webhook failed: {e}")
    else:
        print("[INFO] Skipping set_webhook: missing PUBLIC_BASE_URL or token.")

@app.on_event("shutdown")
async def on_shutdown():
    try:
        await bot.session.close()
    except Exception as e:
        print(f"[WARN] bot session close: {e}")
