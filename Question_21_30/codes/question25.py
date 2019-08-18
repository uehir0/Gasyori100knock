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
y = np.round(y / a).astype(np.int)
x = np.tile(np.arange(aW),(aH,1))
x = np.round(x / a).astype(np.int)

#ここでやっていること
# xが 1 1 1 1 1 2 2 2 2 2
# yが 1 2 3 4 5 1 2 3 4 5 見たいな数列が与えられてる
#y = np.arange(aH).repeat(aW).reshape(aW, -1)#H
#x = np.tile(np.arange(aW), (aH, 1))   #W
#y = np.round(y / a).astype(np.int)
#x = np.round(x / a).astype(np.int)

out = img[y,x]

out = out.astype(np.uint8)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("question25.jpg", out)
