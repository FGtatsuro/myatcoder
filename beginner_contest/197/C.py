import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))

def binary(n, l):
    bit = [0] * l
    for i in range(l):
        if n & 1:
            bit[i] = 1
        n >>= 1
    return bit

ans = float('inf')
for i in range(2 ** (N-1)):
    bit = binary(i, N-1)
    current_xor = 0
    current_or = A[0]
    for i, b in enumerate(bit):
        # xor
        if b == 0:
            current_xor ^= current_or
            current_or = A[i+1]
        # or
        elif b == 1:
            current_or |= A[i+1]
        else:
            assert False
    current_xor ^= current_or
    ans = min(ans, current_xor)
print(ans)
