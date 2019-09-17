import sys
n = int(sys.stdin.readline())
a = [int(i) for i in sys.stdin.readline().split()]
b = [int(i) for i in sys.stdin.readline().split()]

total = 0
for i, v in enumerate(b):
    m1 = min(v, a[i])

    total += m1
    a[i] -= m1

    if m1 == v:
        continue
    v -= m1

    m2 = min(v, a[i+1])
    total += m2
    a[i+1] -= m2
print(total)
