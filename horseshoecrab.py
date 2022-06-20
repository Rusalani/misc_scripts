#import networkx as nx
#import matplotlib.pyplot as plt


import pandas as pd
import numpy as np
import math
from scipy import stats
import statsmodels.api as sm
#data = pd.read_csv('data.txt')

def horseshoe1(data):
    '''

    :param data:
    :return:
    '''

    model = sm.GLM(data['y'], data['width'], family=sm.families.Poisson())
    res = model.fit().deviance
    return res
def horseshoe2(data):
    '''

    :param data:
    :return:
    '''
    model = sm.GLM(data['y'], data[['width','weight']], family=sm.families.Poisson())
    res = model.fit().deviance
    return res
def horseshoe3(data):
    '''
    :param data:
    :return:
    '''
    model = sm.GLM(data['y'], data[['width','weight']], family=sm.families.NegativeBinomial())
    res = model.fit().deviance
    return res

#print(horseshoe2(data))
#print(horseshoe3(data))