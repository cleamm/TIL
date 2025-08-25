import cv2
import numpy as np

ck_img = cv2.imread('data4-1.jpg')[190:350,440:560]
gry_ck_img = cv2.cvtColor(ck_img, cv2.COLOR_BGR2GRAY)
new_img = cv2.imread('data4-2.jpg')
gry_new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT().create() # 검출 및 기술 객체
ck_kp, ck_des = sift.detectAndCompute(gry_ck_img, None) # 특징점 도출
new_kp, new_des = sift.detectAndCompute(gry_new_img, None)

print(len(ck_kp), len(new_kp))
flann_matcher = cv2.DescriptorMatcher().create(cv2.DescriptorMatcher_FLANNBASED) # 매칭 기법중 하나임
knn_matcher = flann_matcher.knnMatch(ck_des, new_des, 2)
m_l = []
T = 0.9 # 해당 값에 따라 유사 특징점 추출 개수가 달라짐
for ck_des, new_des in knn_matcher:
    if ck_des.distance/new_des.distance < T:
        m_l.append(ck_des)

mc_img = np.empty((max(ck_img.shape[0], new_img.shape[0]), ck_img.shape[1]+new_img.shape[1], 3), dtype=np.uint8)
cv2.drawMatches(ck_img, ck_kp, new_img, new_kp, m_l, mc_img, 
                flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('mc_img', mc_img)
cv2.waitKey()
# cv2.imshow('img',ck_img)
# cv2.waitKey()