"""
Unit tests for photo editor interface.

We could only unit test our model based on the code structure.
We can't test our interface functions since all of them would be requiring GUI.
Testing user interaction would not be possible because the interface is GUI
based and cannot be tested through the structure of pytest.
For example testing user interaction testing our export and
import would create a file dialog popup and while it returns
a string we can not put any inputs into the function.
"""
from PIL import Image, ImageChops
from photo_editor_model import PhotoModel

# Hard coded image path used for testing functionality
test_image=Image.open("test_image.jpg")

def test_open_image():
    """
    Tests that `open_img` opens images and updates the attribute `img` to the new image.
    """
    new_photo_model=PhotoModel()
    new_photo_model.open_img("test_image.jpg")
    assert new_photo_model.img==test_image

# update_test is in the form,
# [[[Slider values],Is the new image the same as the original], [Next test case]]
update_test=[
             # Check to see if image is same, assert True
             [[0,1,1,1,1,0,""],True],\
             # Check to see image has changed with brightness, assert False
             [[1,1,1,1,1,0,""],False],\
             # Check to see image has changed more, assert False
             [[0,2,1,1,1,0,""],False],\
             # Check to see image has changed, assert False
             [[0,1,2,1,1,0,""],False],\
             # Check to see image has changed, assert False
             [[0,1,1,2,1,0,""],False],\
             # Check to see image has changed, assert False
             [[0,1,1,1,2,0,""],False],\
             # Check to see image has changed, assert False
             [[0,1,1,1,1,1,""],False],\
             # Check to see image has changed with crop box, assert False
             [[0,1,1,1,1,0,"4 4 100 100"],False],
             # Check to see image is same, assert True
             [[0,1,1,1,1,0,"        "],True],\
             # Check to see image has changed, assert False
             [[0.5,1,1,1,1,0,""],False],\
             # Check to see image has changed, assert False
             [[0.5,6,100,-1,5,-0.6,""],False]]\

def test_update_img():
    """
    Tests changes to each of the slider and crop inputs to determine if
    the manipulated image changed from the original image.
    Also tests whether the default positions of the slider and crop inputs
    creates the same image as the original uploaded image.
    """
    new_photo_model=PhotoModel()
    new_photo_model.img=test_image
    for slider_test in update_test:
        new_photo_model.update_slider=slider_test[0]
        new_photo_model.update_img()
        # Checks if the images are different,
        # ImageChops.difference is None if the images are the same.
        same_image=ImageChops.difference(new_photo_model.newimage, test_image).getbbox() is None
        assert same_image==slider_test[1]
