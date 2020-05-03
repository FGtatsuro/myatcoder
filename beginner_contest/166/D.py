import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x = int(input())

for i in range(-118, 119+1):
    for j in range(-119, 118+1):
        if i**5 -  j**5 == x:
            print(i, j)
            sys.exit(0)
