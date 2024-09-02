import json
from os import getenv
from Bot.config import logger


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


def read_json(path: str = "members.json") -> dict:
    try:
        with open(path, "r") as file:
            content = file.read().strip()
            members = json.loads(content) if content else {}
            logger.info("JSON is successful loaded.")
    except FileNotFoundError:
        members = {}
        logger.warning("JSON is not found")

    return members


def create_json(path: str = "members.json") -> None:
    with open(path, "w") as file:
        json.dump({}, file, indent=4)
        logger.info("new json: "+path)


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

    return owner_list


def is_blocked():
    members = read_json("settings.json")
    logger.info("Checking focus mode.")

    return members.get("blocked", False)


def change_status_blocked(status: bool):
    members = read_json("settings.json")
    members["blocked"] = status
    logger.info(f"Changing focus mode to {status}.")

    with open("settings.json", "w") as file:
        json.dump(members, file, indent=4)


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
