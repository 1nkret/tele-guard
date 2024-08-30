from aiogram.fsm.state import State, StatesGroup


class RemoveMember(StatesGroup):
    chat_id = State()
