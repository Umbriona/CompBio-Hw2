import numpy as np
import Stirling as stir

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
n=100
m=frange(1,100,1)
mutationProbability=0.1


print(stir.stirling1(100,1))


