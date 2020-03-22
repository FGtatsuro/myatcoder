import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

def cond():
    p1 = ((len(s) - 1)//2)
    p2 = (len(s) + 3)//2 - 1
    t1 = s[:p1]
    t2 = s[p2:]
    return s == ''.join(reversed(s)) and t1 == ''.join(reversed(t1)) and t2 == ''.join(reversed(t2))

if cond():
    print('Yes')
else:
    print('No')


