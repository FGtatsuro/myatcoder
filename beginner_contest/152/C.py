import sys
input = sys.stdin.readline

n = int(input())
p = [int(i) for i in input().split()]

ans = 1
_min = p[0]

for i in p[1:]:
    if i <= _min:
        ans += 1
        _min = i

print(ans)
