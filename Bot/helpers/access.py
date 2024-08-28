import json


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
    except FileNotFoundError:
        members = {}

    members[chat_id] = new_member

    with open("members.json", "w") as file:
        json.dump(members, file, indent=4)


def get_all_members() -> dict:
    try:
        with open("members.json", "r") as file:
            content = file.read().strip()
            members = json.loads(content) if content else {}
    except FileNotFoundError:
        members = {}
    except ValueError:
        members = {}

    return members


def remove_member(chat_id: str) -> None:
    members = read_json()

    if chat_id in members:
        members.pop(chat_id)
        with open("members.json", "w") as file:
            json.dump(members, file, indent=4)


def read_json(path: str = "members.json") -> dict:
    try:
        with open(path, "r") as file:
            content = file.read().strip()
            members = json.loads(content) if content else {}
    except FileNotFoundError:
        members = {}

    return members


def create_json(path: str = "members.json") -> None:
    with open(path, "w") as file:
        json.dump({}, file)


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

    owner_list = []
    for key in temp.keys():
        if temp[key]["group"] == "owner":
            owner_list.append(key)

    return owner_list
