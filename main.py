#! python3

from video_file_manager import SeriesManager
from video_file_manager import FolderManager
import file_getter


if __name__ == '__main__':
    myFiles = file_getter.get_video_file()
    for file in myFiles:
        file_name = SeriesManager(file)

        # getting the series name and the season
        name = file_name.get_series_name()
        sn = file_name.get_season()

        # creating the folders and transferring the file
        FolderManager(file, name, sn).video_transfer_file()


