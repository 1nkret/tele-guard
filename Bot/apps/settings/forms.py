from aiogram.fsm.state import StatesGroup, State


class AddNewMember(StatesGroup):
    name = State()
    user_id = State()
    group = State()
