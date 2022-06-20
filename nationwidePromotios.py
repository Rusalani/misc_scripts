#import networkx as nx
#import matplotlib.pyplot as plt


import pandas as pd
from scipy import stats as sp
def compute_p_value(data):
    '''

    :param x list of ints 1-9
    :return: probability that keypad gestures ends in digit
    '''
    p=1
    assert isinstance(data,pd.DataFrame)
    for i in range(3):
        t=list(data.iloc[:,i])
        #print(t)
        p=p*sp.multinomial.pmf(t,sum(t),[.25,.25,.25,.25])

    return p






'''
dict={'shirt':[7,10,5,32],'socks':[24,21,24,5],'pants':[19,19,21,13]}
df = pd.DataFrame(dict)
print(compute_p_value(df) )
'''
