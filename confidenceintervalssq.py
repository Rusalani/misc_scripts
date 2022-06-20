#import networkx as nx
#import matplotlib.pyplot as plt


import pandas as pd
import numpy as np
import math
from scipy import stats
def delta_method_CI(data:np.array,pct: float = .95):
    '''

    delta to give confidence interval
    '''
    assert 0<pct<1
    assert isinstance(data[0],int) or isinstance(data[0],float)
    zscore=0
    if pct ==.9:
        zscore = 1.645
    if pct == .95:
        zscore = 1.96
    if pct == .99:
        zscore = 2.58
    Ephat = np.mean(data)
    Vphat = np.var(data)
    N=len(data) ** .5
    #hold= stats.zscore(pct)
    top = ((2 ** .5) / N) * zscore
    up =Ephat*np.exp(top)
    down = Ephat * np.exp(-top)

    return [down,up]


def bootstrap_method_CI(data:np.array,ndraws:int, nboot:int, pct: float = .95):
    '''

        delta to give confidence interval
    '''
    assert 0 < pct < 1
    assert isinstance(data[0], int) or isinstance(data[0], float)
    boot = np.random.choice(data,(ndraws,nboot))
    mean = boot.mean(axis=0)
    Vphat = np.var(data)
    var  = np.var(boot)

    confidenceInterval_1 = stats.norm.interval(alpha=pct, loc=np.mean(mean), scale=stats.sem(mean))

    return [confidenceInterval_1[0], confidenceInterval_1[1]]





'''
samples = np.random.normal(0,1,100)
samples = samples * samples
#print(bootstrap_method_CI(data=np.random.normal(0, 10, 1000)**2, ndraws=50, nboot=500, pct=.95))

print(bootstrap_method_CI(samples,100,50,.9))
print(bootstrap_method_CI(samples,100,50,.95))
print(bootstrap_method_CI(samples,100,50,.99))
print(delta_method_CI(samples,.9))
print(delta_method_CI(samples,.95))
print(delta_method_CI(samples,.99))
'''






