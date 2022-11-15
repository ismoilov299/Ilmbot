# from prayer_time.vaqt import NamozVaqti
from loader import db
# obj = NamozVaqti('Toshkent')
# print(obj.bomdod())
# print(obj.quyosh_chiqishi())
# print(obj.peshin())
# print(obj.asr())
# print(obj.shom())
# print(obj.xufton())

# users = db.get_users_subscribe()
# print(users)
# # 1 -q 2 - w 3 - e 4 - r 5- t
# for user in users:
#     user = id[1]

# list = [(1, 736342916, 'Zafar', 'Toshkent', 1), (3, 1161180912, 'Исмоилов Младший', 'Toshkent', 1), (157, 5006818392, 'Muhammad Amin', 'Toshkent', 1)]
# for i in list:
#     q, w, e, r, t = i
#     if t == 1:
#         print(q, w, e, r,)
# from datetime import datetime
# import pytz
#
# # current Datetime
# unaware = datetime.now()
# print('Timezone naive:', unaware)
#
# # Standard UTC timezone aware Datetime
# aware = datetime.now(pytz.utc)
# print('Timezone Aware:', aware)
#
# # US/Central timezone datetime
# aware_us_central = datetime.now(pytz.timezone('Asia/Tashkent'))
# print('US Central DateTime', aware_us_central)
# print(datetime.now())



for user in db.get_users_subscribe():
    user_id = user[0:4]
    print(user_id)