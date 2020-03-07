import sys
input = sys.stdin.readline

import collections

s = collections.deque(input().strip())
num = int(input())
query = [0] * num
for i in range(num):
    query[i] = input().strip()

reverse_flag = False
for q in query:
    if q[0] == '1':
        reverse_flag = not reverse_flag
    else:
        _, f, c = q.split()
        if (f == '1' and not reverse_flag) or (f == '2' and reverse_flag):
            s.appendleft(c)
        if (f == '2' and not reverse_flag) or (f == '1' and reverse_flag):
            s.append(c)
if reverse_flag:
    s.reverse()
print(''.join(list(s)))
