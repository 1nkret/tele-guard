from aiogram import types


def check_chat_id(event) -> tuple[str, bool] | str:
    """
    Handling chat_id from chat with telegram bot
    :param event: CallbackQuery or Message (from types)
    :return: chat_id on str
    """
    if isinstance(event, types.Message):
        return str(event.chat.id), True
    elif isinstance(event, types.CallbackQuery):
        return str(event.message.chat.id), False
    else:
        return str()
