import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import Counter
n = int(input())
a = Counter(map(int, input().split()))
a = {k: a[k] for k in a if a[k] >= 2}
if len(a) < 2:
    print(0)
    sys.exit(0)
else:
    k = sorted(a.keys(), reverse=True)
    if a[k[0]] >= 4:
        print(k[0] ** 2)
        sys.exit(0)
    else:
        print(k[0] * k[1])
        sys.exit(0)
