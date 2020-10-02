import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x = int(input())
s = 0
i = 0
while s < x:
    i += 1
    s = ((i + 1) * i) // 2
print(i)
