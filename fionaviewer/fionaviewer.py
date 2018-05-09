#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pyqtgraph

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

from pyqtgraph import PlotWidget
from pyqtgraph.dockarea import *

from plotter import Plotter
from parameters import Parameters
from filebrowser import FileBrowser


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.area = DockArea()
        self.setCentralWidget(self.area)
        self.resize(1000,500)
        self.setWindowTitle('Fionaviewer')      
        pyqtgraph.setConfigOption('background', 'w')
        
        menu = self.menuBar().addMenu('File')
        self.createDocks()
        self.addWidgets()

    def createDocks(self):
        '''Create docks'''   
        self.dock_plot = Dock('Plot (tabbed)')
        self.dock_plot_selection = Dock('Plot Selection (tabbed)')
        self.dock_file_browser = Dock('File Dialog')
        self.dock_parameters = Dock('Parameters')
        self.dock_console = Dock('Console')
        
        self.area.addDock(self.dock_plot, 'right')
        self.area.addDock(self.dock_plot_selection, 'left') 
        self.area.addDock(self.dock_file_browser, 'top')
        self.area.addDock(self.dock_parameters, 'left')
        self.area.addDock(self.dock_console, 'bottom')
        
    def addWidgets(self):
        '''Create widgets and add them to docks'''
        self.plot = PlotWidget(title='Plot')
        self.plot.plot(np.random.normal(size=100))
        self.dock_plot.addWidget(self.plot)

        self.plot_selection = PlotWidget(title='Plot Selection')
        self.plot_selection.plot(np.random.normal(size=100))
        self.dock_plot_selection.addWidget(self.plot_selection)
        
        self.file_browser = FileBrowser()
        self.dock_file_browser.addWidget(self.file_browser)
                           
        self.parameters = Parameters()
        self.parameters.setWindowTitle('Parameters')
        self.parameters.setParameters(self.parameters.p, showTop=False)
        self.dock_parameters.addWidget(self.parameters)
                       
        #widget_console = pg.console.ConsoleWidget()
        #self.dock_console.addWidget(widget_console)
        
    def connectSignalstoSlots(self):
        self.file_browser.connect(self.plot.plot)
        
        
    
            
        
        
