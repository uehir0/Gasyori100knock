import cv2
import numpy as np
import matplotlib.pyplot as plt

input_img = cv2.imread("imori.jpg").astype(np.float)
H,W,C=img.shape

a = 2.
b = 0.
c = 0.
d = 2.
tx = 30
ty = -30

img= np.zeros((H+2,W+2,C),dtype=np.float32)
img[1:H+1,1:W+1]=input_img

H_new=np.round(H*d).astype(np.int)
W_new=np.round(W*a).astype(np.int)
out =np.zeros((H_new+1,W_new+1,C),dtype=np.float32)
#ここで新規にいじりだす拡大されたボードを用意してあげる






out[out>255] = 255 #RGBの値は0~255で表される。
out[out<0] = 0 #float32の時にこれに入れる。
out = out.astype(np.uint8) #uint8に直してあげて出力準備おk。
# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("question29.jpg", out)
