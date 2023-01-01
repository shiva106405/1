# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testuifile2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication
import sys


class test1:
    pass

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(120, 200, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 120, 72, 15))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.checkBox.toggled['bool'].connect(self.label.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
        self.label.setText(_translate("Form", "label_name"))
app1=QApplication(sys.argv)
widge_3=QtWidgets.QMainWindow()
ui1=Ui_Form()
ui1.setupUi(widge_3)
widge_3.show()
sys.exit(app1.exec())

