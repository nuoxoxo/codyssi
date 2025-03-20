lines = open(0).read().splitlines()
nums = list(map(int,lines[:-1]))
ops = lines[-1]
assert len(nums) == len(ops) + 1

p1 = nums[0]
for i,n in enumerate(nums[1:]):
    if ops[i] == '+': p1 += n
    else: p1 -= n
print('part 1:', p1)

ops = ops[::-1]
p2 = nums[0]
for i,n in enumerate(nums[1:]):
    p2 = p2 + n if ops[i] == '+' else p2 - n
print('part 2:', p2)

p3 = nums[0]*10 + nums[1]
for i in range(2,len(nums),2):
    curr = nums[i]*10 + nums[i+1]
    p3 = p3 + curr if ops[i//2-1] == '+' else p3 - curr
print('part 3:', p3)
