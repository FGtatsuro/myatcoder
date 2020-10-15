import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))
mean_ceil = (sum(a) + len(a) -1) // len(a)
mean_floor = int(sum(a) / len(a))

if mean_ceil == mean_floor:
    ans = 0
    for v in a:
        ans += (v - mean_ceil) ** 2
    print(ans)
else:
    ans_ceil = 0
    ans_floor = 0
    for v in a:
        ans_ceil += (v - mean_ceil) ** 2
        ans_floor += (v - mean_floor) ** 2
    print(min(ans_ceil, ans_floor))
