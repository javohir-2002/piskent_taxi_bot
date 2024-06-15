from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


order = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚕 TAXI 🚕")],
    ],
    resize_keyboard=True,
)

status = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Olindi")],
        [KeyboardButton(text="❌ Bekor qilindi")],
    ],
    resize_keyboard=True,
)

cancel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️ Bekor qilish")],
    ],
    resize_keyboard=True,
)
