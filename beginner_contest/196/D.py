import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

H, W, A, B = map(int, input().split())
ans = 0

# i: 0-H*W番目の半畳マスにいる
# bit: 0-H*Wの半畳マスに畳が届いているか
def dfs(i, bit, A, B):
    if i == H * W:
        global ans
        ans += 1
        return
    # i番目の半畳マスに既に畳が届いているか(=iビット目が立っているか)
    if bit & (1<<i):
        dfs(i+1, bit, A, B)
        return
    # i番目の半畳マスに半畳畳を置く(=iビット目を立てる)
    if B:
        dfs(i+1, bit | (1<<i), A, B-1)
    # i番目の半畳マスに一畳畳を置く(=iビット目と i+1ビット目(右にはみだす) or i+Wビット目(下にはみだす)を立てる)
    if A:
        # i番目の半畳マスが右端にある場合は右にはみだせない
        # i+1番目の半畳マスに既に畳が届いている場合(上から)もはみだせない
        if i % W != W-1 and not (bit & (1<<(i+1))):
            dfs(i+1, bit | (1<<i) | (1<<(i+1)), A-1, B)
        # i番目の半畳マスが下端にある場合は下にはみだせない
        # i+1番目の半畳マスに既に畳が届いている場合はありえないが一応
        if i + W < H * W and not (bit & (1<<(i+W))):
            dfs(i+1, bit | (1<<i) | (1<<(i+W)), A-1, B)

dfs(0, 0, A, B)
print(ans)
