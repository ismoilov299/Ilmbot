from aiogram.types import Message, CallbackQuery
from loader import dp, bot, chanel

from keyboards.inline.zam_sura_inline import zaminline

@dp.callback_query_handler(text='ZamSuralat')
async def zam(call: CallbackQuery):
    await call.message.edit_text("""
<b>1 <i>Sharh</i></b>
<b>2 <i>Tiyn</i></b>
<b>3 <i>Fiyl</i></b>
<b>4 <i>Quraysh</i></b>
<b>5 <i>Ma'un</i>  </b>  
<b>6 <i>Kavsar</i>  </b>
<b>7 <i>Kafirun </i></b> 
<b>8 <i>Nasr</i>   </b>
<b>9 <i>Masad</i></b>
<b>10 <i>Ixlos</i></b>
<b>11 <i>Falaq</i></b>
<b>12 <i>Nas</i></b>
""",reply_markup=zaminline,parse_mode='html')

@dp.callback_query_handler(text='sura1')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1059)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel,message_id=1062)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura2')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1179)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=397)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura3')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1057)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=406)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura4')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1047)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=407)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura5')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1049)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=408)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura6')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1058)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=409)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='sura7')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1050)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=410)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='sura8')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1051)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=411)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='sura9')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1052)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=412)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura10')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1053)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=413)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura11')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1054)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=414)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='sura12')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1055)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=415)
    await call.answer(cache_time=60)



