lines = open(0).read().splitlines()

def f(s:str) -> int:
    return sum([ord(_) - ord('A') + 1 for _ in s])

def ff(s:str) -> int:
    N = len(s) // 10
    return f(s[:N]) + sum([int(_) for _ in str(int(len(s[N:len(s)-N])))]) + f(s[len(s)-N:])

def fff(s:str) -> int:
    ss = ''
    count = 0
    prev = None
    for c in s:
        if not prev:
            prev = c
            count = 1
        else:
            if prev == c:
                count += 1
            else:
                ss += str(count) + prev
                count = 1
                prev = c
    ss += str(count) + prev
    res = 0
    for c in ss:
        if c.isdigit():
            res += int(c)
        else:
            res += ord(c) - ord('A') + 1
    return res
        
p1,p2,p3 = 0,0,0
for line in lines:
    p1 += f(line)
    p2 += ff(line)
    p3 += fff(line)
print('part 1:',p1)
print('part 2:',p2)
print('part 3:',p3)
