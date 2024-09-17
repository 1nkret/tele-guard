from aiogram.fsm.state import StatesGroup, State


class PhotoUploadStates(StatesGroup):
    waiting_for_photo = State()
