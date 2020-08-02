import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

k = int(input())
if k % 2 == 0 or k % 5 == 0:
    print(-1)
    sys.exit(0)

l = 9 * k
if k % 7 == 0:
    l //= 7

ans = 1
num = 10
while True:
    if num % l == 1:
        break
    num = (num % l) * 10
    ans += 1
print(ans)
