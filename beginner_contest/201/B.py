import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
ST = [0] * N
for i in range(N):
    name, height = input().split()
    height = int(height)
    ST[i] = (name, height)
ST = sorted(ST, key=lambda m: -m[1])
print(ST[1][0])
