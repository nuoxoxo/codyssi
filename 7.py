import re
A = [list(map(int,re.findall(r'\d+',_))) for _ in open(0).read().splitlines()]
p1,p2,p3 = 0,0,0
comb = set()
count = 0
for a,b,c,d in A:
    assert a < b and c < d
    p1 += b-a+d-c+2
    S = set()
    for n in range(a,b+1): S.add(n)
    for n in range(c,d+1): S.add(n)
    p2 += len(S)
    comb |= S
    count += 1
    if count == 2:
        p3 = max(p3,len(comb))
        comb = S
        count = 1
print('part 1:',p1)
print('part 2:',p2)
print('part 3:',p3)
