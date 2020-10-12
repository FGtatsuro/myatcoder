import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()
k = int(input())
seq_num = []
prev = None
count = None
for i, v in enumerate(s):
    if prev is None:
        prev = v
        count = 1
    elif v == prev:
        count += 1
    else:
        seq_num.append(count)
        prev = v
        count = 1
seq_num.append(count)

if len(set(s)) == 1:
    print((len(s) * k) // 2)
    sys.exit(0)

ans = 0
if s[0] != s[-1]:
    for v in seq_num:
        ans += (v // 2)
    print(ans * k)
elif s[0] == s[-1]:
    ans += (seq_num[0] // 2)
    ans += (seq_num[-1] // 2)
    tmp_ans = 0
    for v in seq_num[1:-1]:
        tmp_ans += (v // 2)
    tmp_ans *= k
    ans += tmp_ans
    ans += (((seq_num[0] + seq_num[-1]) // 2) * (k - 1))
    print(ans)
