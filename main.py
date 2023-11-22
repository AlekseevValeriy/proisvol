import random
import sys

from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self._is_paint = False
        self.button.clicked.connect(self.go)

    def go(self):
        self._is_paint = True
        self.update()

    def paintEvent(self, a0):
        if self._is_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        color = QColor(255, 255, 0)
        radius = random.randint(10, min(self.width(), self.height()) // 2)
        x = random.randrange(0, self.width() -radius)
        y = random.randrange(0, self.width() -radius)
        qp.setBrush(color)
        qp.drawEllipse(x, y, radius, radius)





def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    sys._excepthook = sys.excepthook
    sys.excepthook = exception_hook

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())
