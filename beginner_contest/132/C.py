import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
d = sorted(list(map(int, input().split())))

diff = d[n//2:][0] - d[:n//2][-1]
if diff <= 0:
    print(0)
else:
    print(diff)
