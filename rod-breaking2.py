import random
from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
def sim_triangle_beta(n=1000,a=20,b=1):
    '''
    '''
    assert isinstance(n,int)
    assert n>=1
    assert isinstance(a,int)
    assert isinstance(b,int)
    assert a >=1
    assert b >=1
    count =0
    for x in range(n):
        t=beta.rvs(a,b,size=2)

        s1 = t[0]
        s2 = t[1]
        split1 = min(s1,s2)
        split2 = max(s1,s2) - split1
        split3 = 1- (split2+split1)
        
        
        if split1+split2 > split3 and split1+split3 > split2 and split2+split3 > split1:
               count+=1

    return count/n

print(sim_triangle_beta())
            
