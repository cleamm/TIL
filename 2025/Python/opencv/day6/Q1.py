# 개와 고양이 데이터를 로드하여 기학습된 모델을 이용하여 결과를 도출 및 시각화하시오
# 1. 기학습된 모델을 그대로 사용하시오
# 2. 기학습된 모델의 특징 검출기를 이용하여 분류층을 증가시켜 모델을 학습하시오
# 단 모델은 자유롭게 결정하시오
import os
os.environ["KERAS_BACKEND"] = "torch"

import keras
print(f"Keras backend: {keras.backend.backend()}") # 이 부분이 'torch'로 나와야 합니다.

from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.models import Sequential
from keras.layers import Input, Dense
from keras.activations import relu, leaky_relu, sigmoid, softmax
from keras.losses import categorical_crossentropy, binary_crossentropy
from keras.utils import image_dataset_from_directory
from keras.optimizers import Adam, SGD, RMSprop
from keras.callbacks import EarlyStopping, ModelCheckpoint
import cv2

train = image_dataset_from_directory('cat-dog-dataset20250820/train', batch_size=32, image_size=(224,224))
test = image_dataset_from_directory('cat-dog-dataset20250820/test', batch_size=32, image_size=(224,224))
val = image_dataset_from_directory('cat-dog-dataset20250820/val', batch_size=32, image_size=(224,224))
resnet = ResNet50(weights='imagenet', include_top=False, pooling='avg')
resnet.trainable = False
# print(ResNet50(weights='imagenet').summary())
m = Sequential()
m.add(resnet)
m.add(Dense(128, activation='relu'))
m.add(Dense(1, activation='sigmoid'))
m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
es = EarlyStopping(patience=3, restore_best_weights=True)
ck = ModelCheckpoint('resnet.keras', save_best_only=True)
hy = m.fit(train, epochs=10, validation_data=val, callbacks=[es, ck])

img = cv2.imread(r"C:\Users\devchoi\Desktop\TIL\cat-dog-dataset20250820\test\cat\cat.4000.jpg")
data = cv2.resize(img, (224,224)).reshape(1,224,224,3)
s_x = preprocess_input(data)
# m.trainable=False
py = m.predict(s_x)
output = decode_predictions(py)[0] # 후처리
# print(py.sum(axis=1))
for i in range(5):
    cv2.putText(img, output[i][1]+':'+str(output[i][2]), (10,200+i*20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
cv2.imshow('img', img)
cv2.waitKey()