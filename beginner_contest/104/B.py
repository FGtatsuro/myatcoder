import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

if s[0] != 'A':
    print('WA')
    sys.exit(0)

if s.count('C') != 1:
    print('WA')
    sys.exit(0)

if not (2 <= s.find('C') <= len(s) - 2):
    print('WA')
    sys.exit(0)

if not s.replace('A', '').replace('C', '').islower():
    print('WA')
    sys.exit(0)

print('AC')
