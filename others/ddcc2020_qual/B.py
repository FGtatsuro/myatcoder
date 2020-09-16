import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

s = sum(a)
half = s / 2

cum = 0
for v in a:
    if abs(half - cum) < abs(half - (cum + v)):
        break
    cum += v
print(abs((s - cum) - cum))
