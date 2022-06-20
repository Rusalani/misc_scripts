#import networkx as nx
#import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import numpy as np
from scipy import integrate
import xarray as xr
from functools import reduce
import itertools
#df= pd.read_csv('muscledata.csv')


def get_assoc_tables(df: pd.DataFrame):
    '''

    :param df:
    :return:
    '''
    p = pd.crosstab([df['muscle tension'],df['muscle weight']],columns=[df['muscle type'],df['drug type']])
    temp = np.array(p)
    x = xr.DataArray(temp.reshape((2, 2, 2, 2)),
    coords = {'T': ['hi', 'lo'],
            'W': ['hi', 'lo'],
            'M': ['1', '2'],
            'D': ['1', '2']})
    sym = ['T','W','M','D']
    lis=list()
    for n in range(1,len(sym)):
        lis += list(itertools.combinations(sym,n))
    masterTable = pd.DataFrame(columns=['partial_assoc', 'marginal_assoc', 'dof'],
                               index=lis)
    for value in lis:
        tempvalue ="".join(list(value))
        if len(value)==1:
            seq =['T','W','M','D']
        elif len(value)==2:
            seq =['TW', 'TM', 'TD', 'WM','WD','MD']
        elif len(value)==3:
            seq=['TWM', 'TWD', 'WMD', 'TMD']

        seq2 = seq.copy()
        seq2.remove(tempvalue)
        partial =  model_deviance(seq2, x)-model_deviance(seq, x)
        if len(value) == 1:
            masterTable.at[value,'partial_assoc'] = partial
            masterTable.at[value,'dof'] = 1
        elif len(value) == 2:
            #m = x.sum(value)

            combo = list(itertools.combinations(value, 1))

            indep2 =model_deviance(combo, x)
            indep3 = model_deviance([''.join(value)], x)
            mar = indep2-indep3
            masterTable.at[value, 'partial_assoc'] = partial
            masterTable.at[value,'marginal_assoc'] = mar
            masterTable.at[value, 'dof'] = 1


        elif len(value) == 3:

            combo = list(itertools.combinations(value,2))

            indep2 = model_deviance(combo, x)
            indep3 = model_deviance([''.join(value)], x)
            mar = indep2 - indep3
            masterTable.at[value, 'partial_assoc'] = partial
            masterTable.at[value, 'marginal_assoc'] = mar
            masterTable.at[value, 'dof'] = 1

    return masterTable





def inverse(seq):
    master = set(['T','W','M','D'])
    inv = master - set(seq)
    return list(inv)

def model_deviance(seq,x,niter=6):
    '''
    :param seq: list of generating class codes
    :type seq: list
    :param x: data
    :type x: xr.DataArray
    :param niter: num of IPF iterations
    :type niter: int
    :returns: float deviance
    '''
    assert isinstance(seq,list)

    mui = x * 0 + 1
    for i in range(niter):
        for j in seq:
            inv = inverse(list(j))
            mui = x.sum([*inv]) / mui.sum([*inv]) * mui

    ans = float(2 * (x * np.log(x / mui)).sum())
    return ans



#print(get_assoc_tables(df))

#print(model_deviance(['MW','MT','T'],x))

