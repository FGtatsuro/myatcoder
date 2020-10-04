import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = [0] + list(map(int, input().split())) + [0]
diff = [0] * (n + 1)
for i in range(n + 1):
    diff[i] = abs(a[i+1] - a[i])
ans = sum(diff)
for i in range(1, n + 1):
    print(ans - (diff[i-1] + diff[i]) + (abs(a[i+1] - a[i-1])))
