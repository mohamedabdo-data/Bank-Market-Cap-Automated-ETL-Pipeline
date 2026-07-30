import os
from datetime import datetime


def current_time():
    return datetime.now()


def create_folder(folder):
    os.makedirs(folder, exist_ok=True)


def check_file_exists(path):
    return os.path.exists(path)
