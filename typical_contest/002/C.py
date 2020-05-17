import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import itertools

n = int(input())
w = [0] + list(map(int, input().split()))
w_accum = list(itertools.accumulate(w))

dp = [-1] + [-1] * n
for i in range(n):
    dp[i+1] = [-1] + [-1] * n
    dp[i+1][i+1] = 0

# O(n^3)
def dfs_n3(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        cost = 10 ** 10
        for k in range(i, j):
            cost = min(cost, dfs(i, k)+dfs(k+1, j))
        # 部分木は高さが1段下がっているため、その分を加算する
        cost += (w_accum[j] - w_accum[i-1])
        dp[i][j] = cost
        return dp[i][j]

pivot = [-1] + [-1] * n
for i in range(n):
    pivot[i+1] = [-1] + [-1] * n

# O(n^2)
def dfs_n2(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        cost = 10 ** 10
        first = i
        last = j - 1
        p = first

        # 右と左から1つずつ縮め、first/lastの区間を短くする
        if pivot[i][j-1] != -1:
            first = pivot[i][j-1]
        if pivot[i+1][j] != -1:
            last = pivot[i+1][j]
        #print('i:{},j:{},first:{},last{}'.format(i, j, first, last))
        for k in range(first, last + 1):
            candidate = dfs(i, k)+dfs(k+1, j)
            if cost > candidate:
                cost = candidate
                p = k
        # 部分木は高さが1段下がっているため、その分を加算する
        cost += (w_accum[j] - w_accum[i-1])
        dp[i][j] = cost
        pivot[i][j] = p
        return dp[i][j]

# O(nlogn)
def dfs_nlogn(i, j):
    # TODO
    pass

dfs = dfs_n3
dfs = dfs_n2
#dfs = dfs_nlogn
print(dfs(1, n))
