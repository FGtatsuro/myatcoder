import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
fav = set(range(1, m+1))
for _ in range(n):
    a = set(list(map(int, input().split()))[1:])
    fav = fav.intersection(a)

print(len(fav))
