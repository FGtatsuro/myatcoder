import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x, k, d = map(int, input().split())

x = abs(x)

if x - (k * d) >= 0:
    print(x - (k * d))
    sys.exit(0)
else:
    remain = k - (x // d)
    p_min = x % d
    n_min = abs(p_min -d)
    if remain % 2 == 0:
        print(p_min)
    else:
        print(n_min)
