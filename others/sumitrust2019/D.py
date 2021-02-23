import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input().strip()

import string

ans = 0
for i in string.digits:
    for j in string.digits:
        for k in string.digits:
            i_pos = S.find(i, 0)
            if i_pos == -1:
                continue
            j_pos = S.find(j, i_pos + 1)
            if j_pos == -1:
                continue
            k_pos = S.find(k, j_pos + 1)
            if k_pos == -1:
                continue
            ans += 1
print(ans)
