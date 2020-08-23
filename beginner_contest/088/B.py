import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

if len(a) % 2 != 0:
    a.append(0)

print(sum(a[0::2]) - sum(a[1::2]))
