from PIL import ImageTk, Image


class Sprite:
    def __init__(self, image=None, path_to_image=None):
        self.image = None

        if image is None:
            self.image = ImageTk.PhotoImage(Image.open(path_to_image))

        else:
            self.image = image

    def __str__(self):
        return "sprite"
