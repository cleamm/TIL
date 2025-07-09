import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns
import time

# https://30days.streamlit.app/
# 위 주소에서 따라하며 튜토리얼 진행 가능

# 코드 수정 후 always rerun을 웹창에서 눌러주면 저장할 때마다 새로운 코드를 반영함
# st.set_option('server.runOnSave', True)
st.title('네놈의 첫 streamlit 앱')
st.header('Streamlit에 온 것을 환영한다.')
st.write('이것은 정말 간단한 데이터 앱이야.')
st.write('아마두!~.')
st.markdown('## 배고파')
st.table([['곧','출근','시간'],['곧','점심','시간'],['곧', '퇴근','시간']])
st.markdown('` 테이블을 작성할 땐 DataFrame형식으로 작성해줘야 한다능`')
st.code("print('Hello, Streamlit!')") # 코드 블록

# text
st.title("제목 (Title)")
st.header("헤더 (Header)")
st.subheader("서브헤더 (Subheader)")
st.text("일반 텍스트 (Text)")
st.markdown("`Markdown`도 **지원**합니다.") # 마크다운 문법 지원
st.code("import pandas as pd\nimport numpy as np\nimport streamlit as st\nimport matplotlib.pyplot as plt") # 코드 블록
st.code("df = pd.DataFrame({ 'col1': [1, 2, 3, 4], 'col2': [10,20,30,40] }) \nst.dataframe(df) # css(기능?) 적용")
# data
df = pd.DataFrame({ 'col1': [1, 2, 3, 4], 'col2': [10,20,30,40] })
st.dataframe(df)
st.code("st.table(df) # css(기능?)는 미적용됨")
st.table(df)
st.metric(label='온도', value='25°C', delta='1.5°C') # KPI 지표

# chart
st.code("chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c']) \nst.line_chart(chart_data)")
chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
print(chart_data)
st.line_chart(chart_data)
st.code("st.bar_chart(chart_data)")
st.bar_chart(chart_data)

# matplotlib, Plotly, altair 등 외부 라이브러리 연동
st.code("fig, ax = plt.subplots() \nax.scatter([1,2,3],[1,2,3]) \nst.pyplot(fig)")
fig, ax = plt.subplots()
ax.scatter([1,2,3],[1,2,3])
st.pyplot(fig) # matplotlib 차트표시

# altair
st.header('st.write')
st.code("st.write('hello, *world!* :sunglasses: :+1:') \nst.write(1234)")
st.write('hello, *world!* :sunglasses: :+1:')
st.write(1234)
st.write(1234-123)

st.code('''df = pd.DataFrame({'첫번째 컬럼': [1,2,3,4],'두번째 컬럼': [10,20,30,40]})
st.write(df)
st.write('아래는 DF 입니다', df, '위는 DF 입니다')''')
df = pd.DataFrame({'첫번째 컬럼': [1,2,3,4],'두번째 컬럼': [10,20,30,40]})
st.write(df)
st.write('아래는 DF 입니다', df, '위는 DF 입니다')

st.code("""df2 = pd.DataFrame( np.random.randn(200,3), columns=list('abc'))
c = alt.Chart(df2).mark_circle().encode( x='a', y='b', size='c', tooltip=list('abc') )
st.write(c)""")
df2 = pd.DataFrame( np.random.randn(200,3), columns=list('abc'))
c = alt.Chart(df2).mark_circle().encode( x='a', y='b', size='c', tooltip=list('abc') )
st.write(c)


# 공공데이터 자전거
st.title('22년 12월 서울특별시 공공자전거 이용정보(월별)')
bicycle = pd.read_csv('2025/Python/서울특별시_공공자전거_이용정보(월별)_22.12.csv')
st.write(bicycle)
st.write(bicycle.describe())
c = alt.Chart(bicycle).mark_bar().encode(x='연령대코드', y='이용건수')
st.write(c)


# 1. 버튼 (Button)
st.markdown('# 1. 버튼 (Button)')
st.code("""if st.button('눌러보세요'):
    st.write('버튼이 눌렸습니다!')""")
