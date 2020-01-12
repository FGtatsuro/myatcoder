import sys
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]

submits = [0] * m
for i in range(m):
    p, s = input().split()
    submits[i] = (int(p), s.strip())

answer = [0] * (n+1)
for i in range(n):
    answer[i+1] = {'AC':0, 'WA':0}

for submit in submits:
    p, s = submit[0], submit[1]
    if s == 'WA' and answer[p]['AC'] == 0:
        answer[p]['WA'] += 1
        continue
    if s == 'AC':
        answer[p]['AC'] = 1
        continue

ac_num = 0
wa_num = 0
for a in answer[1:]:
    ac_num += a['AC']
    if a['AC'] == 1:
        wa_num += a['WA']
print(ac_num, wa_num)
