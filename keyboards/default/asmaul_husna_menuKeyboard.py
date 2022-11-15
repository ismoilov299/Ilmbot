
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ismMain = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Allohning 99 ismi', callback_data='99ism'),
            InlineKeyboardButton(text="Ma'nolari", callback_data='mano'),

        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data='menu'),
        ],


    ])