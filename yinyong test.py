from testuifile import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

app1=QApplication(sys.argv)
widge_2=QtWidgets.QWidget
uiform1=Ui_Form()
uiform1.setupUi(widge_2)
widge_2.show()
sys.exit(app1.exec())

