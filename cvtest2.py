import cv2
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from  PyQt5.QtCore import *
from PyQt5.QtGui import *


class qtWindow(QWidget):
    def __init__(self):
        super(qtWindow,self).__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle("a testing qtwindow")
        self.resize(1920,1080)
        self.label1=QtWidgets.QLabel("111111111111111111111111111111111")
        self.label1.setAlignment(Qt.AlignCenter)



cv2.namedWindow("testwindow1",cv2.WINDOW_NORMAL)
cv2.resizeWindow("testwindow1",800,600)
cap1=cv2.VideoCapture("C:/Users/Puck/Downloads/0574.mp4")
#cap1=cv2.VideoCapture(0)

while cap1.isOpened():
    cap1.grab()
    ret,frame1=cap1.retrieve()
    if not ret:
        break
    cv2.imshow("testwindow1",frame1)
    key1=cv2.waitKey(1000//30)
    if key1==ord("q"):
        break
print(frame1)
cap1.release()
cv2.destroyAllWindows()
