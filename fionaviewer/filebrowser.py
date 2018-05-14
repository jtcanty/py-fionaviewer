#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore 
from pyqtgraph import FileDialog

class FileBrowser(QtCore.QObject):
    '''Browse file and extract data'''
    dataChanged = QtCore.pyqtSignal(object)
    
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.file_dialog = FileDialog()     
        
        
    def getOpenFile(self):      
        fname, _filter =self.file_dialog.getOpenFileName(None, 'Open file', 'c:\\',"Text files (*.txt)")
        with open(fname, 'r') as f:
            data = f.readlines()
            data = [int(line.strip()) for line in data]
 
        self.dataChanged.emit(data)

            
    def getNewFile(self):
        print('New File')
        
    
    
    
            
