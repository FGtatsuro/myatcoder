import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())

if n > k:
    n = n % k

print(min(abs(n - k), n))
