# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testuifile3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication
import sys

from cadtest3 import vtInt,vtFloat,vtObject,vtVariant,vtPnt,cad_run,cad_line

cad_run()

pt1=vtFloat([100,100,100])
pt2=vtFloat([200,200,200])

line1=cad_line(pt1,pt2)
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 140, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.showMinimized)
        self.pushButton.clicked.connect(line1.line_draw)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

app1=QApplication(sys.argv)
widge_3=QtWidgets.QMainWindow()
ui1=Ui_Form()
ui1.setupUi(widge_3)
widge_3.show()
sys.exit(app1.exec())





