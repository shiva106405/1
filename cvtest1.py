import cv2
cv2.namedWindow("testwindow1",cv2.WINDOW_NORMAL)
cv2.resizeWindow("testwindow1",800,600)
cap1=cv2.VideoCapture("C:/Users/Puck/Downloads/0574.mp4")
#cap1=cv2.VideoCapture(0)

while cap1.isOpened():
    ret=cap1.grab()
    ret,frame1=cap1.retrieve()
    if not ret:
        break
    cv2.imshow("testwindow1",frame1)
    key1=cv2.waitKey(1000//46)
    if key1==ord("q"):
        break
cap1.release()
cv2.destroyAllWindows()
