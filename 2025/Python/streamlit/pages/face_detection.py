import cv2
import streamlit as st
from PIL import Image
import numpy as np

# 캐스케이드 파일로 얼굴 인식 특징 파일 읽어 들이기
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

# 이미지 읽어오고 반환
@st.cache_data(show_spinner=False)
def load_data(file_path):
    with open(file_path.name, 'wb') as f:
        f.write(file_path.getbuffer())
    # 원본 이름과 이미지 분리
    name, image = file_path.name, cv2.imread(file_path.name)
    return name, image

def detect_faces(image_pil):
    # 1. PIL Image를 NumPy 배열 (RGB)로 변환
    img_rgb = np.array(image_pil.convert('RGB'))
    # 2. RGB 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    faces = cascade.detectMultiScale(gray, 1.1, 4)
    img_bgr_for_drawing = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

    for (x, y, w, h) in faces: # 사각형 그리기: 이미지, 시작점, 끝점, 색상(BGR), 두께
        cv2.rectangle(img_bgr_for_drawing, (x, y), (x+w, y+h), (0, 255, 0), 2) # 초록색 사각형

    return img_bgr_for_drawing



sort = st.radio("검출", options=["이미지", "실시간"], horizontal=1, index=1)
if sort == "이미지":
    file_path = st.file_uploader('image', type=["jpg",'png'])
    if file_path: # 입력 파일
        origin_name, image_file = load_data(file_path)
    try:
        # 그레이스케일로 변환하기
        image_gs = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)

        # 얼굴 인식 실행하기
        face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

        if len(face_list) > 0: # 인식한 부분 표시하기
            color = (0, 0, 255)
            for x, y, w, h in face_list:
                cv2.rectangle(image_file, (x, y), (x + w, y + h), color, thickness=8)
            cv2.imwrite("detect_img.jpg", image_file) # 파일로 출력하기
            bottom_menu = st.columns((2, 2)) # 이미지 비교샷
            with bottom_menu[0]:
                st.image(origin_name)
            with bottom_menu[1]:
                st.image(cv2.cvtColor(image_file, cv2.COLOR_BGR2RGB))
    except:
        st.write("이미지를 삽입해주세요")
    
else:
    FRAME_WINDOW = st.image([]) # 웹캠 스트림을 표시할 Streamlit 위젯
    enable = st.checkbox("카메라 사용하기")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("웹캠을 열 수 없습니다. 카메라가 연결되어 있고 다른 앱에서 사용 중이 아닌지 확인하세요.")
    
    while True:
        ret, frame_bgr = cap.read() # BGR 형식으로 프레임 읽기 (OpenCV 기본)
        if not ret:
            st.write("프레임을 읽을 수 없습니다. 웹캠 스트림을 종료합니다.")
            break
        frame_rgb_for_pil = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB) # BGR을 RGB로 변환 (PIL Image용)
        pil_image_from_frame = Image.fromarray(frame_rgb_for_pil)

        # 얼굴 감지 및 사각형 그리기
        result_img_bgr = detect_faces(pil_image_from_frame)

        # BGR을 RGB로 변환
        FRAME_WINDOW.image(cv2.cvtColor(result_img_bgr, cv2.COLOR_BGR2RGB))

    cap.release() # 웹캠 자원 해제