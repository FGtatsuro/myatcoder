import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for i in range(n)]
a = [-1] + a

def cond(a):
    if 2 not in a:
        return -1

    visited = set()
    current = 1
    count = 0

    while True:
        if current == 2:
            return count
        if current in visited:
            return -1
        count += 1
        visited.update((current,))
        current = a[current]

print(cond(a))
