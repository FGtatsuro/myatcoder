import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
info = [0] * N
for i in range(N):
    info[i] = list(map(int, input().split()))
info = sorted(info, key=lambda x: x[2], reverse=True)

for Cx in range(100 + 1):
    for Cy in range(100 + 1):
        H = None
        ok = True
        for x, y, h in info:
            tmp = abs(x - Cx) + abs(y - Cy) + h
            # 全部0だと特定できないので、かならず0以外があり、ソートしているため0より前にHが入る
            if not H:
                H = tmp
                continue
            if h == 0:
                if H > tmp:
                    ok = False
                    break
            else:
                if tmp != H:
                    ok = False
                    break
        if ok:
            print(Cx, Cy, H)
            sys.exit(0)

