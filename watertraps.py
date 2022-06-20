


def get_trapped_water(seq):
    '''

    :param m:
    :param n:
    :param blocks:
    :return:
    '''

    assert isinstance(seq, list)
    vol=0
    for x in range(1,len(seq)):
        assert isinstance(x,int)
        assert x >= 0
        left = seq[x]
        for y in range(x):
            left = max(left,seq[y])
        right = seq[x]
        for y in range(x+1,len(seq)):
            right = max(right,seq[y])
        vol +=min(left,right) - seq[x]



    return vol


seq = [3, 0, 1, 3, 0, 5]
#get_trapped_water(seq)






