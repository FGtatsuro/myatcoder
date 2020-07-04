import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, x = map(int, input().split())
point = list(map(int, input().split()))
diff = [0] * n
for i in range(n):
    diff[i] = abs(point[i] - x)

def gcd(big, small):
    if small == 0:
        return big
    else:
        return gcd(small, big % small)

import functools

print(functools.reduce(gcd, diff))
