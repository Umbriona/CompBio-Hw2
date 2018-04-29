import numpy as np
import scipy.special
import math
import random as rand




def Coalescent(mutation,populationSize,sampleSize):
    numberOfTriles = 1000
    taverage = np.zeros((sampleSize-1)*numberOfTriles, dtype=np.float32)
    poiProb = np.zeros(100)
    for index1 in range(numberOfTriles):
        taverageSet = np.zeros(sampleSize-1)
        u = mutation/(2*populationSize)
        meanPoi = 0
        tSum = 0
        i=2
        for t in taverageSet:
            meanTj = populationSize/scipy.special.comb(i, 2, exact=True)
            meanTj = np.random.exponential(scale=meanTj, size=None)
            taverageSet[i-2] = meanTj
            i += 1
        j = 1
        for index2 in taverageSet:
            j += 1
            tSum += index2 * j
        meanPoi = u * tSum
        print(tSum)
        for index3 in range(100):
            poiProb[index3] += math.exp(-meanPoi)*meanPoi**index3/math.factorial(index3)/numberOfTriles
    return poiProb