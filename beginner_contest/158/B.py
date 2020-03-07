import sys
input = sys.stdin.readline

n, a, b = [int(i) for i in input().split()]

ans = 0
if a == 0 and b == 0:
    print(ans)
    sys.exit(0)

full = n // (a + b)
ans += a * full

partial = n % (a + b)
if partial >= a:
    ans += a
else:
    ans += partial

print(ans)
