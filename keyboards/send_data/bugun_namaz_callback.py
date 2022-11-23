from keyboards.default.namazKeyboard import namozMenu

from loader import dp, bot, db
from aiogram.types import CallbackQuery
from prayer_time.vaqt import NamozVaqti


def bugun(region):
    ob = NamozVaqti(region)
    return (f""" 
    📍Mintaqa - {region}
    <b>{ob.get_kun()}</b>

    📆<i>{ob.get_sana()}</i>

    🌌 Bomdod: <b>{ob.bomdod()}</b>
    🌄 Quyosh: <b>{ob.quyosh_chiqishi()}</b>
    🌇 Peshin: <b>{ob.peshin()}</b>
    🌆 Asr: <b>{ob.asr()}</b>
    🏙 Shom: <b>{ob.shom()}</b>
    🌃 Xufton: <b>{ob.xufton()}</b>
    
    <b> Nazmoz vaqtlari islom.uz saytidan olindi</b>
    """)



"""CALLBACK_QUERY_HANDLER"""
#Toshkent Andijon Buxoro Guliston Samarqand Namangan Navoiy Jizzax Nukus Qarshi Qo'qon Xiva
@dp.callback_query_handler(text='bugun:toshkent')
async def inline_today_toshkent(call: CallbackQuery):
    await call.message.delete()
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Toshkent"), parse_mode="html",reply_markup=namozMenu)#,reply_markup=types.ReplyKeyboardRemove()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:andijon')
async def inline_today_andijon(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Andijon"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:buxoro')
async def inline_today_buxoro(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Buxoro"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:guliston')
async def inline_today_guliston(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Guliston"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:samarqand')
async def inline_today_sqmqrqand(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Samarqand"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:namangan')
async def inline_today_namangan(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Namangan"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:navoi')
async def inline_today_navoi(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Navoiy"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:jizzax')
async def inline_today_jizzax(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Jizzax"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:nukus')
async def inline_today_nukus(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Nukus"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:qarshi')
async def inline_today_qarshi(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Qarshi"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:qoqon')
async def inline_today_qoqon(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Qo'qon"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:xiva')
async def inline_today_xiva(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Xiva"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:margilon')
async def inline_today_margilon(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text=bugun("Marg'ilon"), parse_mode="html",reply_markup=namozMenu)
    await call.answer(cache_time=60)

