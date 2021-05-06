"""
Photo Interface Class. This class consists of the view and controller
of the program, showing the GUI and allows the user to control the
edits of the picture.

This is the view and controller combined, as our implementation with
tkinter and PIL do not allow for a feasible MVC structure.
"""
import os
from tkinter import filedialog, Tk, Canvas, Button, Scale, CENTER, \
Label, HORIZONTAL, StringVar, DoubleVar, Entry, NW
from tkinter.filedialog import asksaveasfilename
from PIL import ImageTk

class PhotoInterface():
    """
    This is the Photo Interface Class
    """

    def __init__(self, model):
        """
        Create a new model for the photo editor.

        Args:
            model: A photo editor model instance representing the photo
            on the GUI being edited.
        """
        self.model = model
        self.update_image=None
        self.image_path=None
        self._img_path_string=None


    def gui(self):
        """
        The GUI code for the code. Displays the Photo, scales, and buttons.
        """
        root = Tk()
        root.title("Photo Editor")
        canvas = Canvas(root, width = 300, height = 300, bg = '#666666')
        canvas.pack()
        root['background']='#666666'
        # Importing image
        def import_button():
            """
            This function runs when the import button is clicked,
            importing an image and placing it on the display.
            """
            self.image_path = self.img_finder()
            self.model.open_img(self.image_path)
            self.model.newimage=self.model.img
            self.model.newimage.thumbnail((350, 350))
            self.update_image = ImageTk.PhotoImage(self.model.newimage)
            canvas.create_image(0,0,anchor=NW, image=self.update_image)
            canvas.image=self.update_image

        # User Interaction
        def events(event):
            """
            This method runs when any of the scales are adjusted. It
            updates the image onto the display in realtime.
            """
            if self.update_image is not None or int(event) > 10000:
                canvas.delete(self.update_image)
                sliders=[]
                for slider in slider_update:
                    sliders.append(slider.get())
                self.model.slider_values(sliders)
                self.model.update_img()
                self.update_image = ImageTk.PhotoImage(self.model.newimage)
                canvas.create_image(0, 0, anchor=NW, image=self.update_image)
                canvas.image=self.update_image

        # Exporting image
        def export():
            """
            This function runs when the export button is clicked,
            exporting the image with all the edits and prompts the user to
            enter the file name and where to place it.
            """
            if self.update_image is not None:
                ext = self.image_path.split(".")[-1]
                file=asksaveasfilename(defaultextension =f".{ext}",\
                filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
                if file:
                    if canvas.image==self.update_image:
                        self.model.newimage.save(file)
        slider_update=[]
        #Import
        button = Button(root, text = "Import an Image", command = import_button \
                       , bg='#555555', fg='#f8f8ff', relief="groove")
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()
        label.config(font=("Times New Roman", 12))
        # Blur
        var = StringVar()
        label = Label(root, textvariable=var, relief="groove", bg='#555555', fg='#f8f8ff' )
        var.set("Set the Blur")
        label.config(font=("Times New Roman", 12))
        label.pack()
        slider_update.append(DoubleVar())
        scale = Scale(root, from_=0, to=10, variable = slider_update[0], \
                      orient = HORIZONTAL, command = events \
                     , bg='#555555', fg='#f8f8ff', relief="groove")
        scale.set(0)
        scale.pack(anchor = CENTER)
        label.config(font=("Times New Roman", 12))
        # Brightness
        var = StringVar()
        label = Label( root, textvariable=var, relief="groove", \
                      bg='#555555', fg='#f8f8ff')
        var.set("Set the Brightness")
        label.pack()
        label.config(font=("Times New Roman", 12))
        slider_update.append(DoubleVar())
        scale = Scale(root, from_=0, to=10, variable = slider_update[1], \
                      orient = HORIZONTAL, command = events \
                     , bg='#555555', fg='#f8f8ff', relief="groove")
        scale.set(1)
        scale.pack(anchor = CENTER)

        # Sharpness
        var = StringVar()
        label = Label( root, textvariable=var, relief="groove", bg='#555555', fg='#f8f8ff' )
        var.set("Set the Sharpness")
        label.pack()
        label.config(font=("Times New Roman", 12))

        slider_update.append(DoubleVar())
        scale = Scale(root, from_=0, to=10, variable = slider_update[2], \
                      orient = HORIZONTAL, command = events \
                     , bg='#555555', fg='#f8f8ff', relief="groove")
        scale.set(1)
        scale.pack(anchor = CENTER)

        # Contrast
        var = StringVar()
        label = Label( root, textvariable=var, relief="groove", bg='#555555', fg='#f8f8ff' )
        var.set("Set the Contrast")
        label.pack()
        label.config(font=("Times New Roman", 12))
        slider_update.append(DoubleVar())
        scale = Scale(root, from_=0, to=10, variable = slider_update[3], \
                      orient = HORIZONTAL, command = events \
                     , bg='#555555', fg='#f8f8ff', relief="groove")
        scale.set(1)
        scale.pack(anchor = CENTER)

        # Color
        var = StringVar()
        label = Label( root, textvariable=var, relief="groove", bg='#555555', fg='#f8f8ff')
        var.set("Set the Color")
        label.pack()
        label.config(font=("Times New Roman", 12))
        slider_update.append(DoubleVar())
        scale = Scale(root, from_=0, to=10, variable = slider_update[4], \
                      orient = HORIZONTAL, command = events \
                     , bg='#555555', fg='#f8f8ff', relief="groove")
        scale.set(1)
        scale.pack(anchor = CENTER)

        # Rotate
        var = StringVar()
        label = Label( root, textvariable=var, relief="groove", bg='#555555', fg='#f8f8ff')
        var.set("Set the Rotate")
        label.pack()
        label.config(font=("Times New Roman", 12))
        slider_update.append(DoubleVar())
        scale = Scale(root, from_=0, to=360, variable = slider_update[5],\
                      orient = HORIZONTAL, command = events \
                     , bg='#555555', fg='#f8f8ff', relief="groove")
        scale.pack(anchor = CENTER)

        # Crop
        label = Label(root, text = "Crop (left top right bottom with a space \
        \n between each and use slider after)", justify=CENTER, bg='#555555', fg='#f8f8ff')
        label.pack()
        slider_update.append(StringVar())
        crop1 = Entry(root, textvariable=slider_update[6], bg='#555555', \
                      fg='#f8f8ff', relief="groove")
        crop1.pack()
        label.config(font=("Times New Roman", 12))
        # Export
        button = Button(root, text = "Export", command = export, bg='#555555', fg='#f8f8ff')
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()
        label.config(font=("Times New Roman", 12))

        root.mainloop()

    def img_finder(self):
        """
        Asks the user to select an image in their file system and gets the
        relative path.

        Returns:
            IMG_PATH_string: A string of the path of where the image is
            located.
        """
        self._img_path_string = filedialog.askopenfilename(initialdir=os.getcwd())
        return self._img_path_string
