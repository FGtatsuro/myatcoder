import sys
input = sys.stdin.readline

n = int(input())
s, t = input().split()

ans = ''
for i in range(n):
    ans += ''.join([s[i], t[i]])
print(ans)
