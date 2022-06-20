import itertools
def get_power_of3(x):
    '''
    returns list which -1,0,1 to idicate what to mutiple the list by to get input
    '''
    assert isinstance(x,int)
    assert 1 <= x <= 40
    ans=[]
    list3 = [1,3,9,27]
    if x >= 14:
        x=x-27
        ans.append(1)
    else:
        ans.append(0)
    if x >= 5:
        x=x-9
        ans.append(1)
    elif x <= -5:
        x=x+9
        ans.append(-1)
    else:
        ans.append(0)
    if x >= 2:
        x=x-3
        ans.append(1)
    elif x <= -2:
        x=x+3
        ans.append(-1)
    else:
        ans.append(0)
    if x == 1:
        x=x-1
        ans.append(1)
    elif x ==-1:
        x=x+1
        ans.append(-1)
    
    else:
        ans.append(0)
    
        
    ans.reverse()
   
    
    return ans



