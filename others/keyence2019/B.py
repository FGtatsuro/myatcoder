import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

target = 'keyence'

if target in s:
    print('YES')
    sys.exit(0)

for start in range(len(s)):
    for end in range(start + 1, len(s) + 1):
        copy_s = list(s)
        copy_s[start:end] = ''
        if ''.join(copy_s) == target:
            print('YES')
            sys.exit(0)
print('NO')
