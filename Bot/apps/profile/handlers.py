from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from Bot.apps.profile.keyboard import in_kb_settings_access_manage_profile, in_kb_settings_access_manage_remove_member
from Bot.apps.settings.keyboard import settings_access_menu

from Bot.utils.access.members import get_member, remove_member, change_status_whitelisted
from Bot.utils.access.json import read_json

router = Router()


@router.callback_query(lambda c: c.data.startswith("settings_access_manage_profile_"))
async def settings_access_manage_profile(event: types.CallbackQuery):
    user_id = event.data[len('settings_access_manage_profile_'):]
    member = get_member(user_id)
    text = ""

    if member:
        for key, val in member.items():
            text += (
                f"{val['name']}:\n\n"
                f"ID - {key},\n"
                f"GROUP - {val['group'].capitalize()},\n"
            )
    else:
        text = f"No member found with ID: {user_id}"

    await event.message.edit_text(
        text=text,
        reply_markup=in_kb_settings_access_manage_profile(user_id, member[user_id].get("whitelist", False))
    )


@router.callback_query(lambda c: c.data.startswith("settings_access_manage_remove_from_members_") or c.data.startswith("settings_access_manage_remove_from_members_confirm_"))
async def settings_access_manage_profile_remove(event: types.CallbackQuery):
    if "confirm" in event.data:
        user_id = event.data[len("settings_access_manage_remove_from_members_confirm_"):]
        remove_member(user_id)
        await event.message.edit_text(
            text=f"Access manager\n\nUser with id ({user_id}) successful removed from members.",
            reply_markup=settings_access_menu()
        )
    else:
        user_id = event.data[len("settings_access_manage_remove_from_members_"):]
        await event.message.edit_text(
            text=f"Confirm deletion ({user_id})",
            reply_markup=in_kb_settings_access_manage_remove_member(user_id)
        )


@router.callback_query(lambda c: c.data.startswith("settings_profile_whitelist_switch_"))
async def settings_access_manage_profile_whitelist(event: types.CallbackQuery):
    user_id = event.data[len("settings_profile_whitelist_switch_"):]
    status = read_json().get(user_id, {}).get("whitelist", False)
    new_status = False if status else True
    change_status_whitelisted(user_id, new_status)

    await event.message.edit_reply_markup(
        reply_markup=in_kb_settings_access_manage_profile(user_id, new_status)
    )
    await event.answer()


@router.callback_query(lambda c: c.data.startswith("settings_access_manage_remove_cancel_"))
async def settings_access_manage_remove_cancel_handler(event: types.CallbackQuery):
    user_id = event.data[len("settings_access_manage_remove_cancel_"):]
    member = get_member(user_id)
    text = ""

    if member:
        for key, val in member.items():
            text += (
                f"Canceled remove.\n"
                f"{val['name']}:\n\n"
                f"ID - {key},\n"
                f"GROUP - {val['group'].capitalize()},\n"
            )
    else:
        text = f"No member found with ID: {user_id}"

    await event.message.edit_text(
        text=text,
        reply_markup=in_kb_settings_access_manage_profile(user_id, member[user_id].get("whitelist", False))
    )
