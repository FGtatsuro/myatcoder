import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
score = [0] * n
for i in range(n):
    s = input().split()
    score[i] = (s[0].strip(), int(s[1]), i + 1)

for s in sorted(score, key=lambda l: (l[0], -l[1])):
    print(s[2])
