import cv2
# 이미지 준비
img = cv2.imread('data1.jpg', cv2.IMREAD_COLOR_BGR)
r = (0, 0, 255)
g = (0, 255, 0)
b = (255, 0, 0)
ck = [r,g]

# 이벤트 함수 정의
def draw(event, x,y,f,p):
    global ix, iy
    if event == cv2.EVENT_MOUSEMOVE and f == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), 5, ck[0], -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        ck.reverse() # 색 변환
    cv2.imshow('img', img)


cv2.imshow('img', img)
cv2.setMouseCallback('img', draw)
run=True

while run:
    key = cv2.waitKey()
    if ord('a'):
        run=False
else:
    cv2.destroyAllWindows()