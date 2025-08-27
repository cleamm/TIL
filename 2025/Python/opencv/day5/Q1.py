# 1. 사진영역 cut 이미지 생성기 만들기(파일로드, cut, 저장)
# 2. 동작으로 배경제거
# 3. 대상 검출기 만들기(검출대상 로드, 검출정보 로드, 찾기이미지 생성, 저장)
# 번외 영상으로 접근
# PyQt를 이용하여 프로그램을 완성하시오

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
import sys, cv2
import numpy as np

class CutMatchImage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('이미지 분할 생성기')
        self.setGeometry(200,200,430,100) # 윈도우 크기

        f_l_b = QPushButton('파일로드', self)
        c_b = QPushButton('잘라내기', self)
        f_s_b = QPushButton('저장', self)
        e_b = QPushButton('종료', self)
        d_i_b = QPushButton('검출 이미지 로드', self) # 검출 이미지 가져오기
        d_c_b = QPushButton('비교 이미지 로드', self) # 검출 비교 이미지 가져오기
        d_m_b = QPushButton('이미지 매치', self) # 검출 매칭 이미지 출력
        d_sv_b = QPushButton('매치 이미지 저장', self) # 매칭 이미지 저장
        self.label = QLabel('프로그램 ON', self)
        self.p_label = QLabel(' ', self)

        f_l_b.setGeometry(10,10,100,30)
        c_b.setGeometry(110,10,100,30)
        f_s_b.setGeometry(210,10,100,30)
        e_b.setGeometry(310,10,100,30)
        d_i_b.setGeometry(10, 40, 100, 30)
        d_c_b.setGeometry(110, 40, 100, 30)
        d_m_b.setGeometry(210, 40, 100, 30)
        d_sv_b.setGeometry(310, 40, 100, 30)
        self.label.setGeometry(170, 70, 500, 30)

        self.L_C, self.R_C = (0,0,255), (255,0,0)
        self.P_SIZE = 5

        f_l_b.clicked.connect(self.f_l_b_f)
        c_b.clicked.connect(self.c_b_f)
        f_s_b.clicked.connect(self.f_s_b_f)
        e_b.clicked.connect(self.e_b_f)
        d_i_b.clicked.connect(self.d_i_b_f)
        d_c_b.clicked.connect(self.d_c_b_f)
        d_m_b.clicked.connect(self.d_m_b_f)
        d_sv_b.clicked.connect(self.d_sv_b_f)
    
    def f_l_b_f(self): #파일로드
        l_fname = QFileDialog.getOpenFileName(self, '파일 로드', './')
        self.img = cv2.imread(l_fname[0])
        if self.img is None:
            sys.exit('파일이 없습니다.')
        self.label.setText('파일 로드 성공')
        self.show_img = self.img.copy()
        cv2.imshow('show_img', self.show_img)

        self.mask = np.zeros((self.img.shape[0], self.img.shape[1]), np.uint8)
        self.mask[:,:] = cv2.GC_PR_BGD

        self.label.setText('붓 소환')
        self.p_label.setText(f'{self.P_SIZE}')
        cv2.setMouseCallback('show_img', self.dw_b)

    def dw_b(self, event, x,y,f,p):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(self.show_img, (x,y), self.P_SIZE, self.L_C, -1)
            cv2.circle(self.mask, (x,y), self.P_SIZE, cv2.GC_FGD, -1)
        elif event == cv2.EVENT_RBUTTONDOWN:
            cv2.circle(self.show_img, (x,y), self.P_SIZE, self.R_C, -1)
            cv2.circle(self.mask, (x,y), self.P_SIZE, cv2.GC_BGD, -1)
        elif event == cv2.EVENT_MOUSEMOVE and f == cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(self.show_img, (x,y), self.P_SIZE, self.L_C, -1)
            cv2.circle(self.mask, (x,y), self.P_SIZE, cv2.GC_FGD, -1)
        elif event == cv2.EVENT_MOUSEMOVE and f == cv2.EVENT_FLAG_RBUTTON:
            cv2.circle(self.show_img, (x,y), self.P_SIZE, self.R_C, -1)
            cv2.circle(self.mask, (x,y), self.P_SIZE, cv2.GC_BGD, -1)
        cv2.imshow('show_img', self.show_img)

    def b_i_b_f(self):
        self.label.setText('붓 소환')
        self.p_label.setText(f'{self.P_SIZE}')
        cv2.setMouseCallback('show_img', self.dw_b)

    def c_b_f(self):
        backgr = np.zeros((1,65), np.float64)
        foregr = np.zeros((1,65), np.float64)
        cv2.grabCut(self.img, self.mask, None, backgr, foregr, 5, cv2.GC_INIT_WITH_MASK)
        mask1 = np.where((self.mask==cv2.GC_BGD)|(self.mask==cv2.GC_PR_BGD), 0, 1).astype('uint8')
        self.cut_img = self.img * mask1[:,:,np.newaxis]
        cv2.imshow('cut', self.cut_img)

    def f_s_b_f(self):
        s_fname = QFileDialog.getSaveFileName(self, '파일저장', './')
        cv2.imwrite(s_fname[0], self.cut_img)

    def e_b_f(self): # 종료
        cv2.destroyAllWindows()
        self.close()
    
    def d_i_b_f(self): # 검출된 이미지 로드
        l_fname = QFileDialog.getOpenFileName(self, '파일 로드', './')
        self.img = cv2.imread(l_fname[0])
        if self.img is None:
            sys.exit('파일이 없습니다.')
        self.label.setText('파일 로드 성공')
        self.show_img = self.img.copy()
        cv2.imshow('detect_img', self.show_img)

        self.mask = np.zeros((self.img.shape[0], self.img.shape[1]), np.uint8)
        self.mask[:,:] = cv2.GC_PR_BGD

    def d_c_b_f(self):
        l_fname = QFileDialog.getOpenFileName(self, '파일 로드', './')
        self.img = cv2.imread(l_fname[0])
        if self.img is None:
            sys.exit('파일이 없습니다.')
        self.label.setText('파일 로드 성공')
        self.show_img = self.img.copy()
        cv2.imshow('match_img', self.show_img)

        self.mask = np.zeros((self.img.shape[0], self.img.shape[1]), np.uint8)
        self.mask[:,:] = cv2.GC_PR_BGD

    def d_m_b_f(self):
        gry_cut = cv2.cvtColor(cut, cv2.COLOR_BGR2GRAY)
        gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        sift = cv2.SIFT().create()
        cut_kp, cut_des = sift.detectAndCompute(gry_cut, None)
        img_kp, img_des = sift.detectAndCompute(gry_img, None)

        flann_matcher = cv2.DescriptorMatcher().create(cv2.DescriptorMatcher_FLANNBASED)
        knn_matcher = flann_matcher.knnMatch(cut_des, img_des, 2)

        T = 0.5
        m_l = [ck_des for ck_des, new_des in knn_matcher if ck_des.distance/new_des.distance<T]

        mc_img = np.empty((max(cut.shape[0], img.shape[0]), cut.shape[1]+img.shape[1],3), np.uint8)
        cv2.drawMatches(cut, cut_kp, img, img_kp, m_l, mc_img,
                        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

        cv2.imshow('end_img', mc_img)
    def d_sv_b_f(self):
        return 1
app = QApplication(sys.argv)
m_win=CutMatchImage()
m_win.show()
app.exec()