import cv2
import numpy as np
import matplotlib.pyplot as plt

# data = np.array([[0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],
#                 [0,0,1,0,0,0,0,0,0,0],
#                 [0,0,1,1,0,0,0,0,0,0],
#                 [0,0,1,1,1,0,0,0,0,0],
#                 [0,0,1,1,1,1,0,0,0,0],
#                 [0,0,1,1,1,1,1,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],], dtype=np.float32)
# data = np.array([[0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],
#                 [0,0,1,1,1,1,1,1,0,0],
#                 [0,0,1,1,1,1,1,1,0,0],
#                 [0,0,1,1,1,1,1,1,0,0],
#                 [0,0,1,1,1,1,1,1,0,0],
#                 [0,0,1,1,1,1,1,1,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],], dtype=np.float32)

data = np.array([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,1,1,1,1,1,1,0,0],
                [0,0,1,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,1,0,0],
                [0,0,1,1,1,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],], dtype=np.float32)

ux = np.array([[-1,0,1]])
uy = np.array([[-1,0,1]]).T
k = cv2.getGaussianKernel(3,1)
g = np.outer(k,k.T)
dx = cv2.filter2D(data, cv2.CV_32F, ux)
dy = cv2.filter2D(data, cv2.CV_32F, uy)

dyy = dy*dy
dxx = dx*dx
dyx = dy*dx

gdyy = cv2.filter2D(dyy, cv2.CV_32F, g)
gdxx = cv2.filter2D(dxx, cv2.CV_32F, g)
gdyx = cv2.filter2D(dyx, cv2.CV_32F, g)

c = (gdyy*gdxx-gdyx*gdyx) - 0.04*(gdyy*gdxx)*(gdyy+gdxx) # 0.04는 일반적으로 쓰는 k 값

# 위 과정을 통해 해리스 특징점을 추출한 것임

np.set_printoptions(precision=2)

# 시각화를 통해 확인
lst = [dy, dx, dyy, dxx, dyx, gdyy, gdxx, gdyx, c]
str_lst = 'dy, dx, dyy, dxx, dyx, gdyy, gdxx, gdyx, c'
split_lst = str_lst.split(', ')
for i, v in enumerate(lst):
    plt.subplot(3,3,i+1)
    plt.title(f'{split_lst[i]}')
    plt.imshow(v)
    plt.axis('off')
plt.show()