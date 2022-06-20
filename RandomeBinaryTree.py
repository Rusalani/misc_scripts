class Node:
    def __init__(self, val:int=0, left=None, right=None):
        assert left is None or isinstance(left, Node)
        assert right is None or isinstance(right, Node)
        self.val = val
        self.left = left
        self.right = right
        
def get_tree_list(p):
    '''
    '''
    assert isinstance(p,list)

    root = None
    l=[]
    l.extend(range(0,len(p)))
    for x in p:
        assert isinstance(p[x], int)
        current = root
        last = None
        while current != None:
            last = current
            if current.val > x:
                current = current.left
            elif current.val < x:
                current = current.right
            else:
                assert False==True

        if last == None:
            root = Node(x)
        elif last.val > x:
            last.left = Node(x)
        else:
            last.right = Node(x)

    for i in range(0,len(l)):
        current =root
        last=current
        while current.val != l[i]:
            if l[i] > current.val:
                last = current
                current = current.right
            else:
                last = current
                current = current.left
        l[i] = last.val
    return l
        



t= [8,5,1,10,0,4,2,3,7,9,6]
print(get_tree_list(t))
