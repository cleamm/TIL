import numpy as np
from keras.datasets import mnist
from keras.models import load_model
import matplotlib.pyplot as plt
import cv2

(_,_), (X,y) = mnist.load_data()
# print(X[0])
m = load_model('m.keras')
# print(m.summary())

def s_f(in_x):
    x = cv2.resize(in_x, (28,28), interpolation=cv2.INTER_CUBIC)
    s_x = x.reshape(-1, 28*28)/255
    return s_x

def end_f(py):
    out = py.argmax(axis=1)
    return out

print(m.predict(s_f(X[0])).argmax(axis=1))