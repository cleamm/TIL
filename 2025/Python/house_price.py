import streamlit as st
import joblib

clf_name = './2025/Python/boston_lg_clf.joblib'

# pickle을 사용하여 모델 불러오기
clf = None
try:
    with open(clf_name, 'rb') as file:
        loaded_model_pickle = joblib.load(file)
    print(f"모델이 '{clf_name}' 파일에서 성공적으로 불러와졌습니다 (pickle).")
except FileNotFoundError as e:
    print(f"모델이 '{clf_name}' 파일 에러: ", e)

# Streamlit

st.header("보스턴 주택 가격 예측")

crim = st.slider('범죄율', 0, 150, 50)
zn = st.slider('주거지 비율', 0, 150, 50)
indus = st.slider('비상업지역 비율', 0, 150, 50)
chas = st.slider('찰스강 유무', 0, 1, 0)
nox = st.slider('일산화질소 농도', 0, 1000, 50)
rm = st.slider("방의 수", 1, 10, 3)
age = st.slider('건물 연식', 0, 150, 50)
dis = st.slider('머임', 0, 100, 10)
rad = st.slider('고속도로 접근성', 0, 100, 10)
tax = st.slider('1만달러당 재산세', 0, 100, 10)
ptratio = st.slider('교사와 학생비율', 0, 100, 0)
b = st.slider('흑인 비율', 0, 100, 20)
lstat = st.slider('하위계층 비율', 0, 100, 10)

# 예측 버튼
if st.button("주택 가격 예측하기"):
    bmi_dict = {'thin': 1, 'normal': 2, 'fat': 3}
    reverse_mapping_dict = {value: key for key, value in bmi_dict.items()}
    features = [[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]]
    prediction = loaded_model_pickle.predict(features)
    st.success(f'result: {prediction}')
    # st.success(f"{bedrooms},{crime}, {building_age}, {crim}, {indus}, {min_to_center}: { reverse_mapping_dict.get(prediction[0]) } 입니다.")