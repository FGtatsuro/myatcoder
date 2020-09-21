k, s = [int(i) for i in input().split()]

count = 0
for x in range(k+1):
    if s - x > 2 * k:
        continue
    for y in range(k+1):
        if s - (x+y) > k or s -(x+y) < 0:
            continue
        count += 1

print(count)
