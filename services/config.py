import os.path

import yaml
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


def load_config(path='config.yaml') -> yaml:
    """
    Load yaml config
    :param path: path to config
    :return: yaml
    """
    with open(path, 'r') as file:
        try:
            cfg = yaml.safe_load(file)
        except yaml.reader.ReaderError:
            cfg = {}
        if cfg is None:
            return {}
        return cfg


def save_config(cfg, path='config.yaml') -> None:
    """
    Save yaml config
    :param cfg: modified cfg to save
    :param path: path to config.yaml
    :return: None
    """
    with open(path, 'w') as file:
        yaml.dump(cfg, file, default_flow_style=True)
