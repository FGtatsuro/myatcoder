import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

K, N = map(int, input().split())
vw = [0] * N
for i in range(N):
    vw[i] = input().strip().split()
    # 0オリジンに変換
    vw[i][0] = list(map(lambda v: int(v) - 1, vw[i][0]))

def convert(num, base, length):
    bit = [0] * length
    for i in range(length):
        r = num % base
        # 長さは1〜base
        bit[i] = r + 1
        num //= base
    return bit

for i in range(3 ** K):
    len_info = convert(i, 3, K)
    is_correct = True
    for v, w in vw:
        strlen = 0
        for j in v:
            strlen += len_info[j]
        if len(w) != strlen:
            is_correct = False
            break
    if not is_correct:
        continue

    strmap = [0] * K
    for v, w in vw:
        start = 0
        for j in v:
            strmap[j] = w[start:start+len_info[j]]
            start += len_info[j]
    for v in strmap:
        print(v)
    sys.exit(0)
