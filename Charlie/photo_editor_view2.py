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
        global img3, img2
        root = Tk()
        root.title("Simple Photo Editor")
        canvas = Canvas(root, width = 300, height = 300)
        canvas.pack()
        # Importing image
        img_path = self.img_finder()
        self.model.open_img(self, img_path)
        self.img.thumbnail((350, 350))
        img3 = ImageTk.PhotoImage(self.img)
        canvas.create_image(20,20,anchor=NW, image=img3)
        canvas.image=img3

        #blur code
        def blur(event):
            global img3, img2
            canvas.delete(img3)
            img2 = self.img.filter(ImageFilter.BoxBlur(var1.get()))
            img3 = ImageTk.PhotoImage(img2) 
            canvas.create_image(20,20,anchor=NW, image=img3)
            canvas.image=img3
        def brightness(event):
            global img3, img2
            canvas.delete(img3)
            imgg = ImageEnhance.Brightness(self.img)
            img2 = imgg.enhance(var2.get())
            img3 = ImageTk.PhotoImage(img2)
            canvas.create_image(20, 20, anchor=NW, image=img3)
            canvas.image=img3
        def sharpness(event):
            global img3, img2
            canvas.delete(img3)
            imgg = ImageEnhance.Sharpness(self.img)
            img2 = imgg.enhance(var3.get())
            img3 = ImageTk.PhotoImage(img2)
            canvas.create_image(20, 20, anchor=NW, image=img3)
            canvas.image=img3
        def contrast(event):
            global img3, img2
            canvas.delete(img3)
            imgg = ImageEnhance.Contrast(self.img)
            img2 = imgg.enhance(var4.get())
            img3 = ImageTk.PhotoImage(img2)
            canvas.create_image(20, 20, anchor=NW, image=img3)
            canvas.image=img3
        def color(event):
            global img3, img2
            canvas.delete(img3)
            imgg = ImageEnhance.Color(self.img)
            img2 = imgg.enhance(var5.get())
            img3 = ImageTk.PhotoImage(img2)
            canvas.create_image(20, 20, anchor=NW, image=img3)
            canvas.image=img3
        def rotate(event):
            global img3, img2
            canvas.delete(img3)
            img2=self.img.rotate(var6.get(), expand=True)
            img3 = ImageTk.PhotoImage(img2)
            canvas.create_image(20, 20, anchor=NW, image=img3)
            canvas.image=img3
        def crop():
            global img3, img2
            #left, upper, right, lower
            canvas.delete(img3)
            cropped_view=var7.get()
            left=int(cropped_view[:2])
            upper=int(cropped_view[3:5])
            right=int(cropped_view[6:8])
            lower=int(cropped_view[9:11])
            cropped_tup=(left,upper,right,lower)
            img2=self.img.crop(cropped_tup)
            img3 = ImageTk.PhotoImage(img2)
            canvas.create_image(20, 20, anchor=NW, image=img3)
            canvas.image=img3
            
        def export():
            global img3, img2
            ext = img_path.split(".")[-1]
            file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
            if file: 
                if canvas.image==img3:
                    img2.save(file)
                
        # Blur code
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Blur")
        label.pack()

        var1 = DoubleVar()
        scale = Scale(root, from_=0, to=10, variable = var1, orient = HORIZONTAL, command = blur)
        scale.pack(anchor = CENTER) # this displays it to the user
        
        # Brightness
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Brightness")
        label.pack()

        var2 = DoubleVar()
        scale = Scale(root, from_=0, to=10, variable = var2, orient = HORIZONTAL, command = brightness)
        scale.pack(anchor = CENTER) # this displays it to the user
        
        # Sharpness
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Sharpness")
        label.pack()

        var3 = DoubleVar()
        scale = Scale(root, from_=0, to=10, variable = var3, orient = HORIZONTAL, command = sharpness)
        scale.pack(anchor = CENTER) # this displays it to the user

        # Contrast
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Contrast")
        label.pack()

        var4 = DoubleVar()
        scale = Scale(root, from_=0, to=10, variable = var4, orient = HORIZONTAL, command = contrast)
        scale.pack(anchor = CENTER) # this displays it to the user

        # Color
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Color")
        label.pack()

        var5 = DoubleVar()
        scale = Scale(root, from_=0, to=10, variable = var5, orient = HORIZONTAL, command = color)
        scale.pack(anchor = CENTER) # this displays it to the user

        # Rotate
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Rotate")
        label.pack()

        var6 = DoubleVar()
        scale = Scale(root, from_=0, to=360, variable = var6, orient = HORIZONTAL, command = rotate)
        scale.pack(anchor = CENTER) # this displays it to the user

        # Crop
        label=Label(root, text="Crop")
        label.pack()
        var7 = StringVar()
        e1 = Entry(root, textvariable=var7)
        e1.pack()
        
        button = Button(root, text = "Crop", command = crop)
        button.pack(anchor = CENTER)

        # Export
        button = Button(root, text = "Export", command = export)
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()

        root.mainloop()
