import os
import shutil
from pathlib import Path

"""
this will manage docx pdfs and zipfiles
"""


def folder_creator(folder_name):
    # todo: set to private
    doc_path = Path("/home/joe/Documents")
    os.chdir(doc_path)
    zp = Path.cwd() / folder_name
    if zp.exists():
        return Path.cwd() / folder_name
    else:
        os.makedirs(folder_name)
        return Path.cwd() / folder_name


class DocumentManager:

    def __init__(self, the_file):
        self.the_file = the_file

    def doc_transfer(self):

        if self.the_file.endswith(".zip"):
            f = folder_creator("zip_files")
            self.transfer(f)
        elif self.the_file.endswith(".docx"):
            f = folder_creator("word_files")
            self.transfer(f)
        elif self.the_file.endswith(".pdf"):
            f = folder_creator("pdf_files")
            self.transfer(f)
        elif self.the_file.endswith(".xlsx"):
            f = folder_creator("excel_files")
            self.transfer(f)

    def transfer(self, dest):
        src = "/home/joe/Downloads/" + self.the_file
        destination = str(dest)
        shutil.copy(src, destination)
