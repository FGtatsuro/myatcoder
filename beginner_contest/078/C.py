import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

one_time = 1900 * m + 100 * (n - m)
print(one_time * (2 ** m))
