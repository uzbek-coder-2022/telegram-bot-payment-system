from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

start_router = Router()


# Start - bu kommanda botni ishga tushirish uchun yoziladi
@start_router.message(Command(commands=["start"]))
async def bot_start(message: Message):
    await message.answer(text=f"#message\n🖐 Salom, <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> botga xush kelibsiz!.",
                         parse_mode="HTML")
