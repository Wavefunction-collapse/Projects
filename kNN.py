# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:51:32 2020

@author: Nikolai
"""


import cv2
import numpy as np 
import matplotlib.pyplot as plt 

#Feature set containing (x, y) values of 30 known / training data
trainData = np.random.randint(0, 100,( 30, 2)).astype(np.float32)
#print(trainData) #observe the data

#Labels each other either Red or Blue with numbers 0 and 1 
responses = np.random.randint(0,2,(30,1)).astype(np.float32)

#Take Red families and plot them 
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80, 'r','^')

#Take blue families and plot them

blue = trainData[responses.ravel()==1]
plt.scatter(blue[:, 0],blue[:,1],80,'b', 's')



newcomer = np.random.randint(0,100,(10,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

knn = cv2.ml.KNearest_create()
knn.train(trainData,cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbours, dist = knn.findNearest(newcomer, 3)

print("result: ", results, "\n")
print("neighbours: ", neighbours, "\n")
print("distance: ", dist)


plt.show()


