from aiogram.fsm.state import State, StatesGroup


class BotStates(StatesGroup):
    start = State()
    waiting_for_task_id = State()
