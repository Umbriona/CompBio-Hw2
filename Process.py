import numpy as np
import scipy.special
import math
import random as rand




def Coalescent(mutation,populationSize,sampleSize):
    numberOfTriles = 10000
    taverage = np.zeros((sampleSize-1)*numberOfTriles, dtype=np.float32)
    poiProbh = []
    poiProbp = np.zeros(100)
    allels = []
    for index1 in range(numberOfTriles):
        taverageSet = np.zeros(sampleSize-1)
        event = np.zeros(sampleSize-1)

        u = mutation/(2*populationSize)
        counter = 0
        meanPoi = 0
        tSum = 0
        i = 0
        j = 1
        n = 0
        # tavrageSet is  a vector with the exponentialy distributed time t_i in between coalescent events
        for t in taverageSet:
            meanTj = 1/scipy.special.comb(i+2, 2, exact=True)
            meanTj = np.random.exponential(scale=meanTj, size=None)
            taverageSet[i] = meanTj
            i += 1

        # Events that happen in between coalescent events
        # allels is how many allels
        for evt in event:
            mean = mutation * taverageSet[n]/2
            temp = np.random.poisson(mean)/populationSize
            if temp > 0:
                counter += 1
            n += 1
        allels.append(counter)
        # tSum is the summed version of t_i T_c
        for index2 in taverageSet:
            j += 1
            tSum += index2 * j

        meanPoi = u * tSum
        # poiProbh will form the histogram of the poission distribution
        poiProbh.append(np.random.poisson(meanPoi, 100))
        # poiProbp is the theoretical poission distribution
        for index3 in range(100):
            poiProbp[index3] += math.exp(-meanPoi)*meanPoi**index3/math.factorial(index3)/numberOfTriles

    poiProbh = np.array(poiProbh)
    return [poiProbh, poiProbp, allels]