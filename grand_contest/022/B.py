import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))

right = 0
ans = 0
taste = set()
for left in range(N):
    while right < N and A[right] not in taste:
        taste.add(A[right])
        right += 1

    ans = max(ans, right - left)

    if left == right:
        right += 1
    else:
        taste.remove(A[left])

print(ans)
