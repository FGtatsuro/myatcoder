import sys
input = sys.stdin.readline

a, b = [int(i) for i in input().split()]
small = min(a,b)
big = max(a,b)

multi = 1
ans = big
while True:
    ans = big * multi
    if (ans % small) == 0:
        break
    multi += 1

print(ans)
