import cv2
import numpy as np
import matplotlib.pyplot as plt

#feature set containing (x,y) values of 25 known/training data
#contains 25 random data of two families/classes
#float 32 bit numbers - I think - need to confirm
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)

#label each as red or blue
responses = np.random.randint(0,2,(25,1)).astype(np.float32)

#plot red familes/classes
#set class 0
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'b','s')
#if ytou mess up the backet vs parentheses - it'll make a sound - which is awesome and helpful

#plot blue familes/classes
#set to class 1
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

#show the plot
plt.show()
