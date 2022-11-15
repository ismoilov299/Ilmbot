from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


namozMenu =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Namoz vaqtlari⏰', callback_data='namazTime'),
            InlineKeyboardButton(text='Namozni o\'rganish🧎', callback_data='namazType'),

        ],
        [
            InlineKeyboardButton(text="G'usl va Tahorat🚰", callback_data='omoveniye'),
            InlineKeyboardButton(text='Zam suralar📖', callback_data='ZamSuralat'),

        ],
        [
            InlineKeyboardButton(text='Bosh menu⬅️', callback_data='menu'),

        ],


    ])
