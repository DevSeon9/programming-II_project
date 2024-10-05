import sys
from PyQt6.QtWidgets import QApplication
from src.UI.imageApp import ImageApp
from src.UI.autoRander import AutoRander
import os

if __name__ == '__main__':
    if "RESTARTED" not in os.environ:
        os.environ["RESTARTED"] = "1"

        # 애플리케이션 시작
        app = QApplication(sys.argv)

        # 이미지 앱 생성
        window = ImageApp()

        # 파일 감시기 시작
        file_watcher = AutoRander(path='./src/UI')  # src/UI 디렉토리를 감시
        file_watcher.start()  # 파일 감시기 시작

        # UI 업데이트 신호 연결
        file_watcher.update_signal.connect(window.update_ui)

        try:
            window.show()
            sys.exit(app.exec())
        except KeyboardInterrupt:
            file_watcher.stop()
        finally:
            file_watcher.stop()  # 종료 시 감시기 정지
