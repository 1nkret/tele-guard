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
        "group": group
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
        logger.info("Updated data in json (new user)")


def get_all_members() -> dict:
    try:
        with open("members.json", "r") as file:
            content = file.read().strip()
            members = json.loads(content) if content else {}
            logger.info("members.json are successful loaded and returned.")
    except FileNotFoundError:
        members = {}
        logger.warning("File members.json not found")
    except ValueError:
        logger.warning("Value error")
        members = {}

    return members


def remove_member(chat_id: str) -> bool:
    members = read_json()

    if chat_id in members:
        members.pop(chat_id)
        with open("members.json", "w") as file:
            json.dump(members, file, indent=4)
            logger.info("Remove member from json")
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
        json.dump({}, file)
        logger.info("new json: "+path)


def get_str_members() -> str:
    text = "Users:\n\n"

    if get_all_members():
        for key, val in get_all_members().items():
            text += f"ID: {key}, NAME: {val['name']}, {val['group']}\n"
    else:
        text += "Empty. Add new user now!"

    return text


def get_json_members() -> list:
    temp = read_json()

    member_list = []
    for key in temp.keys():
        group = temp[key]["group"]
        if group == "member" or group == "owner":
            member_list.append(key)

    return member_list


def get_json_owners() -> list:
    temp = read_json()
    root = getenv("OWNER")

    owner_list = [root]
    for key in temp.keys():
        if temp[key]["group"] == "owner":
            owner_list.append(key)

    return owner_list