if st.button('눌러보세요'):
    st.write('버튼이 눌렸습니다!')
# 2. 셀렉트박스 (Selectbox)
st.markdown('# 2. 셀렉트박스 (Selectbox)')
st.code("option = st.selectbox('가장 좋아하는 동물은?', ('강아지', '고양이', '앵무새')) \nst.write(f'선택: {option}')")
option = st.selectbox('가장 좋아하는 동물은?', ('강아지', '고양이', '앵무새'))
st.write(f'선택: {option}')

# 3. 슬라이더 (Slider)
st.markdown('# 3. 슬라이더 (Slider)')
st.code('''age = st.slider('나이를 선택하세요', 0, 100, 25) \nst.write(f'당신의 나이는 {age}세 입니다.')''')
age = st.slider('나이를 선택하세요', 0, 100, 25)
st.write(f'당신의 나이는 {age}세 입니다.')

# 4. 텍스트 입력 (Text Input)
st.markdown('# 4. 텍스트 입력 (Text Input)')
st.code('''name = st.text_input('이름을 입력하세요', '홍길동') \nst.write(f'안녕하세요, {name}님!')''')
name = st.text_input('이름을 입력하세요', '홍길동')
st.write(f'안녕하세요, {name}님!')


# 사이드바에 위젯 추가하기
st.markdown('# 사이드바에 위젯 추가하기')
st.code('''add_selectbox = st.sidebar.selectbox("어떤 것을 보시겠습니까?", ("홈", "데이터", "차트"))
col1, col2, col3 = st.columns(3)

with col1:
    st.header("첫 번째 컬럼")
    st.write("내용 1")
with col2:
    st.header("두 번째 컬럼")
    st.line_chart(pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']))
with col3:
    st.header("세 번째 컬럼")
    st.line_chart(pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']))
''')
add_selectbox = st.sidebar.selectbox("어떤 것을 보시겠습니까?", ("홈", "데이터", "차트"))

col1, col2, col3 = st.columns(3)
with col1:
    st.header("첫 번째 컬럼")
    st.write("내용 1")
with col2:
    st.header("두 번째 컬럼")
    st.line_chart(pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']))
with col3:
    st.header("세 번째 컬럼")
    st.line_chart(pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']))


# 카운터
st.markdown('# 카운터')
# 'count'가 session_state에 없으면 0으로 초기화 + 버튼을 누를 때마다 count 1 증가
st.code('''
# 'count'가 session_state에 없으면 0으로 초기화
if 'count' not in st.session_state:
    st.session_state['count'] = 0

# 버튼을 누를 때마다 count 1 증가
if st.button('카운트'):
    st.session_state['count'] += 1
st.write('버튼 클릭 횟수:', st.session_state.count)''')
if 'count' not in st.session_state:
    st.session_state['count'] = 0
if st.button('카운트'):
    st.session_state['count'] += 1
st.write('버튼 클릭 횟수:', st.session_state.count)


# 성능 최적화(캐싱)
st.markdown('# 성능 최적화(캐싱)\n- 함수 위에 데코레이터를 붙이면, 입력값이 동일할 때 함수를 실행하지 않고 이전에 저장된 결과를 즉시 반환')
st.code('''
@st.cache_data # 이 데코레이터가 캐싱 작업을 수행함
def load_data(url):
    df = pd.read_csv(url)
    time.sleep(5)
    return df

st.write('데이터 로딩중...')
df = load_data('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
st.write('데이터 로딩 완료')
st.dataframe(df)
# 해당 코드는 처음 5초만 기다리면 이후엔 즉시 로딩됨
''')
@st.cache_data # 이 데코레이터가 캐싱 작업을 수행함
def load_data(url):
    df = pd.read_csv(url)
    time.sleep(5)
    return df

st.write('데이터 로딩중...')
df = load_data('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
st.write('데이터 로딩 완료')
st.dataframe(df)


# 추가)로고 및 페이지 명칭 변경 기능
st.set_page_config(
    page_title="Choi streamlit",
    page_icon="✨",  # 이모지로 변경
    layout="wide",
    initial_sidebar_state="expanded",
)