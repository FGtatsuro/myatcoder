import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, l = map(int, input().split())
s = [0] * n
for i in range(n):
    s[i] = input().strip()

print(''.join(sorted(s)))
