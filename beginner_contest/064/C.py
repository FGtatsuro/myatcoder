import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
rate = [0] * 9
for v in map(int, input().split()):
    if v // 400 < 8:
        rate[v // 400] = 1
    else:
        rate[8] += 1

ans = sum(rate[:8])
if ans == 0:
    print('1 {}'.format(rate[8]))
elif rate[8] == 0:
    print('{} {}'.format(ans, ans))
else:
    print('{} {}'.format(ans, ans + rate[8]))
