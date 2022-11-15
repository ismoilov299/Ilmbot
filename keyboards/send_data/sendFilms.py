from keyboards.default.menuKeyboard import MEnu
from keyboards.inline.kino import umarSeries, umarSeries2, umarSeries3, films
from keyboards.inline.kino import Oy1, Oy2, Oy3, films
from loader import dp, bot, chanel
from aiogram.types import CallbackQuery, message
from data.config import Chanel



@dp.callback_query_handler(text='kinoMain')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("O'zingizga kerakli filmini tanlang!")
    await call.message.edit_reply_markup(films)

@dp.callback_query_handler(text='Bilol')
async def bilol_callback(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1362,reply_markup=MEnu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='Umar')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()

@dp.callback_query_handler(text='umar1')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=Chanel, message_id=1363)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar2')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1364)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar3')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1365)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar4')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1366)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar5')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1367)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar6')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1368)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar7')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1369)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar8')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1370)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar9')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1371)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='umar10')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1372)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='umarmenu2')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()

@dp.callback_query_handler(text='umarmenu3')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()

@dp.callback_query_handler(text='umar11')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1373)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar12')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1374)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar13')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1375)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar14')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1376)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar15')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1377)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar16')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1378)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar17')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1379)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar18')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1380)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar19')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1381)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar20')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1382)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar21')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1383)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar22')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1384)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar23')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1385)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar24')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1386)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar25')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1387)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar26')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1388)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar27')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1389)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar28')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1390)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar29')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1391)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='umar30')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1392)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
    await call.message.delete()
    await call.answer(cache_time=60)
#
# @dp.callback_query_handler(text='umar30')
# async def send_umar1(call: CallbackQuery):
#     await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1393)
#     await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=umarSeries3)
#     await call.message.delete()
#     await call.answer(cache_time=60)





@dp.callback_query_handler(text='Oy')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()

@dp.callback_query_handler(text='Oy1')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=Chanel, message_id=1395)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy2')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1396)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy3')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1397)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy4')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1398)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy5')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1399)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy6')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1400)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy7')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1401)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy8')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1402)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy9')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1403)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='Oy10')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1404)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy1)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='Oymenu2')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()

@dp.callback_query_handler(text='Oymenu3')
async def Umar_callback(call:CallbackQuery):
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()

@dp.callback_query_handler(text='Oy11')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1405)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy12')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1406)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy13')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1407)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy14')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1408)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy15')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1409)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy16')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1410)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy17')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1411)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy18')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1412)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy19')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1413)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy20')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1414)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy21')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1415)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy22')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1416)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy23')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1417)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy24')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1418)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy25')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1419)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy26')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1420)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy27')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1421)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy28')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1422)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy29')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1423)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Oy30')
async def send_umar1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1424)
    await call.message.answer("O'zingizga kerakli serani tanlang👇",reply_markup=Oy3)
    await call.message.delete()
    await call.answer(cache_time=60)
