import sys
from PyQt5.QtWidgets import QWidget, QApplication

app = QApplication(sys.argv)
widget = QWidget()
widget.resize(480,320)
widget.setWindowTitle("abc!")
widget.show()
sys.exit(app.exec())

