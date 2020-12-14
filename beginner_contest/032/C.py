import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
line = [0] * n
for i in range(n):
    line[i] = int(input())

if 0 in line:
    print(n)
    sys.exit(0)
if k == 0:
    print(0)
    sys.exit(0)

ans = 0
right = 0
total = 1
for left in range(n):
    while right < n and total * line[right] <= k:
        total *= line[right]
        right += 1

    ans = max(ans, right - left)

    if left == right:
        # この場合はtotalが増えていないため、減ずる必要はない
        right += 1
    else:
        total //= line[left]
print(ans)
