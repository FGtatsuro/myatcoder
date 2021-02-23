import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
a = list(map(int, input().split()))

def binary(n, digit):
    bit = [0] * digit
    for i in range(digit):
        if n & 1:
            bit[i] = 1
        n >>= 1
    return bit

INF = 10 ** 15
ans = INF
for i in range(2 ** N):
    bit = binary(i, N)
    if bit.count(1) != K:
        continue

    tmp_ans = 0
    tmp_max = 0
    for i, v in enumerate(bit):
        if v == 0:
            # 最高値の更新のみ
            tmp_max = max(tmp_max, a[i])
        elif v == 1:
            if a[i] > tmp_max:
                # 現状の最高値より高いため見える
                tmp_max = a[i]
            else:
                # 現状の最高値より1だけ高くするためのコスト
                tmp_max = tmp_max + 1
                tmp_ans += (tmp_max - a[i])
        else:
            assert False
    ans = min(ans, tmp_ans)

print(ans)
