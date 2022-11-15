from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(),state=None)
async def bot_help(message: types.Message):
    text = "Bot bo'yicha savol va takliflaringiz bo'lsa adminlarga murojat qiling.\nAdminlar bilan ulanish uchun:@ismoilov299  @davlatovv_z"
    await message.answer((text))
