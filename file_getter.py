import os
from pathlib import Path

import main

# todo: simplify this whole file
"""

this file is for getting a list of specific file types

function of getting all the files in the download folder
it goes to the downloads' folder
gets the list of all the files of a specific type and put them in a list
ex: doc files, music files, etc
:return: the list of a certain filetype from  the /Downloads folder
NOTE: you can add the available filetype that havent been included in this program here
"""
SRC_PATH = main.SRC_PATH
downloadStuff = list(os.walk(SRC_PATH))  # gets every file and folder in that directory


def getfiles(file_type):
    """
    todo: set this as private
    this is a general function that gets a list of files
    it ignores all the folders even if there are folders with file
    :param file_type: a str of the file extension eg .mp4 .png .mp3
    :return:
    """
    file_list = []
    for i, theFile in enumerate(
            downloadStuff[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(file_type):
            file_list.append(theFile)
    return file_list


def get_zip_files():
    """
    get all the zip files
    :return: a list of zip files that are found
    """
    return getfiles(".zip")


def get_document_files():
    """
    gets all the pdfs, docx, xlsx, zip files
    :return: a list of pdfs, docx, zip xlsx files
    """
    file_list = []
    for i, theFile in enumerate(
            downloadStuff[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(".pdf"):
            file_list.append(theFile)
        elif theFile.endswith(".docx"):
            file_list.append(theFile)
        elif theFile.endswith(".xlsx"):
            file_list.append(theFile)
        elif theFile.endswith(".zip"):
            file_list.append(theFile)
    return file_list


def get_image_files():
    """
    gets all the JPG, jpg, png files
    :return: a list of JPG, jpg, png files
    """
    file_list = []
    for i, theFile in enumerate(
            downloadStuff[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(".jpg"):
            file_list.append(theFile)
        elif theFile.endswith(".JPG"):
            file_list.append(theFile)
        elif theFile.endswith(".png"):
            file_list.append(theFile)
    return file_list


def get_video_files():
    """
    gets all the mp4, mkv, webM, MOV files
    :return: a list of mp4, mkv, webM, MOV files
    """
    file_list = []
    for i, theFile in enumerate(
            downloadStuff[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(".mp4"):
            file_list.append(theFile)
        elif theFile.endswith(".mkv"):
            file_list.append(theFile)
        elif theFile.endswith(".webM"):
            file_list.append(theFile)
        elif theFile.endswith(".MOV"):
            file_list.append(theFile)
    return file_list


def get_audio_files():
    """
    gets all the mp3, flac files
    :return: a list of mp3, flac files
    """
    file_list = []
    for i, theFile in enumerate(
            downloadStuff[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(".mp3"):
            file_list.append(theFile)
        elif theFile.endswith(".flac"):
            file_list.append(theFile)
    return file_list


DOC_FILE = get_document_files()
ZIP_FILES = get_zip_files()
AUDIO_FILES = get_audio_files()
IMAGE_FILES = get_image_files()
VIDEO_FILES = get_video_files()
