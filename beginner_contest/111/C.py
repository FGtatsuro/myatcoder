import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
v = list(map(int, input().split()))

odd = []
even = []

for i in range(1, n + 1):
    if i % 2 == 0:
        even.append(v[i - 1])
    else:
        odd.append(v[i - 1])

from collections import Counter
odd = Counter(odd)
even = Counter(even)

if len(odd) == 1 and len(even) == 1:
    if set(odd) == set(even):
        print(n // 2)
    else:
        print(0)
    sys.exit(0)

if len(odd) == 1 and len(even) != 1:
    even = list(sorted(((k, even[k]) for k in even), key=lambda x: -x[1]))

    if list(odd)[0] == even[0][0]:
        print(n // 2 - even[1][1])
    else:
        print(n // 2 - even[0][1])
    sys.exit(0)

if len(odd) != 1 and len(even) == 1:
    odd = list(sorted(((k, odd[k]) for k in odd), key=lambda x: -x[1]))

    if list(even)[0] == odd[0][0]:
        print(n // 2 - odd[1][1])
    else:
        print(n // 2 - odd[0][1])
    sys.exit(0)

if len(odd) != 1 and len(even) != 1:
    even = list(sorted(((k, even[k]) for k in even), key=lambda x: -x[1]))
    odd = list(sorted(((k, odd[k]) for k in odd), key=lambda x: -x[1]))

    if even[0][0] == odd[0][0]:
        print(
            min(
                (n // 2 - even[0][1]) + (n // 2 - odd[1][1]),
                (n // 2 - even[1][1]) + (n // 2 - odd[0][1]),
            )
        )
    else:
        print((n // 2 - even[0][1]) + (n // 2 - odd[0][1]))
    sys.exit(0)

assert False
