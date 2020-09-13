import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

o = input().strip()
e = input().strip()

ans = []
for i, v in enumerate(o):
    ans.append(v)
    if (i != len(o) - 1) or (len(o) == len(e)):
        ans.append(e[i])
print(''.join(ans))
