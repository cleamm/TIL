import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data1.jpg')
hb=cv2.calcHist([img], [0], None, [256], [0,256])
hg=cv2.calcHist([img], [1], None, [256], [0,256])
hr=cv2.calcHist([img], [2], None, [256], [0,256])

bimg = img[:,:,0]
gimg = img[:,:,1]
rimg = img[:,:,2]

print(bimg.shape,gimg.shape,rimg.shape)
print(img.shape)

b_rg=bimg.reshape(-1)
plt.hist(b_rg)
plt.plot(hb, 'b-')
plt.show()