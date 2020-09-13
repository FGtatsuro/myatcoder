import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = int(input())
MOD = 10 ** 9 + 7

if s <= 2:
    print(0)
    sys.exit(0)

cache = {}
# dfs(0)=1が6 <= n <= 9のまとめて取る分をフォローしている
cache[0] = 1
cache[1] = cache[2] = 0
cache[3] = cache[4] = cache[5] = 1
def dfs(n):
    if n in cache:
        return cache[n]
    else:
        ans = 0
        for i in range(3, n + 1):
            ans += dfs(n - i) % MOD
        cache[n] = ans
        return cache[n]

print(dfs(s) % MOD)
