import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

if 'R' not in s:
    print(0)
    sys.exit(0)
else:
    if s == 'RRR':
        print(3)
        sys.exit(0)
    elif 'RR' in s:
        print(2)
        sys.exit(0)
    else:
        print(1)
        sys.exit(0)

