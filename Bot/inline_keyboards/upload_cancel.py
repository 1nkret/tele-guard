from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def upload_cancel_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Cancel",
                                     callback_data="upload_cancel")
            ]
        ]
    )
