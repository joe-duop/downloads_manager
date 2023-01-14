import shutil
from pathlib import Path
import os

"""
methods inside here is for creating folders and transferring files
"""

# the folder paths
document_path = Path("/home/joe/Documents")
image_path = Path("/home/joe/Pictures")
audio_path = Path("/home/joe/Music")


def folder_creator(folder_name, path):
    """
    this function creates folders.
    it checks if the folder exist, if it exists, it returns the src_path
    if it doesn't exist, it creates the folder and returns its src_path
    :param folder_name: the name of the folder that you want to create
    :param path: the src_path where the folder will be created
    :return: a src_path of the folder that was created
    """
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
    """
    creates folders for storing documents
    """
    return folder_creator(folder_name, document_path)


def audio_folder_creator(folder_name):
    """
    creates folders for storing audio
    """
    return folder_creator(folder_name, audio_path)


def image_folder_creator(folder_name):
    """
    creates folders for storing images
    """
    return folder_creator(folder_name, image_path)


def transfer(src, dest):
    """
    used for transferring files
    """
    shutil.copy(src, dest)
