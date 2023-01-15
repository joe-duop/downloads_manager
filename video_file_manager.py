import re
import os
from pathlib import Path
import shutil

from folder_manager import transfer


class SeriesManager:
    """
    this class is for getting the name of the series/video

    works on the following string samples :
    Gangs.of.London.S02.COMPLETE.720p.WEBRip.x264-GalaxyTV[TGx]
    and :
    tvshows4mobile
    Love Death and Robots - S03E07 HD (TvShows4Mobile.Com) otv-wupy4.mp4

    todo
    youtube
    The-SANE-te-Sn-3-EP-2-Gender-Roles-Dark-_30.mp4
    """

    def __init__(self, series_file_name):
        """

        :param series_file_name:
        """
        self.fileName = series_file_name

    def get_season(self):
        """
        todo: this method should be private
        todo: add more matches eg S01 Sn1 Sn01 Season1 Season01
        this method is taking the filename and matching for the season of this episode
        it then identifies the index of the matched object which is the season of that series
        :return: the matched obj which is a string e.g. S01 S28 etc
        :return: None if the the matchObj is None
        """
        file_re = re.compile(r"S\d{2}")
        match_obj = file_re.search(self.fileName)
        if match_obj is None:
            return None
        else:
            return match_obj.group()

    def get_series_name(self):
        """
        todo: this method should be private
        sn holds a str which is the season of the episode(filename) which is used as a cutoff point
        the index variable holds the index position of the sn(where its starts)
        :return: the previous string which is the name of the series + season (S02) add 3
        Gangs.of.London.S02.COMPLETE.720p.WEBRip.x264-GalaxyTV[TGx] - Gangs.of.London.S02
        """
        sn = self.get_season()
        if sn is None:
            return None
        else:
            index = self.fileName.index(sn)
            return self.fileName[:index]


class FolderManager:

    def __init__(self, the_file, name, sn):
        self.the_file = the_file
        self.name = name
        self.sn = sn
        self.video_path = Path("/home/joe/Videos")

    def video_folder_creator(self):
        """
        the_file - the name of the file + extention
        name example -  Love Death and Robots
        season example - S03
        default absolute src_path - /home/joe/Videos/series
        video_path is set to parent folder where the files will be stored
        check if exist.if it exist, the folders are not created
        both if and else returns the same src_path
        is sn is null then cwd/my_videos src_path is returned
        :return: returns the src_path of the folder created
        # todo: this code should be set as PRIVATE
        """
        os.chdir(self.video_path)
        if self.sn is None:
            vp = Path.cwd() / "my_videos"
            if vp.exists():
                return Path.cwd() / "my_videos"
            else:
                os.makedirs("my_videos")
                return Path.cwd() / "my_videos"
            return Path.cwd() / "my_videos"
        else:
            p = Path.cwd() / self.name / self.sn
            if p.exists():
                return str(Path.cwd() / self.name / self.sn)
            else:
                os.makedirs(self.name + "/" + self.sn)
                return str(Path.cwd() / self.name / self.sn)

    def video_transfer_file(self):
        """
        takes in the file_source+fileName and the destination
        :return: true if the file has been transferred
        # todo: confirm if the file file exist, does it get replaced?
        """
        # todo: use a the Path to work both on windows and linux
        src = "/home/joe/Downloads/" + self.the_file
        destination = str(self.video_folder_creator())
        transfer(self.the_file, src, destination)
        return True
