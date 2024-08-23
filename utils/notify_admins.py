import logging

from aiogram import Bot

from data.config import ADMINS  # Admins ro'yxati olinmoqda


async def on_startup_notify(bot: Bot):
    # Bot ishga tushgan vaqtda adminlarga xabar berish
    # ADMINS - adminlar ro'yxati
    for admin in ADMINS:
        try:
            # Bot yuboruvchi xabar
            await bot.send_message(int(admin), "#start\n<blockquote>Bot ishga tushdi</blockquote>", parse_mode="HTML")

        except Exception as err:
            logging.exception(err)  # Xatolik haqida logging


async def on_shutdown_notify(bot: Bot):
    # Bot ishdan to'xtagan vaqtda adminlarga xabar berish
    # ADMINS - adminlar ro'yxati
    for admin in ADMINS:
        try:
            # Bot yuboruvchi xabar
            await bot.send_message(int(admin), "#stop\n<blockquote>Bot ishdan to'xtadi</blockquote>", parse_mode="HTML")

        except Exception as err:
            logging.exception(err)  # Xatolik haqida logging