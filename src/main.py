#!/usr/bin/python3

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Thama Gochy'
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        # self.setLayout(qtw.QVBoxLayout())

        self.show()

if __name__ == "__main__":
    App = qtw.QApplication([])
    Window = MainWindow()
    sys.exit(App.exec_())

