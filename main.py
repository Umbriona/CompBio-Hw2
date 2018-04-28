import numpy as np
import Stirling as stir
import matplotlib.pyplot as plt
from decimal import Decimal

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
def sumProb(mutation,n):
    i=1
    val=0
    while i<n:
        val = val+(i+mutation)
        i+=1
    return val
dt = np.dtype(np.int64)
n=100
m=frange(1,100,1)
mutationProbability=0.1
stirlingNumber = np.zeros([n,])
mNumbers = np.zeros([n,])
i = 0
for num in stirlingNumber:
    stirlingNumber[i] = Decimal(stir.stirling1(100,i+1))
    i+=1
i=0
for num in stirlingNumber:
    mNumbers[i] = i+1
    i+=1

ewensSampling = np.array(stirlingNumber*mutationProbability**(mNumbers-1)/sumProb(mutationProbability,n))

plt.plot(mNumbers,ewensSampling)
