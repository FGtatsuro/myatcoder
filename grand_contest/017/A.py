import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, p = map(int, input().split())
a = list(map(int, input().split()))
even = [v for v in a if v % 2 == 0]
odd = [v for v in a if v % 2 != 0]

factorial = [0] + [0] * n
factorial[0] = 1
for i in range(1, n + 1):
    factorial[i] = factorial[i - 1] * i

if p == 0:
    if len(odd) == 0:
        print(2 ** len(even))
        sys.exit(0)
    else:
        ans = 0
        for i in range(0, len(odd) + 1, 2):
            ans += ((2 ** len(even)) * (factorial[len(odd)] // (factorial[len(odd) - i] * factorial[i])))
        print(ans)
        sys.exit(0)
elif p == 1:
    if len(odd) == 0:
        print(0)
        sys.exit(0)
    else:
        ans = 0
        for i in range(1, len(odd) + 1, 2):
            ans += ((2 ** len(even)) * (factorial[len(odd)] // (factorial[len(odd) - i] * factorial[i])))
        print(ans)
        sys.exit(0)
else:
    assert False
