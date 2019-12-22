import sys
input = sys.stdin.readline

a, b = int(input()), int(input())
print((set([1,2,3]) - set([a,b])).pop())
