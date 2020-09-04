import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

ans = 10 ** 9
for v in a:
    tmp = 0
    while v % 2 == 0:
        tmp += 1
        v //= 2
    ans = min(ans, tmp)
print(ans)
