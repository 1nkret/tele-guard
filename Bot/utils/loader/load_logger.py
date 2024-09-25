import os


def check_logger(log_dir, file):
    log_file_path = log_dir+file
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Создаем файл
    with open(log_file_path, 'w') as log_file:
        log_file.write('Это новый лог-файл.\n')