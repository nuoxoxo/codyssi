A = [_.split() for _ in open(0).read().splitlines()]
for a in A: a[1] = int(a[1])

B = {}
for i in range(10): B[str(i)] = i
cnt = 10
for o in range(ord('A'),ord('Z')+1):
    B[chr(o)] = cnt
    cnt += 1
for o in range(ord('a'),ord('z')+1):
    B[chr(o)] = cnt
    cnt += 1

B['!']=62
B['@']=63
B['#']=64
B['$']=65
B['%']=66
B['^']=67
rev = {v:k for k,v in B.items()}

def conv10(s,base):
    res = 0
    for c in s:
        res = res * base + B[c]
    return res

def conv68(n):
    res = ''
    while n > 0:
        rem = n % 68
        res = rev[rem] + res
        n //= 68
    return res

res = 0
S = 0
for l,r in A:
    tmp = conv10(l,r)
    res = max(res,tmp)
    S += tmp
print('part 1/',res)
print('part 2/',conv68(S),'sum/',S)

"""
we want to find a base 'P' which converts SUM to this form
    b**3 b**2 b**1 b**0

we know that the largest 4-digit num in base P is 
    P ** 4 - 1

deduction/ we look for a P such that
    P ** 4 - 1 >= SUM   bc. SUM must be below P**4-1
    (P is the first number that send P**4-1 above SUM)

hence formula/
    P >= (N+1) ** .25
"""
p3 = (S + 1) ** .25
print('part 3/',int(p3),'- raw/',p3)
