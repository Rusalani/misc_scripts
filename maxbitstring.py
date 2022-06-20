import numpy as np


def findProb(seq,p):
    '''

    :param seq:
    :param p:
    :return: probability of generating sequence based on dictionary
    '''
    prob = 0
    if len(seq) == 0:
        return 1

    test=[]
    for i in p.keys():
        if seq.startswith(i):
            #print(i)
            test.append(seq[len(i):])
    if len(test) == 0:
        return 0
    test2=dict()

    for i in p.keys():
        if seq.startswith(i):
            # print(i)
            test2[i] =(seq[len(i):])

    for i in range(len(test)):
        prob += p[list(test2.keys())[i]] * findProb(test[i], p)

    return prob
def get_ML_seq(seq,plist):
    '''

    :param seq:
    :param plist:
    :return: the most likly plist to generate seq
    '''
    assert isinstance(plist,list)
    assert isinstance(seq,str)

    for i in seq:
        assert i =='0' or i=='1'
    for p in plist:
        assert isinstance(p,dict)
        assert np.isclose(sum(p.values()),1)
        for prob in p.values():
            assert 0 < prob <= 1
        for i in p.keys():
            assert isinstance(i, str)
            for j in i:
                assert j == '0' or j == '1'
    choice = None
    choiceChance=0
    for p in range(len(plist)):

        prob2 = findProb(seq,plist[p])
        if prob2 >  choiceChance:
            choice=plist[p]
            choiceChance=prob2


    if choice is None:
        assert False
    #print(choiceChance)
    return choice



'''
p1 = {'00':1/2, '01':1/4, '10':1/4}
p2 = {'0':1/3, '01':1/3, '10':1/3}
p3 = {'00':1/8, '01':1/4, '0':3/8,'1010':2/8}
plist = [p1,p2,p3]
seq = '10101010100'
print(get_ML_seq(seq,plist))
print(pow(1/3,4))
'''
