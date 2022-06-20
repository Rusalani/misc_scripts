import random
def get_sample(nbits=3,prob=None,n=1):
    '''
    '''
    assert isinstance(nbits,int)
    assert isinstance(n,int)
    assert isinstance(prob,dict)
    assert nbits >=0
    assert n>=0
    summ=0
    for y in prob.keys():
        assert len(y) == nbits
        assert prob[y] >=0
        summ+=prob[y]
    assert(summ==1)
    
    l=[]
    for x in range(n):
        r = random.random()
        i=r
        
        for y in prob.keys():

            if prob[y] >= i:
                l.append(y)
                break
            else:
                i=i-prob[y]
                
    return l
    


p={'000': 0.125, 
 '001': 0.125, 
 '010': 0.125, 
 '011': 0.125, 
 '100': 0.125, 
 '101': 0.125, 
 '110': 0.125, 
 '111': 0.125} 
            
#print(get_sample(nbits=3,prob=p,n=4))
