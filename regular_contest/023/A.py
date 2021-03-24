import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))
S = [0] * (N+1)
S[0] = 0
for i in range(N):
    S[i+1] = S[i] + A[i]

from collections import Counter

c = Counter(S)
ans = 0
for k in c:
    if c[k] >= 2:
        ans += ((c[k] * (c[k]-1)) // 2)
print(ans)
