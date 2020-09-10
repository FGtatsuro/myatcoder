import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, k = map(int, input().split())

num = set()
for v in range(a, a + k):
    if v > b:
        break
    num.add(v)
    print(v)

for v in range(b + 1 - k, b + 1):
    if v < a:
        continue
    if v in num:
        continue
    print(v)
