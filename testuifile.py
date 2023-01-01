# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'testuifile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
app1=QApplication(sys.argv)
widge1=QtWidgets.QMainWindow()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 140, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(120, 200, 91, 19))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.checkBox.setText(_translate("Form", "CheckBox"))


ui1=Ui_Form()
ui1.setupUi(widge1)
widge1.show()
sys.exit(app1.exec())