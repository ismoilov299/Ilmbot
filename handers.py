import asyncio
import sqlite3

import aioschedule as aioschedule
from aiogram.types.message import Message
import requests
from aiogram.utils import executor

from config import dp, bot
from aiogram import types
from keyboards import main_keyboard,asosiy
# from prayer_time import NamozVaqti
from prayer_time.vaqt import NamozVaqti




@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.reply('Namoz vaqti botiga hush kelibsiz', reply_markup=asosiy)


@dp.message_handler(text='Namoz vaqti')
async def pray_time(message:types.Message):
    await message.answer("👳🏻‍♂️ Namoz vaqti uchun Viloyat tanlang!", reply_markup=main_keyboard)

@dp.message_handler(text="back")
async def go_back(mes:types.Message):
    await mes.reply("Namoz vaqti", reply_markup=asosiy)


@dp.message_handler(text='Toshkent')
async def region(msg:types.Message):
    obj = NamozVaqti('Toshkent')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')

@dp.message_handler(text='Samarqand')
async def region(msg:types.Message):
    obj = NamozVaqti('Samarqand')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')


@dp.message_handler(text='Andijon')
async def region(msg:types.Message):
    obj = NamozVaqti('Andijon')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')


@dp.message_handler(text='Urganch')
async def region(msg:types.Message):
    obj = NamozVaqti('Urganch')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')


# KeyboardButton('Urgench'),
# KeyboardButton('Navoi'),
# KeyboardButton('Bukhara'),


@dp.message_handler(text='Navoiy')
async def region(msg:types.Message):
    obj = NamozVaqti('Navoiy')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')


@dp.message_handler(text='Buxoro')
async def region(msg:types.Message):
    obj = NamozVaqti('Buxoro')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')


# KeyboardButton('Termiz'),
# KeyboardButton('Qarshi'),
# KeyboardButton('Guliston'),


@dp.message_handler(text='Termiz')
async def region(msg:types.Message):
    obj = NamozVaqti('Termiz')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')


@dp.message_handler(text='Qarshi')
async def region(msg:types.Message):
    obj = NamozVaqti('Qarshi')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')


@dp.message_handler(text='Guliston')
async def region(msg:types.Message):
    obj = NamozVaqti('Guliston')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')


# KeyboardButton('Jizzax'),
# KeyboardButton("Farg'ona"),
# KeyboardButton('Namangan'),

@dp.message_handler(text='Jizzax')
async def region(msg:types.Message):
    obj = NamozVaqti('Jizzax')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')


@dp.message_handler(text="Farg'ona")
async def region(msg:types.Message):
    obj = NamozVaqti("Farg'оna")
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')


@dp.message_handler(text='Namangan')
async def region(msg:types.Message):
    obj = NamozVaqti('Namangan')
    await msg.reply(f"Sana: {obj.get_sana()}\n\nKun: {obj.get_kun()}\n\nShahar : Tashkent \n\nBomdod  {obj.bomdod()}\n\nQuyosh  {obj.quyosh_chiqishi()}\n\nPeshin  {obj.peshin()}\n\nAsr  {obj.asr()}\n\nShom {obj.shom()} \n\nXufton {obj.xufton()}",parse_mode='html')





#
# import asyncio
# import aioschedule
#
# async def noon_print():
#     print("It's noon!")
#
# async def scheduler():
#     aioschedule.every().day.at("12:00").do(noon_print)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)
#
# async def on_startup(_):
#     asyncio.create_task(scheduler())
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=False, on_startup=on_startup)