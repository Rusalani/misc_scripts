
#import itertools as it

def next_permutation(t:tuple):
    '''

    :param m:
    :param n:
    :param blocks:
    :return:
    '''

    temp = list(t)
    for x in temp:
        assert isinstance(x,int)



    i=len(temp)-1
    while i >0 and temp[i-1] >= temp[i]:
        i-=1

    j = len(temp)-1
    while temp[j] <= temp[i - 1]:
        j-=1
    if i<=0:
        j = len(temp)-1
    tempswap = temp[i-1]
    temp[i-1]=temp[j]
    temp[j]=tempswap

    j = len(temp)- 1
    while i < j :
        tempswap = temp[i]
        temp[i] = temp[j]
        temp[j] = tempswap
        i+=1
        j-=1


    return tuple(temp)











#print(next_permutation([-1,-2,-3,10]))
#print(list(it.permutations([-1,-2,-3,-3])))




