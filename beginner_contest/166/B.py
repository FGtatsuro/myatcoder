import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
has = set()
for _ in range(k):
    input()
    has.update(map(int, input().split()))

no_has = set(range(1, n+1)) - has
print(len(no_has))
