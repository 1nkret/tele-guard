import yaml
import logging


logger = logging.getLogger(__name__)


def load_logging(filename: str) -> None:
    """
    Load logs
    :param filename: file with logs
    :return: None
    """
    logging.basicConfig(filename=f'logs/{filename}.log', level=logging.INFO)


def load_config(path='config.yaml') -> yaml:
    """
    Load yaml config
    :param path: path to config
    :return: yaml
    """
    with open(path, 'r') as file:
        return yaml.safe_load(file)


def save_config(cfg, path='config.yaml') -> None:
    """
    Save yaml config
    :param cfg: modified cfg to save
    :param path: path to config.yaml
    :return: None
    """
    with open(path, 'w') as file:
        yaml.dump(cfg, file, default_flow_style=True)
