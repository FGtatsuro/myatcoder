import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

check_max = 3 * (10 ** 6) + 1
accum = [0] * (check_max)
for i in range(1, check_max):
    accum[i] = accum[i-1] + i

ans = 0
for i in range(1, check_max):
    if accum[i-1] >= n:
        break
    if (n - accum[i-1]) % i == 0:
        ans += 2
print(ans)
