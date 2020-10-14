import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

change = 0
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        change += 1
print(change)
