import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

w, h, x, y = map(int, input().split())
# (x, y)と長方形の中心を結ぶ線分が求める分割を作る
# (x, y)が中心と一致する時は線分は無数に存在する
if w == x * 2 and h == y * 2:
    print('{} 1'.format(w * h * 0.5))
else:
    print('{} 0'.format(w * h * 0.5))
