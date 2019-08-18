import cv2
import numpy as np
img = cv2.imread("imori.jpg").astype(np.float32)
img=(img//64)*64+32
img=img.astype(np.uint8)
cv2.imwrite("question06.jpg",img)
cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
