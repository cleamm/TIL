from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
import sys, cv2

class Video(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('비디오')
        self.setGeometry(200,200,500,100)

        v_on = QPushButton('비디오 킴', self) # 제작
        v_off = QPushButton('비디오 끔', self)
        v_sv = QPushButton('비디오 저장', self)
        v_cc = QPushButton('비디오 캡처', self)
        self.label = QLabel('프로그램이 켜집니다.')

        v_on.setGeometry(10,10,100,30) # 배치
        v_off.setGeometry(110,10,100,30)
        v_sv.setGeometry(210,10,100,30)
        v_cc.setGeometry(310,10,100,30)
        self.label.setGeometry(10,50,400,30)

        v_on.clicked.connect(self.v_on_f) # 동작 결정
        v_off.clicked.connect(self.v_off_f)
        v_sv.clicked.connect(self.v_sv_f)
        v_cc.clicked.connect(self.v_cc_f)

    def v_on_f(self):
        self.label.setText('v_on_f 동작')
        self.cam = cv2.VideoCapture(0)
        if not self.cam.isOpened(): self.close()
        while True:
            ret, self.img = self.cam.read()
            if not ret: break
            cv2.imshow('video', self.img)
            cv2.waitKey(1)

    def v_off_f(self):
        self.label.setText('v_off_f 동작')
        self.cam.release()
        cv2.destroyAllWindows()
        self.close()

    def v_sv_f(self):
        self.label.setText('v_sv 동작')
        fname = QFileDialog.getSaveFileName(self, '파일 저장', './')
        cv2.imwrite(fname[0], self.img)
    
    def v_cc_f(self):
        self.label.setText('v_cc 동작')
        self.cap_img = self.img
        cv2.imshow('cap_img', self.cap_img)

app = QApplication(sys.argv)
m_win = Video()
m_win.show()
app.exec()