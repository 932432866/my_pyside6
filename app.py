import sys
sys.path.append('F:\my\pyside')
from PySide6.QtWidgets import QApplication
from src.main import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
