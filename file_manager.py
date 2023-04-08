#! python3
from folder_manager import *
import file_getter

SOURCE_PATH = file_getter.SRC_PATH


class Manager:
    def __init__(self, the_file):
        self.the_file = the_file  # the name of the file
        self.src = SOURCE_PATH / self.the_file  # the location of the file

    def transfer(self):
        """todo: override this class in the classes below"""
        pass


class AudioManager(Manager):

    def __init__(self, the_file):
        super().__init__(the_file)

    def audio_transfer(self):
        f = AUDIO_FOLDER_CREATOR
        transfer(self.the_file, self.src, f)


class DocumentManager(Manager):

    def __init__(self, the_file):
        super().__init__(the_file)

    def doc_transfer(self):

        if self.the_file.endswith(".zip"):
            f = ZIP_FOLDER_CREATOR
            transfer(self.the_file, self.src, f)
        elif self.the_file.endswith(".docx"):
            f = WORD_FOLDER_CREATOR
            transfer(self.the_file, self.src, f)
        elif self.the_file.endswith(".pdf"):
            f = PDF_FOLDER_CREATOR
            transfer(self.the_file, self.src, f)
        elif self.the_file.endswith(".xlsx"):
            f = EXCEL_FOLDER_CREATOR
            transfer(self.the_file, self.src, f)


class ImageManager(Manager):

    def __init__(self, the_file):
        super().__init__(the_file)

    def image_transfer(self):
        f = IMAGE_FOLDER_CREATOR
        transfer(self.the_file, self.src, f)


class VideoManager(Manager):

    def __init__(self, the_file):
        super().__init__(the_file)

    def video_transfer(self):
        f = vid_folder_creator(self.the_file)
        transfer(self.the_file, self.src, f)
