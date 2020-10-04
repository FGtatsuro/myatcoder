import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k, s = map(int, input().split())

if s == 10 ** 9:
    ans = [s] * k + [s-1] * (n - k)
else:
    ans = [s] * k + [s+1] * (n - k)
print(' '.join((str(v) for v in ans)))
