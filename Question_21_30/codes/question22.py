import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("imori_dark.jpg").astype(np.float)
H, W, C = img.shape

out=img.copy()
#getparameters
m=np.mean(out)
s=np.std(out)
#setparameters
m0=128
s0=52
out=s0 / s * (out - m) + m0
#preparation
out[out<0]=0
out[out>255]=255
out=out.astype(np.uint8)
#show histgram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.savefig("question22_hist.png")
plt.show()

cv2.imwrite("question22_pic.jpg",out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
