import sys
input = sys.stdin.readline

n, k = [int(i) for i in input().split()]
h = sorted([int(i) for i in input().split()], reverse=True)[k:]
print(sum(h))
