import random
#import numpy as np
def multinomial_sample(n, p, k=1):
    '''
    Return samples from a multinomial distribution.

    n:= number of trials
    p:= list of probabilities
    k:= number of desired samples
    '''

    assert isinstance(n,int)
    assert isinstance(p, list)
    assert isinstance(k, int)
    assert n>0 and k >0
    sum=0
    masterList = []
    cleanList = []
    cdf=[]
    for i in p:
        assert isinstance(i,float) or i==0 or i==1
        sum+=i
        cleanList.append(0)
        cdf.append(sum)
    assert(round(sum,5)==1)


    for j in range(k):
        localList=cleanList.copy()
        for i in range(n):
            r = random.uniform(0,1)
            #print(r)
            count=0
            for y in range(len(cdf)):
                if r < cdf[y]:
                    count=y
                    break
            localList[count] +=1
        masterList.append(localList)



    return masterList

temp = multinomial_sample(10,[0,.5,.5],k=10)
#print(temp)
'''
sum1 = 0
sum2=0
sum3=0
for x in temp:
    sum1+= x[0]
    sum2+=x[1]
    sum3+=x[2]

print(str(sum1)+' '+str(sum2)+' '+str(sum3))
'''