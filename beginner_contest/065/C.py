import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
MOD = 10 ** 9 + 7

if abs(n - m) >= 2:
    print(0)
    sys.exit(0)

factorial  = [0] * (10 ** 5 + 1)
factorial[0] = 1
for i in range(1, 10 ** 5 + 1):
    factorial[i] = (i * factorial[i-1]) % MOD

if abs(n - m) == 1:
    print((factorial[n] * factorial[m]) % MOD)
elif n == m:
    print((2 * factorial[n] * factorial[m]) % MOD)
else:
    assert False
