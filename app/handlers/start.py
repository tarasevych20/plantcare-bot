from aiogram import Router, types
from aiogram.filters import CommandStart
from ..services.keyboards import main_menu_kb
from ..services.texts import WELCOME
from ..db import SessionLocal
from ..crud.users import ensure_user

router = Router()

@router.message(CommandStart())
async def start_cmd(msg: types.Message):
    user = msg.from_user
    async with SessionLocal() as db:
        _, created = await ensure_user(
            db,
            user_id=user.id,
            username=user.username,
            first_name=user.first_name
        )

    if created:
        await msg.answer(
            "Привіт! 👋 Я допоможу організувати догляд за твоїми рослинами.\n"
            "Створив твій профіль. Нижче — головне меню.",
            reply_markup=main_menu_kb()
        )
    else:
        await msg.answer(WELCOME, reply_markup=main_menu_kb())
