# Photo Editor
By: Charlie Babe and Arnav Gupta 
<img width="113" alt="Photo Editor" src="https://user-images.githubusercontent.com/78317842/117474351-d6aac300-af28-11eb-8f39-dbdc71cfcb1a.png">

## Summary
We created a photo-editing program that allows users to upload a photo, edit it, then download the edited image. When the user runs the photo editor it creates a pop up and in it the current image being edited is displayed. The user can edit the image by changing the blur, brightness, sharpness, contrast, color, rotation and crop size. The user applies edits to the image by moving sliders or in the case of cropping entering the crop size in a text box. The user imports and export images by pressing buttons which prompt the user to provide the image path and in addition for downloads the name of the new image and image type.

## Installation Instructions
[Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)\
Downloading Tkinter:\
`pip install tk`

[Photo Image Library (PIL) Documentation](https://pypi.org/project/Pillow/)\
Downloading PIL:\
`pip install Pillow`

[Pytest Documentation](https://pypi.org/project/pytest/)\
Downloading Pytest:\
`pip install -U pytest`

## Running Photo Editor
To run the photo editor run `photo_editor_main.py`, this can be done by typing `python photo_editor_main.py` into terminal.

## Demo
Below is a video of the photo editor and how to use it. 
[Video Link](https://drive.google.com/file/d/15PqAqpLfl_OqwUtCBB3dQQAjUz26tqTe/view?usp=sharing)

## Structure
Photo editor is composed of three files `photo_editor_main.py`, `photo_editor_interface.py`, and `photo_editor_model.py` and is not made in the traditional Model, View and Control format. Instead, the file `photo_editor_interface.py` contains both the View and the Control since by using Tkinter Library, the View and Control can not be feasibly separated. The file `photo_editor_model.py` contains the Model and `photo_editor_main.py` runs the photo editor. The file `test_image.jpg` is used for testing purposes through pytest and it's path is hard coded into `test_photo_editor_model`, which is used for unit testing the photo editor.

## GitHub Repository Link
[link to GitHub repository](https://github.com/olincollege/photo-editor)

## About the Authors
Arnav: An Olin Student interested in photography, design, and psychology. [Arnav's GitHub Profile](https://github.com/arnavgupta19)\
Charlie: An Olin student interested in photography, soccer, and computer science. [Charlie's GitHub Profile](https://github.com/Cbabe)

## Sources
[An example photo editor that inspired us!](https://www.codershubb.com/build-a-simple-photo-editor-app-using-python/)
