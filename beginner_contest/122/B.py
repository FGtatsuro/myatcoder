import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

ans = 0
tmp = 0
for v in s:
    if v in ('A', 'C', 'G', 'T'):
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0
# 最後がACGT文字だった場合
ans = max(ans, tmp)

print(ans)
