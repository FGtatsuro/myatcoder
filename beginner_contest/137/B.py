k, x = [int(i) for i in input().split()]

_max = x + k -1
_min = x - k + 1
print(' '.join(str(i) for i in range(_min, _max + 1)))

