import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = list(input().strip())
len_s = len(s)
s = [0] + s
ans = 0
# 1
ans += (len_s - 1)
# len_s
ans += (len_s - 1)
for i in range(2, len_s):
    if s[i] == 'U':
        ans += (i - 1) * 2
        ans += (len_s - i) * 1
    elif s[i] == 'D':
        ans += (i - 1) * 1
        ans += (len_s - i) * 2
    else:
        assert False
print(ans)
