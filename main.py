import numpy as np
import Stirling as stir
import matplotlib.pyplot as plt
from decimal import Decimal
import Process as proc


def sumProb(mutation,n):
    i=1
    val=1
    while i<n:
        val = val*(i+mutation)
        i+=1
    return val
def main():
    n=100
    populationSize = 10000000
    mutationProbability=100
    stirlingNumber = np.zeros([n,])
    mNumbers = np.zeros([n,])

    i = 0
    for num in stirlingNumber:
        stirlingNumber[i] = Decimal(stir.stirling1(n,i+1))
        i+=1
    i=0
    for num in stirlingNumber:
        mNumbers[i] = i+1
        i+=1

    ewensSampling = np.array(abs(stirlingNumber)*mutationProbability**(mNumbers-1)/sumProb(mutationProbability,n))
    evalH, evalP, nAlleles = proc.Coalescent(mutationProbability,populationSize,n)
    plt.plot(mNumbers,ewensSampling)
    #plt.hist(evalH,bins=20,normed=1,facecolor='green')
    n_bins = len(set(nAlleles))
    plt.hist(nAlleles, bins=n_bins, normed=1, facecolor='red')
    plt.title('')
    plt.show()


if __name__  ==  '__main__':
    main()