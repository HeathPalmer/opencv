import numpy as np
import cv2

#to capture video - we need VideoCapture
#to get the camera feed from 1 camera - pass a -1 or 0
#for multiple feeds, pass a 1,2...n for the number of cameras
cap = cv2.VideoCapture(0)

while(True):
    #capture frame by frame
    #returns a bool (True/False)
    ret, frame = cap.read()
    #to check if cap.read initiallized - use cap.isOpened() - if true, awesome
    #if not, use cap.open()

    #if you want a property from the video, then use cap.get(propld)
    #propld is a number between 0 and 18 and each number is a property
    #some of these video properties can be editted using cap.set(propld, value)
    #example is changing frame size:
    cap.get(3)# - width
    cap.get(4)# - height
    #change it to:
    ret = cap.set(3,320)
    ret = cap.set(4,240)
    
    #things we do to the frame - gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Display the frames
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#when things are done - release the capture
cap.release()
cv2.destroyAllWindows()
