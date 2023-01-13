import os
from series_file_manager import SeriesManager
from series_folder_manager import FolderManager


# code for getting the files
def getfiles():
    """
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
        if theFile.endswith(".mp4"):
            file_list.append(theFile)
    return file_list


if __name__ == '__main__':
    myFiles = getfiles()
    for file in myFiles:
        file_name = SeriesManager(file)

        # getting the series name and the season
        name = file_name.get_series_name()
        sn = file_name.get_season()

        # creating the folders and transferring the file
        FolderManager(file, name, sn).video_transfer_file()

