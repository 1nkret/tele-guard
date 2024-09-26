from os import getenv
from dotenv import load_dotenv


def load_env() -> str:
    load_dotenv()

    return getenv("BLOCKER")
