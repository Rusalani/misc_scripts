#import networkx as nx
#import matplotlib.pyplot as plt


from scipy import stats
import numpy as np
from scipy import integrate

def compute_cdf(d):
    '''

    :param x list of ints 1-9
    :return: probability that keypad gestures ends in digit
    '''
    assert isinstance(d,float)
    assert d >=0

    def func(x,y):
        if 0 <=x<=1 and 0<=y<=1:
            return 2* (1-x)*2*(1-y)
        return 0
    #d=math.sqrt(d)
    def bounds1():
        return [-pow(d,.5), pow(d,.5)]
    def bounds2(x):
        return [-pow(d-pow(x,2),.5), pow(d-pow(x,2),.5)]

    ans = integrate.nquad(func,[bounds2,bounds1])


    return ans[0]


def compute_test_pvalue(X) :
    '''

    :param X:
    :return:
    '''
    assert isinstance(X,np.ndarray)
    assert X.shape[1] ==2
    assert X.shape[0] % 2==0


    t=[]
    points=[]
    for row in X:
        if len(t)==0:
            t= row
        else:
            points.append(pow(t[0]-row[0],2) + pow(t[1]-row[1],2))
            t=[]
    cdf=[]
    for d in points:
        cdf.append(compute_cdf(d))

    finans = stats.kstest(points,cdf)

    return finans[1]





'''
print(compute_cdf(.125) )
t=[.5,.5,.25,.25,.3,.3,.1,.1]
t2=np.array(t).reshape((4,2))
print(compute_test_pvalue(t2))
'''