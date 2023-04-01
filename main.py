#! python3
from audio_file_manager import AudioManager
from doc_file_manager import DocumentManager
from image_file_manager import ImageManager
from video_file_manager import SeriesManager
from video_file_manager import FolderManager
import file_getter


def sort_documents():
    print("getting documents-type files...")
    doc_files = file_getter.get_document_files()
    for file in doc_files:
        DocumentManager(file).doc_transfer()
    print("\tdone")


def sort_audios():
    print("getting audio-type files...")
    audio_files = file_getter.get_audio_files()
    for file in audio_files:
        AudioManager(file).audio_transfer()
    print("\tdone")


def sort_images():
    print("getting image-type files...")
    image_files = file_getter.get_image_files()
    for file in image_files:
        ImageManager(file).image_transfer()
    print("\tdone")


def sort_videos():
    print("getting video-type files...")
    video_files = file_getter.get_video_files()
    for file in video_files:
        file_name = SeriesManager(file)

        # getting the series name and the season
        name = file_name.get_series_name()
        sn = file_name.get_season()

        # creating the folders and transferring the file
        FolderManager(file, name, sn).video_transfer_file()
    print("\tdone")


if __name__ == '__main__':
    """
    shutil.Error: Destination path '/home/joe/Documents/excel_files/example.xlsx' already exists
    this error occurs after changing from copy to move
    """
    # todo: if the file exists...ask for replacement or just ignore
    sort_documents()
    sort_images()
    sort_audios()
    sort_videos()

