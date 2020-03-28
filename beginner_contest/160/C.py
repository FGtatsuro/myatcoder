import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

k, n = list(map(int, input().split()))
a = list(map(int, input().split()))

diff = [0] * n
for i in range(len(a) - 1):
    diff[i] = abs(a[i] - a[i+1])
diff[-1] = abs(a[-1] - k) + a[0]

print(k - max(diff))
