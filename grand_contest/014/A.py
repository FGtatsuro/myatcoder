import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, input().split())

ans = 0
pattern = set()
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    p = tuple(sorted((a, b, c)))
    if p in pattern:
        print(-1)
        sys.exit(0)
    pattern.add(p)
    a, b, c = (b + c) // 2, (a + c) // 2, (a + b) // 2
    ans += 1

print(ans)
