import re
import shutil
from pathlib import Path
import os

"""
methods inside here is for creating folders and transferring files
"""

document_path = Path.home() / "Documents"
image_path = Path.home() / "Pictures"
audio_path = Path.home() / "Music"
video_path = Path.home() / "Videos"


def folder_creator(folder_name, path):
    """
    todo: set this to private
    this function creates folders.
    it checks if the folder exist, if it exists, it returns the src_path
    if it doesn't exist, it creates the folder and returns its src_path
    :param folder_name: the name of the folder that you want to create
    :param path: the src_path where the folder will be created
    :return: a src_path of the folder that was created
    """
    the_path = path  # example: Path("/home/joe/Documents")
    os.chdir(the_path)
    fldr = Path.cwd() / folder_name
    if fldr.exists():
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


def video_folder_creator(folder_name):
    """
    creates folders for storing images
    name season
    """
    return folder_creator(folder_name, video_path)


def series_name_formatter(name):
    """
    this function removes all the whitespaces and dots(.) in between the words
    after that it removes the dash(-) and the underscores(_) at the end of the formatted name
    :param name:a string which you want to format
    :return: a string of name
    """
    l = []
    if "." in name:
        l = name.split(".")
    elif " " in name:
        l = name.split()
    s = "_".join(l)
    s = s.rstrip("-")
    s = s.rstrip("_")
    return s


def video_folder_creator(folder_name, name):
    file_re = re.compile(r"S\d{2}")
    match_obj = file_re.search(name)
    if match_obj is None:
        return folder_creator(folder_name, video_path)
    else:
        sn = match_obj.group()
        index = name.index(sn)
        name = series_name_formatter(name[:index])

        # creating the folders
        pth = folder_creator(folder_name, video_path) / name / sn
        if pth.exists():
            return pth
        else:
            os.chdir(folder_creator(folder_name, video_path))
            print(name + " " + sn)
            os.makedirs(name + "/" + sn)
            return pth  # should return my_videos/name/sn/


def vid_folder_creator(name):
    return video_folder_creator("my_videos", name)


# these are the variables that create files
# the parameter is the folder name that will be created
ZIP_FOLDER_CREATOR = doc_folder_creator("zip_files")
WORD_FOLDER_CREATOR = doc_folder_creator("word_files")
PDF_FOLDER_CREATOR = doc_folder_creator("pdf_files")
EXCEL_FOLDER_CREATOR = doc_folder_creator("excel_files")

AUDIO_FOLDER_CREATOR = audio_folder_creator("my_music")
IMAGE_FOLDER_CREATOR = image_folder_creator("my_images")


def transfer(file, src, dest):
    """
    used for transferring files
    :param dest:
    :param src:
    :param file: the name of the file
    """
    print("\tmoving " + file + "...")
    shutil.copy(src, dest)  # change to move in production
