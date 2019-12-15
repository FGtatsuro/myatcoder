import sys
input = sys.stdin.readline
import collections

n = int(input())
bit = []
for i in range(2 ** n):
    bit.append(format(i, '0{}b'.format(n)))
bit = sorted(bit, key=lambda a: -collections.Counter(a)['1'])

say = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        say[i].append([int(i) for i in input().split()])

answer = 0
for b in bit:
    failed = False
    for i, v in enumerate(b):
        if failed:
            break
        if v == '1':
            for s in say[i]:
                if int(b[s[0] - 1]) != s[1]:
                    failed = True
                    break
    if not failed:
        answer = b
        break

print(collections.Counter(b)['1'])
