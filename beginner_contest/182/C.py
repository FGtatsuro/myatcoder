import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = input().strip()
from collections import Counter

c = Counter(int(v) for v in n if int(v) % 3 != 0)
for i in range(1, 10):
    if i not in c:
        c[i] = 0

if int(n) % 3 == 0:
    print(0)
elif int(n) % 3 == 1:
    if len(n) > 1 and (c[1] + c[4] + c[7] >= 1):
        print(1)
    elif len(n) > 2 and (c[2] + c[5] + c[8] >= 2):
        print(2)
    else:
        print(-1)
elif int(n) % 3 == 2:
    if len(n) > 1 and (c[2] + c[5] + c[8] >= 1):
        print(1)
    elif len(n) > 2 and (c[1] + c[4] + c[7] >= 2):
        print(2)
    else:
        print(-1)
else:
    assert False
