# Photo-Editing
Charlie and Arnav's Photo Editing Project\
[Our Photo Editing Program Website!](https://olincollege.github.io/photo-editor/)

## Summary
We created a photo editing program that allows users to upload a photo, edit it, then download the edited image. When the user runs the photo editor it creates a pop-up and in it, the current image being edited is displayed. The user can edit the image by changing the blur, brightness, sharpness, contrast, color, rotation, and crop size. The user applies edits to the image by moving sliders or in the case of cropping entering the crop size in a text box. The user imports and exports images by pressing buttons that prompt the user to provide the image path and in addition for downloads the name of the new image and image type.

## Installation Instructions
To use our program, please install the following in your command line:

[Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)\
Downloading Tkinter:\
`pip install tk`

[Photo Image Library (PIL) Documentation](https://pypi.org/project/Pillow/)\
Downloading PIL:\
`pip install Pillow`

[Pytest Documentation](https://pypi.org/project/pytest/)\
Downloading Pytest:\
`pip install -U pytest`

No changes are needed to run the code.

## Running Photo Editor
To run the photo editor run `photo_editor_main.py`, this can be done by typing `python photo_editor_main.py` in the terminal.

## Structure
The photo editor is composed of three files `photo_editor_main.py`, `photo_editor_interface.py`, and `photo_editor_model.py`, and is not made in the traditional Model, View, and Control format. Instead, the file `photo_editor_interface.py` contains both the View and the Control since by using Tkinter Library, the View and Control can not be feasibly separated. The file `photo_editor_model.py` contains the Model and `photo_editor_main.py` runs the photo editor. The file `test_image.jpg` is used for testing purposes through pytest and its path is hardcoded into `test_photo_editor_model`, which is used for unit testing the photo editor.