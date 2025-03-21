A = [tuple(map(int,line[1:-1].split(','))) for line in open(0).read().splitlines()]
A = sorted([(abs(a)+abs(b),a,b) for a,b in A])
print('part 1/',A[-1][0]-A[0][0])

def coordist(a,b) -> int:
    if a >= 0 and b >= 0 or a <= 0 and b <= 0:
        return abs(a-b)
    return abs(a)+abs(b)

def d(n1,n2) -> int:
    (a,b),(c,d) = n1,n2
    return abs(coordist(a,c))+abs(coordist(b,d))

def findnext(closest,A):
    closest = closest[1:]
    res = 10**20
    node = None
    for curr in A:
        temp = d(closest,curr[1:])
        if res > temp:
            res,node = temp,curr[1:]
            node = curr[1:]
        elif res == temp:
            if node[0] > curr[1] or node[0] == curr[1] and node[1] > curr[2]:
                node = curr[1:]
    return (node,res)
node,dist = findnext(A[0],A[1:])
print('part 2/',dist)

p3 = 0
A = [(0,0,0)] + A
while len(A) > 1:
    nxt,dst = findnext(A[0],A[1:])
    p3 += dst
    temp = [(dst,nxt[0],nxt[1])]
    for a in A[1:]:
        if nxt != a[1:]:
            temp.append(a)
    A = temp
print('part 3/',p3)
    


