from collections import defaultdict,deque

ADJ = defaultdict(list)
for _ in open(0).read().splitlines():
    l,r = _.split(' <-> ')
    ADJ[l].append(r)
    ADJ[r].append(l)
print('part 1:', len(ADJ.keys()))

Q = deque([('STT',0)])
SEEN = set(['STT'])
p2 = 0
while Q:
    node,cost = Q.popleft()
    if cost < 4:
        p2 += 1
    if cost < 3:
        for adj in ADJ[node]:
            if adj not in SEEN:
                SEEN.add(adj)
                Q.append((adj, cost + 1))
print('part 2:', p2)

Q = deque([('STT',0)])
SEEN = set(['STT'])
p3 = defaultdict(int)
while Q:
    node,cost = Q.popleft()
    p3[node] = cost
    for adj in ADJ[node]:
        if adj not in SEEN:
            SEEN.add(adj)
            Q.append((adj, cost + 1))
print('part 3:', sum(p3.values()))

