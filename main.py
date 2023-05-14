#! python3
from file_manager import *
import file_getter

# here you specify the folder which you want to sort the files
SRC_PATH = Path.home() / "Downloads"   # used in the file getter


def sort_documents():
    print("getting documents-type files...")
    doc_files = file_getter.DOC_FILE
    for file in doc_files:
        DocumentManager(file).doc_transfer()
    print("\tdone")


def sort_audios():
    print("getting audio-type files...")
    audio_files = file_getter.AUDIO_FILES
    for file in audio_files:
        AudioManager(file).audio_transfer()
    print("\tdone")


def sort_images():
    print("getting image-type files...")
    image_files = file_getter.IMAGE_FILES
    for file in image_files:
        ImageManager(file).image_transfer()
    print("\tdone")


def sort_videos():
    print("getting video-type files...")
    video_files = file_getter.VIDEO_FILES
    for file in video_files:
        # print(file)
        VideoManager(file).video_transfer()
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

