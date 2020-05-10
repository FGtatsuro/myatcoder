import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c, k = map(int, input().split())

if k <= a:
    print(k)
    sys.exit(0)

ans = a
k = k - a

if k <= b:
    print(ans)
    sys.exit(0)

k = k - b
ans = ans - k
print(ans)
