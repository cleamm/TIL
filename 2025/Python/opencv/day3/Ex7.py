import numpy as np
import cv2

# opencv는 속도 때문에 이용하는 것임(c를 베이스로 구현되었기 때문)
img = cv2.imread('data1.jpg')
ck_img=img[300:400,300:500,:]
cv2.rectangle(img, (300,300), (500,400), (0,255,0))
# 보간법 설정 확인
im_re = cv2.resize(ck_img, (0,0), fx=5, fy=5, interpolation=cv2.INTER_NEAREST) 
cv2.imshow('oj_img', img)
cv2.imshow('ck_img', im_re)
cv2.waitKey()
im_re = cv2.resize(ck_img, (0,0), fx=5, fy=5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('ck_img', im_re)
cv2.waitKey()
im_re = cv2.resize(ck_img, (0,0), fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('ck_img', im_re)

cv2.waitKey()
cv2.destroyAllWindows()