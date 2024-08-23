from aiogram.types import Message
from aiogram import Router


echo_router = Router()


# Echo bot - bu bot kommandalari ichida yo'q xabarlar yuborilganda ishlaydi
@echo_router.message()
async def bot_echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)