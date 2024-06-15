from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from filters.prived_chat import IsPrivate


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ", "/start - Botni ishga tushirish", "/help - Yordam")

    await message.answer("\n".join(text))
