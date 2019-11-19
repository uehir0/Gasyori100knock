import cv2
import numpy as np
img = cv2.imread("imori.jpg")
#_img = img.astype(np.float32)
img[:,:] = img[:,:,(2,1,0)]
cv2.imwrite("question01.jpg",img)
cv2.imshow('',img)
cv2.waitKey(0)
#cv2.imwrite("answer1.jpg",img)
