import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

LIMIT = 10 ** 18

ans = 1
if 0 in a:
    print(0)
    sys.exit(0)
for i in a:
    ans *= i
    if ans > LIMIT:
        print(-1)
        sys.exit(0)
print(ans)
