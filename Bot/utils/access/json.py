import json

from Bot.core.config import logger


def read_json(path: str = "members.json") -> dict:
    try:
        with open(path, "r") as file:
            content = file.read().strip()
            logger.info("JSON is successful loaded.")
            return json.loads(content) if content else {}
    except FileNotFoundError:
        logger.warning("JSON is not found")
        return dict()


def create_json(path: str = "members.json") -> None:
    with open(path, "w") as file:
        json.dump({}, file, indent=4)
        logger.info("new json: "+path)

def write_json(data: dict, path: str = "members.json") -> None:
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
        logger.info(f"Updated data in {path}")
