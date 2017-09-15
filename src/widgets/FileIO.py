#!/usr/bin/env python

from PyQt5.QtWidgets import QFileDialog, QAction, QTextEdit
from PyQt5.QtGui import QIcon

class FileIO(QFileDialog):
    '''Widget for reading in files'''

    def __init__(self):
        super().__init__()

        self.importData()

    def importData(self):

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)