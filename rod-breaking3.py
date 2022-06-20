import random
import math
import scipy.integrate as integrate
import numpy as np
from scipy.stats import beta
def beta_obj(a,b):
    '''
    '''
    
    assert isinstance(a,int)
    assert isinstance(b,int)
    assert a >=1 and 20>=a
    assert b >=1 and 20>=b
    p=beta.pdf(0.5, a, b)
    p2=beta.pdf(1, a, b)
    tp=beta.cdf(.5,a,b)

    t=beta.expect(lambda  x: beta.cdf(.5,a,b),args=(a,b),lb=0,ub=.5)

    result = integrate.dblquad(lambda x,y:beta.pdf(x,a,b)*beta.pdf(y,a,b), .5, 1, lambda x: x-.5, lambda x: .5)
    temp = integrate.quad(lambda x: beta.pdf(x,a,b),0,.5)
    fin=t*2
    finn=result[0]*2



    return finn

#print(beta_obj(20,1))
            
