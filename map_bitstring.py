
def map_bitstring (x):
    '''
    '''
    assert isinstance(x,list)
    dic={}
    for y in x:
        c=0
        assert isinstance(y,str)
        for z in y:
            assert z=='1' or z=='0'
            if z=='1':
                c=c+1
            else:
                c=c-1
        if c>=0:
            dic[y]=1
        else:
            dic[y]=0
                
    return dic
    



x= ['100', '100', '110', '0102', '111', '000', '110', '010', '011', '000']
            
#print(map_bitstring(x))
