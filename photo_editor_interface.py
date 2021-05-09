"""
Photo Interface Class. This class consists of the view and controller
of the program, showing the GUI and allows the user to control the
edits of the picture.

This is the view and controller combined, as our implementation with
Tkinter and PIL do not allow for a feasible MVC structure. For example,
the scales in Tkinter are generated in GUI and output a string of numbers,
creating both a view and control.
"""
import os
from tkinter import filedialog, Tk, Canvas, Button, Scale, CENTER, \
Label, HORIZONTAL, StringVar, DoubleVar, Entry, NW
from tkinter.filedialog import asksaveasfilename
from PIL import ImageTk

class PhotoInterface():
    """
    This is the Photo Interface Class.

    Attributes:
        model: An instance of the model class of the photo editor.
        update_image: Current image being displayed.
        image_path: The path to the original image represented by a string.
        _img_path_string: The private path to the original image represented by a string.

    Methods:
        __init__: Create a new model for the photo editor,
        and stores the slider state and path to the original image.
        gui: Creates the GUI code for the photo editor. Displays the Photo, scales, and buttons.
        img_finder: Asks the user to select an image in their file system and gets the
        relative path.
    """
    def __init__(self, model):
        """
        Create a new model for the photo editor.

        Args:
            model: A photo editor model instance that contains the photo
            on the GUI being edited and the original photo as well as methods
            to open and edit the original photo.
        """
        self.model = model
        self.update_image=None
        self.image_path=None
        self._img_path_string=None


    def gui(self):
        """
        Creates the GUI code for the photo editor.
        Displays the Photo, scales, and buttons in a popup.
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
            prompting a file dialog for the user to pick an image
            and then placing that image on the canvas.
            """
            self.image_path = self.img_finder()
            self.model.open_img(self.image_path)
            self.model.newimage=self.model.img
            self.model.newimage.thumbnail((350, 350))
            self.update_image = ImageTk.PhotoImage(self.model.newimage)
            canvas.create_image(0,0,anchor=NW, image=self.update_image)
            canvas.image=self.update_image

        # User Interaction
        def user_interaction(current_state):
            """
            This function runs when any of the scales are adjusted. It
            updates the image onto the display in real-time.

            Args:
                current_state: An float representing the current
                value of the slider that had been changed.

            """
            if self.update_image is not None or int(current_state) > 10000:
                canvas.delete(self.update_image)
                sliders=[]
                for slider in slider_update:
                    sliders.append(slider.get())
                self.model.update_slider=sliders
                self.model.update_img()
                self.update_image = ImageTk.PhotoImage(self.model.newimage)
                canvas.create_image(0, 0, anchor=NW, image=self.update_image)
                canvas.image=self.update_image

        # Exporting image
        def export():
            """
            This function runs when the export button is clicked,
            exporting the image with all the edits and prompts the user to
            enter the file name, file type, and where to place it.
            """
            ext=self.image_path.split(".")[-1]
            if self.update_image is not None:
                file=asksaveasfilename(defaultextension =f".{ext}",\
                filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
                self.model.newimage.save(file)
        # Import
        button = Button(root, text = "Import an Image", command = import_button \
                       , bg='#555555', fg='#f8f8ff', relief="groove")
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()
        # Sliders
        #Format of Sliders, with values of the range
        sliders=[["Blur",0,10],["Brightness",1,10],["Sharpness",1,10],\
                 ["Contrast",1,10],["Color",1,10],["Rotate",0,360]]
        slider_update=[]
        for count, slider in enumerate(sliders):
            label = Label(root, text=f"Set the {slider[0]}",\
                          relief="groove", bg='#555555', fg='#f8f8ff' )
            label.pack()
            slider_update.append(DoubleVar())
            scale = Scale(root, from_=0, to=slider[2], variable = slider_update[count], \
                          orient = HORIZONTAL, command = user_interaction \
                         , bg='#555555', fg='#f8f8ff', relief="groove")
            scale.set(slider[1])
            scale.pack(anchor = CENTER)
        # Crop
        label = (Label(root, text = "Crop (left top right bottom with a space \
        \n between each and use slider after)", justify=CENTER, bg='#555555', fg='#f8f8ff'))
        label.pack()
        slider_update.append(StringVar())
        crop1 = Entry(root, textvariable=slider_update[6], bg='#555555', \
                      fg='#f8f8ff', relief="groove")
        crop1.pack()
        # Export
        button = Button(root, text = "Export", command = export, bg='#555555', fg='#f8f8ff')
        button.pack(anchor = CENTER)
        label = Label(root)
        label.pack()

        root.mainloop()

    def img_finder(self):
        """
        Asks the user to select an image in their file system and gets the
        relative path. This function is not outside of class to avoid tripping
        a pylint error about having less than two functions in a class.

        Returns:
            A string of the path of where the image is
            located.
        """
        self._img_path_string = filedialog.askopenfilename(initialdir=os.getcwd())
        return self._img_path_string
