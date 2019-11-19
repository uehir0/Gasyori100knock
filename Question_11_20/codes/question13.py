import cv2
import numpy as np
img = cv2.imread("imori.jpg").astype(np.float32)
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

out=np.zeros((H+pad*2,W+pad*2,C),dtype=np.float)
out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

#filter
temp=out.copy()

for y in range (H):
    for x in range(W):
            out[y+pad][x+pad]= np.max(temp[y:y+filtersize, x:x+filtersize])-np.min(temp[y:y+filtersize, x:x+filtersize])

out[out<0]=0
out[out>255]=255

out = out[pad:pad+H, pad:pad+W].astype(np.uint8)
cv2.imwrite("question13.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
