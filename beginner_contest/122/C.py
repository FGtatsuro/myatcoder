import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, q = map(int, input().split())
s = input().strip()

count = [0] * n
c = 0
for i in range(n - 1):
    count[i] = c
    if s[i:i+2] == 'AC':
        c += 1
    count[i+1] = c
count = [0] + count

for _ in range(q):
    l, r = map(int, input().split())
    print(count[r] - count[l])
