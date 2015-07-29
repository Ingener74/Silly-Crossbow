# encoding: utf8
import sys
from PIL import Image
from SillyCrossbow import CropTransparent, SillyCrossbow

if len(sys.argv) < 3:
    raise SystemExit('''
Usage: python silly-crossbow-fire-crop.py <path-to-rgba-png> <threshold>
Example: python silly-crossbow-fire-crop.py data/fire.png 50
''')

print SillyCrossbow()

fire = Image.open(sys.argv[1])
cropper = CropTransparent(fire.width, fire.height, int(sys.argv[2]), fire.tostring())

print cropper.getCroppedOffsetX()
print cropper.getCroppedOffsetY()
print cropper.getCroppedHeight()
print cropper.getCroppedWidth()

crop_rect = cropper.getRect()

print crop_rect.x
print crop_rect.y
print crop_rect.width
print crop_rect.height
