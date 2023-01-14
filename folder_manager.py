import shutil
from pathlib import Path
import os

"""
methods inside here is for creating folders and transferring files
"""


def folder_creator(folder_name, path):
    # todo: set to private
    doc_path = path  # Path("/home/joe/Documents")
    os.chdir(doc_path)
    zp = Path.cwd() / folder_name
    if zp.exists():
        return Path.cwd() / folder_name
    else:
        os.makedirs(folder_name)
        return Path.cwd() / folder_name


def doc_folder_creator(folder_name):
    path = Path("/home/joe/Documents")
    return folder_creator(folder_name, path)


def audio_folder_creator(folder_name):
    path = Path("/home/joe/Music")
    return folder_creator(folder_name, path)


def image_folder_creator(folder_name):
    path = Path("/home/joe/Pictures")
    return folder_creator(folder_name, path)


def transfer(src, dest):
    shutil.copy(src, dest)
