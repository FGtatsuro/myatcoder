import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
ans = 0

if n >= m // 2:
    print(m // 2)
else:
    ans += n
    ans += ((m - n * 2) // 4)
    print(ans)
