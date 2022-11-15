from loader import dp, bot,chanel
from aiogram.types import CallbackQuery, Message

from keyboards.inline.namozturlar_Inline import gusl


@dp.callback_query_handler(text='omoveniye')
async def namoz_turi(call: CallbackQuery):
    await call.message.edit_text("<b>G'usul va Tahorat\n</b>",reply_markup=gusl,parse_mode="html")

@dp.callback_query_handler(text="gusl")
async def gusul(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=655,
                           protect_content=True)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="tahorat")
async def gusul(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=564,
                           protect_content=True)
    await call.answer(cache_time=60)