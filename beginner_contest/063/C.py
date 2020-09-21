import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

s = []
for _ in range(n):
    s.append(int(input()))
s = sorted(s)

ans = sum(s)
if ans % 10 != 0:
    print(ans)
    sys.exit(0)

for v in s:
    if v % 10 != 0:
        print(ans - v)
        sys.exit(0)
print(0)
