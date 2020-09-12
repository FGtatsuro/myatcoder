import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()
t = input().strip()

for i in range(len(s)):
    if t == s[len(s)-i:len(s)] + s[:len(s)-i]:
        print('Yes')
        sys.exit(0)
print('No')
