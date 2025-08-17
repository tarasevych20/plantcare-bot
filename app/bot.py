from aiogram import Bot, Dispatcher
from .config import get_settings

settings = get_settings()
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
