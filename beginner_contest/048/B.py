a, b, x = [int(i) for i in input().split()]

total = 0
if x > b:
    if a == 0:
        total += 1
else:
    q = a // x
    r = a % x
    if r == 0:
        total += 1
    next_ = x * (q + 1)

    if next_ <= b:
        total += 1
        total += ((b - next_) // x)

print(total)
