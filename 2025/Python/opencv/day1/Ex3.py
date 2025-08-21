import cv2

data = cv2.VideoCapture('m_v.avi')
if data.isOpened() == False:
    print('파일로드 불가')
    exit(1)

while True:
    ret, img = data.read()
    if ret == False: # 프레임 단위로 읽어보기 때문에 반드시 있을 거임
        print('동영상 출력 완료')
        break
    cv2.imshow('m',img)
    key = cv2.waitKey(30)
    if key == 27:
        print('동영상 지루하다')
        break

# 작업이 끝나면 반드시 종료할 것
data.release()
cv2.destroyAllWindows()
