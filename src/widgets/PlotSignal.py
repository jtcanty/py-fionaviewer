#!/usr/bin/env python

import pyqtgraph as pg
import numpy as np


class PlotSignal(pg.PlotWidget):
    '''Widget for plotting signals'''

    def __init__(self):
        super().__init__()

        self.plotData = self.plot()

    def getData(self):

