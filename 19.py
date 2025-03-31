A,B = [_.splitlines() for _ in open(0).read().split('\n\n')]

names, vals, pairs = [],[],[]
for a in A:
    name,val = a.split(' | ')
    names.append(name)
    vals.append(int(val))
    pairs.append( (name,int(val)) )

class treenode:
    def __init__(self, pair):
        name,val = pair
        self.name = name
        self.val = val
        self.L = None
        self.R = None
    def __repr__(self):
        return f'{self.name} - {self.val}'# - {self.L!=None} : {self.R!=None}'
    """@staticmethod
    def printer(begin):
        if not begin: return
        Q = [(begin,1)]
        while Q:
            node, curr = Q.pop(0)
            if node.L: Q.append((node.L, curr + 1))
            if node.R: Q.append((node.R, curr + 1))
    """
    def insert(root,node):
        assert node
        assert root
        if root.val > node.val:
            if not root.L:
                root.L = node
            else:
                root.L.insert(node)
        else:
            if not root.R:
                root.R = node
            else:
                root.R.insert(node)

import copy, collections

nodes = [treenode(pair) for pair in pairs]

def BST(arr):
    if not arr:
        return None
    root = arr.pop(0)
    for node in arr:
        root.insert(node)
    return root

def p3():
    root = BST(copy.deepcopy(nodes))
    tar = []
    for b in B:
        name,val = b.split(' | ')
        tar.append((name,int(val)))
    mini,maxi = sorted([_[1] for _ in tar])
    while root:
        if not root:
            break
        if root.val > maxi:
            root = root.L
        elif root.val < mini:
            root = root.R
        else:
            break
    print('part 3/',root)


def p2():
    root = BST(copy.deepcopy(nodes))
    s = [root.name]
    while root:
        if root.val > 500000:
            if not root.L:
                break
            s.append(root.L.name)
            root = root.L
        elif root.val < 500000:
            if not root.R:
                break
            s.append(root.R.name)
            root = root.R
        else:
            break
    res = '-'.join(s)
    assert res.startswith('PkQPEbW-') and res.endswith('-RQIBDKs')
    print('part 2/','\n'+'-'.join(s))

def p1():
    root = BST(copy.deepcopy(nodes))#[:])
    LVS = collections.defaultdict(list)
    Q = ([(root,1)])
    while Q:
        node,lv = Q.pop(0)
        LVS[lv].append(node.val)
        if node.L: Q.append( (node.L, lv+1) )
        if node.R: Q.append( (node.R, lv+1) )
    res = []
    for k,v in LVS.items():
        #print(k,v,sum(v))
        res.append(sum(v))
    print('part 1/',max(res) * len(LVS))

p1()
p2()
p3()



