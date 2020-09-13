import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
MOD = 10 ** 9 + 7

if n == 1:
    print(0)
    sys.exit(0)

print((pow(10, n, MOD) - (pow(9, n, MOD) * 2) + pow(8, n, MOD)) % MOD)
