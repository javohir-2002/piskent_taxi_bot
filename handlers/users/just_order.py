import re
import uuid
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data.texts import WARNING, JUST_ORDER
from loader import dp, bot
from states.order import Order
from data.config import GROUP_ID
from keyboards.default.order import status, order, cancel
from filters.prived_chat import IsPrivate


# Telefon raqam formatini tekshirish uchun funksiya
def is_valid_phone(phone):
    return re.fullmatch(r'(\+998)?\d{9}', phone) is not None


@dp.message_handler(IsPrivate(), Text("✍️ E'lonni qo'lda yozish ✍️"))
async def start_ordering(message: types.Message, state: FSMContext):
    # name = message.text.title()
    # await state.update_data(name=name)
    await message.answer("📞 Bog'lanish uchun telefon raqam kiriting", reply_markup=cancel)
    await Order.phone.set()


@dp.message_handler(IsPrivate(), state=Order.phone)
async def handler_get_phone(message: types.Message, state: FSMContext):
    phone = message.text

    if not phone.startswith('+998'):
        phone = '+998' + phone

    if is_valid_phone(phone):
        await state.update_data(phone=phone)

        await message.answer(JUST_ORDER)
        await Order.next()

    else:
        await message.answer("❌ Telefon raqam noto'g'ri. Iltimos, telefon raqamni to'g'ri formatda kiriting. Masalan: +998901234567 yoki 901234567")


@dp.message_handler(IsPrivate(), state=Order.order_message)
async def handler_get_message(message: types.Message, state: FSMContext):
    order_message = message.text
    await state.update_data(order_message=order_message)

    post_id = ''.join(filter(str.isdigit, str(uuid.uuid4())))[:4]

    data = await state.get_data()

    msg = ""
    msg += f"<b>#️⃣ #E_{post_id}</b>\n\n"
    msg += f"<b>💬 Xabar:</b> {data.get('order_message')}\n\n"
    msg += f"<b>📞 {data.get('phone')}</b>\n\n"

    msg += "<b>✨ @piskent_taxi_bot ✨</b>"

    await message.answer(msg)

    sent_message = await bot.send_message(GROUP_ID, msg, parse_mode="HTML")
    bot["group_message_id"] = sent_message.message_id  # Save the message id

    await message.answer(
        "Post @piskent_taxi_chat guruhiga yuborildi.\nSiz bilan tez orada bog'lanishadi."
    )
    await message.answer(WARNING, reply_markup=status)
    await state.finish()


