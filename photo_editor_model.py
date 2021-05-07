"""
Photo Editor model implementation
"""
from PIL import Image, ImageFilter, ImageEnhance

class PhotoModel():
    """
    Photo editor model stores, opens, and updates the photo.

    Attributes:
        img: original img opened from path in Pillow.
        update: a list of integers for editing the image based on
        its index.
        newimage: the copy of img that is being displayed on the canvas.

    Methods:
        open_img: Open an img in Pillow.
        slider_values: A list of the slider values being updated.
        update_img: Updates the image everytime one of the sliders are
        manipulated.
    """

    def __init__(self):
        """
        Initialize attributes for editing images
        """
        self.img = None
        self.update_slider = None
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
        self.update_slider = slider_values

    def update_img(self):
        """
        Updates the image everytime one of the sliders are
        manipulated.
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
