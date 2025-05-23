from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начать работу',
        ),
        BotCommand(
            command='tasks',
            description='Список активных задач',
        ),
        BotCommand(
            command='done',
            description='Пометить задачу как выполненную',
        ),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
