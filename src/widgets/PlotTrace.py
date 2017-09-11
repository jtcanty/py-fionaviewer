#!/usr/bin/env python

from pyqtgraph import PlotWidget


class PlotTrace(PlotWidget):
    '''Widget for plotting signals'''

    def __init__(self):
        super().__init__()

        self.Data = self.plot()

