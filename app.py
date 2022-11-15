import sqlite3
import time

from aiogram import executor

import data,middlewares,handlers,keyboards
from loader import dp, db, bot
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from aiogram import executor

import asyncio
import aioschedule

from loader import db
from prayer_time.vaqt import NamozVaqti



async def bomdod():
    for user in db.get_users_subscribe():
        try:
           user_id = user[1]
           await bot.send_message(chat_id=user_id,text= '🌌Bomdod vaqti bo\'ldi!')
        except:
            print('block')


async def quyosh():
    for user in db.get_users_subscribe():
        try:
           user_id = user[1]
           await bot.send_message(chat_id=user_id,text= '🌄Quyosh chiqdi!')
        except:
            print('block')


async def peshin():
    for user in db.get_users_subscribe():
        try:
           user_id = user[1]
           await bot.send_message(chat_id=user_id,text= '🌇Peshin vaqti bo\'ldi!')
        except:
            print('block')


async def asr():
    for user in db.get_users_subscribe():
        try:
           user_id = user[1]
           await bot.send_message(chat_id=user_id, text= '🌆Asr vaqti bo\'ldi!')
        except:
            print('block')

async def shom():
    for user in db.get_users_subscribe():
        try:
           user_id = user[1]
           await bot.send_message(chat_id=user_id,text= '🏙Shom vaqti bo\'ldi!')
        except:
            print('block')

async def Xufton():
    for user in db.get_users_subscribe():
        try:
           user_id = user[1]
           await bot.send_message(chat_id=user_id,text= '🌃Xufton vaqti bo\'ldi!')
        except:
            print('block')

for users in db.get_users_subscribe():
    user_regions = users[3]
    print(user_regions)



async def scheduler():
    # for users in db.get_users_subscribe():
    #     user_regions = users[3]
    obj = NamozVaqti(user_regions)
    b  = obj.bomdod()
    q = obj.quyosh_chiqishi()
    w = obj.peshin()
    a = obj.asr()
    sh = obj.shom()
    x = obj.xufton()
    aioschedule.every().day.at(b).do(bomdod)
    aioschedule.every().day.at(q).do(quyosh)
    aioschedule.every().day.at(w).do(peshin)
    aioschedule.every().day.at(a).do(asr)
    aioschedule.every().day.at(sh).do(shom)
    aioschedule.every().day.at(x).do(shom)
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


