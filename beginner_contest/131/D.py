import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
jobs = [0] * n
for i in range(n):
    jobs[i] = tuple(map(int, input().split()))
jobs = sorted(jobs, key=lambda x: x[1])
_sum = 0
for j in jobs:
    _sum += j[0]
    if _sum > j[1]:
        print('No')
        sys.exit(0)
print('Yes')
