#same as playing live camera frame but change the index
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.mp4')
#cap.open(1)
while(cap.isOpened()):
    ret,frame = cap.read()
    cv2.imshow('video output',frame)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
