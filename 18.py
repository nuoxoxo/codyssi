lines = open(0).read().splitlines()
a = []
for l in lines:
    p = l.split()
    name,ql,cs,ma = p[1],int(p[5][:-1]),int(p[8][:-1]),int(p[-1])
    a.append((ql,cs,ma,name))
print('part 1/', sum(_[2] for _ in sorted(a,key=lambda x: (x[0], x[1]))[-5:]))

# p2 - knapsack
def knap(T) -> int:
    N = len(a)
    dp = [ [(0,0,[])]*(T+1) for _ in range(N+1) ] # []
    for r in range(1,N+1):
        ql,cs,ma,name = a[r-1]
        for c in range(T+1): # new cost to test
            dp[r][c] = dp[r-1][c]
            if cs <= c:
                qll,css,comb = dp[r-1][c - cs]
                qll += ql
                css += ma
                arr = comb + [name]
                if qll > dp[r][c][0]:
                    dp[r][c] = (qll,css,arr)
                elif qll == dp[r][c][0] and dp[r][c][1] > css:
                    dp[r][c] = (qll,css,arr)
    l,r,comb = dp[-1][-1]

    print('part 2/' if T == 30 else 'part 3/',f'{l*r} = {l} x {r}')
    print('','\n '.join(comb))

knap(30)
knap(300)
