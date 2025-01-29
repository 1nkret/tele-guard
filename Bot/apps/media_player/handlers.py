from aiogram import Router, types

from Bot.apps.media_player.keyboard import media_player_menu
from Bot.utils.system import media_player
from Bot.utils.access.members import get_from_json_owners

router = Router()


@router.callback_query(lambda c: c.data == "media_player")
async def media_player_handler(event: types.CallbackQuery):
    if str(event.from_user.id) in get_from_json_owners():
        await event.message.edit_text(
            text=f"Teleguard Media Player",
            reply_markup=media_player_menu()
        )


@router.callback_query(lambda c: c.data == "mp_pause_play")
async def media_player_pause_handler(event: types.CallbackQuery):
    media_player.play_pause()

    await event.answer("Play/Pause toggled.")


@router.callback_query(lambda c: c.data == "mp_next")
async def media_player_next_handler(event: types.CallbackQuery):
    media_player.next_track()

    await event.answer("Next track played.")


@router.callback_query(lambda c: c.data == "mp_prev")
async def media_player_prev_handler(event: types.CallbackQuery):
    media_player.prev_track()

    await event.answer("Previous track played.")


@router.callback_query(lambda c: c.data == "mp_volume_p")
async def media_player_prev_handler(event: types.CallbackQuery):
    media_player.volume_up()
    media_player.volume_up()
    media_player.volume_up()
    media_player.volume_up()
    media_player.volume_up()

    await event.answer("Volume+")


@router.callback_query(lambda c: c.data == "mp_volume_m")
async def media_player_prev_handler(event: types.CallbackQuery):
    media_player.volume_down()
    media_player.volume_down()
    media_player.volume_down()
    media_player.volume_down()
    media_player.volume_down()

    await event.answer("Volume-")
