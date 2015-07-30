# encoding: utf8
import sys
from PySide.QtCore import Qt, QRect
from PySide.QtGui import QApplication, QPushButton, QWidget, QPainter, QImage
from PIL import Image
from SillyCrossbow import CropTransparent, SillyCrossbow, crop_image3_from_file
from res import Ui_CropWindow


# noinspection PyPep8Naming
class CropWidget(QWidget, Ui_CropWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.images = [QImage(i) for i in ['data/fire.png',
                                           'data/ship1.png']]
        self.images += [crop_image3_from_file(i, 50)[0] for i in ['data/fire.png',
                                           'data/ship1.png']]

        self.s = 2.
        w = 0
        h = 0
        for i in self.images:
            w += i.width() / self.s
            if h < i.height() / self.s:
                h = i.height() / self.s

        self.resize(w + 10, h + 10)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def paintEvent(self, e):
        painter = QPainter(self)

        x = 0
        s = self.s

        for i in self.images:
            w = int(float(i.width()) / s)
            h = int(float(i.height()) / s)
            painter.drawImage(QRect(x, 0, w, h), i)
            painter.drawRect(x, 0, w, h)
            x += i.width() / s


# if len(sys.argv) < 3:
#     raise SystemExit('''
# Usage: python silly-crossbow-crop.py <path-to-rgba-png> <threshold>
# Example: python silly-crossbow-crop.py data/fire.png 50
# ''')
#
# print SillyCrossbow()
#
# fire = Image.open(sys.argv[1])
# fire.show()
# cropper = CropTransparent(fire.width, fire.height, int(sys.argv[2]), fire.tostring(), True)
#
# print cropper.getCroppedOffsetX()
# print cropper.getCroppedOffsetY()
# print cropper.getCroppedHeight()
# print cropper.getCroppedWidth()
#
# crop_rect = cropper.getRect()
#
# print crop_rect.x
# print crop_rect.y
# print crop_rect.width
# print crop_rect.height
#
# cropped_image, x, y, w, h = crop_image(fire, 50)
# cropped_image.show()

# crim2 = cropper.getCroppedImage()
# crim3 = Image.frombytes(mode='RGBA',
#                         size=(crim2.getWidth(), crim2.getHeight()),
#                         data=str(crim2.getData()))
# crim3.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    push = CropWidget()
    push.show()

    sys.exit(app.exec_())
