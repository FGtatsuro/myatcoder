import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())

count = 1
ans = 0
while True:
    n = int(str(count) * 2)
    if n > N:
        break
    ans += 1
    count += 1
print(ans)
