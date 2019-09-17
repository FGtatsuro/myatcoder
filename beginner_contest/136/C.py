import sys
n = int(sys.stdin.readline())
h = [int(i) for i in sys.stdin.readline().split()]

def cond(h):
    if len(h) == 1:
        return True
    for index in range(n - 1):
        diff = h[index + 1] - h[index]
        if diff == 0:
            continue
        if diff > 0:
            h[index + 1] -= 1
            continue
        if diff < 0:
            return False
    return True

if cond(h):
    print('Yes')
else:
    print('No')
