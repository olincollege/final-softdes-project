from tkinter import * # remove and finalize at the end
from tkinter import ttk # , Tk, Canvas, NW
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
        #self.img_path = "Charlie/random.jpg"
        canvas = Canvas(root, width = 500, height = 500)
        canvas.pack()
        # Importing image
        img_path = self.img_finder()
        #img = self.model.open_img(img_path)
        img.thumbnail((350, 350))
        #imgg = img.filter(ImageFilter.BoxBlur(0))
        img1 = ImageTk.PhotoImage(img)
        canvas.create_image(20,20,anchor=NW, image=img1)
        canvas.image=img1
        
        #blur code
        def blur(event):
            img = Image.open(self.img_path)
            img.thumbnail((350, 350))
            imgg = img.filter(ImageFilter.BoxBlur(var.get()))
            img1 = ImageTk.PhotoImage(imgg) 
            canvas.create_image(20,20,anchor=NW, image=img1)
            canvas.image=img1
        def export():
            ext = img_path.split(".")[-1]
            file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
            if file: 
                if canvas.image==img1:
                    imgg.save(file)              
        # Blur code       
        var = StringVar()
        label = Label( root, textvariable=var, relief=RAISED )
        var.set("Set the Blur")
        label.pack()
        var = DoubleVar()
        scale = Scale(root, from_=0, to=10, variable = var, orient = HORIZONTAL, command = blur)
        scale.pack(anchor = CENTER) # this displays it to the user
        
        #img = ImageTk.PhotoImage(Image.open(self.img_path))

        button = Button(root, text = "Export", command = export)
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()        
        canvas.create_image(20,20, anchor=NW, image=img)
        canvas.image = img
              
        root.mainloop()