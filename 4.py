import sys
from PyQt5.QtWidgets import QApplication,QWidget
app1=QApplication(sys.argv)
widget=QWidget()
widget.resize(480,320)
widget.setWindowTitle("abc!")
widget.show()
sys.exit(app1.exec())

