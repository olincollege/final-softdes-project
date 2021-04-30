from tkinter import * # remove and finalize at the end
from tkinter import ttk # , Tk, Canvas, NW
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

class PhotoModel():
    def __init__(self):
        self.img=None
        self.update=None
        self.newimage=None
    def open_img(self, img_path):
        self.img = Image.open(img_path)
    def update_img(self):
        self.newimage = self.img.filter(ImageFilter.BoxBlur(self.update[0])
        self.newimage = ImageEnhance.Brightness(self.newimage)
        self.newimage = self.newimage.enhance(self.update[1])
        self.newimage = ImageEnhance.Sharpness(self.newimage)
        self.newimage = self.newimage.enhance(self.update[2])
        self.newimage = ImageEnhance.Contrast(self.newimage)
        self.newimage = self.newimage.enhance(self.update[3])
        self.newimage = ImageEnhance.Color(self.newimage)
        self.newimage = self.newimage.enhance(self.update[4])
        self.newimage=self.newimage.rotate(self.update[5], expand=True)
        if len(str(self.update[6]))==11:
            cropped_view=self.update[6]
            left=int(cropped_view[:2])
            upper=int(cropped_view[3:5])
            right=int(cropped_view[6:8])
            lower=int(cropped_view[9:11])
            cropped_tup=(left,upper,right,lower)
            self.newimage=self.newimage.crop(cropped_tup)
    def slider_values(self,slider_values):
        self.update=slider_values
