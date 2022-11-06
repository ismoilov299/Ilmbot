from aiogram import executor, types

import asyncio
import aioschedule
from prayer_time.vaqt import NamozVaqti
from config import bot, dp


async def noon_print():
    print("yuborildi!")
    obj = NamozVaqti('Toshkent')
    vv = obj.bomdod()
    await bot.send_message(chat_id=1161180912,text=f"{vv} bomdod vaqti bo'ldi")
    await bot.send_message(chat_id=5006818392,text=f"{vv} bomdod vaqti bo'ldi")


async def peshin():
    time = NamozVaqti('Toshkent')
    peshin_vaqti = time.peshin()
    await bot.send_message(chat_id=1161180912,text=f"{peshin_vaqti} Peshin vaqti bo'ldi")
    await bot.send_message(chat_id=5006818392,text=f"{peshin_vaqti} Peshin vaqti bo'ldi")

async def asr():
    time = NamozVaqti('Toshkent')
    asr_vaqti = time.asr()
    await bot.send_message(chat_id=1161180912,text=f"{asr_vaqti} Asr vaqti bo'ldi")
    await bot.send_message(chat_id=5006818392,text=f"{asr_vaqti} Asr vaqti bo'ldi")

async def shom():
    time = NamozVaqti('Toshkent')
    asr_vaqti = time.shom()
    await bot.send_message(chat_id=1161180912,text=f"{asr_vaqti} Shom vaqti bo'ldi")
    await bot.send_message(chat_id=5006818392,text=f"{asr_vaqti} Shom vaqti bo'ldi")

async def Xufton():
    time = NamozVaqti('Toshkent')
    xufton_vaqti = time.xufton()
    await bot.send_message(chat_id=1161180912,text=f"{xufton_vaqti} Shom vaqti bo'ldi")
    await bot.send_message(chat_id=5006818392,text=f"{xufton_vaqti} Shom vaqti bo'ldi")






async def scheduler():
    obj = NamozVaqti('Toshkent')
    w = obj.peshin()
    a = obj.asr()
    sh = obj.shom()
    x = obj.xufton()
    aioschedule.every().day.at(w).do(peshin)
    aioschedule.every().day.at(a).do(asr)
    aioschedule.every().day.at(sh).do(shom)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)







async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    from handers import dp
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)

