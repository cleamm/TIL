# import streamlit as st
# import pickle
# filename_pickle = 'bmi20000_svm.pkl'
# loaded_model_pickle = None
# with open(filename_pickle, 'rb') as file:
#     loaded_model_pickle = pickle.load(file)
# print(f'모델이 {filename_pickle}에서 성공적으로 불어와짐')

# st.header('bmi data')
# st_height = st.slider('키', 100, 220, 160)
# st_weight = st.slider('몸무게', 40, 120, 60)

# if st.button('bmi 예측하기'):
#     bmi_dict = {'thin': 1, 'normal':2, 'fat':3}
#     reverse_mapping_dict = {value: key for key, value in bmi_dict.items()}
#     features = ([st_height, st_weight])
#     prediction = loaded_model_pickle.predict(features)
#     st.success(f'st{st.height}, {st_weight} : {reverse_mapping_dict}')

import pickle
import streamlit as st
import sys
print(sys.version)

filename_pickle = './2025/Python/bmi20000_svm.pkl'

# pickle을 사용하여 모델 불러오기
loaded_model_pickle = None
try:
    with open(filename_pickle, 'rb') as file:
        loaded_model_pickle = pickle.load(file)
    print(f"모델이 '{filename_pickle}' 파일에서 성공적으로 불러와졌습니다 (pickle).")
except FileNotFoundError as e:
    print(f"모델이 '{filename_pickle}' 파일 에러: ", e)

# Streamlit

st.header("BMI data")

st_height = st.slider("키(cm)", 100, 220, 160)
st_weight = st.slider("몸무게(kg)", 40, 120, 60)


# 예측 버튼
if st.button("BMI 예측하기"):
    bmi_dict = {'thin': 1, 'normal': 2, 'fat': 3}
    reverse_mapping_dict = {value: key for key, value in bmi_dict.items()}
    features = [[st_height, st_weight]]
    prediction = loaded_model_pickle.predict(features)
    st.success(f"{st_height},{st_weight}: { reverse_mapping_dict.get(prediction[0]) } 입니다.")