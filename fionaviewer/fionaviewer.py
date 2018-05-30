#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import numpy as np
import pyqtgraph

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

from pyqtgraph import PlotWidget
from pyqtgraph.dockarea import *

from plotter import Plotter
from parameters import Parameters
from filebrowser import FileBrowser
from fitter import Fitter


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.area = DockArea()
        self.setCentralWidget(self.area)
        self.resize(1200,700)
        self.setWindowTitle('Fionaviewer')      
        pyqtgraph.setConfigOption('background', 'w')
        
        self.file_browser = FileBrowser()
        self.fitter = Fitter()
        
        self.createDocks()
        self.addWidgets()
        self.createMenu()   

    def createDocks(self):
        '''Create docks'''   
        self.dock_plot = Dock('Plot (tabbed)', size=(500,500))
        self.dock_plot_selection = Dock('Plot Selection (tabbed)', size=(500,200))
        self.dock_parameters = Dock('Parameters', size=(150,700))
        self.dock_console = Dock('Console', size=(1200,150))
        
        self.area.addDock(self.dock_plot, 'right')
        self.area.addDock(self.dock_plot_selection, 'bottom', self.dock_plot) 
        self.area.addDock(self.dock_parameters, 'left')
        self.area.addDock(self.dock_console, 'bottom')
        
    def addWidgets(self):
        '''Create widgets and add them to docks'''
        data = np.random.normal(size=100)
        
        self.plotter = Plotter(self.file_browser, data)
        self.dock_plot.addWidget(self.plotter)

        self.plot_selection = Plotter(self.file_browser, data)
        self.dock_plot_selection.addWidget(self.plot_selection)
                           
        self.parameters = Parameters()
        self.parameters.setWindowTitle('Parameters')
        self.parameters.setParameters(self.parameters.parameterTree, showTop=False)
        self.dock_parameters.addWidget(self.parameters)
                       
        #widget_console = pg.console.ConsoleWidget()
        #self.dock_console.addWidget(widget_console)
        
    def createMenu(self):
        openAction = QtGui.QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.file_browser.getFileName)
        
        newAction = QtGui.QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.file_browser.getNewFile)
        
        saveAction = QtGui.QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.file_browser.saveNewFile)
        
        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.closeApplication)
        
        fitAction = QtGui.QAction('Fit', self)
        fitAction.setShortcut('Ctrl+F')
        fitAction.triggered.connect(self.fitter.fitTraceWithSIC)
        
        self.plotter.plotItem.ctrlMenu.addAction(fitAction)                         
       
        menubar = self.menuBar()
        filemenu = menubar.addMenu('File')
        filemenu.addAction(openAction)
        filemenu.addAction(newAction)
        filemenu.addAction(saveAction)
        filemenu.addAction(exitAction)
                                  
        
    def closeApplication(self):
        sys.exit()
             

        
        
    
            
        
        
