from aiogram.filters.state import State, StatesGroup


class Broadcast(StatesGroup):
    message = State()
