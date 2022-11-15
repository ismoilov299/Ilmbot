from aiogram.types import CallbackQuery, Location, Message, ReplyKeyboardRemove

from masjid_aniqlash.distance import choose_shortes
from keyboards.default.DefaultLocation import location
from keyboards.default.menuKeyboard import MEnu
from loader import dp, bot

@dp.callback_query_handler(text='masjidMain')
async def masjid(call: CallbackQuery):
    await call.message.answer(text="Lokatsiyangizni yuboring va sizga eng yaqin bo'lgan masjidni aniqlang✅", reply_markup=location)
    await call.answer(cache_time=60)

@dp.message_handler(text="Asosiy menu⬅")
async def menu(msg: Message):
    await msg.answer("Asosiy menu", reply_markup=MEnu)
    await msg.answer(".", reply_markup=ReplyKeyboardRemove(True))
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id+2)

@dp.message_handler(content_types='location')
async def get_contact(msg: Message):
    closest_masjid = choose_shortes(msg.location)
    for distance, url, masjid_location in closest_masjid:
        await msg.answer(f"<b>{masjid_location['name']}</b>🕌"f"\nMasofa: {distance:.1f} км", disable_web_page_preview=True)
        await msg.answer_location(latitude=masjid_location["lat"],
                                  longitude=masjid_location["lon"])
