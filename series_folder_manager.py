import os
from pathlib import Path
import shutil


class FolderManager:
    """
    filename example -  Love Death and Robots
    season example - S03
    default absolute path - /home/joe/Videos/series
    """
    def __init__(self, the_file, name, sn):
        self.the_file = the_file
        self.name = name
        self.sn = sn
        self.series_path = Path("/home/joe/Videos/series")      # this is a posix path not str

    def video_folder_creator(self):
        """
        series_path is set to parent folder where the files will be stored
        check if exist.if it exist, the folders are not created
        both if and else returns the same path
        is sn is null then cwd/my_videos path is returned
        :return: returns the path of the folder created
        # todo: this code should be set as PRIVATE
        """
        os.chdir(self.series_path)
        if self.sn is None:
            vp = Path.cwd()/"my_videos"
            if vp.exists():
                return Path.cwd()/"my_videos"
            else:
                os.makedirs("my_videos")
                return Path.cwd()/"my_videos"
            return Path.cwd()/"my_videos"
        else:
            p = Path.cwd()/self.name/self.sn
            if p.exists():
                return str(Path.cwd()/self.name/self.sn)
            else:
                os.makedirs(self.name + "/" + self.sn)
                return str(Path.cwd()/self.name/self.sn)

    def video_transfer_file(self):
        """
        takes in the file_source+fileName and the destination
        :return: true if the file has been transferred
        # todo: confirm if the file file exist, does it get replaced?
        """
        print("moving " + self.the_file + " to " + str(self.video_folder_creator()) + "...")
        # todo: use a the Path to work both on windows and linux
        src = "/home/joe/Downloads/" + self.the_file
        destination = str(self.video_folder_creator())
        shutil.copy(src, destination)
        return True

    def doc_folder_creator(self):
        pass

    def doc_folder_transfer(self):
        pass


