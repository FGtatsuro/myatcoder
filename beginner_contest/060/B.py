a, b, c = [int(i) for i in input().split()]

def cond(a, b, c):
    if a == 1:
        return True
    candidate = []
    i = 1
    while True:
        r = (a * i) % b
        if r in candidate:
            break
        i += 1
        candidate.append(r)
    if c in candidate:
        return True
    return False

if cond(a, b, c):
    print('YES')
else:
    print('NO')
