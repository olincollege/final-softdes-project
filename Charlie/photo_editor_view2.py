from tkinter import * # remove and finalize at the end
from tkinter import ttk # , Tk, Canvas, NW
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

class PhotoView():
# create labels, scales and comboboxes
    
    
    def __init__(self, model):
        self.model = model

    def img_finder(self):
        img_path = filedialog.askopenfilename(initialdir=os.getcwd()) 
        return img_path

    def GUI(self):
        global self.newimage
        root = Tk()
        root.title("Simple Photo Editor")
        canvas = Canvas(root, width = 300, height = 300)
        canvas.pack()
        # Importing image
        img_path = self.img_finder()
        self.model.open_img(self, img_path)
        self.newimage=self.img
        self.newimage.thumbnail((350, 350))
        self.newimage = ImageTk.PhotoImage(self.newimage)
        canvas.create_image(20,20,anchor=NW, image=self.newimage)
        canvas.image=self.newimage

        #blur code
        def events(event):
            global self.newimage
            canvas.delete(self.newimage)
            sliders=[var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get()]
            self.model.slider_values(self,sliders)
            self.model.update_img(self)
            self.newimage = ImageTk.PhotoImage(self.newimage)
            canvas.create_image(20, 20, anchor=NW, image=self.newimage)
            canvas.image=self.newimage
            
        def export():
            global self.newimage
            ext = img_path.split(".")[-1]
            file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
            if file: 
                if canvas.image==self.newimage:
                    img2.save(file)
                
        # Blur code
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Blur")
        label.pack()

        var1 = DoubleVar()
        scale = Scale(root, from_=1, to=10, variable = var1, orient = HORIZONTAL, command = events)
        scale.pack(anchor = CENTER) # this displays it to the user
        
        # Brightness
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Brightness")
        label.pack()

        var2 = DoubleVar()
        scale = Scale(root, from_=1, to=10, variable = var2, orient = HORIZONTAL, command = events)
        scale.pack(anchor = CENTER) # this displays it to the user
        
        # Sharpness
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Sharpness")
        label.pack()

        var3 = DoubleVar()
        scale = Scale(root, from_=1, to=10, variable = var3, orient = HORIZONTAL, command = events)
        scale.pack(anchor = CENTER) # this displays it to the user

        # Contrast
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Contrast")
        label.pack()

        var4 = DoubleVar()
        scale = Scale(root, from_=1, to=10, variable = var4, orient = HORIZONTAL, command = events)
        scale.pack(anchor = CENTER) # this displays it to the user

        # Color
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Color")
        label.pack()

        var5 = DoubleVar()
        scale = Scale(root, from_=1, to=10, variable = var5, orient = HORIZONTAL, command = events)
        scale.pack(anchor = CENTER) # this displays it to the user

        # Rotate
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Rotate")
        label.pack()

        var6 = DoubleVar()
        scale = Scale(root, from_=0, to=360, variable = var6, orient = HORIZONTAL, command = events)
        scale.pack(anchor = CENTER) # this displays it to the user

        # Crop
        label=Label(root, text="Crop")
        label.pack()
        var7 = StringVar()
        e1 = Entry(root, textvariable=var7)
        e1.pack()

        # Export
        button = Button(root, text = "Export", command = export)
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()

        root.mainloop()
