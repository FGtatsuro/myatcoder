import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
cond = [0] * m
for i in range(m):
    a, b = map(int, input().split())
    cond[i] = (a, b)
k = int(input())
people = [0] * k
for i in range(k):
    c, d = map(int, input().split())
    people[i] = (c, d)

ans = 0
for i in range(2 ** k):
    binfmt = format(i, '0{}b'.format(k))
    place = [0] + [0] * n
    for j in range(k):
        which = binfmt[j]
        if which == '0':
            place[people[j][0]] = 1
        elif which == '1':
            place[people[j][1]] = 1
        else:
            assert False

    tmp_ans = 0
    for a, b in cond:
        if place[a] == 1 and place[b] == 1:
            tmp_ans += 1
    ans = max(ans, tmp_ans)
print(ans)
