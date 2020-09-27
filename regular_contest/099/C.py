import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
a = list(map(int, input().split()))
one_index = a.index(1)
l_min = max(0, one_index - k + 1)
l_max = one_index

ans = 10 ** 7
for i in range(l_min, l_max + 1):
    r = min(n - 1, i + k - 1)
    l_ans = ((i + (k - 1) - 1) // (k - 1))
    r_ans = ((((n - 1) - r) + (k - 1) - 1) // (k - 1))
    ans = min(ans, l_ans + r_ans + 1)
print(ans)
