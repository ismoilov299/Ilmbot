from keyboards.inline.quran_Inline import quraninline1, quraninline2, quraninline3, quraninline4, quraninline5, \
    quraninline6, quraninline7, quraninline8
from loader import dp, bot, chanel
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text='1')
async def send_sura1(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=418)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1065)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='2')
async def send_sura2(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=419)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1066)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='3')
async def send_sura3(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=420)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1067)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='4')
async def send_sura4(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=421)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1068)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)


@dp.callback_query_handler(text='5')
async def send_sura5(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=422)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1069)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='6')
async def send_sura6(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=423)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1070)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='7')
async def send_sura7(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=424)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1071)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='8')
async def send_sura8(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=425)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1072)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='9')
async def send_sura9(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=426)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1073)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='10')
async def send_sura10(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=427)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1074)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='11')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=428)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1075)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='12')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=429)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1076)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='13')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=430)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1077)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='14')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=431)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1078)
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='15')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=432)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1079)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='16')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=433)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1080)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='17')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=434)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1081)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='18')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=435)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1082)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='19')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=436)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1083)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='20')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=437)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1084)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='21')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=438)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1085)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='22')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=439)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1086)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='23')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=440)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1087)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='24')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=441)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1088)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='25')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=442)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1089)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='26')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=443)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1090)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='27')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=444)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1091)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='28')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=445)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1092)
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='29')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=446)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1093)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='30')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=447)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1094)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='31')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=448)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1095)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='32')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=449)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1096)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='33')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=450)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1097)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='34')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=451)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1098)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='35')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=452)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1099)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='36')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=453)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1100)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='37')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=454)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1101)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='38')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=455)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1102)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='39')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=456)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1103)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='40')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=457)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1104)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='41')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=458)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1105)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='42')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=459)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1106)
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='43')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=460)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1107)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='44')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=461)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1108)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='45')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=462)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1109)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='46')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=463)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1110)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='47')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=464)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1111)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='48')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=465)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1112)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='49')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=466)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1113)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='50')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=467)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1114)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='51')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=468)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1115)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='52')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=469)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1116)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='53')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=470)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1117)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='54')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=471)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1118)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='55')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=472)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1119)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='56')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=473)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1120)
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='57')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=474)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1121)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='58')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=475)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1122)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='59')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=476)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1123)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='60')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=477)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1124)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='61')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=357)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1125)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='62')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=359)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1126)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='63')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=360)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1127)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='64')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=361)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1128)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='65')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=362)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1129)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='66')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=363)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1130)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='67')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=364)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1131)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='68')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=365)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1132)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='69')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=366)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1133)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='70')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=367)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1134)
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='71')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=368)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1135)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='72')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=369)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1136)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='73')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=370)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1137)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='74')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=371)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1138)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='75')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=372)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1139)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='76')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=373)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1140)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='77')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=374)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1141)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='78')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=375)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1142)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='79')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=376)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1143)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='80')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=378)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1144)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='81')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=379)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1145)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='82')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=380)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1146)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='83')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=381)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1147)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='84')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=382)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1148)
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='85')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=383)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1149)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='86')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=384)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1150)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='87')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=385)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1151)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='88')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=386)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1152)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='89')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=391)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1153)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='90')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=392)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1154)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='91')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=393)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1155)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='92')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=394)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1156)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='93')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=395)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1157)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='94')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=396)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1158)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='95')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=397)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1159)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='96')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=416)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1160)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='97')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=398)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1161)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='98')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=399)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1162)
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='99')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=400)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1163)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='100')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=401)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1164)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='101')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=402)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1165)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='102')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=403)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1166)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='103')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=404)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1167)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='104')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=405)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1168)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='105')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=406)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1169)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='106')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=407)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1170)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='107')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=408)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1171)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='108')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=409)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1172)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='109')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=410)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1173)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='110')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=411)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1174)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='111')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=412)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1175)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='112')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=413)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1176)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text='113')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=414)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1177)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)


@dp.callback_query_handler(text='114')
async def send_sura(call: CallbackQuery):
    await call.message.delete()
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=415)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id=chanel, message_id=1178)
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)

    await call.answer(cache_time=60)