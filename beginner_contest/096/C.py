import sys
h, w = [int(i) for i in sys.stdin.readline().split()]
s = [sys.stdin.readline().strip() for _ in range(h)]

WHITE = '.'
BLACK = '#'

def can_draw():
    for i in range(h):
        for j in range(w):
            if s[i][j] == WHITE:
                continue

            top = i - 1
            bottom = i + 1
            left = j - 1
            right = j + 1

            if top >= 0:
                if s[top][j] == BLACK:
                    continue

            if bottom < h:
                if s[bottom][j] == BLACK:
                    continue

            if left >= 0:
                if s[i][left] == BLACK:
                    continue

            if right < w:
                if s[i][right] == BLACK:
                    continue

            return False
    return True

if can_draw():
    print('Yes')
else:
    print('No')
