#import networkx as nx
import matplotlib.pyplot as plt


import pandas as pd
import numpy as np
import math
from scipy import stats
from scipy.misc import derivative
from scipy.integrate import quad
from scipy.integrate import simps
def gen_length_samples(n):
    '''

    :param n:
    :return:
    '''
    l=np.zeros(n)
    x = np.random.uniform(0,1,n)
    pi = np.random.uniform(0,np.pi,n)
    pi_test = np.rad2deg(pi)
    #l= x / np.cos(pi)
    for i in range(n):
        if pi[i] >= np.pi/2 :

            test = 180 - pi_test[i]
            temp = np.cos(np.deg2rad(test))
            temp2 =  np.cos(np.pi - pi[i])
            if(x[i] / np.cos(np.pi - pi[i]) > 2**.5):
                l[i] = math.sqrt(1+x[i]**2)
            else:
                l[i] = x[i]/ np.cos( np.pi -pi[i])


        elif 0 <= 1/np.sin(pi[i]) <= 2**.5:
            l[i]=1/np.sin(pi[i])

        else:
            l[i] =(1-x[i])/ np.cos(pi[i])
    return l


#l=gen_length_samples(n=100)

#fig, axs = plt.subplots(1,1)
#axs.hist(l, bins=10)
#plt.show()
def conditional_prob_H1(X):
    '''

    :param X:
    :return:
    '''

    def func (x):
        if 0 <= X <= 1:
            return 2 / np.pi
        return 2 / np.pi * (np.pi / 2 - np.arcsin(1 / x) + np.arccos(1 / x) - math.sqrt(x ** 2 - 1) + 1)




    t=derivative(func, X, dx=1e-6)

    return t

def conditional_prob_H0(x):
    '''

    :param x:
    :return:
    '''
    return stats.norm.pdf(x,loc=0,scale=.1)

def false_alarm_probability(thresh):
    '''

    :param thresh:
    :return:
    '''
    t = quad(conditional_prob_H0,a=thresh,b=2**.5)
    return t[0]

#print(false_alarm_probability(.05))


def true_detection_probability(thresh):
    '''

    :param thresh:
    :return:
    '''


    def func (x):
        if 0 <= x <= 1:
            return 2 / np.pi
        if x <2**.5:
            return 2 / np.pi * (np.pi / 2 - np.arcsin(1 / x) + np.arccos(1 / x) - math.sqrt(x ** 2 - 1) + 1)

        return 0

    t = quad(func, a=thresh, b=2 ** .5,points=[1])
    return t[0]
#print(true_detection_probability(.05))
def get_auc():
    '''

    :return:
    '''
    t=np.linspace(0, 2**.5,100)
    x=[]
    y=[]
    for i in t:
        x.append(true_detection_probability(i))
        y.append(false_alarm_probability(i))

    plt.plot(y, x)
    plt.xlabel('false_alarm_probability')
    plt.ylabel('true_detection_probability')
    hold = simps(y, x)
    plt.show()

    curve = -simps(x,y) *2
    return curve

print(get_auc())