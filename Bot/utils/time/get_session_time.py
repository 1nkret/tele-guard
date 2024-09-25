import random
from datetime import datetime, timedelta

from services.config import load_config, save_config

started_session = datetime.now()


def session_time() -> str:
    timer = str(datetime.now() - started_session).split(".")[0]

    result = f"\n\nSession time: {timer}"
    return result
