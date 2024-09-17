import json

from Bot.core.config import logger
from Bot.utils.access.json import read_json


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
