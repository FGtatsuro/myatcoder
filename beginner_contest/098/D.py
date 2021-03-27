import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))

right = 0
ans = 0
_sum = 0
_sum_xor = 0
for left in range(N):
    while right < N and (_sum + A[right]) == (_sum_xor^A[right]):
        _sum += A[right]
        _sum_xor ^= A[right]
        right += 1

    ans += (right - left)

    if left == right:
        right += 1
    else:
        _sum -= A[left]
        _sum_xor ^= A[left]

print(ans)
