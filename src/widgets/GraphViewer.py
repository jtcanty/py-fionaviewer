#!/usr/bin/env python

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt4 import QtGui

class Graph(FigureCanvasQTAgg):
    '''Matplotlib graph widget'''
    def __init__(self):
        super().__init__()
