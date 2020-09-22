import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())

if k == 1:
    print(1)
    sys.exit(0)

# 場合分けをする必要はなかった
#if k <= n:
#    ans = ((n - k) + 1) / n
#    upper = k - 1
#else:
#    ans = 0
#    upper = n
#for i in range(1, upper + 1):
#    tmp = 1 / n
#    while i < k:
#        tmp *= (1 / 2)
#        i *= 2
#    ans += tmp
ans = 0
for i in range(1, n + 1):
    tmp =  1 / n
    while i < k:
        tmp *= (1 / 2)
        i *= 2
    ans += tmp
print(ans)
