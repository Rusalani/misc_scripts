def slide_window(x,width,increment):
    '''
    '''
    assert isinstance(x,list)
    assert isinstance(width,int)
    assert isinstance(increment,int)
    assert width > 0
    assert increment > 0
    masterlist = []
    templist = []
    count=0
    index=0
    while index < len(x):
        if count== width:
            masterlist.append(templist)
            templist=[]
            index=index-width + increment
            count=0
        templist.append(x[index])
        count=count+1
        index=index+1
    if count== width:
            masterlist.append(templist)
            templist=[]
            index=index-width + increment
            count=0
    return masterlist
            

            

