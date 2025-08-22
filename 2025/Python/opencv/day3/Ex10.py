import cv2
import numpy as np

img = cv2.imread('data1.jpg')
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 그레이스케일로 변환

# 엣지검출하는 방법 중 소벨 검출
gr_dx = cv2.Sobel(gry_img, cv2.CV_32F, 1,0, ksize=3) # dx 검출
gr_dy = cv2.Sobel(gry_img, cv2.CV_32F, 0,1, ksize=3) # dy 검출

s_x = cv2.convertScaleAbs(gr_dx)
s_y = cv2.convertScaleAbs(gr_dy)
eg_d = cv2.addWeighted(s_x, 0.5, s_y, 0.5, 0)

cv2.imshow('img', img)
cv2.imshow('gry_img', gry_img)
cv2.imshow('x', s_x)
cv2.imshow('y', s_y)
cv2.imshow('eg', eg_d)
cv2.waitKey()
cv2.destroyAllWindows()