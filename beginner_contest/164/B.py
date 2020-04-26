import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c, d = map(int, input().split())

def cond():
    count1 = c // b
    if c % b != 0:
        count1 += 1
    count2 = a // d
    if a % d != 0:
        count2 += 1
    return count1 <= count2

if cond():
    print('Yes')
else:
    print('No')
