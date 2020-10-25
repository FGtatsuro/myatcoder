import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

ans = set()
_sum = 0
for i in range(1, n + 1):
    ans.add(i)
    _sum += i
    if _sum == n:
        break
    elif _sum > n:
        ans.remove(_sum - n)
        break

for v in ans:
    print(v)
