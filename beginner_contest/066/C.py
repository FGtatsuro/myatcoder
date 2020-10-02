import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))
even = []
odd = []
for i, v in enumerate(a):
    v = str(v)
    if (i + 1) % 2 == 0:
        even.append(v)
    else:
        odd.append(v)

if n % 2 == 0:
    print(' '.join(list(reversed(even)) + odd))
else:
    print(' '.join(list(reversed(odd)) + even))
