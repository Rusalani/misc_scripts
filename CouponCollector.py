#import networkx as nx
#import matplotlib.pyplot as plt


import pandas as pd
import numpy as np
import math
from scipy import stats
import networkx as nx
import itertools

def sim_avg_coupons(probs,ntrials):
    '''

    simulate collecting coupons
    '''
    assert isinstance(probs,np.ndarray)
    assert isinstance(ntrials,int)
    assert ntrials>0
    count = 0
    numCou = np.arange(len(probs))
    for i in range(ntrials):
        collected = set()
        count2=0
        while len(collected) != len(set(numCou)):
            c = np.random.choice(numCou, p=probs)
            collected.add(c)
            count2+=1
        count+=count2

    return count / ntrials


#probs = np.array([0.07692308, 0.23076923, 0.30769231, 0.38461538])

#print(sim_avg_coupons(probs,10))

def get_3coupon_MarkovMatrix(probs):
    '''

        simulate collecting coupons
    '''
    assert isinstance(probs, np.ndarray)
    assert len(probs)==3
    s = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

    markov = np.zeros((len(s),len(s)))

    markov[0][1] = probs[0]
    markov[0][2]=probs[1]
    markov[0][3]=probs[2]
    markov[1][1] = probs[0]
    markov[1][4]=probs[1]
    markov[1][5]=probs[2]
    markov[2][2]=probs[1]
    markov[2][4] = probs[0]
    markov[2][6] = probs[2]
    markov[3][3] = probs[2]
    markov[3][5] = probs[0]
    markov[3][6] = probs[1]

    markov[4][4] = probs[0]+probs[1]
    markov[4][7]=probs[2]

    markov[5][5] = probs[0] + probs[2]
    markov[5][7] = probs[1]

    markov[6][6] = probs[2] + probs[1]
    markov[6][7] = probs[0]
    markov[7][7]=1
    return markov


def getprob(probs,one,two):
    p = 0
    three = set(two) - set(one)
    if len(three)==0:
        for i in one:
            p+= probs[i-1]
    else:
        return probs[list(three)[0]-1]
    return p

#probs = np.array([.1,.2,.3,.2,.2])


def get_coupon_Markov_graph(probs):
    '''

    :param probs:
    :return:
    '''
    assert isinstance(probs, np.ndarray)
    G = nx.DiGraph()
    coupons = list(range(len(probs)))
    s=[]
    for i in range(len(probs)+1):
        s.append(list(itertools.combinations(coupons, r=i)))

    for i in s:
        G.add_nodes_from(i)

    for i in s:
        for j in i :
            if len(j)==len(probs):
                G.add_edge(j, j)
                G.add_weighted_edges_from([(j, j, 1)])
            elif not (len(j)==0):
                G.add_edge(j,j)
                p=getprob(probs,j,j)
                G.add_weighted_edges_from([(j,j,p)])


    for i in range(len(probs)):
        for s1 in s[i]:
            for s2 in s[i + 1]:
                #print(s1)
                #print(s2)
                if set(s1).issubset(set(s2)):
                    G.add_edge(s1, s2)
                    p = getprob(probs, s1, s2)
                    G.add_weighted_edges_from([(s1, s2, p)])

    #nx.draw(G, with_labels = True)
    #import matplotlib.pyplot as plt
    #plt.show()
    #for u, v, w in G.edges(data=True):
    #    print(u, v, w['weight'])

    return G

#get_coupon_Markov_graph(probs)

def sim_nxgraph_coupon(probs,nsteps):
    '''

    :param probs:
    :param nsteps:
    :return:
    '''
    assert isinstance(probs, np.ndarray)
    G = get_coupon_Markov_graph(probs)
    masterList = []
    head = ()
    masterList.append(head)
    for j in range(nsteps):
        t = G.edges(head,data=True)
        dest=[]
        p=[]
        for i in t:
            dest.append(i[1])
            p.append(i[2]['weight'])
        index = np.random.choice(len(dest),1,p=p)
        choice = dest[index[0]]
        masterList.append(choice)
        head=choice

    return masterList
#probs = np.array([1/2,1/3,1/6])
'''
probs= np.array([0.07692307692307693,
  0.23076923076923078,
  0.3076923076923077,
  0.38461538461538464])

print(sim_nxgraph_coupon(probs,10))
'''


def get_coupon_MarkovMatrix(probs):
    '''

        :param probs:
        :param nsteps:
        :return:
    '''
    assert isinstance(probs, np.ndarray)
    G = get_coupon_Markov_graph(probs)
    coupons = list(range(len(probs)))
    s=[]
    for i in range(len(probs)+1):
        s.append(list(itertools.combinations(coupons, r=i)))

    flat_list = list(itertools.chain(*s))

    markov = np.zeros((len(flat_list),len(flat_list)))
    nodes = list(G.nodes)
    for n in nodes:
        t = G.edges(n,data=True)
        for i in t:
            x = flat_list.index(n)
            y = flat_list.index(i[1])
            markov[x][y] = i[2]['weight']
    return markov


probs = np.array([1/3,1/3,1/3])
#print(get_coupon_MarkovMatrix(probs))

def get_mean_boxes(probs):
    '''

            :param probs:
            :param nsteps:
            :return:
    '''
    assert isinstance(probs, np.ndarray)
    coupons = list(range(len(probs)))
    #s=[]
    totalsum=0
    for i in range(1,len(probs)+1):
        s = (list(itertools.combinations(probs, r=i)))
        tempsum=0
        for j in s:
            tempsum += 1/sum(j)
        totalsum += ((-1)**(i+1)) * tempsum
    return totalsum



#get_mean_boxes(probs)