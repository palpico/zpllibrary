import math

from PIL import ImageOps, Image

from zpllibrary.shared import PositionedElement


class DownloadGraphic(PositionedElement):
    def __init__(self, x, y, image_path="",
                 storage="R"):
        super().__init__(x, y)
        self.image = image_path
        self.storage = storage

    def render(self, options):
        im = Image.open(self.image)
        width, height = im.size
        newsize = (round(options.scale(width)), round(options.scale(height)))
        im1 = im.resize(newsize)
        bytes_per_row = math.ceil(newsize[0] / 8.0) # Width
        total_bytes = math.ceil(newsize[1] * bytes_per_row) # Height
        compression_type="A"
        data = self.convert_image(im1)
        text = self.origin.render(options)
        if compression_type == "A":
            text += "^GFA" + ","
            text += str((len(data))) + ","
            text += str(total_bytes) + ","
            text += str(bytes_per_row) + ","
            text += data

            return text

    def convert_image(self, image, compression_type='A'):

        image = ImageOps.invert(image.convert('L')).convert('1')

        if compression_type == "A":
            return image.tobytes().hex().upper()
