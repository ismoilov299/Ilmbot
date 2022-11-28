import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import reply_keyboard

from keyboards.default.menuKeyboard import MEnu

from data.config import ADMINS
from loader import dp, bot, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum va rohmatullohi va barokatuhu, {message.from_user.full_name}!☺️", reply_markup=MEnu)
    name = message.from_user.full_name

    try:
        db.add_user(user_id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError and Exception:
        pass
        # for admin in ADMINS:
        #     await bot.send_message(chat_id=admin,text=(f"Start comandasi:\n{err}"))




