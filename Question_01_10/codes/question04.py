import cv2
import numpy as np
img = cv2.imread("imori.jpg").astype(np.float32)
b = img[:,:,0].copy()
g = img[:,:,1].copy()
r = img[:,:,2].copy()
H,W,C = img.shape

gray=0.2126*r+0.7152*g+0.0722*b
gray=gray.astype(np.uint8)

maxX=0

for pt in range (1,255):
    c0 = gray[np.where(gray<pt)]
    m0 = np.mean(c0) if len(c0)>0 else 0
    w0 = len (c0) /(H*W)
    c1 = gray[np.where(gray>=pt)]
    m1 = np.mean(c1) if len(c1)>0 else 0
    w1 = len (c1) /(H*W)
    X = w0*w1*((m0-m1)**2)
    if X>maxX:
        maxX=X
        th=pt

gray [gray<th]=0
gray [gray>=th]=255
out=gray.copy()

cv2.imwrite("question04.jpg",out)
cv2.imshow("result",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
