from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Додати рослину"), KeyboardButton(text="🌿 Мої рослини")],
            [KeyboardButton(text="🗓 Мій графік"), KeyboardButton(text="⚙️ Налаштування")],
        ],
        resize_keyboard=True
    )
