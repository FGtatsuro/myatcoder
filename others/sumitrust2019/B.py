n = int(input())

import math

def cal():
    # https://qiita.com/drken/items/97e37dd6143e33a64c8c
    ok = n
    ng = 0
    # 隣接するまで繰り返す
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        # 小数が絡む場合は厳密な判定は二分探索の外でした方が良いか?
        # 本来確かめたいのはint(mid * 1.08) == n
        if mid * 1.08 >= n:
            ok = mid
        else:
            ng = mid
    return ok


ans = cal()
if int(ans * 1.08) == n:
    print(ans)
else:
    print(':(')
