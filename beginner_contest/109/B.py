import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

words = []
for _ in range(n):
    w = input().strip()

    if w in words:
        print('No')
        sys.exit(0)

    if len(words) == 0:
        words.append(w)
        continue

    if words[-1][-1] != w[0]:
        print('No')
        sys.exit(0)
    else:
        words.append(w)
print('Yes')
