import numpy as np
import cv2

img = cv2.imread('data1.jpg')
re_img = cv2.resize(img, (0,0), fx=0.4, fy=0.4)
gry_img = cv2.cvtColor(re_img, cv2.COLOR_BGR2GRAY)

g1 = cv2.GaussianBlur(gry_img, (3,3), 0,0)
g2 = cv2.GaussianBlur(gry_img, (5,5), 0,0)
g3 = cv2.GaussianBlur(gry_img, (7,7), 0,0)
g4 = cv2.GaussianBlur(gry_img, (9,9), 0,0)
g5 = cv2.GaussianBlur(gry_img, (15,15), 0,0) # 커널이 커질수록 퍼짐 작용이 커짐
# 보통 스무딩 효과,그리고 원근법

g_all_img = np.hstack((gry_img,g1,g2,g3,g4,g5))
# cv2.imshow('g', g_all_img)

# 아래는 엠보싱 필터라고 함
k = np.array([[-1,0,0],
              [0,0,0],
              [0,0,1]])
# 위의 커널을 바꾸면 샤프닝, 컨볼루션(비선형) 등의 내용을 적용하도록 할 수 있음
# 오버플로우 => 255값을 넘기면 생기는 문제 -> 0으로 다시 시작함
# 언더플로우 => 0 미만에서 생기는 문제 -> 255로 다시 시작함

gry_img16 = np.int16(gry_img)
t1 = np.uint8(np.clip(cv2.filter2D(gry_img16, -1, k)+128, 0, 255)) # 0보다 낮은 건 0, 255보다 큰건 255
t2 = np.uint8(cv2.filter2D(gry_img16, -1, k)+128)
t3 = cv2.filter2D(gry_img16, -1, k)
# 클립핑은 범위를 벗어났을 때의 왜곡을 방지하기 위함임

cv2.imshow('t1', t1)
cv2.imshow('t2', t2)
cv2.imshow('t3', t3)
cv2.waitKey()
cv2.destroyAllWindows()