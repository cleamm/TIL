import cv2
import numpy as np

cam = cv2.VideoCapture(0)
if cam.isOpened() == False:
    print('연결불가')
    exit(1)

# 동작 확인
ret, img = cam.read()
if ret==False:
    print('캡쳐 불가')
    exit(1)

# 영상 저장을 위한 코덱설정
codec = cv2.VideoWriter_fourcc('M','J','P','G')
fps = 30
h, w = img.shape[:2] # 이미지 크기
m_v = cv2.VideoWriter('m_v.avi', codec, fps, (w,h))

if m_v.isOpened() == False:
    print('동영상 생성 불가')
    exit(1)

while True:
    # print('카메라 인식됨')
    ret, img = cam.read()
    if ret==False:
        print('캡쳐 불가')
        break

    flip_img = cv2.flip(img, 1) # 좌우 반전
    m_v.write(flip_img) # 영상을 녹화
    cv2.imshow('cam', flip_img) # 반전한 이미지 출력
    # cv2.imshow('cam', img) # 반전하지 않은 이미지

    key = cv2.waitKey(1)
    print(key)
    if key==27: # esc버튼을 누르면 종료되도록
        break
cam.release()
m_v.release()
cv2.destroyAllWindows()