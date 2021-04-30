from tkinter import * # remove and finalize at the end
from tkinter import ttk # , Tk, Canvas, NW
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

class PhotoModel():
    def __init__(self):
        self.img=None
        self.update= [1,1,1,1,1,1,1,1]
        self.newimage=None
        
    def open_img(self, img_path):
        self.img = Image.open(img_path)
        
    def slider_values(self,slider_values):
        self.update=slider_values
        
    def update_img(self):
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
        self.newimage=newimage.rotate(self.update[5], expand=True)
        if len(str(self.update[6]))==11:
            cropped_view=self.update[6]
            left=int(cropped_view[:2])
            upper=int(cropped_view[3:5])
            right=int(cropped_view[6:8])
            lower=int(cropped_view[9:11])
            cropped_tup=(left,upper,right,lower)
            self.newimage=newimage.crop(cropped_tup)