import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()
if len(s) == 1:
    print(0)
    sys.exit(0)
if len(s) == 2 and s[0] == s[1]:
    print(0)
    sys.exit(0)

# [i][0]: index iが1文字分割
# [i][1]: index iが2文字分割
dp = [[0] * 2 for _ in range(len(s))]
# 3文字以上では1文字/2文字の仮想結果が使われる
# 1文字
dp[0][0] = dp[0][1] = 1
# 2文字
if s[0] == s[1]:
    # 実際には常に2文字分割になる
    dp[1][0] = dp[1][1] = 1
else:
    dp[1][0] = 2
    dp[1][1] = 1

# 3文字以上
for i in range(2, len(s)):

    # [i][0]: 末尾の分割を1文字にする場合

    # 末尾2文字が同じ場合
    # - 1つ前を2文字分割にしなくてはならない
    if s[i] == s[i-1]:
        dp[i][0] = dp[i-1][1] + 1
    # 末尾2文字が異なる場合
    # - 1つ前が1文字分割
    # - 1つ前が2文字分割
    else:
        dp[i][0] = max(dp[i-1][0] + 1, dp[i-1][1] + 1)


    # [i][1]: 末尾の分割を2文字にする場合
    # 末尾前の2文字が末尾の2文字と同じ場合
    # 末尾前を1文字分割にしなくてはならない
    if s[i-3:i-1] == s[i-1:i+1]:
        dp[i][1] = dp[i-2][0] + 1
    # 末尾前の2文字が末尾の2文字と異なる場合
    # - 末尾前が1文字分割
    # - 末尾前が2文字分割
    else:
        dp[i][1] = max(dp[i-2][0] + 1, dp[i-2][1] + 1)

print(max(dp[-1][0], dp[-1][1]))
