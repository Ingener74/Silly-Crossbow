# encoding: utf8
from PIL import Image
from SillyCrossbow import CropTransparent
from PySide.QtGui import QImage, QColor


def crop_image(image, threshold):
    cropper = CropTransparent(image.width, image.height, threshold, image.tostring())
    x = cropper.getCroppedOffsetX()
    y = cropper.getCroppedOffsetY()
    width = cropper.getCroppedWidth()
    height = cropper.getCroppedHeight()

    cropped_image = image.crop((x, y, x + width, y + height))

    return cropped_image, x, y, width, height


def crop_image_from_file(filename, threshold):
    return crop_image(Image.open(filename), threshold)


def crop_image2(image, threshold):
    cropper = CropTransparent(image.width, image.height, threshold, image.tostring(), True)
    x = cropper.getCroppedOffsetX()
    y = cropper.getCroppedOffsetY()
    width = cropper.getCroppedWidth()
    height = cropper.getCroppedHeight()
    image = cropper.getCroppedImage()

    return image, x, y, width, height


def crop_image2_from_file(filename, threshold):
    return crop_image2(Image.open(filename), threshold)


def crop_image3(image, threshold):
    if image.mode == 'RGB':
        image = image.convert('RGBA')
    im, ox, oy, w, h = crop_image(image=image, threshold=threshold)
    qimage = QImage(w, h, QImage.Format_ARGB32)

    for x in xrange(0, im.width):
        for y in xrange(0, im.height):
            color = im.getpixel((x, y))
            qimage.setPixel(x, y, QColor(color[0], color[1], color[2], color[3]).rgba())

    return qimage, ox, oy, w, h


def crop_image3_from_file(filename, threshold):
    return crop_image3(Image.open(filename), threshold=threshold)
