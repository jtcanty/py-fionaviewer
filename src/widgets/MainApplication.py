#!/usr/bin/env python

from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    '''Primary application interface'''

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


