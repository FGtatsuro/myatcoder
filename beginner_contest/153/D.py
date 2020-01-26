import sys
input = sys.stdin.readline

h = int(input())

def count(h):
    if h == 1:
        return 1
    else:
        return 1 + 2 * count(h // 2)

print(count(h))

