from environs import Env
env = Env()
env.read_env()
# .envni o'qish uchun
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list('ADMINS')
Chanel = "@testislomyolida"



