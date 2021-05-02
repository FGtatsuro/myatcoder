import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

R, C = map(int, input().split())
state = [0] * R
for i in range(R):
    state[i] = list(map(int, input().split()))
c_sum = [0] * C
for i in range(C):
    for j in range(R):
        if state[j][i] == 0:
            c_sum[i] += 1

def binary(n, l):
    ans = [0] * l
    for i in range(l):
        if n & 1:
            ans[i] = 1
        n >>= 1
    return ans

def from_binary(bit):
    ans = 0
    for i in range(len(bit)):
        if bit[i] == 1:
            ans += 2 ** i
    return ans

# 配列
ans = 0
for i in range(2**R):
    target_row = binary(i, R)
    tmp_sum = c_sum[:]
    for j, v1 in enumerate(target_row):
        if v1 == 0:
            continue
        for k, v2 in enumerate(state[j]):
            if v2 == 0:
                tmp_sum[k] -= 1
            elif v2 == 1:
                tmp_sum[k] += 1
            else:
                assert False
    tmp_ans = 0
    for v in tmp_sum:
        tmp_ans += max(R-v, v)
    ans = max(ans, tmp_ans)
print(ans)

# XOR
#column_bit = [[] for _ in range(C)]
#for i in range(C):
#    for j in range(R):
#        column_bit[i].append(state[j][i])
#ans = 0
#for i in range(2**R):
#    tmp_ans = 0
#    for bit in column_bit:
#        zero = 0
#        one = 0
#        for v in binary(i ^ from_binary(bit), R):
#            if v == 0:
#                zero += 1
#            elif v == 1:
#                one += 1
#        tmp_ans += max(zero, one)
#    ans = max(ans, tmp_ans)
#print(ans)
