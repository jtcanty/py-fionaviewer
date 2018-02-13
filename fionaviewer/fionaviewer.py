#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QMainWindow
from PyQt5.QtCore import Qt
import pyqtgraph as pg

import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType

import pyqtgraph.console


import numpy as np

from pyqtgraph.dockarea import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.area = DockArea()
        self.setCentralWidget(self.area)
        self.resize(1000,500)
        self.setWindowTitle('Fionaviewer')      
        pg.setConfigOption('background', 'w')
        
        self.createDocks()
        self.addWidgets()
        
    def createDocks(self):
        '''Create docks'''   
        self.d1 = Dock('Dock1 (tabbed) - Plot', size=(500,200))
        self.d2 = Dock('Dock2 (tabbed) - Plot', size=(500,200))
        self.d3 = Dock('Dock3 - File Dialog', size=(100,100))
        self.d4 = Dock('Dock4 - Parameters', size=(100,100))
        self.d5 = Dock('Dock5 - Console', size=(100,100))
        
        self.area.addDock(self.d1, 'right')
        self.area.addDock(self.d2, 'left') 
        self.area.addDock(self.d3, 'top')
        self.area.addDock(self.d4, 'bottom')
        self.area.addDock(self.d5, 'bottom', self.d4)
        
    def addWidgets(self):
        '''Add widgets to docks'''
        w1 = pg.PlotWidget(title='Dock 1 plot')
        w1.plot(np.random.normal(size=100))
        self.d1.addWidget(w1)

        w2 = pg.PlotWidget(title='Dock 2 plot')
        w2.plot(np.random.normal(size=100))
        self.d2.addWidget(w2)
        
        w3 = pg.FileDialog()
        self.d3.addWidget(w3)
                           
        w4 = ParameterTree()
        self.d4.addWidget(w4)
                       
        w5 = pg.console.ConsoleWidget()
        self.d5.addWidget(w5)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())