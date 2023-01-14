import os
import shutil
from pathlib import Path

from folder_manager import folder_creator, transfer, doc_folder_creator

"""
this will manage docx pdfs and zipfiles
"""


class DocumentManager:

    def __init__(self, the_file):
        self.the_file = the_file
        self.src = "/home/joe/Downloads/" + self.the_file

    def doc_transfer(self):

        if self.the_file.endswith(".zip"):
            f = doc_folder_creator("zip_files")
            transfer(self.src, f)
        elif self.the_file.endswith(".docx"):
            f = doc_folder_creator("word_files")
            transfer(self.src, f)
        elif self.the_file.endswith(".pdf"):
            f = doc_folder_creator("pdf_files")
            transfer(self.src, f)
        elif self.the_file.endswith(".xlsx"):
            f = doc_folder_creator("excel_files")
            transfer(self.src, f)
