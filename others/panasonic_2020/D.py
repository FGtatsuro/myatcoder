import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())

def dfs(seq):
    if len(seq) == N:
        yield seq
        return
    _max = 0
    if len(seq) != 0:
        _max = max(seq) + 1
    for i in range(0, _max+1):
        new_seq = seq.copy()
        new_seq.append(i)
        yield from dfs(new_seq)

chr_base = ord('a')
for l in dfs([]):
    print(''.join(chr(v + chr_base) for v in l))
