import json
from os import getenv

from Bot.core.config import logger
from Bot.utils.access.status import is_blocked
from Bot.utils.access.json import read_json


def add_new_member(
        chat_id: str,
        name: str,
        group: str,
) -> None:
    new_member = {
        "name": name,
        "group": group,
        "whitelist": False
    }

    try:
        with open("members.json", "r") as file:
            content = file.read().strip()
            members = json.loads(content) if content else {}
            logger.info("members.json is successful loaded.")
    except FileNotFoundError:
        logger.warning("File members.json not found.")
        members = {}

    members[chat_id] = new_member

    with open("members.json", "w") as file:
        json.dump(members, file, indent=4)
        logger.info("Updated data in json (new user).")


def remove_member(chat_id: str) -> bool:
    members = read_json()

    if chat_id in members:
        members.pop(chat_id)
        with open("members.json", "w") as file:
            json.dump(members, file, indent=4)
            logger.info("Remove member from json.")
        return True
    return False


def get_from_json_members() -> list:
    temp = read_json()
    logger.info("Getting from json list with id`s members.")

    member_list = []
    for key in temp.keys():
        group = temp[key]["group"]
        if group == "member" or group == "owner":
            member_list.append(key)

    return member_list


def get_from_json_owners() -> list:
    temp = read_json()
    root = getenv("OWNER")
    logger.info("Getting from json list with id`s owners.")

    owner_list = [root]
    for key in temp.keys():
        if temp[key]["group"] == "owner":
            owner_list.append(key)

    return list(set(owner_list))


def is_whitelisted(chat_id: str):
    members = read_json()
    logger.info(f"Checking is {chat_id} in whitelist...")
    is_owner = members.get(chat_id, {})["group"] == "owner"

    return True if is_owner else members.get(chat_id, {}).get("whitelist", False)


def change_status_whitelisted(
        chat_id: str,
        status: bool
):
    members = read_json()
    members[chat_id]["whitelist"] = status
    logger.info(f"Changing whitelist status {chat_id} to {status}")

    with open("members.json", "w") as file:
        json.dump(members, file, indent=4)


def get_member(chat_id: str) -> dict:
    members = read_json()
    return {chat_id: members[chat_id]} if chat_id in members else None


def focus_mode_immunity(chat_id: str) -> str:
    if is_whitelisted(chat_id) and is_blocked():
        return "🌙"
    else:
        return str()
