from folder_manager import folder_creator, audio_folder_creator, transfer


class AudioManager:

    def __init__(self, the_file):
        self.the_file = the_file
        self.src = "/home/joe/Downloads/" + self.the_file

    def audio_transfer(self):
        f = audio_folder_creator("my_music")
        transfer(self.src, f)
        if self.the_file.endswith(".mp3"):
            transfer(self.src, f)
        elif self.the_file.endswith(".flac"):
            transfer(self.src, f)
