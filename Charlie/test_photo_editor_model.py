"""
Unit tests for photo editor interface.
"""
import pytest
from PIL import Image, ImageChops
from photo_editor_model import PhotoModel

test_image=Image.open("test_random.jpg")
def test_open_image():
    new_photo_model=PhotoModel()
    new_photo_model.open_img("test_random.jpg")
    assert new_photo_model.img==test_image
def test_slider_values():
    new_photo_model=PhotoModel()
    new_photo_model.slider_values([1,2,3,4,5,6,7])
    assert [1,2,3,4,5,6,7] == new_photo_model.update

update_test=[[[0,1,1,1,1,0,""],True],[[1,1,1,1,1,0,""],False],\
             [[0,2,1,1,1,0,""],False],[[0,1,2,1,1,0,""],False],\
             [[0,1,1,2,1,0,""],False],[[0,1,1,1,2,0,""],False],\
             [[0,1,1,1,1,1,""],False],[[0,1,1,1,1,0,"4 4 100 100"],False]]
def test_update_img():
    new_photo_model=PhotoModel()
    new_photo_model.img=test_image
    for slider_test in update_test:
        new_photo_model.slider_values(slider_test[0])
        new_photo_model.update_img()
        same_image=ImageChops.difference(new_photo_model.newimage, test_image).getbbox()==None
        assert same_image==slider_test[1]