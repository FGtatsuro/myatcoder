import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x, y = map(int, input().split())

ans = 0
while x <= y:
    ans += 1
    x *= 2
print(ans)
