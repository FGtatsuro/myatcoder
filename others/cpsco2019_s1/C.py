import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = list(map(int, input().split()))

def dfs(seq):
    if len(seq) == K:
        yield seq
        return
    last = -1
    if len(seq) != 0:
        last = seq[-1]
    remain = K - len(seq)
    for i in range(last+1, N-remain+1):
        new_seq = seq.copy()
        new_seq.append(i)
        yield from dfs(new_seq)

candidate = set()
for l in dfs([]):
    total = 0
    for v in l:
        total += A[v]
    candidate.add(total)
# c<=(10^8)*6 だが、硬貨は10^9まであることに注意。INFは大きめに設定しないと間違う
ans = 10 ** 15
for c in candidate:
    # c<=(10^8)*6
    count = 0
    while c:
        r = c % 10
        count += (r // 5)
        count += (r % 5)
        c //= 10
    ans = min(ans, count)
print(ans)
