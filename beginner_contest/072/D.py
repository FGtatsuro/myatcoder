import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
p = [0] + list(map(int, input().split()))

ans = 0
for i in range(1, n + 1):
    if p[i] != i:
        continue

    if i == 1:
        p[2], p[1] = p[1], p[2]
    elif i == n:
        p[n], p[n-1] = p[n-1], p[n]
    else:
        p[i+1], p[i] = p[i], p[i+1]
    ans += 1

print(ans)
