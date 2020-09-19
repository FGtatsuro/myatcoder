import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

if s[-1] == 's':
    print(s + 'es')
else:
    print(s + 's')
