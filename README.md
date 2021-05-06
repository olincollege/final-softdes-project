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
To run the photo editor type `python Main.py` in terminal. The file `test_image.jpg` is used for testing purposes using pytest and it's path is hard coded into `test_photo_editor_model`.

## Structure

Photo Editor is composed of three files `Main.py`, `photo_editor_model2.py`, and `photo_editor_view2.py` and is made in Model, View and Control format. The file `photo_editor_view2.py` contains both the View and the Control since by using Tkinter View and Control can not be separated. The file `photo_editor_model2.py` contains the Model and `Main.py` runs the photo editor.