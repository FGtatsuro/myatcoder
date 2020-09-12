import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
t = [0] + list(map(int, input().split()))
m = int(input())

ans = sum(t)
for _ in range(m):
    p, x = map(int, input().split())
    print(ans - (t[p] - x))
