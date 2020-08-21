import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(''.join(input().split()))
i = 4
while i ** 2 <= n:
    if i ** 2 == n:
        print('Yes')
        sys.exit(0)
    i += 1
print('No')
