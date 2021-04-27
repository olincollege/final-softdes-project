from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
class PhotoView():
# create labels, scales and comboboxes
    def GUI(self):
        root = Tk()
        root.title("Simple Photo Editor")
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Hey!? How are you doing?")
        label.pack()
        var = DoubleVar()
        scale = Scale( root, variable = var, orient = HORIZONTAL)
        scale.pack(anchor = CENTER)
        def sel():
           selection = "Value = " + str(var.get())
           label.config(text = selection)
        button = Button(root, text = "Get Scale Value", command = sel)
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()
        canvas = Canvas(root, width = 300, height = 300)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open("random.jpg"))
        canvas.create_image(20,20, anchor=NW, image=img)
        canvas.image = img
        root.mainloop()