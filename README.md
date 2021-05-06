# Photo-Editing
Charlie and Arnav's Final Softdes Project: Photo editing

## Installation Instructions
[Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)\
Downloading Tkinter:\
`pip install tk`

[Photo Image Library (PIL) Documentation](https://pypi.org/project/Pillow/)\
Downloading PIL:\
`pip install Pillow`

[pytest Documentation](https://pypi.org/project/pytest/)\
Downloading pytest:\
`pip install -U pytest`

## Running Photo Editor
To run the photo editor type `python photo_editor_main.py` in terminal. The file `test_image.jpg` is used for testing purposes using pytest and it's path is hard coded into `test_photo_editor_model`.

## Structure

Photo Editor is composed of three files `photo_editor_main.py`, `photo_editor_interface.py`, and `photo_editor_model.py` and is made in Model, View and Control format. The file `pphoto_editor_interface.py` contains both the View and the Control since by using Tkinter View and Control can not be separated. The file `photo_editor_model.py` contains the Model and `photo_editor_main.py` runs the photo editor.