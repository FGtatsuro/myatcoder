import sys
n = int(sys.stdin.readline())
p = [int(i) for i in sys.stdin.readline().split()]

if p == sorted(p):
    print('YES')
elif len(p) == 2:
    print('YES')
else:
    swap_index = []
    for i, v in enumerate(p[:-1]):
        if v > p[i + 1]:
            if len(swap_index) == 0:
                swap_index.append(i)
            else:
                swap_index.append(i + 1)
                break
    if len(swap_index) == 1:
        print('NO')
    else:
        p[swap_index[0]], p[swap_index[1]] = p[swap_index[1]], p[swap_index[0]]
        if p == sorted(p):
            print('YES')
        else:
            print('NO')
