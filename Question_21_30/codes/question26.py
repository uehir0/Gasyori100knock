import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("imori.jpg").astype(np.float)
H,W,C=img.shape

# Nearest Neighbor
a = 1.5
aH = int(a * H)
aW = int(a * W)

y = np.arange(aH).repeat(aW).reshape(aW,aH)
y = (y / a)
x = np.tile(np.arange(aW),(aH,1))
x = (x / a)

fy = np.floor(y).astype(np.int)
fx = np.floor(x).astype(np.int)

fy = np.minimum(fy, W-2)
fx = np.minimum(fx, W-2)

dy = y - fy
dx = x - fx

dy = np.repeat(np.expand_dims(dy, axis=-1), 3, axis=-1)
dx = np.repeat(np.expand_dims(dx, axis=-1), 3, axis=-1)


out = (1-dx) * (1-dy) * img[fy, fx] + dx * (1 - dy) * img[fy, fx+1] + (1 - dx) * dy * img[fy+1, fx] + dx * dy * img[fy+1, fx+1]

#ここでやっていること
# xが 1 1 1 1 1 2 2 2 2 2
# yが 1 2 3 4 5 1 2 3 4 5 見たいな数列が与えられてる


out[out>255]=255
out = out.astype(np.uint8)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("question26.jpg", out)
