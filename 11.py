a,b,c = open(0).read().strip().split('\n\n')
A = list(map(int,a.split()))
b = [list(map(int,_.split('-'))) for _ in b.split()]
c = int(c)

a = A[:]
for l,r in b:
    l,r=l-1,r-1
    assert l<len(a) and r<len(a)
    a[l],a[r]=a[r],a[l]
print('part 1/',a[c-1])

a = A[:]
for i,(l,m) in enumerate(b):
    if i == len(b)-1:
        r = b[0][0]-1
    else:
        r = b[i+1][0]-1
    l,m=l-1,m-1
    a[m],a[r],a[l]=a[l],a[m],a[r]
print('part 2/',a[c-1])

a = A
for pair in b:
    l,r = sorted(pair)
    l,r = l-1,r-1
    L,R = r-l,len(a)-r
    for i in range(min(L,R)):
        a[l+i],a[r+i]=a[r+i],a[l+i]
print('part 3/',a[c-1])


