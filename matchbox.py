import numpy as np



def gen_transition_matrix(init_state=(2,2),pL=0.5):
    '''

    :param init_state:
    :param pL:
    :return:
    '''

    states = {}
    c=-1
    for i in range(init_state[0]+1):
        for j in range(init_state[1]+1):
            states[(i,j)] = c
            c+=1
    states.pop((0,0))
    masterArray = np.zeros((len(states),len(states)))

    for i in range(init_state[0]+1):
        for j in range(init_state[1]+1):
            if i==0 and j==0:
                t=0
            elif i==0 or j==0:
                masterArray[states[(i,j)]][states[(i,j)]]=1
            else:
                masterArray[states[(i, j)]][states[(i-1, j)]] = pL
                masterArray[states[(i, j)]][states[(i, j-1)]] = 1 - pL

    return masterArray,states

#print(gen_transition_matrix(pL='time'))

def sim_chain(init_state=(2,2),pL=1/2):
    '''

    :param init_state:
    :param pL:
    :return:
    '''
    masterArray,states = gen_transition_matrix(init_state, pL)

    key_list = list(states.keys())
    val_list = list(states.values())
    l = list(range(len(states)))
    next = init_state
    while next[0]!=0 and next[1]!=0:
        index = states[next]
        next = np.random.choice(l,p=masterArray[index])
        next = key_list[val_list.index(next)]
        yield next
        #print('check')

#print(list(sim_chain()))
#from functools import lru_cache
def get_Smk(m,n,k):
    '''

    :param m:
    :param n:
    :param k:
    :return:
    '''
    if (n==0 and k==m) or(m==0 and k==n):
        return 1
    if (n==0) or(m==0):
        return 0
    return .5*get_Smk(m-1,n,k) + .5*get_Smk(m,n-1,k)

#print([get_Smk(3,3,i) for i in range(1,4)])
def get_Smn(m,n,i,j,pL=0.5):
    '''

    :param m:
    :param n:
    :param i:
    :param j:
    :param pL:
    :return:
    '''
    assert isinstance(pL,float or int) and 0<= pL <=1
    assert isinstance(m,int) and m >=0
    assert isinstance(n, int)and n >=0
    assert isinstance(i, int)and i >=0
    assert isinstance(j, int)and j >=0

    if (n==0 and i==m and j==0) or(m==0 and i==0 and j==n):
        return 1
    if (n==0) or(m==0):
        return 0
    return pL*get_Smn(m-1,n,i,j,pL) + (1-pL)*get_Smn(m,n-1,i,j,pL)
print([get_Smn(8,8,0,i) for i in range(1,9)])