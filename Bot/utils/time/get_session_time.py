import random
from datetime import datetime, timedelta

from services.config import load_config, save_config

started_session = datetime.now()
session_update = started_session


def session_time() -> str:
    global session_update
    now = datetime.now()
    if now - session_update > timedelta(seconds=random.randint(5, 15)):
        cfg = load_config()
        cfg["session_time_update"] = now
        save_config(cfg)
        session_update = now

    timer = str(session_update - started_session).split(".")[0]
    result = f"\n\nSession time: {timer}"

    return result
