import cv2
import numpy as np
img = cv2.imread("imori_noise.jpg")
H,W,C=img.shape

#gray scale
b = img[:,:,0].copy()
g = img[:,:,1].copy()
r = img[:,:,2].copy()

gray = 0.2126 * r + 0.7152 * g + 0.0722 * b #0.2126+0.7152+0.0722 = 1
gray = gray.astype(np.uint8)

#LoGfiltersize
LoGfiltersize=5
s=3
pad=LoGfiltersize//2
gray_=np.zeros((H+pad*2,W+pad*2),dtype=np.float)
gray_[pad:pad+H, pad:pad+W] = gray.copy().astype(np.float)

#What is LoGfilter?
#LoG(x,y) = (x**2 + y**2 - s**2) / (2 * pi * s^6) * np.exp(-(x**2+y**2) / (2*s**2))
#LoGfilter producer
LoGfilter=np.zeros((LoGfiltersize,LoGfiltersize),dtype=np.float)
for x in range (-pad,-pad+LoGfiltersize):
    for y in range(-pad,-pad+LoGfiltersize):
        LoGfilter[x+pad,y+pad]=(x**2 + y**2 - s**2) / (2 * np.pi * s**6) * np.exp(-(x**2+y**2) / (2*s**2))
LoGfilter/=LoGfilter.sum()



#LoGfilter
temp=gray_.copy()

for y in range (H):
    for x in range(W):
            gray_[y+pad][x+pad]= np.sum(LoGfilter * temp[y:y+LoGfiltersize, x:x+LoGfiltersize])

gray_[gray_<0]=0
gray_[gray_>255]=255
out = gray_[pad:pad+H, pad:pad+W].astype(np.uint8)
cv2.imwrite("question19.jpg",out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
