import cv2
import numpy as np

img = cv2.imread("imori.jpg").astype(np.float)

img /= 255

#parameters
c=1
g=2.2

out=img.copy()

out = (1/c * img) ** (1/g)
out*=255
out[out>255]=255
out[out<0]=0
out=out.astype(np.uint8)
#show picture
cv2.imwrite("question24_pic.jpg",out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
