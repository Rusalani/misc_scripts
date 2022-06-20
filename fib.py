def fibonacci(n):
    '''
    '''
    assert isinstance(n,int)
    assert n >0
    l=[]
    count =0
    while n > count:
        if len(l) <2:
            l.append(1)
            count=count+1
            yield l[count-1]
        else:
            count=count+1
            l.append(l[count-2] + l[count-3])
            yield l[count-1]


            
            
#t = fibonacci(100)
#for i in t:
#    print(i)
