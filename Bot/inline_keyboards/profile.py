from aiogram import types


def in_kb_settings_access_manage_profile(
        user_id: str,
        whitelist: bool
):
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Whitelist [✓]" if whitelist else "Whitelist [X]",
                callback_data="settings_profile_whitelist_switch_"+user_id
            ),
            types.InlineKeyboardButton(
                text='Remove',
                callback_data='settings_access_manage_remove_from_members_' + user_id
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Back',
                callback_data='settings_access'
            )
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def in_kb_settings_access_manage_remove_member(user_id: str):
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Cancel",
                callback_data="settings_access_manage_"+user_id
            ),
            types.InlineKeyboardButton(
                text="Confirm",
                callback_data="settings_access_manage_remove_from_members_confirm_"+user_id
            )
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
