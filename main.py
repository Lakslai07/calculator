import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.window_init()

    def window_init(self):
        minsize = QSize(450, 600)
        maxsize = QSize(800, 750)

        win_icon = QIcon("Calculator.png")

        self.setWindowIcon(win_icon)
        self.setWindowTitle("Калькулятор")
        self.setMinimumSize(minsize)
        self.setMaximumSize(maxsize)

app = QApplication(sys.argv)

window = Mywindow()
window.show()



sys.exit(app.exec_())
