import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
m, a, r, c, h = [0] * 5
for _ in range(n):
    s = input().strip()
    if s[0] == 'M':
        m += 1
    if s[0] == 'A':
        a += 1
    if s[0] == 'R':
        r += 1
    if s[0] == 'C':
        c += 1
    if s[0] == 'H':
        h += 1
march = [m, a, r, c, h]

ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans += (march[i] * march[j] * march[k])
print(ans)
