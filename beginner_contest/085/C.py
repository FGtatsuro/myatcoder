n, y = [int(i) for i in input().split()]

def cond():
    for i in range(n + 1):
        for j in range(n - i, -1, -1):
            k = n - i - j
            if (10000  * i + 5000 * j + 1000 * k) == y:
                return '{} {} {}'.format(i, j, k)
    return ""

c = cond()
if c:
    print(c)
else:
    print('-1 -1 -1')

