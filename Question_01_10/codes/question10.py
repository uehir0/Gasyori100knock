import cv2
import numpy as np
img = cv2.imread("imori_noise.jpg")
H,W,C=img.shape

#prameters
Ksize=3
#creating case
pad=Ksize//2
out=np.zeros((H+pad*2,W+pad*2,C),dtype=np.float)
out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

#


#filter
temp=out.copy()

for y in range (H):
    for x in range(W):
        for c in range(C):
            out[y+pad][x+pad][c]= np.median(np.reshape(temp[y:y+Ksize, x:x+Ksize, c].copy(),(1,Ksize*Ksize)))

out = out[pad:pad+H, pad:pad+W].astype(np.uint8)
cv2.imwrite("question10.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
