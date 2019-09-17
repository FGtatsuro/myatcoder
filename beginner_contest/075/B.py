import sys
h, w = [int(i) for i in sys.stdin.readline().split()]
s = [sys.stdin.readline().strip() for _ in range(h)]
result = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            result[i][j] = '#'
            continue
        count = 0
        top = (i - 1)
        bottom = (i + 1)
        left = (j - 1)
        right = (j + 1)

        if top >= 0:
            if left >= 0:
                if s[top][left] == '#':
                    count += 1
            if s[top][j] == '#':
                count += 1
            if right < w:
                if s[top][right] == '#':
                    count += 1
        if bottom < h:
            if left >= 0:
                if s[bottom][left] == '#':
                    count += 1
            if s[bottom][j] == '#':
                count += 1
            if right < w:
                if s[bottom][right] == '#':
                    count += 1
        if left >= 0:
            if s[i][left] == '#':
                count += 1
        if right < w:
            if s[i][right] == '#':
                count += 1
        
        result[i][j] = str(count)

for r in result:
    print(''.join(r))
