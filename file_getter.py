import os

"""
this file is for getting a list of specific file types

function of getting all the files in the download folder
it goes to the downloads' folder
gets the list of all the files of a specific type and put them in a list
:return: the list of a certain filetype in  the /Downloads folder
"""
src_path = "/home/joe/Downloads"
a = list(os.walk(src_path))


def getfiles(file_type):
    """
    this is a general function that gets a list of files
    it ignores all the folders even if there are folders with file
    :param file_type: a str of the file extension eg .mp4 .png .mp3
    :return:
    """
    file_list = []
    for i, theFile in enumerate(
            a[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
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
    gets all the pdfs, docx, xlsx files
    :return: a list of pdfs, docx, xlsx files
    """
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
    """
    gets all the JPG, jpg, png files
    :return: a list of JPG, jpg, png files
    """
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
    """
    gets all the mp4, mkv, webM, MOV files
    :return: a list of mp4, mkv, webM, MOV files
    """
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
    """
    gets all the mp3, flac files
    :return: a list of mp3, flac files
    """
    file_list = []
    for i, theFile in enumerate(
            a[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(".mp3"):
            file_list.append(theFile)
        elif theFile.endswith(".flac"):
            file_list.append(theFile)
    return file_list
