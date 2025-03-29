from collections import defaultdict
ADJ = defaultdict(list)
for _ in open(0).read().splitlines():
    l,_,r,_,v = _.split()
    ADJ[l].append((r,int(v)))

def p12(begin,p2=False):
    Q = [(begin, 0)]
    SEEN = set([begin])
    D = defaultdict(int)
    while Q:
        node,dist = Q.pop(0)
        D[node] = dist
        for adj,cost in ADJ[node]:
            if adj not in SEEN:
                SEEN.add(adj)
                if not p2:
                    cost = 1
                Q.append((adj, dist + cost))
    res = 1
    for n in sorted(D.values())[-3:]:
        res *= n
    return res
print('part 1/',p12('STT'))
print('part 2/',p12('STT',True))

def p3():
    D = defaultdict(int)
    for begin in list(ADJ.keys()):
        Q = [(begin, 0,[begin])]
        while Q:
            node,dist,path = Q.pop(0)
            if len(path) > 1 and path[-1] == path[0]:
                D[begin] = max(D[begin],dist)
            for adj,cost in ADJ[node]:
                if adj not in path or (adj == path[0] and adj not in path[1:]):
                    Q.append((adj, dist + cost, path + [adj]))
    return sorted(D.values())[-1]
print('part 3/',p3())
