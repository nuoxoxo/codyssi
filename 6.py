raw = open(0).read().splitlines()
F,A = [int(_.split()[-1]) for _ in raw[:3]], sorted(list(map(int,raw[4:])))
N = len(A)
assert(N % 2 == 1)

def f(n) -> int:
    return n ** F[2] * F[1] + F[0]

print('part 1:', f(A[N//2]))
print('part 2:', f(sum([_ for _ in A if _ % 2 == 0])))

ok = 0
for a in A:
    if f(a) < 15000000000000:
        ok = max(ok,a)
print('part 3:', ok)
