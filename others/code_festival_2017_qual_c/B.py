import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

odd = 1
for v in a:
    if v % 2 == 0:
        odd *= 2
    else:
        odd *= 1

print(3 ** n - odd)
