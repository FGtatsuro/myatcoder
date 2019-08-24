import sys

n = int(sys.stdin.readline())
a = [[int(i) for i in sys.stdin.readline().strip().split()] for _ in range(2)]

if n == 1:
    print(a[0][0] + a[1][0])
else:
    import itertools
    top_accum = list(itertools.accumulate(a[0]))
    bottom_accum_reverse = list(reversed(list(itertools.accumulate(reversed(a[1])))))

    count_max = 0
    for i in range(n):
        count_max = max(count_max, top_accum[i] + bottom_accum_reverse[i])
    print(count_max)
