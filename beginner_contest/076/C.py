import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()
t = input().strip()

if len(t) > len(s):
    print('UNRESTORABLE')
    sys.exit(0)

ans = []
for i in range(len(s) - len(t) + 1):
    tmp_ans = []
    for j in range(len(s)):
        # 比較範囲外: ?ならば辞書順が前になるようaに置換、そうでなければsの値を使う
        if j < i or i + len(t) <= j:
            if s[j] == '?':
                tmp_ans.append('a')
            else:
                tmp_ans.append(s[j])
        # 比較範囲内: ?ならばtの値を、そうでなければ同じ値かを判断する
        else:
            if s[j] == '?':
                tmp_ans.append(t[j-i])
            elif s[j] == t[j-i]:
                tmp_ans.append(t[j-i])
            else:
                break
    if len(tmp_ans) == len(s):
        ans.append(''.join(tmp_ans))

if len(ans) == 0:
    print('UNRESTORABLE')
else:
    print(sorted(ans)[0])
