import os, shutil, pathlib
l_path = pathlib.Path(r'C:\Users\devchoi\Desktop\TIL\cat-dog-dataset20250820\train')
from keras.utils import image_dataset_from_directory
ds = image_dataset_from_directory(l_path, None, image_size=(224,224), batch_size=32, shuffle=False)
from keras.applications.densenet import preprocess_input, DenseNet121, decode_predictions
ds = ds.map(preprocess_input)
file_paths = getattr(ds, 'file_paths', None)

import cv2
m = DenseNet121(weights='imagenet')
py=m.predict(ds)
for i, path in enumerate(file_paths):
    top5 = decode_predictions(py[i:i+1])[0]
    img = cv2.imread(path)

    h, w = img.shape[:2]

    if w > 900:
        scale = 900./w
        img = cv2.resize(img, (900, int(h*scale)), interpolation=cv2.INTER_AREA)

    x, y = 10, 30
    line_h = 26
    for k, (_, name, p) in enumerate(top5):
        text = f'{k}.{name}: {p:.2%}'
        cv2.putText(img, text, (x, y+(k*line_h)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255), 2, cv2.LINE_AA)
    cv2.imshow('img', img)
    key = cv2.waitKey()
    if key == 27:
        break
cv2.destroyAllWindows()
# 기학습된 모델의 특징 검출기를 이용하여 분류층을 증가시켜 모델을 학습하시오
l_path = pathlib.Path(r'C:\Users\devchoi\Desktop\TIL\cat-dog-dataset20250820\train')
tr_ds = image_dataset_from_directory(l_path, validation_split=0.2, subset='training', image_size=(224,224), batch_size=32)
val_ds = image_dataset_from_directory(l_path, validation_split=0.2, subset='validation', image_size=(224,224), batch_size=32)

print(tr_ds.class_name)
class_n = len(tr_ds.class_name)
# tr_ds = tr_ds.map(lambda x, y : (preprocess_input(x), y))
# val_ds = val_ds.map(lambda x, y : (preprocess_input(x), y))


# 백본을 사용했다고 함
base = DenseNet121(weights='imagenet', include_top=False, input_shape=(224,224,3)) # 특징 검출기만 만들어짐
base.trainable = False

from keras.models import Sequential, Model
from keras.layers import Input, Dense, Dropout, BatchNormalization, Flatten, GlobalAveragePooling2D
from keras.optimizers import Adam
# 이미 불러온 백본을 이용하여 파인튜닝할 경우는 lr값을 더 줄여서 사용하는 것이 좋은 경우가 많음(보편적이며 이미 어느정도 유사하다는 가정)
from keras.losses import binary_crossentropy, sparse_categorical_crossentropy
from keras.callbacks import EarlyStopping, ModelCheckpoint

input_l = Input(shape=(224,224,3))
x = base(input_l, training=False)
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.4)(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.3)(x)

output_l = Dense(class_n, activation='softmax')(x)
Model(input_l, output_l)

m.compile(optimizer=Adam(learning_rate=0.0001), loss=sparse_categorical_crossentropy)
# 이렇게 학습률이 낮은 경우는 배치정규화는 보통 안하는 게 좋다고 함
call_bk = [ModelCheckpoint('b_m.keras', monitor='val_acc', mode='max', save_best_only=True, verbose=1),
           EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)]

m.fit(tr_ds, validation_data=val_ds, epochs=8, callbacks=call_bk)