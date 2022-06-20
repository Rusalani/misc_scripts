import pandas as pd
import numpy as np
def multinomial_cond_exp(n,p,cond='x2') :
    '''

    :param n:
    :param p:
    :param cond:
    :return:
    '''
    assert isinstance(p,list or np.ndarray)
    assert isinstance(n,int)
    assert n >=0
    assert isinstance(cond,str)
    for i in p:
        assert isinstance(i,float)
        assert 0<=i<=1
    assert sum(p)==1
    col = []
    for i in range(len(p)):
        col.append('x'+str(i))
    cond = cond.replace('x','')
    if cond.find('+'):
        cond=cond.split('+')
        for i in cond:
            assert int(i)
            assert 0<=int(i)<=len(p)-1



    index = [int(i) for i in cond]
    summ=0
    for i in  range(len(p)):
        if i in index:
            summ+=p[i]
    valIndex = summ

    summ = sum(p) - valIndex
    newp = []
    for i in range(len(p)):
        newp.append(p[i]/summ)

    df=pd.DataFrame(columns=col)
    df.index.name='cond'
    for i in range(n+1):
        insert = []
        for y in range(len(p)):
            if y not in index:
                insert.append(newp[y] * (n-i))
            else:

                insert.append(i*(p[y]/valIndex))
        df.loc[len(df.index)] = insert
    return df


'''
p=[1/4,1/3,1-1/4-1/3]
n=5
print(multinomial_cond_exp(n,p,'x3+x1'))
'''