import sys
input = sys.stdin.readline

h, n = [int(i) for i in input().split()]
magic = [0] * n
for i in range(n):
    magic[i] = [int(i) for i in input().split()]

BIG = 10 ** 9
memo = [BIG] * (h+1)

def solve(remain_hp):
    if memo[remain_hp] != BIG:
        return memo[remain_hp]

    _min = BIG
    for m in magic:
        if remain_hp - m[0] <= 0:
            _min = min(_min, m[1])
        else:
            _min = min(_min, solve(remain_hp - m[0]) + m[1])
    memo[remain_hp] = _min
    return memo[remain_hp]

for i in range(1, h+1):
    solve(i)

print(memo[h])
