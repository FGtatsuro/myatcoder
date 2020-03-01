import sys
input = sys.stdin.readline

n = int(input())

s = [0] * n
for i in range(n):
    s[i] = input().strip()

import collections

counter = collections.Counter(s).most_common()

first = counter.pop(0)
answers = [first[0]]
value = first[1]

for c in counter:
    if c[1] != value:
        break
    answers.append(c[0])

answers = sorted(answers)
for a in answers:
    print(a)
