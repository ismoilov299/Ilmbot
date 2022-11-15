from loader import dp, bot, chanel
from aiogram.types import CallbackQuery
from keyboards.inline.namozturlar_Inline import qoidalar


# FARZ_____________________


@dp.callback_query_handler(text='f:bomdod')
async def send_sura(call: CallbackQuery):
    # await bot.delete_message()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=686)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=692)
@dp.callback_query_handler(text='f:peshin')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=680)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=694)

@dp.callback_query_handler(text='f:asr')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=681)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=696)

@dp.callback_query_handler(text='f:shom')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=682)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=697)

@dp.callback_query_handler(text='f:xufton')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=684)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=699)
@dp.callback_query_handler(text='juma')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=689)

@dp.callback_query_handler(text='janoza')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=690)

# SUNNAT__________________


@dp.callback_query_handler(text='s:bomdod')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=685)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=691)

@dp.callback_query_handler(text='s:peshin2')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=679)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=695)
@dp.callback_query_handler(text='s:peshin4')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=678)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=693)

@dp.callback_query_handler(text='s:shom')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=683)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=698)
@dp.callback_query_handler(text='s:xufton')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=705)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=700)



# VOJIB _______________________

@dp.callback_query_handler(text='vitr')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=702)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=701)

@dp.callback_query_handler(text='hayit')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=703)

# NAMOZ TURLARI ______________________

@dp.callback_query_handler(text='in')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1186)

@dp.callback_query_handler(text='tn')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1193)


@dp.callback_query_handler(text='mn')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1187)


@dp.callback_query_handler(text='shn')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1188)


@dp.callback_query_handler(text='zn')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1189)


@dp.callback_query_handler(text='shn2')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1190)


@dp.callback_query_handler(text='tavban')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1194)


@dp.callback_query_handler(text='tasbeh')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1195)

@dp.callback_query_handler(text='hn')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1191)


@dp.callback_query_handler(text='an')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1192)


@dp.callback_query_handler(text='markab')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1196)

@dp.callback_query_handler(text="amalF")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1197)

@dp.callback_query_handler(text="amalV")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1198)

@dp.callback_query_handler(text="amalS")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1199)

@dp.callback_query_handler(text="mustahab")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1200)

@dp.callback_query_handler(text="harom")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1201)

@dp.callback_query_handler(text="muboh")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1202)

@dp.callback_query_handler(text="makruh1")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1203)

@dp.callback_query_handler(text="makruh2")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1204)

@dp.callback_query_handler(text="odob")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1205)

@dp.callback_query_handler(text="buzuvchi")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1208)

@dp.callback_query_handler(text="sajda")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1206)

@dp.callback_query_handler(text="sutra")
async def qoidalar(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1207)


