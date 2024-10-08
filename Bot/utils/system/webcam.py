import time
import cv2
import os

from Bot.core.config import logger


async def prop_frame(
        id_cam: int = 0,
):
    """
    Configure your webcam
    :param id_cam: id your cam (default 0)
    :param x: width
    :param y: height
    :return: VideoCapture
    """
    cap = cv2.VideoCapture(id_cam)

    return cap


def is_dir_exists(path: str = "media/take_photo/") -> None:
    """
    If directory not issue - function is create it.
    :param path: Your dir
    :return: None
    """
    if not os.path.exists(path):
        logger.info("Create dir "+path)
        os.makedirs(path)


def generate_snapshot_id(
        directory: str = "media/take_photo/",
        prefix: str = "snapshot"
) -> int:
    """
    Generate your id for snapshot
    :param directory: your directory
    :param prefix: name of your file
    :return: snapshot id
    """
    existing_ids = set()

    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.startswith(prefix):
                name_without_prefix = entry.name[len(prefix):]
                name_without_extension = os.path.splitext(name_without_prefix)[0]
                if name_without_extension.isdigit():
                    existing_ids.add(int(name_without_extension))

    return max(existing_ids, default=0) + 1


async def webcam(chat_id: str) -> str:
    """
    Call webcam and do screenshot image. Save as '/your_path/media/take_photo/snapshot(id).jpg'
    :return: None
    """
    cap = await prop_frame()

    if not cap.isOpened():
        logger.warning("Camera is not loaded")
        ret, frame = None, None
    else:
        ret, frame = cap.read()

    if ret:
        time.sleep(1)
        file_path = f'media/take_photo/{chat_id}/'
        is_dir_exists(file_path)
        file_name = f'snapshot{generate_snapshot_id(file_path)}'
        file_ext = '.jpg'
        full_path = f'{file_path}{file_name}{file_ext}'

        cv2.imwrite(full_path, frame)
        logger.info(f"Photo saved as {full_path}")
    else:
        logger.warning("Cant load image")
        full_path = f'media/take_photo/default.jpg'

    cap.release()
    cv2.destroyAllWindows()

    return full_path
