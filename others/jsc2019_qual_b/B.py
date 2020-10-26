import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
a = list(map(int, input().split()))
MOD = 10 ** 9 + 7

from collections import Counter

# 各数の出現数と累積和
_max = max(a)
count = [0] + [0] * _max
c = Counter(a)
for i in c:
    count[i] += c[i]
accum = [0] + [0] * _max
for i in range(_max):
    accum[i+1] += accum[i] + count[i+1]

# 以前の繰り返しの転倒数の総和
ans = 0
tmp_ans = 0
for v in a:
    tmp_ans += (n - accum[v])
ans += ((tmp_ans) * ((k * (k - 1)) // 2)) % MOD

# 数列A内部での転倒数の総和
tmp_ans = 0
for i in range(1, n):
    pivot = a[i]
    for j in range(0, i):
        if a[j] > a[i]:
            tmp_ans += 1
ans += ((tmp_ans) * k) % MOD
print(ans % MOD)
