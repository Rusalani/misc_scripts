import numpy as np
import random
def gen_rand_slash(m=6,n=6,direction='back'):
    '''
    generate random slash with min length

    :param m:
    :param n:
    :param direction:
    :return:
    '''
    assert isinstance(m,int)
    assert isinstance(n,int)
    assert m >=2
    assert n>=2
    assert direction == 'back' or direction == 'forward'
    table = np.zeros((m,n))

    i = random.randint(-m+1,m-1)
    while len(np.diag(table,i)) <=1:
        i = random.randint(-m + 2, m - 2)

    x = len(np.diag(table,i))

    i1 = random.randint(0, x-1)
    i2 = i1
    while i2 == i1:
        i2 = random.randint(0, x-1)

    if i2 < i1:
        swap = i2
        i2=i1
        i1=swap

    xi = 0
    yi=i
    if i <0:
        swap = xi
        xi=yi
        yi=swap
        xi=xi*-1

    for y in range(i1,i2+1):
        table[xi+y][yi+y] = 1



    if direction == 'forward':
        return np.flipud(table)

    return table

#for y in range(10):
#    print(gen_rand_slash(2,3))
