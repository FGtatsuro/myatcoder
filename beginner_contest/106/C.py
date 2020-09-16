import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = [i for i in input().strip()]
k = int(input())

while k:
    v = s.pop(0)
    if v != '1':
        print(v)
        sys.exit(0)
    else:
        k -= 1
print(1)
