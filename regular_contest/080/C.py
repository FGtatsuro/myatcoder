import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

two = []
four = []
others = []

for v in a:
    if v % 4 == 0:
        four.append(v)
    elif v % 2 == 0:
        two.append(v)
    else:
        others.append(1)

if len(two) % 2 != 0:
    others.append(two[0])
if len(four) + 1 >= len(others):
    print('Yes')
else:
    print('No')
