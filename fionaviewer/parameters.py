#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType

class Parameters(ParameterTree):
    
    def __init__(self):
        ParameterTree.__init__(self)
        
        self.params = [
            {'name':'Processing', 'type':'group', 'children':[
                {'name':'Fit', 'type':'list', 'values':['SIC','Bayesian','Chi-Squared']},
                {'name':'Filter', 'type':'list', 'values':['Decimate','Running Mean','L1 Piecewise-constant','Median','Butterworth']},
             ]},
            {'name':'Parameters', 'type':'group', 'children':[
                {'name':'Frame Rate', 'type':'float', 'value': 100},
                {'name':'Decimation Factor', 'type':'float', 'value':1},
                {'name':'Cutoff Freq (Hz)', 'type':'float', 'value':1},
                {'name':'Filter Order', 'type':'int', 'value':1}
            ]}
        ]
                
        # Create tree of Parameter objects
        self.parameterTree = Parameter.create(name='params', type='group', children=self.params)
        self.parameterTree.sigTreeStateChanged.connect(self.parameterChanged)
        
     
    def parameterChanged(self, change):
        for i in change:
            print(i)
        
        
        
       
