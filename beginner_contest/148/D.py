import sys
input = sys.stdin.readline

n = int(input())
a = [int(i) for i in input().split()]

target = 1
size = 0
for i in range(n):
    if a[i] == target:
        target += 1
    else:
        size += 1

if size == n:
    print(-1)
else:
    print(size)
