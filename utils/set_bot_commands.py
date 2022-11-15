from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Boshlang"),
            types.BotCommand("help", "Adminlar bilan bog'lanish"),
            # types.BotCommand("admins", "Adminlar"),
        ]
    )
