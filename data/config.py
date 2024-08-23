from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("bot_token")  # Bot tokenini
PAYMENT_TOKEN = env.str("payment_token")  # To'lov tokenini
ADMINS = env.list("admins")  # adminlar ro'yxatini
IP = env.str("ip")  # Hosting ip manzili
