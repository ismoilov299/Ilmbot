import asyncio

from aiogram.utils import executor

from config import dp, bot


@dp.message_handler()
async def time_msg(message):
    try:
        timer_sec = int(message.text)
        if timer_sec <= 0:
            raise ValueError()

    except (TypeError, ValueError):
        await bot.send_message(chat_id=message.chat.id, text="vaqtni kiriting!")
        return
    new_msg = await bot.send_message(chat_id=message.chat.id,text=f"vaqt: {timer_sec}")

    for sec_left in range(timer_sec - 1, -1, -1 ):
        await asyncio.sleep(1)
        await new_msg.edit_text(text=f"vaqt: {sec_left}")

    await bot.send_message(chat_id=message.chat.id, text="vaqt tugadi")



if __name__ == '__main__':
    executor.start_polling(dp)