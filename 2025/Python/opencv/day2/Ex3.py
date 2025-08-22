import cv2
oj_img = cv2.imread('data1.jpg') # .은 상위폴더, ./하위폴더
img=oj_img.copy()

def cut(event, x,y,f,p):
    global sx, sy, ex, ey, img # 이미지도 변한다는 것을 전역적으로 전달되어야 함
    if event == cv2.EVENT_LBUTTONDOWN:
        sx, sy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        ex, ey = x,y
        img = img[sy:ey, sx:ex]
    cv2.imshow('img',img)

# cv2.namedWindow('img')
cv2.imshow('img', img)
cv2.setMouseCallback('img', cut)
run=True
while True:
    key=cv2.waitKey()
    if key == ord('a'):
        run = False
        cv2.destroyAllWindows()
    if key == ord('c'):
        img = oj_img.copy()
        cv2.imshow('img', img)
# else:
#     cv2.destroyAllWindows()
