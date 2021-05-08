"""
Program runs the photo editor
"""
from photo_editor_interface import PhotoInterface
from photo_editor_model import PhotoModel

def main():
    """
    Opens the photo editor.
    """
    model = PhotoModel()
    photo = PhotoInterface(model)
    photo = PhotoInterface(model)
    photo.gui()

if __name__ == "__main__":
    main()
