from keras.datasets import mnist
import numpy as np
import cv2
import matplotlib.pyplot as plt

(_,_), (X,y) = mnist.load_data()

datas=np.array([X[(y==i)][0] for i in range(10)])
print(datas.shape)
str_lst = 'dy, dx, dyy, dxx, dyx, gdyy, gdxx, gdyx, c'
split_lst = str_lst.split(', ')

for data in datas:
    ux=np.array([[-1,0,1]])
    uy=np.array([[-1,0,1]]).T
    k=cv2.getGaussianKernel(3,1)
    g=np.outer(k,k.T)
    dx=cv2.filter2D(data,cv2.CV_32F,ux)
    dy=cv2.filter2D(data,cv2.CV_32F,uy)

    dyy=dy*dy
    dxx=dx*dx
    dyx=dy*dx

    gdyy=cv2.filter2D(dyy,cv2.CV_32F,g)
    gdxx=cv2.filter2D(dxx,cv2.CV_32F,g)
    gdyx=cv2.filter2D(dyx,cv2.CV_32F,g)

    C=(gdyy*gdxx-gdyx*gdyx)-0.04*(gdyy+gdxx)*(gdyy+gdxx)
    #비최대 억제

    for i in range(1,C.shape[0]-1):
        for j in range(1,C.shape[1]-1):
            if C[j,i]>0.1 and sum(sum(C[j,i]>C[j-1:j+2,i-1:i+2]))==8:
                data[j,i]=9

    np.set_printoptions(precision=2)

    lst = [dy, dx, dyy, dxx, dyx, gdyy, gdxx, gdyx, C]

    for i, v in enumerate(lst):
        plt.subplot(3,3,i+1)
        plt.title(f'{split_lst[i]}')
        plt.imshow(v)
        plt.axis('off')
    plt.show()

    print(data)
    plt.imshow(data)
    plt.title('data')
    plt.axis('off')
    plt.show()