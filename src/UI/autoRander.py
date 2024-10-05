import time
import sys
import importlib
import watchdog.events
import watchdog.observers
from PyQt6.QtCore import pyqtSignal, QObject

class ChangeHandler(watchdog.events.FileSystemEventHandler):
    def __init__(self, update_signal):
        self.update_signal = update_signal

    def on_modified(self, event):
        if event.src_path.endswith("imageApp.py"):
            print("imageApp.py 파일이 수정되었습니다. 애플리케이션을 업데이트합니다.")
            importlib.reload(sys.modules['src.UI.imageApp'])  # 수정된 모듈을 재로딩
            self.update_signal.emit()  # 신호를 방출하여 UI 업데이트를 요청

class AutoRander(QObject):
    update_signal = pyqtSignal()  # UI 업데이트 신호 정의

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.observer = watchdog.observers.Observer()

    def start(self):
        event_handler = ChangeHandler(self.update_signal)
        self.observer.schedule(event_handler, self.path, recursive=False)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()
