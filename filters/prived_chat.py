from aiogram import types

from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter):
    """Shaxsiy yozishmami yoki yo'qligini aniqlaydigan filter."""

    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE
