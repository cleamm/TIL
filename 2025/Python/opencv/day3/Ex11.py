import cv2
import numpy as np

img = cv2.imread('data1.jpg')
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 캐니는 소벨과 연산 방법이 다름
eg = cv2.Canny(gry_img, 100, 100)

cv2.imshow('canny', eg)
cv2.waitKey()
cv2.destroyAllWindows()