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
        var.set("Set the Blur")
        label.pack()
        var = DoubleVar()
        scale = Scale( root, from_=0, to=10, variable = var, orient = HORIZONTAL)
        scale.pack(anchor = CENTER)
        
        canvas = Canvas(root, width = 300, height = 300)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open("Charlie/random.jpg"))
        
        def sel():
            img = Image.open("Charlie/random.jpg")
            img.thumbnail((350, 350))
            imgg = img.filter(ImageFilter.BoxBlur(var.get()))
            img1 = ImageTk.PhotoImage(imgg) 
            canvas.create_image(20,20,anchor=NW, image=img1)
            canvas.image=img1
        
        button = Button(root, text = "Apply Blur", command = sel)
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()        
        canvas.create_image(20,20, anchor=NW, image=img)
        canvas.image = img
        
        
        root.mainloop()