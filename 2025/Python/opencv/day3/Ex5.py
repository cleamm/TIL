import cv2
import numpy as np
import matplotlib.pyplot as plt

# 히스토그램 평활화: 어두운 건 어둡게 밝은 건 밝게
img = cv2.imread('data3.jpg')
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
g_h = cv2.calcHist([gry_img], [0], None, [256], [0,256])
cv2.imshow('gr_img', gry_img)
plt.plot(g_h)
# plt.show()

e_img = cv2.equalizeHist(gry_img)
e_h = cv2.calcHist([e_img], [0], None, [256], [0,256])
cv2.imshow('e_img', e_img)
plt.plot(e_h)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()