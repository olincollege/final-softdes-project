"""
Photo Editor model implementation
"""
from PIL import Image, ImageFilter, ImageEnhance

class PhotoModel():
    """
    Photo editor model stores, opens, and updates the photo.
    """

    def __init__(self):
        """
        Initialize attributes for editing images
        Attributes:
            img: original img opened from path in Pillow.
            update: a list of integers for editing the image based on
            its index
            newimage: the copy of img that is being displayed on the canvas.
        """
        self.img = None
        self.update = None
        self.newimage = None

    def open_img(self, img_path):
        """
        Open an img in Pillow
        Args:
            img_path:a string of the img_path.
        """
        self.img = Image.open(img_path)

    def slider_values(self, slider_values):
        """
        A list of the slider values being updated
        """
        self.update = slider_values

    def update_img(self):
        """
        This function updates the image everytime one of the sliders are
        manipulated.
        """
        self.newimage = self.img.filter(ImageFilter.BoxBlur(self.update[0]))
        newimage = self.newimage
        newimage = ImageEnhance.Brightness(self.newimage)
        newimage = newimage.enhance(self.update[1])
        newimage = ImageEnhance.Sharpness(newimage)
        newimage = newimage.enhance(self.update[2])
        newimage = ImageEnhance.Contrast(newimage)
        newimage = newimage.enhance(self.update[3])
        newimage = ImageEnhance.Color(newimage)
        newimage = newimage.enhance(self.update[4])
        self.newimage = newimage.rotate(self.update[5], expand=True)
        if len(str(self.update[6]))>=7:
            cropped_view=self.update[6].split()
            left=int(cropped_view[0])
            upper=int(cropped_view[1])
            right=int(cropped_view[2])
            lower=int(cropped_view[3])
            cropped_tup=(left,upper,right,lower)
            self.newimage=newimage.crop(cropped_tup)
