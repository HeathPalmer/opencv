import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    #print(ret)
    #print(frame) 

    cv2.imshow("Frame", frame)
    keypress = cv2.waitKey(1)
    if keypress == ord('q'):
        break

capture.release()
cv2.destroyALLWindows()
