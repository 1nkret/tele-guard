from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def media_player_menu():
    buttons = [
        [
            InlineKeyboardButton(
                text="[<<]",
                callback_data="mp_prev"
            ),
            InlineKeyboardButton(
                text="Play / Pause",
                callback_data="mp_pause_play"
            ),
            InlineKeyboardButton(
                text="[>>]",
                callback_data="mp_next"
            )
        ],
        [
            InlineKeyboardButton(
                text="Volume-",
                callback_data="mp_volume_m"
            ),
            InlineKeyboardButton(
                text="Volume+",
                callback_data="mp_volume_p"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="main_functions"
            )
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
