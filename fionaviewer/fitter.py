import numpy as np
import pandas as pd
import random
import math
import statsmodels.api as sm
from scipy.optimize import curve_fit


class Fitter():
    
    def __init__(self):
        self.currentStepIndices = []
        self.minDwellLength = 1
        self.numSteps = 0
       
    def fitTraceWithSIC(self, plotData):
        '''Fit the simulated traces using the SIC step-fitting algorithm

        Args:
            plotData (np.array): The coordinates of the plotted trace
            currentStepIndices (list): Array of indices of the recorded steps
            minDwellLength (int): Minimum number of points to be considered a dwell
            currentSIC (float): Minimized SIC value of the current fit

        Returns:  
            fit (array): A numpy array of coordinates corresponding to the optimal SIC fit 

        '''
            
        plotDataLength = len(plotData)

        # Calculate initial SIC value
        currentSIC = self.getSchwarzInformationCriterion(numSteps, plotDataLength, plotData)

        while True:
            # Compute SIC and add new step
            (nextSIC, newStepIndex) = self.getLogLikelihood(plotData, currentStepIndices, 
                                                       plotDataLength, numSteps)
            if currentSIC >= nextSIC:
                currentStepIndices.append(newStepIndex)
                currentSIC = nextSIC
                continue

            elif currentSIC < nextSIC:
                break

        # Assemble steps into a trace fit
        fitPlotData = _merge_steps(plotData, currentStepIndices)

        return (fitPlotData, currentStepIndices)
        

    def getLogLikelihood(self, plotData, currentStepIndices, plotDataLength, numSteps):
        ''' Calculate the minimum SIC statistic for all models with n steps. 

        Args:
            minSIC (float): The lowest SIC score
            bestStepIndex (int): Index of step that yielded the lowest SIC score 

        '''
        
        fitSIC = np.zeros(plotDataLength)

        for step in range(0, plotDataLength):
            if step in currentStepIndices:
                continue

            if step == 0:
                continue

            # Set new step at current point and calculate global variance of all dwells.
            temp = currentStepIndices + [step]
            plotDataSplit = np.split(plotData, np.sort(temp))
            dwellVariance = [np.var(plotDataSplit[j]) * len(plotDataSplit[j]) for j in range(0, len(plotDataSplit))]
            globalVariance = (1 / plotDataLength) * sum(dwellVariance)

            # Compute SIC score
            numSteps = len(plotDataSplit) - 1
            SIC = self.getSchwarzInformationCriterion(numSteps, plotDataLength, plotData)
            fitSIC[step] = SIC

        # Extract minimum SIC score and step position
        stepIndices = (fitSIC != 0)
        bestStepIndex = np.argmin(fitSIC[stepIndices])
        stepIndex = np.arange(fitSIC.shape[0])[stepIndices][bestStepIndex]
        minSIC = fitSIC[stepIndex]

        return (minSIC, stepIndex)


    def getSchwarzInformationCriterion(self, numSteps, plotDataLength, plotData):
        '''Compute the current SIC score
        
            (p + 2)log(n) + nlog(sigma^2)
            
            p = number of paraemters
            n = number of data points
            sigma^2 = variance
        
        '''
        
        P = numSteps
        N = plotDataLength
        Variance = np.var(plotData)
        SIC = (P + 2) * np.log(N) + N * np.log(Variance)

        return SIC
                
    
    def mergeSteps(self, plotData, currentStepIndices):
        '''Construct the optimal SIC fit and plot it. Output the fit coordinates'''
        
        fitSplit = np.split(plotData, np.sort(currentStepIndices))
        meanDwellValue = np.array([np.mean(fitSplit[i]) for i in range(0, len(fitSplit))])
        dwellFits = [meanDwellValue[j] * np.ones(len(fitSplit[j])) for j in range(0, len(fitSplit))]
        dataFit = np.concatenate(dwellFits)

        return dataFit 

    