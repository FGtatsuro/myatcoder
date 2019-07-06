_input = [i for i in open(0).read().split('\n') if i]
n, y = [int(i) for i in _input[0].split()]

answer = (-1, -1, -1)
for i1 in range(n + 1):
    if answer != (-1, -1, -1):
        break
    for i2 in range(n - i1 + 1):
        total = 10000 * i1 + 5000 * i2 + 1000 * (n - i1 - i2)
        if total == y:
            answer = (i1, i2, (n - i1 - i2))
            break
print(*answer)
