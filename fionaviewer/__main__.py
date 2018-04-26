#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from fionaviewer import MainWindow


def main():
    win = MainWindow()
    win.show()
    
    return app.exec_()
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main()
    sys.exit(0)