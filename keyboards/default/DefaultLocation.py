from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

location = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text="Lokatsiya yuboring📍",request_location=True)],[KeyboardButton(text="Asosiy menu⬅")]])