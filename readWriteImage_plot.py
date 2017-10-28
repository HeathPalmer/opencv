import cv2 #import opencv library
import numpy as np
from matplotlib import pyplot as plt

#read the image
#img=cv2.imread('opencv-logo.png',0)#read image as greyscale

#display image on screen
#cv2.imshow('opencv-logo',img)
#k=cv2.waitKey(0) & 0xFF
#if k==27:
#    cv2.destroyAllWindows() #destroy all windows
#elif k==ord('s'): #wait for 's' to be pressed
    #saved image into new file
    #press 's' to save image
#    cv2.imwrite('opencv-logo_grayscale.png',img)
#    cv2.destroyAllWindows #press 'esc' to close window

img = cv2.imread('opencv-logo.png',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
