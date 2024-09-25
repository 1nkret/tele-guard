import os.path

import json
import logging


logger = logging.getLogger(__name__)


def load_logging(filename: str) -> None:
    """
    Load logs
    :param filename: file with logs
    :return: None
    """
    if not os.path.exists("logs/"):
        os.mkdir("logs/")
    logging.basicConfig(filename=f'logs/{filename}.log', level=logging.INFO)


def load_config(path='config.json') -> json:
    """
    Load yaml config
    :param path: path to config
    :return: yaml
    """
    if not os.path.exists(path):
        return {}

    with open(path, 'r') as file:
        try:
            cfg = json.load(file)
        except json.decoder.JSONDecodeError:
            return {}

    return cfg


def save_config(cfg, path='config.json') -> None:
    """
    Save yaml config
    :param cfg: modified cfg to save
    :param path: path to config.yaml
    :return: None
    """
    with open(path, 'w') as file:
        json.dump(cfg, file, indent=4)
