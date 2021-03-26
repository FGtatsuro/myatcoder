import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
a = list(map(int, input().split()))

right = 0
ans = 0
current = 0
for left in range(N):
    while (left == right) or (right < N and current < a[right]):
        current = a[right]
        right += 1

    ans += (right - left)

    if left == right:
        right += 1

print(ans)

