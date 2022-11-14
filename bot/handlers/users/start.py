from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import start_buttons 

from loader import dp, base, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    lname = message.from_user.last_name
    username = message.from_user.username
    tg_id = message.from_user.id
    try:
        base.foydalanuvchi_qoshish(first_name=name, username=username, tg_id=tg_id, last_name=lname)
        print('#2' * 10)
    except Exception:
        pass


    print('#3' * 10)
    await message.answer(f"<b>Assalomu alekum, {message.from_user.full_name}!</b>\n\nUptdown rasmiy botiga xush kelibsiz.\n\n/help buyrug'i yordamida nimalarga qodir ekanligimni bilib oling!")
    await message.answer(text="O'zingizni kerakli bo'limni tanglang:", reply_markup=start_buttons)
