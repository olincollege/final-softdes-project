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
<<<<<<< HEAD
    photo=PhotoView(model)
=======
    photo = PhotoView(model)
    #img_path = photo.img_path()
    # model.open_img(img_path)
>>>>>>> 6e92ac6298170cba038a86fe3a33f73d413717ef
    photo.GUI()


if __name__ == "__main__":
    main()
