#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyqtgraph import PlotWidget

class Plotter(PlotWidget):
    '''Widget for plotting data'''
    def __init__(self, filebrowser):
        PlotWidget.__init__(self)
        
        self.pData = self.plot()
        self.filebrowser = filebrowser
        self.filebrowser.dataChanged.connect(self.handleDataChanged)
        
    def handleDataChanged(self, data):
        self.pData.setData(data)

        
           
        
        
    
        
        