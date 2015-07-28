# encoding: utf8
from PIL import Image
from SillyCrossbow import CropTransparent

fire = Image.open('data/fire.png')
cropper = CropTransparent(fire.width, fire.height, 50, fire.tostring())

print cropper.getCroppedOffsetX()
print cropper.getCroppedOffsetY()
print cropper.getCroppedHeight()
print cropper.getCroppedWidth()

crop_rect = cropper.getRect()

print crop_rect.x
print crop_rect.y
print crop_rect.width
print crop_rect.height
