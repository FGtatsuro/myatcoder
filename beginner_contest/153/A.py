import sys
input = sys.stdin.readline

h, a = [int(i) for i in input().split()]

ans = 0
while True:
    ans += 1
    h -= a
    if h <= 0:
        break

print(ans)
