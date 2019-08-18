import cv2
import numpy as np
img = cv2.imread("imori.jpg")
H,W,C=img.shape

#gray scale
b = img[:,:,0].copy()
g = img[:,:,1].copy()
r = img[:,:,2].copy()

gray = 0.2126 * r + 0.7152 * g + 0.0722 * b #0.2126+0.7152+0.0722 = 1
gray = gray.astype(np.uint8)

#filtersize
filtersize=3
pad=filtersize//2
gray_=np.zeros((H+pad*2,W+pad*2),dtype=np.float)
gray_[pad:pad+H, pad:pad+W] = gray.copy().astype(np.float)

#filter producer
filter=np.array([[0,-1,0],[0,1,0],[0,0,0]])
#filter=np.array([[0,0,0],[-1,1,0],[0,0,0]])

#filter
temp=gray_.copy()

for y in range (H):
    for x in range(W):
            gray_[y+pad][x+pad]= np.sum(filter * temp[y:y+filtersize, x:x+filtersize])

gray_[gray_<0]=0
gray_[gray_>255]=255
out = gray_[pad:pad+H, pad:pad+W].astype(np.uint8)
cv2.imwrite("question14_gray_vertical.jpg",out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
