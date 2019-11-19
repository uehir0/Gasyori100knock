import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape

count=0
S = H * W * C
Zmax=img.max()
out=img.copy()

for i in range (1,255):
    count_=np.where(img == i)
    count+=len(img[count_])
    temp = Zmax / S * count
    out[count_] = temp

out=out.astype(np.uint8)

#show histgram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.savefig("question23_hist.png")
plt.show()

cv2.imwrite("question23_pic.jpg",out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
