



from aiogram.types.message import Message

from aiogram.dispatcher.filters import Command


from config import dp, bot
from aiogram import types
from keyboards import asosiy, adminMenu, main_keyboard
from loader import db
from prayer_time.vaqt import NamozVaqti


ADMINS= 1161180912

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    for user in db.get_users_subscribe():
        print(user[3])
    await message.reply('Namoz vaqti botiga hush kelibsiz', reply_markup=asosiy)



@dp.message_handler(Command("admins"),user_id=ADMINS)
async def show_menu(message: Message):
    await message.answer("Admin menu",reply_markup=adminMenu)

@dp.message_handler(text="All users", user_id=ADMINS)
async def get_all_users(message: Message):
    users = f"XAMMA USERSLAR:{db.select_all_users()}"

    await bot.send_message(chat_id=message.from_user.id, text=users)

#
@dp.message_handler(text="Follow namaz", user_id=ADMINS)
async def count_obuna(message: Message):
    def count():
        msg = ""
        i = ""
        for i, us in enumerate(db.count_obuna()):
            msg += f"""{i+1}.<b>{us[1]}</b>({us[2]})\n"""
            i += i
        return f"{msg}\n\nObunachilar soni {i}"
    await bot.send_message(chat_id=message.from_user.id, text=count())

@dp.message_handler(text='Namoz vaqti')
async def pray_time(message:types.Message):
    await message.answer("👳🏻‍♂️ Namoz vaqti uchun Viloyat tanlang!",reply_markup=main_keyboard)

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


@dp.message_handler(text='Samarqand')
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