import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

exp = 0
while 2 ** (exp + 1) <= n:
    exp += 1
print(2 ** exp)
