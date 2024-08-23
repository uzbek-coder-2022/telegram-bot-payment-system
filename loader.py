from aiogram import Bot, Dispatcher
import logging, sys
from aiogram.fsm.storage.memory import MemoryStorage
from data import config

logging.basicConfig(level=logging.INFO, stream=sys.stdout)  # Logni yuklash

bot = Bot(token=config.BOT_TOKEN)  # Bot obyekti yaratiladi
dp = Dispatcher(bot=bot, storage=MemoryStorage())  # Botda ish jarayonini boshqarish va birlashtirish uchun Dispatcher yaratiladi
