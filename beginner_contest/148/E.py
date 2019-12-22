import sys
input = sys.stdin.readline

n = int(input())

if n % 2 != 0:
    print(0)
    sys.exit(0)

ans = 0
base = 1
while True:
    base *= 5
    even = base * 2
    if n < even:
        break
    ans += n // even

print(ans)
