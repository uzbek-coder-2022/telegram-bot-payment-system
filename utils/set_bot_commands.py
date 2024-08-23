from aiogram import Bot, types

# Bot kommmandalarini o'rnatish
async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        # Bot kommandalarini ro'yxat shaklida berish
        [
            # command -> siz botda ishlatayotgan buyruq nomi
            # description -> buyruq haqida ma'lumot ya'ni botda nima vazifa bajarishi
            types.BotCommand(command="start", description="Botni ishga tushurish"),
            types.BotCommand(command="help", description="Yordam")
        ]
    )
