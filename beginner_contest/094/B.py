import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

to_zero = [i for i in a if i < x]
to_n = [i for i in a if i > x]
print(min(len(to_zero), len(to_n)))

