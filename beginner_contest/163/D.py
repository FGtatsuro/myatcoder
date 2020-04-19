import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

MOD = 10 ** 9 + 7

n, k = map(int, input().split())

#def mpow(x, n):
#    result = 1
#    while n > 0:
#        if (n & 1):
#            result = (result * x) % MOD
#        x = (x * x) % MOD
#        n >>= 1
#    return result
#
#factorial = [0] * (n + 2)
#inverse = [0] * (n + 2)
#factorial[0] = 1
#inverse[0] = 1
#
#for i in range(1, n + 2):
#    factorial[i] = (factorial[i-1] * i) % MOD
#    inverse[i] = mpow(factorial[i], MOD - 2) % MOD

ans = 0

sum_cache = [0] + [0] * n
for i in range(1, n+1):
    sum_cache[i] = sum_cache[i-1] + i

for i in range(k, n+1):
    #ans += (factorial[n+1] * inverse[n+1-i] * inverse[i]) % MOD
    ans += ((sum_cache[n] - sum_cache[n-i]) - sum_cache[i-1] + 1) % MOD
# n + 1
ans += 1

print(ans % MOD)
