from keyboards.default.asmaul_husna_menuKeyboard import ismMain
from keyboards.inline.asmaul_husna_Inline import ismlarinline1, ismlarinline2, ismlarinline3, ismlarinline4, \
    ismlarinline5, ismlarinline6, ismlarinline7, ismlarinline8, ismlarinline9, ismlarinline10
from loader import dp, bot,chanel
from aiogram.types import CallbackQuery, Message


# @dp.message_handler(text='Allohning 99 ismi')
# async def ismlar_99(msg: Message):
#     await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=chanel, message_id=709,
#                            protect_content=True)
#     await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=chanel, message_id=1214,
#                            protect_content=True)
#     await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=chanel, message_id=1215,
#                            protect_content=True)


# @dp.callback_query_handler(text='99ism')
# async def namaz_time(call: CallbackQuery):
#     await call.message.delete()
#     await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=709)
#     await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1214)
#     await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1215)
#     await call.message.answer("""<b>Alloh, deb chorlangiz, yoki Rahmon – Mehribon, deb chorlangiz. Qanday chorlasangizlarda (joizdir). Zero, U zotning goʻzal ismlari bordir"</b>("Al-isro" surasi, 110-oyat).""",reply_markup=ismMain, parse_mode="html")


@dp.callback_query_handler(text='..1')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1425)

    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup = ismlarinline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..2')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1426)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup = ismlarinline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..3')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1427)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup = ismlarinline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..4')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=837)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup = ismlarinline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..5')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=838)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup = ismlarinline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..6')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=839)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup = ismlarinline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..7')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=840)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup = ismlarinline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..8')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=841)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup = ismlarinline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..9')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=842)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup = ismlarinline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..10')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=843)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup = ismlarinline1)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='..11')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=844)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..12')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=845)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..13')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=846)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..14')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=847)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..15')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=848)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..16')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=849)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..17')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=850)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..18')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=851)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=945)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=946)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..19')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=852)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..20')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=853)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..21')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=854)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..22')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=855)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..23')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=856)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..24')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=857)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=943)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=944)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..25')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=858)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..26')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=859)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..27')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=860)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..28')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=861)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..29')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=862)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..30')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=863)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..31')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=864)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..32')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=865)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..33')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=866)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..34')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=867)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..35')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=868)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..36')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=869)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=948)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=949)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..37')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=870)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=979)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=980)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..38')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=871)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..39')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=872)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..40')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=873)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..41')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=874)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..42')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1032)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=952)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=953)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..43')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=875)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=972)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=973)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=974)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..44')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=876)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..45')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=877)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..46')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=878)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..47')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=879)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..48')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=880)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..49')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=881)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..50')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=882)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..51')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=843)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..52')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=884)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..53')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=885)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..54')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=886)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..55')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=887)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..56')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=888)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=939)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..57')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=889)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..58')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=890)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=959)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=960)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..59')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=891)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..60')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=892)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..61')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=893)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..62')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1033)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..63')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=894)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=970)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=971)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..64')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=895)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..65')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=897)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..66')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=898)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..67')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1034)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..68')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=899)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..69')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=900)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=931)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=932)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..70')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=901)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..71')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=902)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..72')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=903)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..73')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=904)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..74')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=905)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..75')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=906)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..76')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=907)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..77')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=908)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=937)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=938)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..78')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=909)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..79')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=910)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..80')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=911)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..81')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=912)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..82')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=913)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..83')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=914)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..84')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=915)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..85')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=916)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..86')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=917)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..87')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=918)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..88')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=919)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..89')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=920)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..90')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=921)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..91')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=922)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline10)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..92')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=923)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline10)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..93')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=924)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline10)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..94')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=925)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline10)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..95')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=926)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline10)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..96')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=927)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline10)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..97')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=928)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline10)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..98')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=929)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline10)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='..99')
async def send_ism(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=930)
    await call.message.answer("Allohning go'zal ismlari ma'nolari", reply_markup=ismlarinline10)
    await call.answer(cache_time=60)