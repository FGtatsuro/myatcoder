import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()
t = input().strip()
len_s = len(s)
len_t = len(t)
s = '0' + s
t = '0' + t

# 文字列でそのまま処理しようとするとTLE/MLE
#dp = [[''] * (len_t+2) for _ in range(len_s+2)]
#dp[0+1][0+1] = ''
#for i in range(1, len_s+1):
#    for j in range(1, len_t+1):
#        if s[i] == t[j]:
#            dp[i+1][j+1] = dp[i][j] + s[i]
#        else:
#            dp[i+1][j+1] = dp[i][j]
#
#        if len(dp[i+1][j]) > len(dp[i+1][j+1]):
#            dp[i+1][j+1] = dp[i+1][j]
#        if len(dp[i][j+1]) > len(dp[i+1][j+1]):
#            dp[i+1][j+1] = dp[i][j+1]

# dp[i+1][j+1]: sのi文字目(0<=i<=len(s)), tのj文字目(0<=j<=len(t))までのLCS
dp = [[0] * (len_t+2) for _ in range(len_s+2)]
# 初期値
dp[0+1][0+1] = 0
for i in range(1, len_s+1):
    for j in range(1, len_t+1):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

# FYI: https://kyopro-friends.hatenablog.com/entry/2019/01/12/231000
# DP配列から文字列を作成する
ans_len = dp[len_s+1][len_t+1]
ans = [0] + [0] * ans_len
# 後ろから走査
i = len_s
j = len_t
while ans_len:
    # 両方ともLCSに使われる
    if s[i] == t[j]:
        ans[ans_len] = s[i]
        ans_len -= 1
        i -= 1
        j -= 1
    # sの末尾がLCSに使われない
    elif dp[i+1][j+1] == dp[i][j+1]:
        i -= 1
    # jの末尾がLCSに使われない
    elif dp[i+1][j+1] == dp[i+1][j]:
        j -= 1
    else:
        assert False
print(''.join(ans[1:]))
