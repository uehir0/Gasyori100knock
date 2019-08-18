import cv2
import numpy as np
img =cv2.imread("imori.jpg")
out=img.copy()
H,W,C=img.shape
G=8
Uh=int(H/G)
Uw=int(W/G)
for y in range(Uh):
    for x in range(Uw):
        for c in range(C):
            out[G*y:G*(y+1),G*x:G*(x+1),c]=np.max(out[G*y:G*(y+1),G*x:G*(x+1),c]).astype(np.int)

cv2.imwrite("question08.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
