from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_cmd(msg: types.Message):
    text = (
        "Привіт! Я допоможу організувати догляд за твоїми кімнатними рослинами.\n"
        "➕ Додай рослини, обери зручні дні та час — і я нагадаю, що робити."
    )
    await msg.answer(text)
