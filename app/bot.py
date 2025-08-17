from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties  # <-- додали
from .config import get_settings

settings = get_settings()

# було: bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, parse_mode="HTML")
bot = Bot(
    token=settings.TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")  # <-- правильно для aiogram 3.x
)

dp = Dispatcher()
