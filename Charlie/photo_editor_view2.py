from tkinter import Tk, Label, Button
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

class MyFirstGUI:

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        
        self.var = DoubleVar()
        self.scale_range = Scale(master, variable = self.var, orient = HORIZONTAL, command=self.sel(var))
        self.scale_range.pack(anchor = CENTER)
        
        self.label = Label(master, text=self.selection)
        self.label.pack()

        self.canvas = Canvas(root, width = 300, height = 300)
        self.canvas.pack()
        self.img = ImageTk.PhotoImage(Image.open("random.jpg"))
        self.canvas.create_image(20,20, anchor=NW, image=self.img)
        self.canvas.image = self.img
    def sel(var):
        self.selection = "Value = " + str(var)
        print(self.selection)
    def brightness(self):
        print("here")
        print(str(var.get()))
    def greet(self):
        print("Greetings!")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

"""
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
class PhotoView():
# create labels, scales and comboboxes
    def __init__(self, master):
            self.master = master
            master.title("A simple GUI")

            self.label = Label(master, text="This is our first GUI!")
            self.label.pack()

            self.greet_button = Button(master, text="Greet", command=self.greet)
            self.greet_button.pack()

            self.close_button = Button(master, text="Close", command=master.quit)
            self.close_button.pack()

    def greet(self):
        print("Greetings!")

    root = Tk()
    my_gui = PhotoView(root)
    root.mainloop()
    root = Tk()
    root.title("Simple Photo Editor")
    def GUI(self):
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Our photo editor!")
        label.pack()
        var = DoubleVar()
        scale = Scale( root, variable = var, orient = HORIZONTAL)
        scale.pack(anchor = CENTER)
        button = Button(root, text = "Get Scale Value", command = self.sel(var.get()))
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()
        canvas = Canvas(root, width = 300, height = 300)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open("random.jpg"))
        canvas.create_image(20,20, anchor=NW, image=img)
        canvas.image = img
    def sel(self,var):
        selection = "Value = " + str(var)
        label = Label(root, textvariable=selection)
    def brightness(self):
        print("here")
        print(str(var.get()))
    root.mainloop()
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
"""
