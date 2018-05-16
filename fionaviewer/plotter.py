#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyqtgraph as pg

from pyqtgraph import PlotWidget, ViewBox
from PyQt5 import QtCore

class Plotter(PlotWidget):
    '''Widget for plotting data'''
    def __init__(self, filebrowser):
        PlotWidget.__init__(self)
        
        self.pData = self.plot()
        self.filebrowser = filebrowser
        self.filebrowser.dataChanged.connect(self.handleDataChanged)
        
        self.region = pg.LinearRegionItem
        self.region.setZvalue(10)
        self.addItem(self.region, ignoreBounds=True)
        
        self.region.sigRegionChanged.connect(updateRange)
        self.sigRangeChanged.connect(updateRegion)
        
        self.region.setRegion([1000, 2000])
        
    def handleDataChanged(self, data):
        self.pData.setData(data)
        
    def crossHair(self):
        vLine = pg.InfiniteLine(angle=90, movable=False)
        hLine = pg.InfiniteLine(angle=0, movable=False)
        self.addItem(vLine, ignoreBounds=True)
        self.addItem(hLine, ignoreBounds=True)
        
    def updateRange(self):
        self.region.setZValue(10)
        minX, maxX = self.region.getRegion()
        self.setXRange(minX, maxX, padding=0)
        
    def updateRegion(self,viewRange):
        rng = viewRange[0]
        self.region.setRegion(rng)
        
        
    def mouseMoved(evt):
            
        
           
        
        
    
        
        