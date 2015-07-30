# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/crop.ui'
#
# Created: Thu Jul 30 14:29:45 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CropWindow(object):
    def setupUi(self, CropWindow):
        CropWindow.setObjectName("CropWindow")
        CropWindow.resize(914, 427)

        self.retranslateUi(CropWindow)
        QtCore.QMetaObject.connectSlotsByName(CropWindow)

    def retranslateUi(self, CropWindow):
        CropWindow.setWindowTitle(QtGui.QApplication.translate("CropWindow", "Crop", None, QtGui.QApplication.UnicodeUTF8))

