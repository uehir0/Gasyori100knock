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

dx1 = fx - (x-1)
dx2 = fx - x
dx3 = (x+1) - fx
dx4 = (x+2) - fx
dy1 = fy - (y-1)
dy2 = fy - y
dy3 = (y+1) - fy
dy4 = (y+2) - fy

dxs = [dx1, dx2, dx3, dx4]
dys = [dy1, dy2, dy3, dy4] #ここまではわかる

def weight(t):
    a = -1
    at = np.abs(t) #
    w = np.zeros_like(t)
    ind = np.where(at <= 1)
    w[ind] = ((a+2) * np.power(at, 3) - (a+3) * np.power(at, 2) + 1)[ind]
    ind = np.where((at > 1) & (at <= 2))
    w[ind] = (a*np.power(at, 3) - 5*a*np.power(at, 2) + 8*a*at - 4*a)[ind]
    return w

w_sum = np.zeros((aH, aW, C), dtype=np.float32)
out = np.zeros((aH, aW, C), dtype=np.float32)

for j in range(-1, 3):
    for i in range(-1, 3):
        ind_x = np.minimum(np.maximum(fx + i, 0), W-1)
        ind_y = np.minimum(np.maximum(fy + j, 0), H-1)

        #wx=weight((dxs[i+1]**2+dys[j+1]**2)**(1/2))
        #wy=weight((dxs[i+1]**2+dys[j+1]**2)**(1/2))
        wx = weight(dxs[i+1]) #dxs
        wy = weight(dys[j+1])
        wx = np.repeat(np.expand_dims(wx, axis=-1), 3, axis=-1)
        wy = np.repeat(np.expand_dims(wy, axis=-1), 3, axis=-1)

        w_sum += wx * wy
        out += wx * wy * img[ind_y, ind_x]

out /= w_sum
out[out>255] = 255
out = out.astype(np.uint8)

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("question27.jpg", out)
