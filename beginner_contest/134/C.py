import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]

first = max(a)
if a.count(first) > 1:
    second = first
else:
    b = a[:]
    b.remove(first)
    second = max(b)

for i in a:
    if i != first:
        print(first)
    else:
        print(second)
