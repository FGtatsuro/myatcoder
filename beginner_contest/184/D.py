import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c = sorted(map(int, input().split()))
dp = {}

def solve(x, y, z):
    if x == 100 or y == 100 or z == 100:
        return 0
    if (x, y, z) in dp:
        return dp[(x, y, z)]
    ans = (x / (x + y + z)) * (solve(x + 1, y, z) + 1) + \
            (y / (x + y + z)) * (solve(x, y + 1, z) + 1) + \
            (z / (x + y + z)) * (solve(x, y, z + 1) + 1)
    dp[(x, y, z)] = ans
    return ans

print(solve(a, b, c))
