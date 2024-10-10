from aiogram import types
from Bot.utils.access.json import read_json
from Bot.apps.paginator.keyboard import paginate_buttons


def settings_menu():
    members = read_json("settings.json")
    status = members.get("blocked", False)

    buttons = [
        [
            types.InlineKeyboardButton(
                text="🔐 Access",
                callback_data="settings_access"
            ),
            types.InlineKeyboardButton(
                text="[✓] Focus" if status else "[X] Focus",
                callback_data="settings_focus_mode_switch"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Update",
                callback_data="update_project"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="🏠 Home 🏠",
                callback_data="menu"
            )
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def settings_access_menu(page=1):
    json = read_json().items()
    members = [
        {
            "text": '👑 '+val['name'] if val['group'] == 'owner' else '👤 '+val['name'],
            "callback_data": f"settings_access_manage_profile_{key}"
        } for key, val in json
    ]

    buttons = [members[i:i + 2] for i in range(0, len(members), 2)]

    markup = paginate_buttons(
        buttons=buttons,
        page=page,
        back_callback_data="settings",
        buttons_per_page=2,
        add_button={"text": "📝 ADD", "callback_data": "add_new_member"}
    )

    return markup


def settings_cancel_access():
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="❌ Cancel ❌",
                    callback_data="settings_access_cancel"
                )
            ]
        ]
    )


def settings_choose_group():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="👑 Owner",
                callback_data="access_choose_group_owner"
            ),
            types.InlineKeyboardButton(
                text="👤 Member",
                callback_data="access_choose_group_member"
            )
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def back_to_menu_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Menu",
                callback_data="menu"
            )
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
