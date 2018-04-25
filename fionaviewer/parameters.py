#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyqtgraph as pg
from pyqtgraph.parametertree import Parameter, ParameterTree

class Parameters(ParameterTree):
    
    def __init__(self):
        super(ParameterTree, self).__init__()
        self.params = [
            {'name':'Processing', 'type':'group', 'children':[
                {'name':'Fit', 'type':'list', 'values':['SIC','Bayesian','Chi-Squared']},
                {'name':'Filter', 'type':'list', 'values':['Decimate','Running Mean','L1 Piecewise-constant','Median','Butterworth']},
             ]},
            {'name':'Parameters', 'type':'group', 'children':[
                {'name':'Frame Rate', 'type':'float', 'value': 100},
                {'name':'Decimation Factor', 'type':'float', 'value':1},
                {'name':'Cutoff Freq (Hz)', 'type':'float', 'value':1},
                {'name':'Filter Order', 'type',:'int', 'value':1}
            ]}
        ]
        
        
        # Create tree of Parameter objects
        self.p = Parameter.create(name='params', type='group', children=params)
        self.w = setWindowTitle('Parameters')
