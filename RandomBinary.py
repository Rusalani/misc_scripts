#import networkx as nx
#import matplotlib.pyplot as plt


#import pandas as pd
#import numpy as np
#import math
#from scipy import stats
#import statsmodels.api as sm

#data = pd.read_csv('data.txt')

class Node:
    def __init__(self, val:int=0, left=None, right=None):
        assert isinstance(left,Node) or left is None
        assert isinstance(right,Node) or right is None
        self.val = val
        self.left = left
        self.right = right

def get_tree_list(p):
    '''

    :param p:
    :return:  list that represents the binary tree
    '''
    assert isinstance(p,list)
    assert all(isinstance(i, int) for i in p)
    assert len(p) == len(set(p))
    root = None
    l = []
    l.extend(range(0, len(p)))
    for x in p:
        assert isinstance(p[x], int)
        current = root
        last = None
        while current != None:
            last = current
            if current.val > x:
                current = current.left
            elif current.val < x:
                current = current.right
            else:
                assert False == True

        if last == None:
            root = Node(x)
        elif last.val > x:
            last.left = Node(x)
        else:
            last.right = Node(x)

    for i in range(0, len(l)):
        current = root
        last = current
        while current.val != l[i]:
            if l[i] > current.val:
                last = current
                current = current.right
            else:
                last = current
                current = current.left
        l[i] = last.val
    return l


#t= [8,5,1,10,0,4,2,3,7,9,6]
#print(get_tree_list(t))
