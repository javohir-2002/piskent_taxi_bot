from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from data.texts import WELCOME_TEXT
from keyboards.default.order import order
from filters.prived_chat import IsPrivate


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(WELCOME_TEXT, parse_mode="HTML")
    await message.answer(
        "Taxi chaqirish uchun <b>🚕 TAXI 🚕</b> tugmasiga bosing", reply_markup=order
    )
