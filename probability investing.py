import numpy as np
import itertools
def est_pdf(p):
    '''

    :param p:
    :return: pdf of numbers of succees
    '''
    assert isinstance(p,list)
    for i in p:
        assert isinstance(i,float)
        assert 0<i<1
    k=[]
    chosen=[]
    for i in range(len(p)+1):
        prob=0
        per = list(itertools.combinations(p,i))
        for x in per:
            localProb=1
            seen=[]
            for y in p:
                ta = seen.count(y)
                te = x.count(y)
                if y not in x or (x.count(y)>0 and x.count(y)==seen.count(y)):

                    localProb=localProb*(1-y)
                else:

                    seen.append(y)

                    localProb=localProb*y
            prob+=localProb
        k.append(prob)

    summ=sum(k)
    return k

'''
p = [0.34537093, 0.75580255, 0.61383029, 0.06516869, 0.46175061, 0.57079639, 0.03297377, 0.88347158, 0.91001774,
         0.09064271]
p2=[.4,.4,.4]
print(est_pdf(p2))
'''