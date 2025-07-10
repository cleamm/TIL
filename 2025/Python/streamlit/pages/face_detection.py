import cv2
import streamlit as st

# 이미지 읽어오고 반환
@st.cache_data(show_spinner=False)
def load_data(file_path):
    with open(file_path.name, 'wb') as f:
        f.write(file_path.getbuffer())
    # 원본 이름과 이미지 분리
    name, image = file_path.name, cv2.imread(file_path.name)
    return name, image

file_path = st.file_uploader('image', type=["jpg",'png'])

# 입력 파일
if file_path :
    origin_name, image_file = load_data(file_path)

# 캐스케이드 파일 설정하기
cascade_file = "haarcascade_frontalface_alt.xml"

# 그레이스케일로 변환하기
image_gs = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)

# 얼굴 인식 특징 파일 읽어 들이기
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_file)

# 얼굴 인식 실행하기
face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

if len(face_list) > 0:
    # 인식한 부분 표시하기
    color = (0, 0, 255)
    for face in face_list:
        x, y, w, h = face
        cv2.rectangle(image_file, (x, y), (x + w, y + h), color, thickness=8)
    # 파일로 출력하기
    cv2.imwrite("detect_img.jpg", image_file)
    bottom_menu = st.columns((2, 2))
    with bottom_menu[0]:
        st.image(origin_name)
    with bottom_menu[1]:
        st.image(cv2.cvtColor(image_file, cv2.COLOR_BGR2RGB))
else:
    print("no face")
