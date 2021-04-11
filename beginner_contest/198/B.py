import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = input().strip()

for i in range(20):
    n = '0' * i + N
    if len(n) % 2 == 0:
        a, b = n[:len(n)//2], n[len(n)//2:]
    else:
        a, b = n[:len(n)//2], n[len(n)//2+1:]
    if a == b[::-1]:
        print('Yes')
        sys.exit(0)
print('No')
