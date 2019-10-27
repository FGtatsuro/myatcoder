n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]

import sys
import math

a.sort()
f.sort(reverse=True)

def cond(score):
    _max = 0
    count = 0
    for i in range(n):
        if a[i] * f[i] <= score:
            continue
        target = (score // f[i])
        count += a[i] - target
        if count > k:
            return False, -1
        _max = max(_max, target * f[i])
    if count <= k:
        return True, _max

def binary_search(start, end, result):
    middle = math.ceil((start + end) / 2)
    if middle == end:
        if result[start]:
            return start
        else:
            return end
    is_ok, score = cond(middle)
    result[middle] = is_ok
    if is_ok:
        return binary_search(start, min(middle, score), result)
    else:
        return binary_search(middle, end, result)

# 0
if sum(a) <= k:
    print(0)
    sys.exit(0)

max_score = 0
for i in range(n):
    max_score = max(max_score, a[i] * f[i])

# max
if k == 0:
    print(max_score)
    sys.exit(0)

# 1 - max
if cond(1)[0]:
    print(1)
    sys.exit(0)

result = {1: False, max_score: True}
print(binary_search(1, max_score, result))
