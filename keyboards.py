from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Toshkent'),
            KeyboardButton('Samarqand'),
            KeyboardButton('Andijon'),
        ],
        [
            KeyboardButton('Urganch'),
            KeyboardButton('Navoi'),
            KeyboardButton('Buxoro'),
        ],
        [
            KeyboardButton('Termiz'),
            KeyboardButton('Qarshi'),
            KeyboardButton('Guliston'),
        ],
        [
            KeyboardButton('Jizzax'),
            KeyboardButton("Farg'ona"),
            KeyboardButton('Namangan'),
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

adminMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='All users'),
            KeyboardButton(text='Follow namaz')
        ],
    ],
    resize_keyboard=True)

asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Namoz vaqti")
        ]
    ],
    resize_keyboard=True
)