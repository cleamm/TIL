import streamlit as st
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import joblib

# Streamlit
st.header("와인 종류 예측")
alcohol = st.slider('도수', 0., 20., 10.)
sugar = st.slider('당', 0., 100., 4.)
pH = st.slider('산의 농도', 0., 10., 3.)

# 결정 트리
wine = pd.read_csv('https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv')
scaler = MinMaxScaler()
X = scaler.fit_transform(wine[['alcohol', 'sugar', 'pH']].values)
clf = joblib.load('wine_clf.joblib') # 모델 로드

# 예측 버튼
if st.button("와인 종류 예측하기"):
    features = [[alcohol, sugar, pH]]
    prediction = clf.predict(scaler.transform(features))
    st.success(f'result: {'red wine' if prediction == 0 else 'white wine'}')