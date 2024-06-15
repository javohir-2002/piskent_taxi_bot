from aiogram import types
from aiogram.types import ChatType


def private_chat_only(handler):
    async def wrapped(message: types.Message, *args, **kwargs):
        if message.chat.type != ChatType.PRIVATE:
            return
        return await handler(message, *args, **kwargs)

    return wrapped
