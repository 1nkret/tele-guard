from datetime import datetime
from Bot.config import started_session


def session_time() -> str:
    timer = str(datetime.now() - started_session).split(".")[0]
    result = f"\n\nSession time: {timer}"

    return result
