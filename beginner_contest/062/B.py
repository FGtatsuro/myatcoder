import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
print('#' * (w + 2))
for i in range(h):
    print('#{}#'.format(input().strip()))
print('#' * (w + 2))
