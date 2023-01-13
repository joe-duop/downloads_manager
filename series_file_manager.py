#! python3
import re

"""
this class is for getting the name of the series
"""


class SeriesManager:
    """
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
