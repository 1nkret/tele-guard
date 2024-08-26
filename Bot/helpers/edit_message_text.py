from aiogram.exceptions import TelegramBadRequest
from Bot.config import bot

attempts = {}


async def edit_message_text(
        chat_id: int | str,
        message_id: int,
        text: str,
        reply_markup=None,
        **kwargs
):
    """
    Функция для попытки редактирования сообщения с обработкой ошибок и повторными попытками.
    Запоминает количество попыток редактирования для улучшения поиска message_id.

    :param chat_id: ID чата, в котором находится сообщение
    :param message_id: ID сообщения, которое нужно редактировать
    :param text: Новый текст сообщения
    :param reply_markup: Новый reply_markup (если есть)
    :param kwargs: Дополнительные именованные аргументы
    """
    chat_id = str(chat_id)
    if chat_id not in attempts:
        attempts[chat_id] = {'attempts': 0, "message_id": message_id}

    retries = 5

    while attempts[chat_id]['attempts'] < retries:
        print(attempts)
        try:
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id-attempts[chat_id]["attempts"],
                text=text,
                reply_markup=reply_markup,
                **kwargs
            )
            attempts[chat_id]['attempts'] = 0
            return
        except TelegramBadRequest:
            attempts[chat_id]['attempts'] += 1
            if attempts[chat_id]['attempts'] > 1:
                attempts[chat_id]["message_id"] -= 1

    await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup
        )
