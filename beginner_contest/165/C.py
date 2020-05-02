import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, q = map(int, input().split())
pairs = [0] * q
for i in range(q):
    pairs[i] = list(map(int, input().split()))

from collections import deque

def dfs(min_val, length):
    if length == 0:
        return list([deque()])
    if min_val == m:
        return list([deque([m]) * length])
    ans = list()
    for i in range(min_val, m+1):
        remain = dfs(i, length-1)
        for j in remain:
            j.appendleft(i)
        ans.extend(remain)
    return ans

ans = 0
for i in dfs(1, n):
    tmp = 0
    for a, b, c, d in pairs:
        if (i[b-1] - i[a-1]) == c:
            tmp += d
    ans = max(ans, tmp)

print(ans)
