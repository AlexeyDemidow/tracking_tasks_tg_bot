from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from utils.states import BotStates

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    text = (
        "👋 Добро пожаловать в Tracking Task Bot! \n\n"
        "📌 Здесь вы можете:\n"
        "• Получать список ваших задач 📋\n"
        "• Отслеживать дедлайны ⏳\n"
        "• Получать уведомления 📲\n\n"
        "Введите /tasks чтобы посмотреть свои задачи.\n"
        "Введите /done чтобы изменить статус задачи задачи."
    )
    await message.answer(text)
    await state.set_state(BotStates.start)
