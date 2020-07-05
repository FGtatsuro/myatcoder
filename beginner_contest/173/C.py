import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w, k = map(int, input().split())
board = [0] * h
for i in range(h):
    board[i] = list(input().strip())

ans = 0
for i in range(2 ** h):
    for j in range(2 ** w):
        bin_i = format(i, '0{}b'.format(h))
        bin_j = format(j, '0{}b'.format(w))
        black = 0
        for ch in range(h):
            for cw in range(w):
                if bin_i[ch] == '1':
                    continue
                if bin_j[cw] == '1':
                    continue
                if board[ch][cw] == '#':
                    black += 1
        if black == k:
            ans += 1
print(ans)
