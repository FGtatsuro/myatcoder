import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

S = input().strip()

for i in range(len(S)):
    if (i + 1) % 2 == 1:
        if S[i].isupper():
            print('No')
            sys.exit(0)
    else:
        if S[i].islower():
            print('No')
            sys.exit(0)
print('Yes')
