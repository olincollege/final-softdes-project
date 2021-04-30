from photo_editor_view2 import PhotoView
from photo_editor_model2 import PhotoModel

def main():
    
    model = PhotoModel
    photo=PhotoView(model)
    photo.GUI()
if __name__ == "__main__":
    main()