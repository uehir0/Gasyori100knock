import cv2

img = cv2.imread("./assets/helloworld.png")
cv2.imshow("imori", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
