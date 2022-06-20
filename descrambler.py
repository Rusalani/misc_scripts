from itertools import *
def descrambler2(s,list2,l,i,dic):
    tempstr=s

    def helper(x):
        for char in x:
            if x.count(char) > tempstr.count(char):
                return False
        return True
    if (len(tempstr) == 0):
        yield ' '.join(list2)
    else:
        master=list(filter(helper,dic[l[i]] ))

        for x in master:
            tempstr = subtract(tempstr,x)
            list2.append(x)
            i+=1
            yield from descrambler2(tempstr,list2,l,i,dic)
            i-=1
            tempstr = tempstr+x
            list2.remove(x)

def descrambler(s,l):
    '''
    descrambles a string into words baseed on google 10000 no swears
    '''
    assert isinstance(s, str)
    assert isinstance(l, tuple)
    assert s.isalpha()
    sum=0
    for i in list(l):
        assert (isinstance(i, int))
        assert i > 0
        sum+=i
    assert sum== len(s)

    dic = {}
    for x in list(l):
        dic[x]=[]

    with open("/tmp/google-10000-english-no-swears.txt") as f:
        lines = f.readlines()
        for line in lines:
            for x in list(l):
                if x==len(line.strip()):
                    dic[x].append(line.strip())
                    break


    return descrambler2(s,[],l,0,dic)
    
def subtract(a,b):
    for x in b:
        a=a.replace(x,'',1)
    return a
            
#print(list(descrambler('trleeohelh',(5,5))))
#print(list(descrambler('choeounokeoitg',(3,5,6))))
#print(list(descrambler('qeodwnsciseuesincereins',(4,7,12))))
