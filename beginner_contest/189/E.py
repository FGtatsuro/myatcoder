import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
unit = [0] + [0] * n
for i in range(n):
    x, y = map(int, input().split())
    unit[i+1] = (x, y)

m = int(input())
op_accum = [0] * (m + 1)
# (原点, xベクトル, yベクトル)
op_accum[0] = ((0, 0), (1, 0), (0, 1))
for i in range(m):
    op = input().strip()
    if op[0] == '1':
        op_accum[i+1] = (
            (op_accum[i][0][1], -op_accum[i][0][0]),
            (op_accum[i][1][1], -op_accum[i][1][0]),
            (op_accum[i][2][1], -op_accum[i][2][0]),
        )
    elif op[0] == '2':
        op_accum[i+1] = (
            (-op_accum[i][0][1], op_accum[i][0][0]),
            (-op_accum[i][1][1], op_accum[i][1][0]),
            (-op_accum[i][2][1], op_accum[i][2][0]),
        )
    elif op[0] == '3':
        _, diff = map(int, op.split())
        op_accum[i+1] = (
            (-op_accum[i][0][0] + diff * 2, op_accum[i][0][1]),
            (-op_accum[i][1][0] + diff * 2, op_accum[i][1][1]),
            (-op_accum[i][2][0] + diff * 2, op_accum[i][2][1]),
        )
    elif op[0] == '4':
        _, diff = map(int, op.split())
        op_accum[i+1] = (
            (op_accum[i][0][0], -op_accum[i][0][1] + diff * 2),
            (op_accum[i][1][0], -op_accum[i][1][1] + diff * 2),
            (op_accum[i][2][0], -op_accum[i][2][1] + diff * 2),
        )
    else:
        assert False

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    x, y = unit[b]
    
    vector = (
        (
            (op_accum[a][1][0] - op_accum[a][0][0]),
            (op_accum[a][1][1] - op_accum[a][0][1])
        ),
        (
            (op_accum[a][2][0] - op_accum[a][0][0]),
            (op_accum[a][2][1] - op_accum[a][0][1])
        )
    )

    # 90度回転
    if vector == ((1, 0), (0, 1)):
        x, y = x, y
    elif vector == ((0, -1), (1, 0)):
        x, y = y, -x
    elif vector == ((-1, 0), (0, -1)):
        x, y = -x, -y
    elif vector == ((0, 1), (-1, 0)):
        x, y = -y, x
    # 対称移動
    elif vector == ((-1, 0), (0, 1)):
        x, y = -x, y
    elif vector == ((0, -1), (-1, 0)):
        x, y = -y, -x
    elif vector == ((1, 0), (0, -1)):
        x, y = x, -y
    elif vector == ((0, 1), (1, 0)):
        x, y = y, x
    else:
        assert False

    x, y = op_accum[a][0][0] + x, op_accum[a][0][1] + y
    print(x, y)
