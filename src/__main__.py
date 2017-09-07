#!/usr/bin/env python

import sys


from PyQt5.QtWidgets import QApplication
from widgets.MainApplication import MainWindow


def main():

    w = MainWindow()

    w.show()
    return app.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main()
    sys.exit(0)
