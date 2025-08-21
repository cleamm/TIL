import cv2
img = cv2.imread('data1.jpg', cv2.IMREAD_COLOR_BGR)
ck_img = img[:,:,:]

def draw(event, x,y,f,p):
    global ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, (ix,iy), (x,y), (0,0,255), 5)
    cv2.imshow('img', img)


print(img.shape)
cv2.imshow('img', img)
cv2.setMouseCallback('img', draw)
while True:
    if cv2.waitKey() == ord('a'):
        cv2.destroyAllWindows()
        break
    if cv2.waitKey() == ord('c'):
        ck_img = cv2.imread('data1.jpg', cv2.IMREAD_COLOR_BGR)
        cv2.imshow('img', ck_img)