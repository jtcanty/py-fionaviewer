#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyqtgraph as pg

from pyqtgraph import PlotWidget, ViewBox
from PyQt5 import QtCore

class Plotter(PlotWidget):
    '''Widget for plotting data'''
    def __init__(self, filebrowser, data):
        PlotWidget.__init__(self)
        
        self.label = pg.LabelItem(justify='right')
        self.data = data
        self.pData = self.plot(self.data)
        self.filebrowser = filebrowser
        self.filebrowser.dataChanged.connect(self.handleDataChanged)
        
        self.region = pg.LinearRegionItem()
        self.region.setZValue(10)
        self.addItem(self.region, ignoreBounds=True)
        self.region.setRegion([1000, 2000])
        
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.addItem(self.vLine, ignoreBounds=True)
        self.addItem(self.hLine, ignoreBounds=True)
        
        self.region.sigRegionChanged.connect(self.updateRegion)
        self.sigRangeChanged.connect(self.updateRange)
        
        self.vb = self.plotItem.vb
        
        #proxy = pg.SignalProxy(self.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved())
        self.scene().sigMouseMoved.connect(self.mouseMoved)
    
    def handleDataChanged(self, xData, yData):
        self.pData.setData(xData, yData)
        
    def updateRegion(self):
        self.region.setZValue(10)
        minX, maxX = self.region.getRegion()
        self.setXRange(minX, maxX, padding=0)
        
    def updateRange(self, viewRange):
        rng = self.viewRange()[0]
        self.region.setRegion(rng)
               
    def mouseMoved(self, evt):
        pos = evt
        if self.sceneBoundingRect().contains(pos):
            mousePoint = self.vb.mapSceneToView(pos)
            index = int(mousePoint.x())

            if index > 0 and index < len(self.data):
                self.label.setText("<span style='font-size: 12pt'>x=%0.1f, <span style='color: red'>y=%0.1f"
                                   % (mousePoint.x(), self.data[index]))
                self.vLine.setPos(mousePoint.x())
                self.hLine.setPos(mousePoint.y())
                
                

            
        
            
        
           
        
        
    
        
        