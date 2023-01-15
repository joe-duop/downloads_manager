from folder_manager import image_folder_creator, transfer


class ImageManager:

    def __init__(self, the_file):
        self.the_file = the_file
        self.src = "/home/joe/Downloads/" + self.the_file  # todo: set as a global var to all classes

    def image_transfer(self):
        f = image_folder_creator("my_images")   # todo: make this folder a var for easy change
        transfer(self.the_file, self.src, f)
        if self.the_file.endswith(".jpg"):
            transfer(self.the_file, self.src, f)
        elif self.the_file.endswith(".JPG"):
            transfer(self.the_file, self.src, f)
        elif self.the_file.endswith(".png"):
            transfer(self.the_file, self.src, f)
