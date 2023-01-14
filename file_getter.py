import os

"""
this file is for getting a list of specific file types
"""


def getfiles(file_type):
    """
    # todo: this function should be set to private
    function of getting all the video files in the download folder
    it goes to the downloads' folder
    gets the list of all the .mp4 folders and put them in a list
    :return: the list of mp4 files in  the /Downloads folder
    """
    path = "/home/joe/Downloads"
    a = list(os.walk(path))
    file_list = []
    for i, theFile in enumerate(
            a[0][-1]):  # -1 for getting the last list 0- for getting only the files in/home/joe/Downloads
        if theFile.endswith(file_type):
            file_list.append(theFile)
    return file_list


def get_mp4_files():
    return getfiles(".mp4")


def get_zip_files():
    return getfiles(".zip")


def get_mp3_files():
    return getfiles(".mp3")


def get_pdf_files():
    return getfiles(".pdf")


def get_docx_files():
    return getfiles(".docx")

