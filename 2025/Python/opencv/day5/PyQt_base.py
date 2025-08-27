from PyQt6.QtWidgets import QMainWindow, QApplication
import sys, cv2

class C_n(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('윈도우 이름')
        self.setGeometry(200,200,600,100) # 윈도우 크기

app = QApplication(sys.argv)
m_win=C_n()
m_win.show()
app.exec()