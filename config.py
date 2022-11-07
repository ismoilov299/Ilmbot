from aiogram import Bot, Dispatcher
import dotenv
import os

dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
