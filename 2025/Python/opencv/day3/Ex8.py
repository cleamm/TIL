import numpy as np
import cv2

cam = cv2.VideoCapture(0)
k = np.array([[-1,0,0],[0,0,0],[0,0,1]]) # 엠보싱 필터
while True:
    ret, img = cam.read()
    if ret == False:
        print('캡처불가')
        break
    cv2.imshow('oj_img', img)
    gr_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img', gr_img)
    s = cv2.GaussianBlur(gr_img, (15,15), 0, 0)
    cv2.imshow('s', s)
    ck1_img = cv2.filter2D(gr_img,-1, k)
    gry_img16 = np.int16(gr_img)
    e = np.uint8(np.clip(cv2.filter2D(gry_img16, -1, k)+128, 0, 255))
    cv2.imshow('ck1', ck1_img)
    cv2.imshow('e', e)
    key = cv2.waitKey(1) # 숫자를 입력하여 실시간으로 입력되도록 설정
    if key == 27:
        break
cv2.destroyAllWindows()