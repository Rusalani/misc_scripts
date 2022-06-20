import random
def sim_triangle(n=100):
    '''
    '''
    assert isinstance(n,int)
    assert n>=1
    count =0
    for x in range(n):
        s1 = random.uniform(0, 1)
        s2 = random.uniform(0, 1)
        split1 = min(s1,s2)
        split2 = max(s1,s2) - split1
        split3 = 1- (split2+split1)
        #print(split1)
        #print(split2)
        #print(split3)
        #print(split1+split2+split3)
        
        if split1+split2 > split3 and split1+split3 > split2 and split2+split3 > split1:
               count+=1

    return count/n

#print(sim_triangle())
            
