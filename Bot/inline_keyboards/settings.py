from aiogram import types


def settings_menu():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Access",
                callback_data="settings_access"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Back to menu",
                callback_data="menu"
            )
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def settings_access_menu():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="ADD",
                callback_data="add_new_member"
            ),
            types.InlineKeyboardButton(
                text="REMOVE",
                callback_data="remove_member"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="BACK",
                callback_data="settings"
            )
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def settings_cancel_access():
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Cancel",
                    callback_data="settings_access_cancel"
                )
            ]
        ]
    )


def settings_choose_group():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Owner",
                callback_data="access_choose_group_owner"
            ),
            types.InlineKeyboardButton(
                text="Member",
                callback_data="access_choose_group_member"
            )
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
