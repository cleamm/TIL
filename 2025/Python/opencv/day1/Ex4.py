import cv2
import matplotlib.pyplot as plt

# 이진화
img = cv2.imread('2025/Python/opencv/day1/dog.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('2025/Python/opencv/day1/dog.jpg', cv2.IMREAD_COLOR)
print('변환전')
print(img.shape)
print(img[0,0])
print(img[200,200])
cv2.imshow('img1',img)
# cv2.waitKey()

print('변환후')
ret, th_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print(th_img.shape)
print(th_img[0,0])
print(th_img[200,200])
cv2.imshow('img2',th_img)
cv2.waitKey()

cv2.destroyAllWindows()