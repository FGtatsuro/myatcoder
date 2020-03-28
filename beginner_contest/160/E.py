import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x, y, a, b, c = list(map(int, input().split()))
p = sorted(sorted(list(map(int, input().split())), reverse=True)[:x])
q = sorted(sorted(list(map(int, input().split())), reverse=True)[:y])
r = list(map(int, input().split()))
print(sum(sorted(p + q + r, reverse=True)[:x+y]))
