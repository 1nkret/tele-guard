from services.config import save_config
from datetime import datetime


async def update_time(cfg):
    cfg["session_time_update"] = datetime.now()
    save_config(cfg)
