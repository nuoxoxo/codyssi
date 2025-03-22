line = open(0).read().strip()
a = [_ for _ in line if _.isalpha()]#))
print('part 1/',len(a))

def f(c) -> int:
    return ord(c)-ord('a')+1 if c.islower() else ord(c)-ord('A')+1+26

p2 = sum([f(_) for _ in a])
print('part 2/',p2)

p3 = p2
A = list(line)
for i,c in enumerate(A):
    if not c.isalpha() and i>0:
        if A[i-1].isalpha():
            fc = f(A[i-1])
        elif A[i-1].isnumeric():
            fc = int(A[i-1])
        else:
            assert False
        fc = (fc*2-5-1)%52+1
        A[i] = str(fc)
        p3 += fc
print('part 3/',p3)
