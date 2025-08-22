import numpy as np
import cv2
img = cv2.imread('data2.png', cv2.IMREAD_UNCHANGED) # PNG 파일을 읽기 위해선 unchanged를 사용해야 함
print(img.shape)
# cv2.imshow('img1',img[:,:,0])
# cv2.imshow('img2',img[:,:,1])
# cv2.imshow('img3',img[:,:,2])
# cv2.imshow('img4',img[:,:,3])
tr_img = img[(img.shape[0]//3)*2:,:,3] # 세번째 글자들을 출력함
print(img.shape, tr_img.shape)
# se = np.uint8([[0,0,1,0,0],
#                [0,1,1,1,0],
#                [1,1,1,1,1],
#                [0,1,1,1,0],
#                [0,0,1,0,0]])
se = np.uint8([[0,1,1,1,0],
               [1,1,1,1,1],
               [1,1,1,1,1],
               [1,1,1,1,1],
               [0,1,1,1,0]])
d1 = cv2.dilate(tr_img, se, iterations=1) # 팽창 연산
d2 = cv2.erode(tr_img, se, iterations=1) # 침식 연산
d3 = cv2.dilate(cv2.erode(tr_img, se, iterations=1), se, iterations=1) # 열림 연산
d4 = cv2.erode(cv2.dilate(tr_img, se, iterations=1), se, iterations=1) # 닫힘 연산
# cv2.imshow('img',tr_img)
cv2.imshow('d1',d1)
cv2.imshow('d2',d2)
cv2.imshow('d3',d3)
cv2.imshow('d4',d4)
# 목적이 무엇인가에 따라 사용하는 것이 달라짐
cv2.waitKey()
cv2.destroyAllWindows()