from aiogram.types import Message, CallbackQuery

from loader import dp

from keyboards.inline.asmaul_husna_Inline import ismlarinline1, ismlarinline2, ismlarinline3, ismlarinline4, ismlarinline5, ismlarinline10, ismlarinline6, ismlarinline7, ismlarinline8, ismlarinline9


@dp.callback_query_handler(text='.2')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='.1')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='.3')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline3)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='.4')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline4)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='.5')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline5)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='.6')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='.7')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline7)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='.8')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline8)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='.9')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline9)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='.10')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline10)
    await call.answer(cache_time=60)
