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
        root = Tk()
        root.title("Simple Photo Editor")
        canvas = Canvas(root, width = 300, height = 300)
        canvas.pack()
        # Importing image
        def import_button():
            global update_image, img_path
            img_path = self.img_finder()
            self.model.open_img(img_path)
            self.model.newimage=self.model.img
            self.model.newimage.thumbnail((350, 350))
            update_image = ImageTk.PhotoImage(self.model.newimage)
            canvas.create_image(0,0,anchor=NW, image=update_image)
            canvas.image=update_image

        #blur code
        def events(event):
            global update_image
            canvas.delete(update_image)
            sliders=[var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get()]
            self.model.slider_values(sliders)
            self.model.update_img()
            update_image = ImageTk.PhotoImage(self.model.newimage)
            canvas.create_image(0, 0, anchor=NW, image=update_image)
            canvas.image=update_image
            
        def export():
            global update_image, img_path
            ext = img_path.split(".")[-1]
            file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
            if file: 
                if canvas.image==update_image:
                    self.model.newimage.save(file)
        
        #Import 
        button = Button(root, text = "Import", command = import_button)
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()

        # Blur 
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
        label = Label(root, text = "Crop (left top right bottom with a space \n between each and use slider after)")
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
