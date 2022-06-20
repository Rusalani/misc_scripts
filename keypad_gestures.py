#import networkx as nx
#import matplotlib.pyplot as plt
def getAllpath(x,masterList):
    i = x[-1]
    y=[]
    if i==1:
        y=[2,4,5]
        for z in y:
            if z not in x:
                x.append(z)
                masterList.append(x.copy())
                getAllpath(x, masterList)
                x.pop()
    if i==2:
        y = [1, 4, 3,5,6]
        for z in y:
            if z not in x:
                x.append(z)
                masterList.append(x.copy())
                getAllpath(x, masterList)
                x.pop()
    if i==3:
        y = [2,5,6]
        for z in y:
            if z not in x:
                x.append(z)
                masterList.append(x.copy())
                getAllpath(x, masterList)
                x.pop()
    if i==4:
        y = [1, 2,5,7,8]
        for z in y:
            if z not in x:
                x.append(z)
                masterList.append(x.copy())
                getAllpath(x, masterList)
                x.pop()
    if i==5:
        y = [1,2,3,4,6,7,8,9]
        for z in y:
            if z not in x:
                x.append(z)
                masterList.append(x.copy())
                getAllpath(x, masterList)
                x.pop()
    if i==6:
        y = [2,3,5,8,9]
        for z in y:
            if z not in x:
                x.append(z)
                masterList.append(x.copy())
                getAllpath(x, masterList)
                x.pop()
    if i==7:
        y = [4,5,8]
        for z in y:
            if z not in x:
                x.append(z)
                masterList.append(x.copy())
                getAllpath(x, masterList)
                x.pop()
    if i==8:
        y = [4,5,6,7,9]
        for z in y:
            if z not in x:
                x.append(z)
                masterList.append(x.copy())
                getAllpath(x, masterList)
                x.pop()
    if i==9:
        y = [5,6,8]
        for z in y:
            if z not in x:
                x.append(z)
                masterList.append(x.copy())
                getAllpath(x, masterList)
                x.pop()

    return  masterList



def get_estimated_completion_prob(x):
    '''

    :param x list of ints 1-9
    :return: probability that keypad gestures ends in digit
    '''
    assert isinstance(x,list)
    assert len(x)==len(list(set(x)))
    assert len(x)!=0
    for i in x:
        assert isinstance(i,int)
        assert 0<i<10

    #assert x in getAllpath([x[0]],[])

    ans= {}
    master=getAllpath(x,[])
    for i in range(1,10):
        if i not in x:
            count=0
            for path in master:
                if path[-1]==i:
                    count+=1
            if count!=0:
                ans.update({i:count/len(master)})
    return ans






'''
x = [1,2,5,8]
#x=[1]
print(get_estimated_completion_prob(x) )
'''