import re
import uuid
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data.texts import WARNING
from loader import dp, bot
from states.order import OrderData, Order
from data.config import GROUP_ID
from keyboards.default.order import status, order, cancel
from filters.prived_chat import IsPrivate


# Telefon raqam formatini tekshirish uchun funksiya
def is_valid_phone(phone):
    return re.fullmatch(r'(\+998)?\d{9}', phone) is not None


@dp.message_handler(IsPrivate(), Text("⬅️ Bekor qilish"), state="*")
async def cancel_order(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Buyurtma bekor qilindi. Taxi chaqirish uchun <b>🚕 TAXI 🚕</b> tugmasiga bosing",
        reply_markup=order,
    )


# @dp.message_handler(IsPrivate(), Text("🚕 TAXI 🚕"))
# async def start_ordering(message: types.Message, state: FSMContext):
#     await message.answer("👤 Ismingizni kiriting.", reply_markup=cancel)
#     await OrderData.from_where.set()


@dp.message_handler(IsPrivate(), Text("🚕 TAXI 🚕"))
async def start_ordering(message: types.Message, state: FSMContext):
    # name = message.text.title()
    # await state.update_data(name=name)
    await message.answer("📍 Qayerdan olib ketish kerak?", reply_markup=cancel)
    await OrderData.from_where.set()


@dp.message_handler(IsPrivate(), state=OrderData.from_where)
async def get_user_from_where(message: types.Message, state: FSMContext):
    from_where = message.text.capitalize()
    await state.update_data(from_where=from_where)
    await message.answer("🚕 Qayerga olib borish kerak?")
    await OrderData.next()


@dp.message_handler(IsPrivate(), state=OrderData.to_where)
async def get_user_to_where(message: types.Message, state: FSMContext):
    to_where = message.text.capitalize()
    await state.update_data(to_where=to_where)
    # await message.answer("👥 Odam soni nechta?")
    await message.answer("💰 Qancha to'laysiz?")
    await OrderData.next()


# @dp.message_handler(IsPrivate(), state=OrderData.num_of_people)
# async def get_num_of_people(message: types.Message, state: FSMContext):
#     num_of_people = message.text
#     await state.update_data(num_of_people=num_of_people)
#     await message.answer("💰 Qancha to'laysiz?")
#     await OrderData.next()


@dp.message_handler(IsPrivate(), state=OrderData.price)
async def get_price(message: types.Message, state: FSMContext):
    price = message.text
    await state.update_data(price=price)
    await message.answer("📞 Bog'lanish uchun telefon raqam kiriting")
    await OrderData.next()


@dp.message_handler(IsPrivate(), state=OrderData.phone)
async def get_phone(message: types.Message, state: FSMContext):
    phone = message.text

    if not phone.startswith('+998'):
        phone = '+998' + phone

    post_id = ''.join(filter(str.isdigit, str(uuid.uuid4())))[:4]

    if is_valid_phone(phone):
        await state.update_data(phone=phone)

        data = await state.get_data()

        msg = ""
        # msg += f"<b>👤 {data.get('name')}</b>\n\n"
        msg += f"<b>#️⃣ #E_{post_id}</b>\n\n"
        msg += f"<b>📍 {data.get('from_where')}</b> | <b>{data.get('to_where')}</b> 🚕\n\n"
        msg += f"<b>💰 {data.get('price')} | {data.get('phone')}</b> 📞\n\n"
        # msg += f"<b>👥 Odam soni:</b> {data.get('num_of_people')}\n\n"
        # msg += f"<b>💬 Qo'shimcha:</b> {data.get('addition')}\n\n"
        msg += "<b>✨ @piskent_taxi_bot ✨</b>"

        await message.answer(msg)

        sent_message = await bot.send_message(GROUP_ID, msg, parse_mode="HTML")
        bot["group_message_id"] = sent_message.message_id  # Save the message id

        await message.answer(
            "Post @piskent_taxi_chat guruhiga yuborildi.\nSiz bilan tez orada bog'lanishadi."
        )
        await message.answer(WARNING, reply_markup=status)
        await state.finish()

    else:
        await message.answer("❌ Telefon raqam noto'g'ri. Iltimos, telefon raqamni to'g'ri formatda kiriting. Masalan: +998901234567 yoki 901234567")


@dp.message_handler(IsPrivate(), Text(equals=["✅ Olindi", "❌ Bekor qilindi", "🗑 E'lonni o'chirish"]))
async def delete_group_post(message: types.Message):
    group_message_id = bot.get("group_message_id")

    if group_message_id:
        await bot.delete_message(GROUP_ID, group_message_id)
        await message.answer("Post o'chirildi.", reply_markup=order)
        await message.answer(
        "Taxi chaqirish uchun <b>🚕 TAXI 🚕</b> tugmasiga bosing", reply_markup=order
        )
    else:
        await message.answer(
            "Post o'chirib bo'lmadi, xabar identifikatori topilmadi.",
            reply_markup=order,
        )
