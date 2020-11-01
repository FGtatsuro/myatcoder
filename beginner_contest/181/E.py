import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
h = sorted(map(int, input().split()))
w = list(map(int, input().split()))

def bs(ok, ng, cond):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if cond(mid):
            ok = mid
        else:
            ng = mid
    return ok

if n == 1:
    ans = 10 ** 10
    for v in w:
        ans = min(ans, abs(h[0] - v))
    print(ans)
    sys.exit(0)

diff1 = [0] * (n//2)
diff2 = [0] * (n//2)
for i in range(n // 2):
    diff1[i] = abs(h[i*2] - h[i*2 + 1])
    diff2[i] = abs(h[i*2+1] - h[(i+1)*2])
diff1_accum = [0] * (n//2)
diff2_accum = [0] * (n//2)
diff1_accum[0] = diff1[0]
diff2_accum[0] = diff2[0]
for i in range(1, n // 2):
    diff1_accum[i] = diff1_accum[i-1] + diff1[i]
    diff2_accum[i] = diff2_accum[i-1] + diff2[i]

#print(bs(n - 1, 0, lambda x: h[x] > 4))
#print(bs(0, n - 1, lambda x: h[x] < 4))
#print(h)
#print(diff1_accum, diff2_accum)
ans = None
for v in w:
    if v >= h[-1]:
        tmp = abs(v - h[-1]) + diff1_accum[-1]
    elif v <= h[0]:
        tmp = abs(v - h[0]) + diff2_accum[-1]
    else:
        insert_index = bs(n - 1, 0, lambda x: h[x] > v)
        # 端の場合は特殊ケースとして処理する
        if insert_index == n - 1:
            tmp = abs(v - h[-1]) + diff1_accum[-1]
        elif insert_index == 1:
            tmp = abs(v - h[0]) + diff2_accum[-1]
        else:
            if insert_index % 2 == 0:
                tmp = abs(v - h[insert_index]) + diff1_accum[insert_index//2-1] + diff2_accum[-1] - diff2_accum[insert_index//2-1]
            else:
                tmp = abs(v - h[insert_index - 1]) + diff1_accum[insert_index//2-1] + diff2_accum[-1] - diff2_accum[insert_index//2-1]
    if ans is None:
        ans = tmp
    else:
        ans = min(ans, tmp)
# 確認用
#for v in w:
#    if v >= h[-1]:
#        target = h + [v]
#        tmp = abs(v - h[-1]) + diff1_accum[-1]
#    elif v <= h[0]:
#        target = [v] + h
#        tmp = abs(v - h[0]) + diff2_accum[-1]
#    else:
#        insert_index = bs(n - 1, 0, lambda x: h[x] > v)
#        target = h.copy()
#        target.insert(insert_index, v)
#    tmp = 0
#    for i in range((n+1) // 2):
#        tmp += abs(target[i*2] - target[i*2+1])
#    print(target, tmp)
print(ans)
