import cv2
import numpy as np
img = cv2.imread("imori.jpg")
H,W,C=img.shape

filtersize=3
#cotains g
pad=filtersize//2
out=np.zeros((H+pad*2,W+pad*2,C),dtype=np.float)
out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

#filter producer
#filter=np.array([[0,-1,0],[0,1,0],[0,0,0]])
filter=np.array([[0,0,0],[-1,1,0],[0,0,0]])

#filter
temp=out.copy()

for y in range (H):
    for x in range(W):
        for c in range(C):
            out[y+pad][x+pad][c]= np.sum(filter * temp[y:y+filtersize, x:x+filtersize, c])


out = out[pad:pad+H, pad:pad+W].astype(np.uint8)
cv2.imwrite("question14_rgb.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
