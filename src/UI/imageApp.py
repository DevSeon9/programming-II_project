from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSlot

class ImageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.app_width = 800
        self.app_height = 600

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle('이미지 선택 및 표시')
        self.setGeometry(100, 100, 800, 600)  # 창 크기 (800x600)

        # 레이아웃 생성
        self.layout = QVBoxLayout()  # 레이아웃을 인스턴스 변수로 저장

        # 이미지 표시 라벨
        self.image_label = QLabel('이미지가 여기에 표시됩니다.', self)
        self.image_label.setFixedSize(600, 400)  # 이미지 라벨 크기 고정
        self.image_label.setStyleSheet("border: 1px solid black;")  # 테두리 추가

        # 버튼 생성
        self.button = QPushButton('이미지 선택', self)
        self.button.clicked.connect(self.select_image)

        # 레이아웃에 라벨과 버튼 추가
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.button)

        # 레이아웃을 윈도우에 설정
        self.setLayout(self.layout)

    def select_image(self):
        # 파일 탐색기 열기
        file_name, _ = QFileDialog.getOpenFileName(self, '이미지 파일 선택', '', 'Images (*.png *.jpg *.bmp)')

        # 파일이 선택되었을 경우
        if file_name:
            # QPixmap으로 이미지 불러오기
            pixmap = QPixmap(file_name)

            # 이미지를 QLabel 크기에 맞게 조정
            pixmap = pixmap.scaled(self.image_label.width(), self.image_label.height())

            # QLabel에 이미지 설정
            self.image_label.setPixmap(pixmap)

    @pyqtSlot()  # 슬롯으로 정의
    def update_ui(self):
        # UI를 업데이트하는 메서드
        self.initUI()  # 기존 UI를 재설정하는 방식 대신 레이아웃이나 요소를 업데이트할 수 있습니다.
        self.show()  # 새로고침 후 창 보여주기



