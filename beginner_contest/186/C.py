import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

ans = n
for i in range(1, n + 1):
    if '7' in str(i):
        ans -= 1
        continue
    if '7' in oct(i):
        ans -= 1
        continue
print(ans)

