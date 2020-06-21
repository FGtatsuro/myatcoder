import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
p = list(map(int, input().split()))

print(sum(sorted(p)[:k]))
