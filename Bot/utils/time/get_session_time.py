from Bot.core.config import started_session, session_update


def session_time() -> str:
    timer = str(session_update - started_session).split(".")[0]
    result = f"\n\nSession time: {timer}"

    return result
