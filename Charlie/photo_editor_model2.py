from tkinter import * # remove and finalize at the end
from tkinter import ttk # , Tk, Canvas, NW
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

class PhotoModel():
    def __init__(self):
        self.img=None

    def open_img(self, img_path):
        self.img = Image.open(img_path)
