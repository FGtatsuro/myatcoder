import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())

ans = 0
check = 10 ** 3
if 0 < N < check:
    print(ans)
    sys.exit(0)
if check <= N < check ** 2:
    ans += (N % (check ** 2) - (check - 1)) * 1
    print(ans)
    sys.exit(0)
ans += ((check ** 2 - 1) % (check ** 2) - (check - 1)) * 1
if check ** 2 <= N < check ** 3:
    ans += (N % (check ** 3) - (check ** 2 - 1)) * 2
    print(ans)
    sys.exit(0)
ans += ((check ** 3 - 1) % (check ** 3) - (check ** 2 - 1)) * 2
if check ** 3 <= N < check ** 4:
    ans += (N % (check ** 4) - (check ** 3 - 1)) * 3
    print(ans)
    sys.exit(0)
ans += ((check ** 4 - 1) % (check ** 4) - (check ** 3 - 1)) * 3
if check ** 4 <= N < check ** 5:
    ans += (N % (check ** 5) - (check ** 4 - 1)) * 4
    print(ans)
    sys.exit(0)
ans += ((check ** 5 - 1) % (check ** 5) - (check ** 4 - 1)) * 4
# N = 10 ** 15
if N == check ** 5:
    print(ans + 5)
