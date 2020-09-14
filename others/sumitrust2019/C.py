import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x = int(input())

def cond(x):
    q, r = x // 100, x % 100
    q5, r5 = r // 5, r % 5
    if r5 == 0:
        return q >= q5
    else:
        return q >= q5 + 1

if cond(x):
    print(1)
else:
    print(0)
