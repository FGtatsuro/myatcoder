import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
prev_time = 0
prev_point = (0, 0)
for i in range(n):
    t, x, y = map(int, input().split())
    dist = abs(x - prev_point[0]) + abs(y - prev_point[1])
    if dist > (t - prev_time):
        print('No')
        sys.exit(0)

    if (t - prev_time) % 2 != dist % 2:
        print('No')
        sys.exit(0)
    prev_time = t
    prev_point = (x, y)
print('Yes')
