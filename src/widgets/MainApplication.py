#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from pyqtgraph.dockarea import DockArea
from PyQt5 import QtCore,QtGui
import pyqtgraph.console
from PyQt5.QtWidgets import QApplication,QMainWindow
import numpy as np

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.dock_area = DockArea()
        self.setCentralWidget(self.dock_area)
        self.resize(1000,500)
        self.setWindowTitle('py-fionaviewer')

        self.createDocks()

    def createDocks(self):
        '''Create all the dock widgets and add to DockArea'''

        # Create widgets
        self.fit = Fit()
        self.filter = Filter()
        self.file_io = FileIO()
        self.trace_plotter = PlotTrace()
        self.dock_display_settings = DisplaySettings()

        # Add widgets to doc
        self.dock_fit = Dock('Fit Signal',widget = self.fit)
        self.dock_filter = Dock('Filter Methods',widget = self.filter)
        self.dock_file_io = Dock('File IO',widget = self.file_io)
        self.dock_trace_plotter = Dock('Signal Plot',widget = self.trace_plotter)
        self.dock_display_settings = Dock('Display Settings',widget = self.display_settings)

        # Add docks to dock area
        self.dock_area.addDock(self.dock_fit)
        self.dock_area.addDock(self.dock_filter)
        self.dock_area.addDock(self.dock_file_io)
        self.dock_area.addDock(self.dock_trace_plotter)
        self.dock_area.addDock(self.dock_display_settings)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())