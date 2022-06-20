
def recur(array,row,col):
    if row == len(array)-1 and col == len(array[0])-1:
        return 1
    right =0
    down =0
    if row!=len(array)-1 and array[row+1][col]!='#':
        right = recur(array,row+1,col)
    if col!=len(array[0])-1 and array[row][col+1]!='#':
        down = recur(array,row,col+1)
    return right+down

def count_paths(m,n,blocks):
    '''

    :param m:
    :param n:
    :param blocks:
    :return:
    '''
    assert isinstance(m,int)
    assert isinstance(n, int)
    assert m > 0 and n >0
    assert isinstance(blocks, list)
    array = [ ['.' for i in range(n)] for j in range(m)]
    for x in blocks:
        assert isinstance(x,tuple)
        assert 0<=x[0]<=m-1 and 0<=x[1]<=n-1
        assert not(x[0] ==0 and x[1]==0)
        assert not (x[0] ==m-1 and x[1]==n-1)
        array[x[0]][x[1]] = '#'

    count = recur(array,0,0)


    return count



#print(count_paths(3,4,[(0,3),(1,1)]))






