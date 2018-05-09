#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyqtgraph import FileDialog
from pyqtgraph import QtGui


class FileBrowser(FileDialog):
    
    def __init__(self):
        super(FileBrowser, self).__init__()
        
    def getOpenFile(self):
        fname =FileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Text files (*.txt)")
        with open(fname) as f:
            data = f.read()
            
        return data
            
