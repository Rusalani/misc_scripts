
import math
import random


def est_prob(n:int, m:int, niter:int=100)->float:
    '''

    :param n:
    :param m:
    :param niter:
    :return:
    '''

    assert n >=4
    assert m>=3
    assert n>m
    l=[]
    c=0
    for x in range(niter):

        l = random.choices(range(n),k=m)
        if len(l) == len(set(l)):
            c += 1
    return c/niter


def get_prob_shape(n: int, m: int, equilateral: bool = False) -> float:
    '''
    :param n: num sides in regular polygon (n>=4)
    :type n: int
    :param m: num vertices for inscribed polygon (m>=3)
    :type m: int
    '''
    assert n >= 4
    assert m >= 3
    assert n > m
    denom = pow(n,m)
    if equilateral:
        if n %m ==0:
            return int(n/m) * math.factorial(m) / denom
        else:
            return 0
    return math.factorial(n)/math.factorial((n-m))  /denom

18*6






#print(est_prob(10,9,10000))

#print(est_prob(5,4,10000))
#print(est_prob(6,5,10000))
#print(est_prob(10,3,10000))

#print(get_prob_shape(5,4))
#print(get_prob_shape(6,5))
#print(get_prob_shape(10,3))