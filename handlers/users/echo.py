from aiogram import types

from loader import dp
from filters.prived_chat import IsPrivate


# Echo bot
@dp.message_handler(IsPrivate(), state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
