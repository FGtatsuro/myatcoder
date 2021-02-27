import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
ans = 0
ans_set = set()
i = 2
while i ** 2 <= N:
    j = 2
    while i ** j <= N:
        if i ** j not in ans_set:
            ans += 1
            ans_set.add(i ** j)
        j += 1
    i += 1
print(N - ans)
