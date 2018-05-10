#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyqtgraph import FileDialog
from pyqtgraph import QtGui

from PyQt5.QtCore import QObject, pyqtSignal


class FileBrowser(FileDialog):
    
    def __init__(self):
        super(FileBrowser, self).__init__()
        
    def getOpenFile(self):      
        fname, _filter =FileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Text files (*.txt)")
        with open(fname, 'r') as f:
            data = f.readlines()
            data = [int(line.strip()) for line in data]

        data_changed = pyqtSignal(data, name='dataChanged')

    
            
    def getNewFile(self):
        print('New File')
        
    
    
    
            
