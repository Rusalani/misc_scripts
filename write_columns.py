def write_columns(data,fname):
    '''
    '''
    assert isinstance(data,list)
    assert isinstance(data[0],int) or isinstance(data[0],float)
    with open(fname, 'w') as f:
        for x in data:
            t = '{:.2f}, {:.2f}, {:.2f}\n'.format(x,x*x,(x+x*x)/3)
            f.write(str(t))


            
            
#write_columns([10.0,.1],'temp.txt')
