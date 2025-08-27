import os
os.environ["KERAS_BACKEND"] = "torch"

from keras.datasets import cifar100
import numpy as np

(tr_x, tr_y), (tt_x, tt_y) = cifar100.load_data()
# print(tr_x.shape)
# print(np.unique(tr_y))

# CNN
from keras.models import Sequential
from keras.layers import Input, Conv2D, Dense, MaxPooling2D, GlobalAveragePooling2D, Dropout, BatchNormalization, Flatten, Rescaling
from keras.optimizers import Adam, SGD, RMSprop, Adagrad, Nadam
from keras.losses import categorical_crossentropy, sparse_categorical_crossentropy
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau

# 100종 분류기 완성하기
print(tr_x.shape, tr_y.shape)
m = Sequential()
m.add(Input(shape=(32,32,3)))
m.add(Rescaling(scale=1./255))

m.add(Conv2D(128, 3, 1, padding='same', activation='relu'))
m.add(BatchNormalization())
m.add(Conv2D(128, 3, 1, padding='same', activation='relu'))
m.add(BatchNormalization())
m.add(Conv2D(128, 3, 1, padding='same', activation='relu'))
m.add(BatchNormalization())
m.add(MaxPooling2D())
m.add(Dropout(0.4))

m.add(Conv2D(256, 3, 1, padding='same', activation='relu'))
m.add(BatchNormalization())
m.add(Conv2D(256, 3, 1, padding='same', activation='relu'))
m.add(BatchNormalization())
m.add(Conv2D(256, 3, 1, padding='same', activation='relu'))
m.add(BatchNormalization())
m.add(MaxPooling2D())
m.add(Dropout(0.3))

m.add(Conv2D(512, 3, 1, padding='same', activation='relu'))
m.add(BatchNormalization())
m.add(Conv2D(512, 3, 1, padding='same', activation='relu'))
m.add(BatchNormalization())
m.add(Conv2D(512, 3, 1, padding='same', activation='relu'))
m.add(BatchNormalization())
m.add(MaxPooling2D())
m.add(Dropout(0.4))

m.add(GlobalAveragePooling2D())
m.add(Dense(512, activation='relu'))
m.add(Dense(100, activation='softmax'))

es = EarlyStopping(patience=10, monitor='val_loss', restore_best_weights=True)
ck = ModelCheckpoint('cifar100test1.keras', monitor='val_acc', mode='max', save_best_only=True)
re = ReduceLROnPlateau(patience=3, min_lr=1e-7, verbose=1, factor=0.7) # 성능향상이 일어나지 않으면 조정 => 학습률 
# 학습하다가 진동성이 큰 데이터는 해주는 것이 좋음
m.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])
# print(m.summary())
hy = m.fit(tr_x, tr_y, validation_split=.2, batch_size=256, epochs=100, callbacks=[es, ck, re])
print(m.evaluate(tr_x, tr_y), m.evaluate(tt_x, tt_y))