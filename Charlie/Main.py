"""
Program runs the photo editor
"""
from photo_editor_view2 import PhotoView
from photo_editor_model2 import PhotoModel


def main():
    """
    Open the photo editor
    """
    model = PhotoModel()
    photo = PhotoView(model)
    photo = PhotoView(model)
    photo.GUI()


if __name__ == "__main__":
    main()
