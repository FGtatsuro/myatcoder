import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

Q = int(input())
N = 10 ** 5
like_2017 = [0] * (N+1)

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(3, N+1):
    if is_prime(i) and is_prime((i+1) // 2):
        like_2017[i] = 1

S = [0] * (N+1)
for i in range(N):
    S[i+1] = S[i] + like_2017[i]

for _ in range(Q):
    l, r = map(int, input().split())
    print(S[r+1] - S[l])
