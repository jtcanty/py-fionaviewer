import numpy as np
import pandas as pd
import random
import math
import statsmodels.api as sm
from scipy.optimize import curve_fit


class Fitter():
    '''Time series fitting'''
    def __init__(self, filebrowser):     
        self.currentStepIndices = []
        self.minDwellLength = 1
        self.numSteps = 0
        self.filebrowser = filebrowser
        self.filebrowser.dataChanged.connect(self.handlePlotData)

    def fitTraceWithSIC(self):
        '''Fit the simulated traces using the SIC step-fitting algorithm

        Args:
            plotData (np.array): The coordinates of the plotted trace
            currentStepIndices (list): Array of indices of the recorded steps
            minDwellLength (int): Minimum number of points to be considered a dwell
            currentSIC (float): Minimized SIC value of the current fit

        Returns:  
            fit (array): A numpy array of coordinates corresponding to the optimal SIC fit 

        '''
        try:
            self.plotData = self.yData           
            self.plotDataLength = len(self.xData)
            
        except AttributeError:
            return

        # Calculate initial SIC value
        currentSIC = self.getSchwarzInformationCriterion()

        while True:
            # Compute SIC and add new step
            (nextSIC, newStepIndex) = self.getLogLikelihood()
            if currentSIC >= nextSIC:
                currentStepIndices.append(newStepIndex)
                currentSIC = nextSIC
                continue

            elif currentSIC < nextSIC:
                break

        # Assemble steps into a trace fit
        fitPlotData = _merge_steps(plotData, currentStepIndices)

        return (fitPlotData, currentStepIndices)
        

    def getLogLikelihood(self):
        ''' Calculate the minimum SIC statistic for all models with n steps. 

        Args:
            minSIC (float): The lowest SIC score
            bestStepIndex (int): Index of step that yielded the lowest SIC score 

        '''
        
        fitSIC = np.zeros(self.plotDataLength)

        for step in range(0, self.plotDataLength):
            if step in self.currentStepIndices:
                continue

            if step == 0:
                continue

            # Set new step at current point and calculate global variance of all dwells.
            temp = self.currentStepIndices + [step]
            plotDataSplit = np.split(self.plotData, np.sort(temp))
            dwellVariance = [np.var(self.plotDataSplit[j]) * len(plotDataSplit[j]) for j in range(0, len(plotDataSplit))]
            globalVariance = (1 / self.plotDataLength) * sum(dwellVariance)

            # Compute SIC score
            numSteps = len(plotDataSplit) - 1
            SIC = self.getSchwarzInformationCriterion()
            fitSIC[step] = SIC

        # Extract minimum SIC score and step position
        stepIndices = (fitSIC != 0)
        bestStepIndex = np.argmin(fitSIC[stepIndices])
        stepIndex = np.arange(fitSIC.shape[0])[stepIndices][bestStepIndex]
        minSIC = fitSIC[stepIndex]

        return (minSIC, stepIndex)


    def getSchwarzInformationCriterion(self):
        '''Compute the current SIC score
        
            (p + 2)log(n) + nlog(sigma^2)
            
            p = number of paraemters
            n = number of data points
            sigma^2 = variance
        
        '''
        
        P = self.numSteps
        N = self.plotDataLength
        Variance = np.var(self.plotData)
        SIC = (P + 2) * np.log(N) + N * np.log(Variance)

        return SIC
                
    
    def mergeSteps(self):
        '''Construct the optimal SIC fit and plot it. Output the fit coordinates'''
        
        fitSplit = np.split(self.plotData, np.sort(self.currentStepIndices))
        meanDwellValue = np.array([np.mean(fitSplit[i]) for i in range(0, len(fitSplit))])
        dwellFits = [meanDwellValue[j] * np.ones(len(fitSplit[j])) for j in range(0, len(fitSplit))]
        dataFit = np.concatenate(dwellFits)

        return dataFit 
    
    def handlePlotData(self, xData, yData):
        self.xData = xData
        self.yData = yData
        

    