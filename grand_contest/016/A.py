import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()
from collections import Counter
c = Counter(s)

ans = 10 ** 7
for k in c:
    copy_s = list(s)
    tmp_ans = 0
    
    while set(copy_s) != {k}:
        tmp_s = [0] * (len(copy_s) - 1)
        for i in range(len(copy_s)):
            if copy_s[i] == k:
                if i == 0:
                    tmp_s[i] = k
                elif i == len(copy_s) - 1:
                    tmp_s[i-1] = k
                else:
                    tmp_s[i] = k
                    tmp_s[i-1] = k
            else:
                if i != len(copy_s) - 1:
                    tmp_s[i] = copy_s[i]
        tmp_ans += 1
        copy_s = tmp_s

    ans = min(ans, tmp_ans)
print(ans)
