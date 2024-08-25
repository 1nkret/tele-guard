import asyncio
from time import time
from keyboard import is_pressed as kb_is_pressed
from services.config import save_config


async def check_sequence(
        sequence: list,
        locker: bool,
        config
) -> bool:
    """
    Checking input sequence on your keyboard.
    :param sequence: List of sequence (example: ['F5', 'F7', 'F5', 'F7', 'F5']
    :param locker: is locked telegram
    :param config: cfg yaml
    :return: bool
    """
    start_time = time()
    sequence_index = 0

    while time() - start_time < 3:
        if kb_is_pressed(sequence[sequence_index]):
            sequence_index += 1
            if sequence_index == len(sequence):
                config["locked"], config["exit_count"] = locker, 0
                save_config(config)
                return True
        await asyncio.sleep(0.1)
    return False
