# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settingDialog(object):
    def setupUi(self, settingDialog):
        settingDialog.setObjectName("settingDialog")
        settingDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(settingDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(settingDialog)
        self.buttonBox.accepted.connect(settingDialog.accept)
        self.buttonBox.rejected.connect(settingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(settingDialog)

    def retranslateUi(self, settingDialog):
        _translate = QtCore.QCoreApplication.translate
        settingDialog.setWindowTitle(_translate("settingDialog", "Dialog"))

