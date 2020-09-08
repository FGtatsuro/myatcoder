import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

last = a
if b % 10 != 0 and (last % 10) > (b % 10):
    last = b
if c % 10 != 0 and (last % 10) > (c % 10):
    last = c
if d % 10 != 0 and (last % 10) > (d % 10):
    last = d
if e % 10 != 0 and (last % 10) > (e % 10):
    last = e

target = [a, b, c, d, e]
target.remove(last)
ans = 0
for v in target:
    ans += (((v + 10 - 1) // 10) * 10)
ans += last
print(ans)
