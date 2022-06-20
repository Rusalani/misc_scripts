import random
def sim_ngon(n=3,ns=100000):
    '''
simulate breaking the unit length rod at n points uniformly at random and returning
the corresponding probability of using the so-generated fragments to create a valid polygon
    '''
    assert isinstance(n,int)
    assert n>=2
    assert isinstance(ns,int)
    assert ns>0
    count =0
    for x in range(ns):
        tempadd=1
        sides=[]
        legnths=[]
        for y in range(n):
            sides.append(random.uniform(0, 1))
        sides.sort()
        legnths.append(sides[0])
        for y  in range(1,n):
            legnths.append(sides[y] - sides[y-1])
        
        legnths.append(1-sum(legnths))
        
        
        for z in legnths:
            if sum(legnths) - z <= z:
                tempadd=0
                break
        count+=tempadd

    return count/ns

def prob_n_breaks(n=4):
    '''                                                                        
         compute the probability of forming a nonzero area polygon with `n` breaks.
    '''
    assert isinstance(n,int)
    assert n >=2
    return 1- (n+1)/(pow(2,n))
    
            
#print(sim_ngon(n=2))
#print(prob_n_breaks(1))
