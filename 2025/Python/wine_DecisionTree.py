import streamlit as st
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Streamlit
st.header("와인 종류 예측")
alcohol = st.slider('도수', 0., 20., 10.)
sugar = st.slider('당', 0., 100., 4.)
pH = st.slider('산의 농도', 0., 10., 3.)

# 결정 트리
wine = pd.read_csv('https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv')
X = wine[['alcohol', 'sugar', 'pH']].values
y = wine['class']
scaler = MinMaxScaler()
X = scaler.fit_transform(X)
clf = DecisionTreeClassifier(max_depth=36,
                            min_impurity_decrease=0.00015640163917149342,
                            min_samples_leaf=1,
                            min_samples_split=2)
clf.fit(X, y)

# 예측 버튼
if st.button("와인 종류 예측하기"):
    features = [[alcohol, sugar, pH]]
    prediction = clf.predict(scaler.transform(features))
    st.success(f'result: {'red wine' if prediction == 0 else 'white wine'}')