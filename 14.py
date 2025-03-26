import re
A = [list(map(int,re.findall(r'\d+',_))) for _ in open(0).read().splitlines()]
inv = [_ for _ in list(zip(*A))]
res = 10**20
for a in A: res = min(sum(a),res)
for a in inv: res = min(sum(a),res)
print('part 1/',res)

import heapq
def dij(p3=False) -> int:
    R,C = len(A),len(A[0])
    D = ((1,0),(0,1),(-1,0),(0,-1)) if not p3 else((1,0),(0,1))#,(-1,0),(0,-1))
    dp = [[10**20] * C for _ in range(R)]
    dp[0][0] = A[0][0]
    Q = []
    heapq.heappush(Q,(A[0][0],0,0))
    while Q:
        cost, r, c = heapq.heappop(Q)
        for dr,dc in D:
            rr, cc = r + dr, c + dc
            if -1<rr<R and -1<cc<C and dp[rr][cc] > dp[r][c] + A[rr][cc]:
                dp[rr][cc] = dp[r][c] + A[rr][cc]
                heapq.heappush(Q,(A[rr][cc],rr,cc))
    return dp[R-1][C-1] if p3 else dp[14][14]
print('part 2/',dij())
print('part 3/',dij(42))
