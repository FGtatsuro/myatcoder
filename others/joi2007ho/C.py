import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
xy = []
# 座標の存在判定が必要
exist = set()
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))
    exist.add((x, y))

# 2点が決まれば正方形は一意に定まる
ans = 0
for i in range(len(xy)):
    for j in range(i+1, len(xy)):
        # i: 左下/j: 右下で固定しても問題ない
        x1, y1 = xy[i]
        x2, y2 = xy[j]

        vx, vy = (x2 - x1, y2 - y1)
        # 左上が存在しうるか
        x3 = x1 + (-vy)
        y3 = y1 + vx
        if (x3, y3) not in exist:
            continue

        # 右上が存在しうるか
        x4 = x3 + vx
        y4 = y3 + vy
        if (x4, y4) not in exist:
            continue

        ans = max(ans, (x2 - x1) ** 2 + (y2 - y1) ** 2)
print(ans)
