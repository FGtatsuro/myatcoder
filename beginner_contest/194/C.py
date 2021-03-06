import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))
square_sum = 0
for v in A:
    square_sum += v ** 2
print((square_sum * (len(A) - 1)) - ((sum(A) ** 2) - square_sum))
