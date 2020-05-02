import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x = int(input())

year = 1
total = 100
while True:
    total = int(total * 1.01)
    if total >= x:
        break
    year += 1
print(year)
