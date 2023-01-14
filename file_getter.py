import os

"""
this file is for getting a list of specific file types
"""


def getfiles(file_type):
    """
    # todo: this function should be set to private
    function of getting all the video files in the download folder
    it goes to the downloads' folder
    gets the list of all the files of a specific type and put them in a list
    :return: the list of a certain filetype in  the /Downloads folder
    """
    path = "/home/joe/Downloads"
    a = list(os.walk(path))
    file_list = []
    for i, theFile in enumerate(
            a[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(file_type):
            file_list.append(theFile)
    return file_list


def get_zip_files():
    return getfiles(".zip")


def get_document_files():
    path = "/home/joe/Downloads"
    a = list(os.walk(path))
    file_list = []
    for i, theFile in enumerate(
            a[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(".pdf"):
            file_list.append(theFile)
        elif theFile.endswith(".docx"):
            file_list.append(theFile)
        elif theFile.endswith(".xlsx"):
            file_list.append(theFile)
    return file_list


def get_image_files():
    path = "/home/joe/Downloads"
    a = list(os.walk(path))
    file_list = []
    for i, theFile in enumerate(
            a[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(".jpg"):
            file_list.append(theFile)
        elif theFile.endswith(".JPG"):
            file_list.append(theFile)
        elif theFile.endswith(".png"):
            file_list.append(theFile)
    return file_list


def get_video_files():
    path = "/home/joe/Downloads"
    a = list(os.walk(path))
    file_list = []
    for i, theFile in enumerate(
            a[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
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
    path = "/home/joe/Downloads"
    a = list(os.walk(path))
    file_list = []
    for i, theFile in enumerate(
            a[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(".mp3"):
            file_list.append(theFile)
        elif theFile.endswith(".flac"):
            file_list.append(theFile)
    return file_list

