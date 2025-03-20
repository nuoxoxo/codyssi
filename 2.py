lines = [True if s=='TRUE' else False for s in open(0).read().splitlines()]
print('part 1:', sum([i + 1 for i,v in enumerate(lines) if v]))

A, temp = [], []
for i in range(len(lines)):
    temp.append(lines[i])
    if (i+1) % 4 == 0:
        A.append(temp)
        temp = []
p2 = 0
for a in A:
    p2 += (a[0] & a[1]) + (a[2] | a[3])
print('part 2:', p2)

p3 = 0
while 1:
    p3 += sum(lines)
    N = len(lines)
    if N == 2:
        break
    temp = []
    i = 0
    while i < N:
        temp.extend((lines[i] & lines[1+i],lines[2+i] | lines[3+i]))
        i += 4
    lines = temp
print('part 3:', p3)
