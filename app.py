import sqlite3
import time

import data,middlewares,handlers,keyboards
from data.config import ADMINS
from loader import dp, db, bot
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from aiogram import executor

import asyncio
import aioschedule

from loader import db
from prayer_time.vaqt import NamozVaqti, api_namaz

print(ADMINS[0])




# functionlar namzo vaqtlari uchun
async def bomdod(userID):
    try:
        await bot.send_message(chat_id=userID, text='🌌Bomdod vaqti bo\'ldi!')
    except Exception as ex:
        print(ex)

async def quyosh(userID):
    try:
       await bot.send_message(chat_id=userID,text= '🌄Quyosh chiqdi!')
    except Exception as ex:
       print(ex)


async def peshin(userID):
    try:
       await bot.send_message(chat_id=userID,text= '🌇Peshin vaqti bo\'ldi!')
    except Exception as ex:
       print(ex)


async def asr(userID):
    try:
       await bot.send_message(chat_id=userID, text= '🌆Asr vaqti bo\'ldi!')
    except Exception as ex:
       print(ex)
async def shom(userID):
    try:
       await bot.send_message(chat_id=userID,text= '🏙Shom vaqti bo\'ldi!')
    except Exception as ex:
       print(ex)
async def Xufton(userID):
    try:
       await bot.send_message(chat_id=userID,text= '🌃Xufton vaqti bo\'ldi!')
    except Exception as ex:
       print(ex)

#schedule namoz vaqti ucun

async def scheduler():
    for user in db.get_users_subscribe():
        for time in db.get_times():
            if user[3] == time[0]:
                aioschedule.every().day.at(time[1]).do(bomdod,user[1])
                aioschedule.every().day.at(time[2]).do(quyosh,user[1])
                aioschedule.every().day.at(time[3]).do(peshin,user[1])
                aioschedule.every().day.at(time[4]).do(asr,user[1])
                aioschedule.every().day.at(time[5]).do(shom,user[1])
                aioschedule.every().day.at(time[6]).do(Xufton,user[1])
                aioschedule.every().day.at('03:33').do(api_namaz)    #schedule db namaz upadte uchun

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)




async def on_startup(dispatcher):
    asyncio.create_task(scheduler())
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    try:
        db.create_table_users()
    except Exception and sqlite3.Error as sq:
        print()

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=False, on_startup=on_startup)


