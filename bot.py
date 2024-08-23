from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands
import asyncio

from handlers.users.start import start_router
from handlers.users.help import help_router
from handlers.users.echo import echo_router
from handlers.users.payment import payment_router

from loader import dp, bot

# Routerni yuklash
dp.include_routers(start_router, payment_router, help_router, echo_router)

async def on_startup(dispatcher):
    # Bot kommandalarini ishga tushirish
    await set_default_commands(bot)

    # Bot ishga tushgani haqida adminlarga xabar berish
    dispatcher.startup.register(on_startup_notify)

    # Bot ishdan to'xtagani haqida adminlarga xabar berish
    dispatcher.shutdown.register(on_shutdown_notify)


async def main():
    # Bot ishga tushganda boshqa parametrlarni yuklash
    await on_startup(dp)

    # Botni ishga tushirish
    await dp.start_polling(bot)


if __name__ == "__main__":  # Logni yuklash
    asyncio.run(main())  # Asinxron funksiyani ishga tushirish