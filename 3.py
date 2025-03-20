lines = [[l,int(r)] for line in open(0).read().splitlines() for l,r in [line.split()]]
print('part 1:', sum([_[1] for _ in lines]))

p2 = sum([int(_[0],_[1]) for _ in lines])
print('part 2:', p2)

p3 = ''
base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#'
while p2:
    r = p2 % 65
    p3 = base[r] + p3 
    p2 //= 65
print('part 3:', p3)
