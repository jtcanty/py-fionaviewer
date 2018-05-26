#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import scipy.io as sio

import numpy as np

from PyQt5 import QtCore 
from pyqtgraph import FileDialog

class FileBrowser(QtCore.QObject):
    '''Browse file and extract data'''
    dataChanged = QtCore.pyqtSignal(object, object)
    
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.file_dialog = FileDialog()           
        
    def getFileName(self):      
        fname, _filter =self.file_dialog.getOpenFileName(None, 'Open file', 'c:\\',"Text files (*.txt);; MAT files (*.mat);;"
                                                         "Excel files (*.csv, *.xls, *.xlsx)")
        openFileMapping = {
            '.txt': self.readTextFile,
            '.mat': self.readMatFile,
            '.csv': self.readExcelFile,
            '.xls': self.readExcelFile,
            '.xlsx': self.readExcelFile
        }
        
        filePath, fileSuffix = os.path.splitext(fname)
        openFileMapping[fileSuffix](fname)                
    
    def readTextFile(self, fname):
        with open(fname, 'r') as txt:
            data = txt.readlines()          
            data_array = np.empty((1,2), float)
            for line in data:
                lineSplit = list(map(float, line.split('\t')))
                lineSplitArray = np.array(lineSplit, ndmin=2)
                data_array = np.append(data_array, lineSplitArray, axis=0)
                
            xData = data_array[:,0]
            yData = data_array[:,1]

        self.dataChanged.emit(xData, yData)
        
    def readMatFile(self, fname):
        mat = sio.loadmat(fname)
        data = mat['data']
        xData = data[:,0]
        yData = data[:,1]
        
        self.dataChanged.emit(xData, yData)
               
    def readExcelFile(self, f):
        print('hi')
    
    def getNewFile(self):
        print('hi')

    
    
    
            
