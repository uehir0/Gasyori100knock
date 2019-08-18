import cv2
import numpy as np
import matplotlib.pyplot as plt
#import image
img = cv2.imread("imori_dark.jpg").astype(np.float)
H, W, C = img.shape
#goal trans(float)
a, b = 0., 255.
#check min and max
img_min=img.min()
img_max=img.max()
#check
temp=img.copy()

temp[temp<img_min]=a
temp[temp>img_max]=b

temp = (b-a)/(img_max-img_min) * (temp-img_min) + a
out = temp.astype(np.uint8)
#show histgram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.savefig("question21_hist.png")
plt.show()

cv2.imwrite("question21_pic.jpg",out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
