from aiogram.fsm.state import StatesGroup, State


class ErrorForm(StatesGroup):
    title = State()
    message = State()
