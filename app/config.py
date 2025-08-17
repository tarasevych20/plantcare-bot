import os
from pydantic import BaseModel

class Settings(BaseModel):
    TELEGRAM_BOT_TOKEN: str
    WEBHOOK_SECRET_PATH: str
    PUBLIC_BASE_URL: str
    DATABASE_URL: str
    DEFAULT_TZ: str = "Europe/Kyiv"
    DEFAULT_NOTIFY_TIME: str = "09:00"

def get_settings() -> Settings:
    return Settings(
        TELEGRAM_BOT_TOKEN=os.environ.get("TELEGRAM_BOT_TOKEN", ""),
        WEBHOOK_SECRET_PATH=os.environ.get("WEBHOOK_SECRET_PATH", "webhook-secret-uuid"),
        PUBLIC_BASE_URL=os.environ.get("PUBLIC_BASE_URL", "http://localhost:8000"),
        DATABASE_URL=os.environ.get("DATABASE_URL", ""),
        DEFAULT_TZ=os.environ.get("DEFAULT_TZ", "Europe/Kyiv"),
        DEFAULT_NOTIFY_TIME=os.environ.get("DEFAULT_NOTIFY_TIME", "09:00"),
    )
