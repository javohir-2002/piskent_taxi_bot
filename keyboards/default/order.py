from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


order = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚕 TAXI 🚕"), KeyboardButton(text="✍️ E'lonni qo'lda yozish ✍️")],
        [KeyboardButton(text="Xatolik haqida xabar berish")],
    ],
    resize_keyboard=True,
)

status = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🗑 E'lonni o'chirish")],
        # [KeyboardButton(text="✅ Olindi")],
        # [KeyboardButton(text="❌ Bekor qilindi")],
    ],
    resize_keyboard=True,
)

cancel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️ Bekor qilish")],
    ],
    resize_keyboard=True,
)

errors = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Xatolik haqida xabar berish")],
    ],
    resize_keyboard=True,
)
