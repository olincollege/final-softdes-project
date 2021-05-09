"""
Photo Editor model implementation
"""
from PIL import Image, ImageFilter, ImageEnhance

class PhotoModel():
    """
    Photo editor model stores, opens, and updates the uploaded photo.

    Attributes:
        img: Original image opened from the image's path in Pillow.
        update_slider: A list of integers for editing the image based on
        its index.
        newimage: The edited image that is being displayed on the canvas.

    Methods:
        __init__: Initialize attributes for editing images.
        open_img: Open an image in Pillow.
        update_img: Updates the image every time one of the sliders are
        manipulated.
    """

    def __init__(self):
        """
        Initialize attributes for editing images.
        """
        self.img = None
        self.update_slider = []
        self.newimage = None

    def open_img(self, img_path):
        """
        Opens an image in Pillow.

        Args:
            img_path: A string of the image path.
        """
        self.img = Image.open(img_path)
    def update_img(self):
        """
        Updates the image every time one of the sliders are
        manipulated. Reapplies all editing to the original image
        in a consistent order of edits.
        """
        self.newimage = self.img.filter(ImageFilter.BoxBlur(self.update_slider[0]))
        self.newimage = ImageEnhance.Brightness(self.newimage)
        self.newimage = self.newimage.enhance(self.update_slider[1])
        self.newimage = ImageEnhance.Sharpness(self.newimage)
        self.newimage = self.newimage.enhance(self.update_slider[2])
        self.newimage = ImageEnhance.Contrast(self.newimage)
        self.newimage = self.newimage.enhance(self.update_slider[3])
        self.newimage = ImageEnhance.Color(self.newimage)
        self.newimage = self.newimage.enhance(self.update_slider[4])
        self.newimage = self.newimage.rotate(self.update_slider[5], expand=True)
        cropped_view=self.update_slider[6].split()
        if len(cropped_view)==4:
            left=int(cropped_view[0])
            upper=int(cropped_view[1])
            right=int(cropped_view[2])
            lower=int(cropped_view[3])
            cropped_tup=(left,upper,right,lower)
            self.newimage=self.newimage.crop(cropped_tup)
