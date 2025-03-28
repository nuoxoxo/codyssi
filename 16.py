A,M,DOWN = open(0).read().split('\n\n')
G = [list(map(int,_.split(' '))) for _ in A.splitlines()]
R,C = len(G),len(G[0])

def go(cmd,g):
    assert cmd
    ins = cmd.split()
    if 'SHIFT' in ins:
        rc,ofs = int(ins[2])-1,int(ins[4])
        if 'ROW' in ins:
            temp = [None] * C
            for c,n in enumerate(g[rc]):
                pos = (c + ofs) % C
                temp[pos] = n
            g[rc] = temp
        elif 'COL' in ins:
            temp = [g[r][rc] for r in range(R)]
            for r in range(R):
                pos = (r + ofs) % R
                temp[pos] = g[r][rc]
            for r,n in enumerate(temp): g[r][rc] = n
    elif 'ALL' not in ins:
        t,rc = int(ins[1]),int(ins[3])-1
        if 'MULTIPLY' in ins:
            if 'ROW' in ins:
                for c in range(C): g[rc][c] *= t
            elif 'COL' in ins:
                for r in range(R): g[r][rc] *= t
        elif 'ADD' in ins:
            if 'ROW' in ins:
                for c in range(C): g[rc][c] += t
            elif 'COL' in ins:
                for r in range(R): g[r][rc] += t
        elif 'SUB' in ins:
            if 'ROW' in ins:
                for c in range(C): g[rc][c] -= t
            elif 'COL' in ins:
                for r in range(R): g[r][rc] -= t
    elif 'ALL' in ins:
        t = int(ins[1])
        if 'MULTIPLY' in ins:
            for r in range(R):
                for c in range(C): g[r][c] *= t
        elif 'ADD' in ins:
            for r in range(R):
                for c in range(C): g[r][c] += t
        elif 'SUB' in ins:
            for r in range(R):
                for c in range(C): g[r][c] -= t
    for r in range(R):
        for c in range(C):
            g[r][c] = (g[r][c] + 1073741824) % 1073741824
    return g

def p3():
    g = [_[:] for _ in G]
    ACT, B = DOWN.splitlines(), M.splitlines()
    memo = ACT[:]
    while B:
        if not ACT:
            ACT = memo[:]
        line = ACT.pop(0)
        if line == 'TAKE':
            cmd = B.pop(0)
            line = ACT.pop(0)
            if line == 'CYCLE': B.append(cmd)
            elif line == 'ACT': g = go(cmd,g)
    res = max(max([sum(_) for _ in g]), max([sum(_) for _ in zip(*g)]))
    assert res in [19022,19367666299]
    return res

def p2():
    g = [_[:] for _ in G]
    ACT, B = DOWN.splitlines(), M.splitlines()
    while ACT:
        line = ACT.pop(0)
        if line == 'TAKE': cmd = B.pop(0)
        if line == 'CYCLE': B.append(line)
        if line == 'ACT': g = go(cmd,g)
    res = max(max([sum(_) for _ in g]), max([sum(_) for _ in zip(*g)]))
    assert res in [11496,386210424]
    return res

def p1():
    g = [_[:] for _ in G]
    for line in M.splitlines(): g = go(line,g)
    rmax,cmax = max([sum(_) for _ in g]), max([sum(_) for _ in zip(*g)])
    assert max(rmax,cmax) in [18938,20787739575]
    return max(rmax,cmax)

print('part 1/',p1())
print('part 2/',p2())
print('part 3/',p3())
