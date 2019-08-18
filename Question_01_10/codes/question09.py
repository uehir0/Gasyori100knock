import cv2
import numpy as np
img = cv2.imread("imori_noise.jpg")
H,W,C=img.shape

#prameters
sigma=1.3
Ksize=3
#cotains g
pad=Ksize//2
out=np.zeros((H+pad*2,W+pad*2,C),dtype=np.float)
out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

#g producer
g=np.zeros((Ksize,Ksize,C),dtype=np.float)
for x in range (-pad,-pad+Ksize):
    for y in range(-pad,-pad+Ksize):
        g[x+pad,y+pad]=np.exp((x**2 + y**2)/(2*sigma**2))
g/=sigma * np.sqrt(2 * np.pi)
g/=g.sum()

#filter
temp=out.copy()

for y in range (H):
    for x in range(W):
        for c in range(C):
            out[y+pad][x+pad][c]= np.sum(g * temp[y:y+Ksize, x:x+Ksize, c])

out = out[pad:pad+H, pad:pad+W].astype(np.uint8)
cv2.imwrite("question09.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
