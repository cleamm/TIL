import cv2
import matplotlib.pyplot as plt

# img = cv2.imread('2025/Python/opencv/day1/dog.jpg', cv2.IMREAD_COLOR)
img1 = cv2.imread('2025/Python/opencv/day1/dog.jpg', cv2.IMREAD_GRAYSCALE)
img2= cv2.imread('2025/Python/opencv/day1/dog.jpg', cv2.IMREAD_COLOR)
img3= cv2.imread('2025/Python/opencv/day1/dog.jpg', cv2.IMREAD_COLOR_RGB)
# cv2.namedWindow('m')
# cv2.imshow('m', img1)
rgb_img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
gry_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
print(type(img1))
print(type(img2))
cv2.imshow('img1', rgb_img)
cv2.imshow('img2', gry_img)
cv2.waitKey()
# plt.imshow(img2)
plt.show()
cv2.destroyAllWindows()