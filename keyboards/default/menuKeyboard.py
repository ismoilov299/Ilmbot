
from aiogram.types import InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery, Message

from keyboards.default.asmaul_husna_menuKeyboard import ismMain
from keyboards.default.namazKeyboard import namozMenu
from keyboards.inline.arab_tili import dars
from keyboards.inline.asmaul_husna_Inline import ismlarinline1
from keyboards.inline.dars import QuranTartli
from keyboards.inline.duo_inline import duoMenu
from keyboards.inline.kitoblar_Inline import kbsend
from keyboards.inline.quran_Inline import quronMenu, quraninline1

from keyboards.inline.sahobalar_inline import sbsend
from loader import dp, bot

MEnu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Namoz🕋', callback_data='namozMenu'),
            InlineKeyboardButton(text='Qur\'on📖', callback_data='quronMain'),

        ],
        [
            InlineKeyboardButton(text='Duo va Zikirlar🤲', callback_data='duoMain'),
        ],
        [
            InlineKeyboardButton(text='Sahobalar👳🏻‍♂️️', callback_data='sahobaMain'),
            InlineKeyboardButton(text='Asmaul Husna', callback_data='ismMain'),

        ],
        [
            InlineKeyboardButton(text='Yaqin Masjid🕌️️', callback_data='masjidMain'),
            InlineKeyboardButton(text='Kitoblar📚', callback_data='kitobMain'),

        ],
        [
            InlineKeyboardButton(text='Filmlar🎞', callback_data='kinoMain'),
            InlineKeyboardButton(text='Darsliklar📕', callback_data='darsMain'),

        ],
    ])



@dp.callback_query_handler(text='namozMenu')
async def menuNamaz(call:CallbackQuery):
    await call.message.edit_text("<b>«Ahlingizni namoz (o‘qish)ga buyuring va (o‘zingiz ham) unga (namozga) bardoshli bo‘ling!»</b>\n(Toha, 132).",parse_mode='html')
    await call.message.edit_reply_markup(namozMenu)



# @dp.callback_query_handler(text='namazTime')
# async def namaz_time(call: CallbackQuery):
#     await call.message.edit_text()
#     await call.message.edit_reply_markup()

@dp.callback_query_handler(text='darsMain')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("O'zingizga kerakli darsni tanlang!")
    await call.message.edit_reply_markup(dars)

# tartiliMenu2
@dp.callback_query_handler(text='tartili')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("O'zingizga kerakli darsni tanlang!")
    await call.message.edit_reply_markup(QuranTartli)



@dp.callback_query_handler(text='99ism')
async def namaz_time(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=709)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1214)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=1215)
    await call.message.answer("""<b>Alloh, deb chorlangiz, yoki Rahmon – Mehribon, deb chorlangiz. Qanday chorlasangizlarda (joizdir). Zero, U zotning goʻzal ismlari bordir"</b>("Al-isro" surasi, 110-oyat).""",reply_markup=ismMain, parse_mode="html")


@dp.callback_query_handler(text='mano')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("Allohning go'zal ismlarining ma'nolari")
    await call.message.edit_reply_markup(ismlarinline1)


@dp.callback_query_handler(text='ismMain')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("""<b>Alloh, deb chorlangiz, yoki Rahmon – Mehribon, deb chorlangiz. Qanday chorlasangizlarda (joizdir). Zero, U zotning goʻzal ismlari bordir"</b>("Al-isro" surasi, 110-oyat).""",parse_mode="html")
    await call.message.edit_reply_markup(ismMain)


@dp.callback_query_handler(text='kitobMain')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("01 - Musulmonning odobi\n"
                         "02 - VIjdon azobi\n"
                         "03 - Payg'ambarlar tarixi\n"
                         "04 - Oisha r.a\n"
                         "05 - Qiyomat va Oxirat \n"
                         "06 - Ibodati islomiya\n"
                         "07 - Tarixi Muhammadiy\n"
                         "08 - Saodat asri qissalari\n"
                         "09 - Hadis va Hayot (9 juz)\n"
                         "10 - Qirq hadisi qudusiy")
    await call.message.edit_reply_markup(kbsend)

