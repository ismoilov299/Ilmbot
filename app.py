import datetime

from aiogram import executor

import asyncio
import aioschedule

from loader import db
from prayer_time.vaqt import NamozVaqti
from config import bot


for user in db.get_users_subscribe():
    user_regions = user[3]
    print(user_regions)

# for user in db.get_users_subscribe():
#     user_id = user[1]

async def bomdod():
    print("yuborildi!")
    for user in db.get_users_subscribe():
        print(user[1])
    obj = NamozVaqti('Toshkent')
    vv = obj.bomdod()
    # await bot.send_message(chat_id=user[1],text=f"{vv} bomdod vaqti bo'ldi")
    await bot.send_message(chat_id=5006818392,text=f"{vv} bomdod vaqti bo'ldi")


async def peshin():
    for user in db.get_users_subscribe():
        try:
           user_id = user[1]
           print(user_id)
           await bot.send_message(chat_id=user_id,text= 'Peshin vaqti bo\'ldi')
        except:
            print('block')


async def asr():
    time = NamozVaqti('Toshkent')
    asr_vaqti = time.asr()
    # await bot.send_message(chat_id=user[1],text=f"{asr_vaqti} Asr vaqti bo'ldi")
    await bot.send_message(chat_id=5006818392,text=f"{asr_vaqti} Asr vaqti bo'ldi")

async def shom():
    time = NamozVaqti('Toshkent')
    asr_vaqti = time.shom()
    # await bot.send_message(chat_id=user[1],text=f"{asr_vaqti} Shom vaqti bo'ldi")
    await bot.send_message(chat_id=5006818392,text=f"{asr_vaqti} Shom vaqti bo'ldi")

async def Xufton():
    time = NamozVaqti('Toshkent')
    xufton_vaqti = time.xufton()
    # await bot.send_message(chat_id=user[1],text=f"{xufton_vaqti} Shom vaqti bo'ldi")
    await bot.send_message(chat_id=5006818392,text=f"{xufton_vaqti} Shom vaqti bo'ldi")






async def scheduler():
    delta = datetime.timedelta(hours=5)
    obj = NamozVaqti('Toshkent')
    w = obj.peshin()
    a = obj.asr()
    sh = obj.shom()
    x = obj.xufton()
    aioschedule.every().day.at(w).do(peshin)
    aioschedule.every().day.at(a).do(asr)
    aioschedule.every().day.at(sh).do(shom)
    aioschedule.every().day.at(x).do(shom)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)







async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    from handers import dp
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)

