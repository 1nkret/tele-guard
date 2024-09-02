from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from Bot.helpers.check_chat_id import check_chat_id
from Bot.helpers.access import *

from Bot.forms.AddNewMember import AddNewMember
from Bot.forms.RemoveMember import RemoveMember

from Bot.inline_keyboards.settings import *

router = Router()


@router.callback_query(lambda c: c.data == "settings")
@router.message(Command("settings"))
async def settings_command(event: types.Message or types.CallbackQuery):
    chat_id, is_message = check_chat_id(event)

    if chat_id in get_from_json_owners():
        if is_message:
            await event.answer(
                text="Settings menu",
                reply_markup=settings_menu()
            )
        else:
            await event.message.edit_text(
                text="Settings menu",
                reply_markup=settings_menu()
            )


@router.callback_query(lambda c: c.data == "settings_access")
async def settings_access(event: types.CallbackQuery):
    await event.message.edit_text(
        text="Access manager",
        reply_markup=settings_access_menu()
    )


@router.callback_query(lambda c: c.data == "add_new_member")
async def settings_access_add_new_member_name(event: types.CallbackQuery, state: FSMContext):
    await state.set_state(AddNewMember.name)
    await event.message.answer(
        text="Type user name:",
        reply_markup=settings_cancel_access()
    )


@router.message(AddNewMember.name)
async def settings_access_add_new_member_id(event: types.Message, state: FSMContext):
    await state.update_data(name=event.text)
    await state.set_state(AddNewMember.user_id)
    await event.answer(
        text="Now type user id:",
        reply_markup=settings_cancel_access()
    )


@router.message(AddNewMember.user_id)
async def settings_access_add_new_member_group(event: types.Message, state: FSMContext):
    if event.text.isdigit():
        await state.update_data(user_id=event.text)
        await state.set_state(AddNewMember.group)
        await event.answer(
            text="Now choose group:",
            reply_markup=settings_choose_group()
        )
    else:
        await event.answer(
            text="Its not chat id! Try again.",
            reply_markup=settings_cancel_access()
        )


@router.callback_query(lambda c: c.data.startswith("access_choose_group"))
async def settings_access_add_new_member_done(event: types.CallbackQuery, state: FSMContext):
    await state.update_data(group=event.data[len("access_choose_group_"):])
    data = await state.get_data()

    add_new_member(
        chat_id=data["user_id"],
        name=data["name"],
        group=data["group"]
    )

    await event.message.answer(
        text="Access manager\n\nNew member added.",
        reply_markup=settings_access_menu()
    )

    await state.clear()


@router.callback_query(lambda c: c.data == "settings_access_cancel")
async def settings_access_cancel(event: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await event.message.edit_text(
        text="Access manager\n\nCanceled.\n",
        reply_markup=settings_access_menu()
        )