@dp.callback_query_handler(text='quronMain')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("""<b>Qur'on karim haqida ma'lumotlar:</b>\n
• <i>Qur'onning ismi Furqon</i>
• <i>Qur'onning laqabi. Majid</i>
• <i>Qur'on nozil bo'lgan yil. 611 milodiy yili</i>
• <i>Qur'on nozil bo'lgan oyi. Ramazon oyi</i>
• <i>Qur'on nozil bo'lgan kecha. Qadr kechasi</i>
• <i>Qur'on nozil bo'lgan joy. Makka Hiro g'ori</i>
• <i>Vahiy farishtasi. <b>Jabroil Alayhi Salom</b></i>
• <i>Vahiyni qabul qilgan. <b>Muhammad Sallohu Alayhi Vasallam</b></i>
• <i>Birinchi nozil bo'lgan sura. Alaq surasining 5 ta oyati</i>
• <i>Oxirgi nozil bölgan sura. Nasr surasi</i>
• <i>Eng buyuk sura. Baqara surasi</i>
• <i>Eng kichkina sura. Kavsar surasi</i>
• <i>Eng barokatli oyat. Oyatul kursi</i>
• <i>Eng buyuk oyat. Baqara suraning 286-oyati</i>
• <i>Qur'onning onasi. Fotiha surasi</i>
• <i>Qur'onni qalbi. Yosin surasi</i>
• <i>Qur'onning  kelini. Rahmon surasi</i>
• <i>Nozil bulgan muddat. 23 yilda</i>
• <i>Qur'on necha juz. 30 juz(pora)</i>
• <i>Qur'onning suralari. 114 ta</i>
• <i>Qur'onning  oyatilari 6236ta(bazi manbalarda 6666)</i>
• <i>Qur'onning sajdalari. 14 sajda</i>
• <i>Qur'onning ruku'lari. 540 ta</i>""",parse_mode="html")
    await call.message.edit_reply_markup(quronMenu)

@dp.callback_query_handler(text='next')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("01- Fotiha surasi\n"
                                 "02- Baqara surasi\n"
                                 "03- Oli Imron surasi\n"
                                 "04- Niso surasi\n"
                                 "05- Moida surasi\n"
                                 "06- An’om surasi\n"
                                 "07- A’rof surasi\n"
                                 "08- Anfol surasi\n"
                                 "09- Tavba surasi\n"
                                 "10- Yunus surasi\n"
                                 "11- Hud surasi\n"
                                 "12- Yusuf surasi\n"
                                 "13- Ra’d surasi\n"
                                 "14- Ibrohim surasi")
    await call.message.edit_reply_markup(quraninline1)

@dp.callback_query_handler(text='sahobaMain')
async def namaz_time(call: CallbackQuery):
    await call.message.edit_text("01 - Abu Bakr As-Siddiq r.a\n"
                         "02 - Umar ibn Xattob r.a\n"
                         "03 - Usmon ibn Affon r.a\n"
                         "04 - Ali ibn Abu Tolib r.a\n"
                         "05 - Talha ibn Ubaydulloh r.a\n"
                         "06 - Sa'd ibn Abu Vaqqos r.a\n"
                         "07 - Abdurahmon ibn Avf r.a\n"
                         "08 - Said ibn Zayd r.a\n"
                         "09 - Abu Ubayda ibn Jarroh r.a\n"
                         "10 - Zubayr ibn Avvom r.a")
    await call.message.edit_reply_markup(sbsend)

@dp.callback_query_handler(text='menu')
async def Umar_callback(call:CallbackQuery):

    await call.message.edit_text("Asosiy menu")
    await call.message.edit_reply_markup(MEnu)


