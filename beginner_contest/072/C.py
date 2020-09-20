import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

t = [0] * (max(a) + 1)
for v in a:
    t[v] += 1

if max(a) <= 1:
    print(sum(t))
    sys.exit(0)

ans = 0
for i in range(0, max(a) - 1):
    ans = max(ans, t[i] + t[i+1] + t[i+2])

print(ans)

